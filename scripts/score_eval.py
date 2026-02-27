#!/usr/bin/env python3
import argparse
import csv
from pathlib import Path


def to_float(v):
    try:
        return float(v)
    except Exception:
        return None


def yes(v):
    return str(v or "").strip().lower() in {"yes", "y", "true", "1", "pass"}


def compute_metrics(csv_path: Path):
    rows = list(csv.DictReader(csv_path.open()))
    total = len(rows)
    scored = [r for r in rows if str(r.get("quality", "")).strip()]
    quality_vals = [to_float(r.get("quality")) for r in scored]
    quality_vals = [q for q in quality_vals if q is not None]

    pass_count = sum(1 for r in rows if yes(r.get("pass")))
    error_count = sum(1 for r in rows if yes(r.get("error")))

    latency_vals = [to_float(r.get("latency_ms")) for r in rows]
    latency_vals = [x for x in latency_vals if x is not None]

    cost_vals = [to_float(r.get("cost_usd")) for r in rows]
    cost_vals = [x for x in cost_vals if x is not None]

    return {
        "total_cases": total,
        "scored_cases": len(quality_vals),
        "pass_rate": (pass_count / total) if total else 0.0,
        "error_rate": (error_count / total) if total else 0.0,
        "avg_quality": (sum(quality_vals) / len(quality_vals)) if quality_vals else None,
        "avg_latency_ms": (sum(latency_vals) / len(latency_vals)) if latency_vals else None,
        "avg_cost_usd": (sum(cost_vals) / len(cost_vals)) if cost_vals else None,
    }


def fmt(v, pct=False):
    if v is None:
        return "n/a"
    if pct:
        return f"{v*100:.1f}%"
    return f"{v:.2f}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--suite', required=True, help='Eval suite name, e.g. feedback-to-prd')
    parser.add_argument('--file', choices=['baseline', 'improved'], default='baseline')
    args = parser.parse_args()

    csv_name = 'baseline_results.csv' if args.file == 'baseline' else 'improved_results.csv'
    csv_path = Path('evals') / args.suite / csv_name

    if not csv_path.exists():
        raise SystemExit(f"CSV not found: {csv_path}")

    m = compute_metrics(csv_path)

    print(f"[score_eval] Suite: {args.suite}")
    print(f"[score_eval] File: {csv_path}")
    print(f"- total cases: {m['total_cases']}")
    print(f"- scored cases: {m['scored_cases']}")
    print(f"- pass rate: {fmt(m['pass_rate'], pct=True)}")
    print(f"- error rate: {fmt(m['error_rate'], pct=True)}")
    print(f"- avg quality: {fmt(m['avg_quality'])}")
    print(f"- avg latency (ms): {fmt(m['avg_latency_ms'])}")
    print(f"- avg cost (USD): {fmt(m['avg_cost_usd'])}")


if __name__ == '__main__':
    main()
