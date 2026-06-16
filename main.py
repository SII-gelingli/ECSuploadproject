#!/usr/bin/env python
"""
CLI entry point for the Electrochemical Condition Agent.

Usage:
    # Interactive mode
    python main.py

    # One-shot mode
    python main.py --reaction "CC(=O)c1ccccc1>>CC(O)c1ccccc1"

    # With options
    python main.py --reaction "CC(=O)c1ccccc1>>CC(O)c1ccccc1" --model claude-sonnet-4-20250514
    python main.py --device cuda
"""
import sys
import argparse
from pathlib import Path

# Set up project paths
_this_dir = Path(__file__).parent
sys.path.insert(0, str(_this_dir))

from config import AgentConfig


def create_agent(args):
    """Initialize the agent with all dependencies."""
    from models.loader import ModelManager
    from agent.loop import ElectrochemAgent

    # Build config from CLI args
    config = AgentConfig(
        device=args.device,
        max_tool_rounds=args.max_rounds,
    )
    if args.model:
        config.model = args.model
    if args.api_key:
        config.api_key = args.api_key

    if not config.api_key:
        print("Error: ANTHROPIC_API_KEY not set. Set via environment variable or --api_key.")
        sys.exit(1)

    # Initialize model manager (lazy-loads models on first use)
    model_manager = ModelManager(device=config.device)

    # Initialize retriever (may be None if index not built)
    retriever = None
    try:
        from rag.retriever import ReactionRetriever
        index_path = config.faiss_index_path
        db_path = config.reaction_db_path
        if Path(db_path).exists():
            retriever = ReactionRetriever(index_path, db_path)
            print(f"  Reaction database loaded.")
        else:
            print(f"  Note: Reaction database not found. Run 'python build_index.py' to enable similar reaction search.")
    except Exception as e:
        print(f"  Warning: Could not load retriever: {e}")

    # Initialize mechanism retriever (may be None if KB not built)
    mechanism_retriever = None
    try:
        from rag.mechanism_retriever import MechanismRetriever
        from config import MECHANISM_KB_DIR
        if Path(MECHANISM_KB_DIR).exists():
            mechanism_retriever = MechanismRetriever(MECHANISM_KB_DIR)
            print(f"  Mechanism KB loaded ({mechanism_retriever.num_papers} papers).")
        else:
            print(f"  Note: Mechanism KB not found. Run 'python yield_prediction/scripts/build_mechanism_kb.py' to enable mechanism search.")
    except Exception as e:
        print(f"  Warning: Could not load mechanism retriever: {e}")

    agent = ElectrochemAgent(config, model_manager, retriever, mechanism_retriever)
    return agent


def run_interactive(agent):
    """Run interactive multi-turn conversation."""
    from utils.display import (
        print_banner, print_user_prompt, print_separator,
        display_callback,
    )

    print_banner()
    print("Type your question about electrochemical reaction conditions.")
    print("Enter a reaction SMILES like: CC(=O)c1ccccc1>>CC(O)c1ccccc1")
    print("Type 'quit' or 'exit' to end. Type 'reset' to start a new conversation.\n")
    print_separator()

    while True:
        print_user_prompt()
        try:
            user_input = input().strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in ('quit', 'exit', 'q'):
            print("Goodbye!")
            break
        if user_input.lower() == 'reset':
            agent.reset()
            print("Conversation reset.\n")
            print_separator()
            continue

        try:
            agent.chat(user_input, display_callback=display_callback)
        except Exception as e:
            print(f"\nError: {type(e).__name__}: {e}")

        print_separator()


def run_one_shot(agent, reaction_smiles: str, query: str = None):
    """Run a single query and print the response."""
    from utils.display import display_callback

    if query:
        message = query
    else:
        message = (
            f"Please analyze this electrochemical reaction and recommend optimal conditions: "
            f"{reaction_smiles}"
        )

    try:
        agent.chat(message, display_callback=display_callback)
    except Exception as e:
        print(f"\nError: {type(e).__name__}: {e}")
        sys.exit(1)


