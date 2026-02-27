# Baseline Runbook — feedback-to-prd

## Goal
Create the first measurable quality baseline for the `feedback-to-prd` eval suite.

## Inputs
- `test_cases.json` (10 cases)
- `rubric.md`
- `baseline_results.csv`

## Scoring Rules
- **quality**: 1-5
- **pass**: `yes` if quality >= 4 and output is actionable
- **error**: `yes` if output has hallucination, schema break, or misses core problem
- **latency_ms**: observed runtime
- **cost_usd**: estimated/request cost

## Run Steps
1. For each `case_id`, run your current feature flow.
2. Score output against rubric and fill one row in `baseline_results.csv`.
3. In `notes`, capture the key failure mode briefly.
4. After all 10 are complete, summarize in `report.md`:
   - pass rate
   - top 2 failure clusters
   - highest-ROI fix to test next

## Fast Summary Formula
- pass rate = `yes` rows / 10
- avg quality = mean(quality)
- error rate = `error=yes` rows / 10

## Next Artifact
After baseline scoring, implement one fix and fill `improved_results.csv` for failed cases first.
