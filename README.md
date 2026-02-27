# ai-eval-lab

Evaluation-focused repo for AI product features.

## Purpose
Build repeatable eval harnesses that measure quality, reliability, latency, and cost so product decisions are evidence-driven.

## Eval Packs
- support-copilot
- feedback-to-prd
- lead-qualification

## Core Metrics
- Quality score (1-5)
- Pass rate
- Error/hallucination rate
- Latency
- Cost per run

## Quickstart
```bash
python3 scripts/run_eval.py --suite support-copilot
python3 scripts/score_eval.py --suite support-copilot
```