def run_debate(agent, reaction_smiles: str, query: str, args):
    """Run a single query through the multi-model debate pipeline."""
    from agent.debate_config import DebateConfig
    from agent.debate_orchestrator import DebateOrchestrator

    debate_config = DebateConfig(
        enabled=True,
        api_key=agent.config.api_key,
        base_url=agent.config.base_url,
    )
    if args.recommender_b_model:
        debate_config.recommender_b_model = args.recommender_b_model
    if args.judge_model:
        debate_config.judge_model = args.judge_model

    orchestrator = DebateOrchestrator(agent, debate_config)

    message = query or (
        f"Please analyze this electrochemical reaction and recommend optimal conditions: "
        f"{reaction_smiles}"
    )

    def display_callback(event_type, data):
        if event_type == "phase_start":
            print(f"\n{'='*60}")
            print(f"  {data}")
            print(f"{'='*60}")
        elif event_type == "phase_end":
            print(f"  >> {data}")
        elif event_type == "recommendation_a":
            print(f"\n--- Recommendation A (Claude + Tools) ---")
            print(data[:500] + "..." if len(data) > 500 else data)
        elif event_type == "recommendation_b":
            print(f"\n--- Recommendation B (GPT) ---")
            print(data[:500] + "..." if len(data) > 500 else data)
        elif event_type == "critique":
            by = data.get("by", "?")
            of = data.get("of", "?")
            text = data.get("text", "")
            print(f"\n--- Critique by {by} of Proposal {of} ---")
            print(text[:300] + "..." if len(text) > 300 else text)
        elif event_type == "revision":
            by = data.get("by", "?")
            text = data.get("text", "")
            print(f"\n--- Revised Proposal {by} ---")
            print(text[:300] + "..." if len(text) > 300 else text)
        elif event_type == "judgment":
            print(f"\n{'='*60}")
            print("  FINAL JUDGMENT (Gemini)")
            print(f"{'='*60}")
            print(data)
        elif event_type == "error":
            print(f"\n  [WARNING] {data}")

    try:
        result = orchestrator.run_debate(message, display_callback=display_callback)
        print(f"\nPhases completed: {result.phases_completed}")
        if not result.judgment:
            print("\n--- Final Answer (fallback) ---")
            print(result.final_answer)
    except Exception as e:
        print(f"\nDebate Error: {type(e).__name__}: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Electrochemical Condition Recommendation Agent',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                                          # Interactive mode
  %(prog)s --reaction "CC(=O)c1ccccc1>>CC(O)c1ccccc1"  # One-shot
  %(prog)s --reaction "CC=CC>>CC(O)CC" --query "What solvent should I use?"
  %(prog)s --reaction "CC(=O)c1ccccc1>>CC(O)c1ccccc1" --debate  # Debate mode
        """,
    )
    parser.add_argument('--reaction', type=str, default=None,
                        help='Reaction SMILES for one-shot mode')
    parser.add_argument('--query', type=str, default=None,
                        help='Custom query (used with --reaction)')
    parser.add_argument('--model', type=str, default=None,
                        help='Claude model to use (default: claude-opus-4-6)')
    parser.add_argument('--api_key', type=str, default=None,
                        help='Anthropic API key (or set ANTHROPIC_API_KEY env var)')
    parser.add_argument('--device', type=str, default='cpu',
                        choices=['cpu', 'cuda'],
                        help='Inference device (default: cpu)')
    parser.add_argument('--max_rounds', type=int, default=15,
                        help='Max tool call rounds (default: 15)')
    # Debate mode arguments
    parser.add_argument('--debate', action='store_true',
                        help='Enable multi-model debate mode')
    parser.add_argument('--recommender-b-model', type=str, default='gpt-5.4',
                        help='Recommender B model (default: gpt-5.4)')
    parser.add_argument('--judge-model', type=str, default='gemini-3.1-pro-preview',
                        help='Judge model (default: gemini-3.1-pro-preview)')

    args = parser.parse_args()

    print("Initializing agent...")
    agent = create_agent(args)
    print("Agent ready.\n")

    if args.debate:
        if not args.reaction:
            print("Error: --debate requires --reaction (one-shot mode only).")
            sys.exit(1)
        run_debate(agent, args.reaction, args.query, args)
    elif args.reaction:
        run_one_shot(agent, args.reaction, args.query)
    else:
        run_interactive(agent)


if __name__ == '__main__':
    main()
