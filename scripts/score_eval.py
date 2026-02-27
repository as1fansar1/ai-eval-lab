#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--suite', required=True)
args = parser.parse_args()

print(f"[score_eval] Suite: {args.suite}")
print("[score_eval] Placeholder scoring complete. Add metric aggregation here.")
