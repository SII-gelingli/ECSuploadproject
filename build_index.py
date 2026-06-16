#!/usr/bin/env python
"""
One-time script: build FAISS index from train.pt and alkene reaction data.

Usage:
    python build_index.py
    python build_index.py --train_data /path/to/train.pt
    python build_index.py --alkene_data data/alkene_reactions_by_yield
"""
import sys
import argparse
from pathlib import Path

# Set up paths
_this_dir = Path(__file__).parent
sys.path.insert(0, str(_this_dir))

from config import TRAIN_DATA_PATH, FAISS_INDEX_PATH, REACTION_DB_PATH

# Default alkene data path
ALKENE_DATA_DIR = _this_dir / "data" / "alkene_reactions_by_yield"


def main():
    parser = argparse.ArgumentParser(description='Build FAISS index from training data')
    parser.add_argument('--train_data', type=str, default=str(TRAIN_DATA_PATH),
                        help='Path to train.pt')
    parser.add_argument('--alkene_data', type=str, default=str(ALKENE_DATA_DIR),
                        help='Path to alkene_reactions_by_yield directory')
    parser.add_argument('--no_train', action='store_true',
                        help='Skip train.pt data (use only alkene data)')
    parser.add_argument('--no_alkene', action='store_true',
                        help='Skip alkene reaction data')
    parser.add_argument('--output_dir', type=str, default=str(_this_dir / 'data'),
                        help='Output directory for index and database')
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    index_path = str(output_dir / 'faiss_index.bin')
    db_path = str(output_dir / 'reaction_db.pkl')

    alkene_dir = None if args.no_alkene else args.alkene_data
    train_path = None if args.no_train else args.train_data

    from rag.index_builder import build_faiss_index
    count = build_faiss_index(train_path, index_path, db_path, alkene_data_dir=alkene_dir)
    print(f"\nDone! Indexed {count} reactions.")
    print(f"  Index: {index_path}")
    print(f"  Database: {db_path}")


if __name__ == '__main__':
    main()
