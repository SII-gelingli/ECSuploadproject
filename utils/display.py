"""
Terminal display utilities: colored output and formatting for the agent CLI.
"""
import sys
import json


# ── ANSI color codes ───────────────────────────────────────────

class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    BG_BLUE = '\033[44m'
    BG_GREEN = '\033[42m'


def colored(text: str, color: str) -> str:
    return f"{color}{text}{Colors.RESET}"


def bold(text: str) -> str:
    return f"{Colors.BOLD}{text}{Colors.RESET}"


def dim(text: str) -> str:
    return f"{Colors.DIM}{text}{Colors.RESET}"


# ── Display functions ──────────────────────────────────────────

def print_banner():
    """Print welcome banner."""
    print(colored("=" * 70, Colors.CYAN))
    print(colored("  Electrochemical Condition Recommendation Agent", Colors.BOLD + Colors.CYAN))
    print(colored("  Powered by Claude + Trained ML Models", Colors.DIM + Colors.CYAN))
    print(colored("=" * 70, Colors.CYAN))
    print()


def print_user_prompt():
    """Print the user input prompt."""
    print(colored("\nYou: ", Colors.GREEN + Colors.BOLD), end="", flush=True)


def print_thinking(text: str):
    """Display agent's thinking/reasoning text."""
    print(colored("\n[Thinking]", Colors.YELLOW + Colors.BOLD))
    for line in text.strip().split('\n'):
        print(colored(f"  {line}", Colors.YELLOW))


def print_tool_call(name: str, inputs: dict):
    """Display a tool call."""
    print(colored(f"\n  >> Calling tool: ", Colors.BLUE) + colored(name, Colors.BLUE + Colors.BOLD))
    # Show key parameters concisely
    for key, value in inputs.items():
        if isinstance(value, str) and len(value) > 80:
            value = value[:77] + "..."
        elif isinstance(value, list) and len(value) > 3:
            value = str(value[:3]) + f" ... ({len(value)} items)"
        print(colored(f"     {key}: ", Colors.DIM) + str(value))


def print_tool_result(name: str, result_str: str):
    """Display a tool result summary."""
    try:
        result = json.loads(result_str)
        if 'error' in result:
            print(colored(f"  << {name}: ERROR - {result['error']}", Colors.RED))
        else:
            # Show a brief summary
            summary_parts = []
            if 'num_results' in result:
                summary_parts.append(f"{result['num_results']} results")
            if 'recommendations' in result:
                summary_parts.append(f"7 condition types")
            if 'joint_schemes' in result:
                summary_parts.append(f"{result.get('num_unique_schemes', '?')} schemes")
            if 'yield_predictions' in result:
                yields = [r['predicted_yield'] for r in result['yield_predictions']]
                summary_parts.append(f"yields: {yields}")
            if 'results' in result and isinstance(result['results'], list):
                summary_parts.append(f"{len(result['results'])} molecules")

            summary = ", ".join(summary_parts) if summary_parts else "OK"
            print(colored(f"  << {name}: {summary}", Colors.GREEN))
    except (json.JSONDecodeError, KeyError):
        print(colored(f"  << {name}: (result received)", Colors.GREEN))


def print_response(text: str):
    """Display the agent's final response."""
    print(colored("\nAgent:", Colors.MAGENTA + Colors.BOLD))
    print(text)


def print_separator():
    print(colored("-" * 70, Colors.DIM))


def display_callback(event_type: str, data):
    """
    Callback for ElectrochemAgent.chat() to display events in real-time.

    Event types: 'thinking', 'tool_call', 'tool_result', 'response'
    """
    if event_type == 'thinking':
        print_thinking(data)
    elif event_type == 'tool_call':
        print_tool_call(data['name'], data['input'])
    elif event_type == 'tool_result':
        print_tool_result(data['name'], data['result'])
    elif event_type == 'response':
        print_response(data)
