# Video 2 — How the Amazon model works

AI-assisted recording draft for educational coursework; not investment advice. Target 4:40; maximum 5:00. This is a proposed speaking script, not a transcript of a recording or evidence of student validation.

## Before recording

- Open the final submitted repository, an editor with its folder tree, a terminal in `Amazon-Project`, and `outputs/visible-result.html` in a browser. Use a readable font and webcam overlay as required. Close unrelated or private tabs.
- The current package is a local draft. Use the real repository URL and actual frozen commit/file hashes once available. Do not say instructional-team access is verified until it has been checked.
- Run the commands below once to rehearse. Save any prior experimental outputs first because `build_report.py` overwrites generated outputs. Record from the same version that you submit.
- Complete your required AI-off claim, three possible failures, and locked changed-input test yourself before recording the final validation segment. Preserve your prior prediction, actual input change, run time, frozen version, result, and interpretation. The prepared capex example below is an AI-authored rehearsal only; it is already disclosed and cannot become your independent prior prediction.
- Keep the report's historical date visible: February 6, 2026. FY2025 is the base and 2026–2030 are forecasts. The date remains a proposed course cutoff, not a verified instructor instruction.

## Timed screen actions

| Time | Show | Action and purpose |
|---|---|---|
| 0:00–0:30 | Repository folder tree and README | Show the actual submitted URL/version, scope, units, and reproduction instructions. |
| 0:30–1:05 | `data/inputs.json`, then `model.py` | Point to `history`, `assumptions`, `controls`, and `sources`; then `load()` and `opening()`. Distinguish reported facts from forecasts. |
| 1:05–1:50 | `model.py`, `calculate()` | Find `growths`, `capex`, `predep`, `cfo`, and `b['ppe']`. Explain revenue, capacity spending, depreciation, and the three-statement links. |
| 1:50–2:30 | `calculate()` valuation block | Find `fcff=`, `terminal_reinvestment=`, and `bridge=`. Explain FCFF, terminal reinvestment, and EV-to-equity. |
| 2:30–3:10 | Terminal, then visible HTML | Run the two reproduction commands. Read actual output, then refresh/open the rebuilt result. |
| 3:10–4:10 | Tests and actual validation evidence | Briefly show `ModelTests`; then show your own completed highest-risk validation evidence. The optional rehearsal example is clearly AI-authored. |
| 4:10–4:40 | Terminal share, assumptions document | Explain the main economic limitation, the role of the interface, and remaining gaps. |

Do not slowly scroll through entire files. Use editor Find on the exact function or variable names above and rehearse the tab switches.

## Exact reproduction commands

From the extracted `Amazon-Project` folder, using Python 3.10 or newer:

```powershell
python -m unittest -v
python build_report.py
```

Then open `outputs/visible-result.html`. The model/tests/report generator use Python's standard library. The current baseline has eight test methods and 29 internal base checks. Read the actual terminal count when recording; do not claim success if your run fails. Current expected base is $73.31 per share and 94.2% terminal share of enterprise value.

For the separate live dashboard: `python app.py`, then open `http://127.0.0.1:8767`. The report can be viewed without starting this server. The course audit script requires pandas and is a separate mechanical completeness check; it does not validate the investment conclusion.

## Natural speaking script

**0:00–0:30 — Start on the README and folder tree**

“This project asks whether a fund with no Amazon position should initiate one. I’m using a historical valuation date of February 6, 2026, with five forecast years. Financial amounts are in millions of dollars, and the per-share result is in dollars. I used AI to help build this draft, and the remaining review items are disclosed in the project.”

**0:30–1:05 — Inputs and opening balances**

“The project separates financial inputs from calculation logic. This JSON file contains historical figures, forecast assumptions, allowed driver ranges, and source links. The load function reads it. The opening function reorganizes the balance sheet for the model. For example, it separates capital-expenditure payables from trade payables and removes debt and financing items from operating accruals. That matters because those items should not flow through operating working capital.”

**1:05–1:50 — Operating model and statement links**

“The calculate function forecasts North America, international, and AWS revenue separately. My working approach connects AWS demand to later infrastructure spending, so faster growth also requires capacity. It does not become free revenue. Operating profit uses margins before property depreciation, then subtracts modeled depreciation. These margin inputs are analyst assumptions, not reported segment EBITDA. Investment and depreciation update property assets. Net income and stock compensation update equity, and operating, investing, and financing cash flows update cash. The balance and cash-flow checks test whether those links remain consistent.”

**1:50–2:30 — Valuation**

“Free cash flow starts with after-tax operating profit, adds back depreciation, and subtracts cash capital spending, finance-lease additions, and the change in working capital. Stock compensation stays an economic expense. Terminal reinvestment is tied to growth divided by return on invested capital. The model discounts operating cash flows, then adds excess cash, securities, and a discounted private-investment estimate. It subtracts debt and financing claims and divides equity value by a diluted-share proxy.”

**2:30–3:10 — Run and show output**

“I’ll reproduce the saved result using the README. First I run the tests, then rebuild the report. [Pause and read the actual result.] This version produces approximately seventy-three dollars and thirty-one cents per share. The HTML report shows the linked statements, valuation bridge, scenario cases, and sensitivity tables. The JSON file retains unrounded results. This is a provisional model output, not a validated price target.”

**3:10–4:10 — Validation: replace the bracketed evidence with your own completed work**

“The automated suite checks a known-answer discounting example, stored-data reconciliations, scenario direction, invalid inputs, failure recovery, and 512 combinations of control boundaries. A passing stored-data check does not independently prove a source was transcribed correctly. These tests were AI-assisted.

“For my required independent test, this is the claim I recorded before the run: [your own AI-off claim]. Here is my timestamped prediction and frozen version. I changed [actual input] from [before] to [after]. The result was [actual result]. Compared with my prediction, [your own interpretation]. This test supports [narrow conclusion], but it does not establish [remaining limitation].”

**4:10–4:40 — Finish on terminal dependence**

“The largest limitation is economic calibration. About ninety-four percent of enterprise value comes from the terminal period, and the forecast shifts to a simplified terminal investment rule. A balanced model can still have unrealistic margins or capital requirements. Before endorsing the recommendation, I need defensible capital productivity, terminal convergence, and a date-matched cost of capital. The app displays this same calculation engine; the README and saved outputs allow someone else to reproduce it.”

## Optional AI-authored rehearsal: investment burden

This is a software demonstration, not the student's locked human test. It was executed during preparation with the current files. It asks how the model responds when the 2026 capex anchor rises from $200bn to $220bn. Because later annual capex is scaled from that anchor, this changes the investment path as well as the first year; do not describe it as a single isolated $20bn cash outflow.

```powershell
python -c "from model import calculate; a=calculate(); b=calculate({'capex_2026':220000}); print('BASE', a['value']['per_share'], 'HIGHER CAPEX', b['value']['per_share']); print('2026 FCFF', a['years'][0]['fcff'], b['years'][0]['fcff'])"
```

Observed current outputs:

| Measure | Base anchor $200bn | Higher anchor $220bn |
|---|---:|---:|
| Value per share | $73.31 | $59.92 |
| 2026 FCFF, $m | -56,848.11 | -76,498.11 |

Suggested rehearsal narration: “This AI-prepared sensitivity holds the demand and margin assumptions fixed and increases the capex path. The modeled value falls from about seventy-three dollars to about sixty dollars. This checks the implemented investment burden. It does not establish whether higher spending would actually produce more revenue, better service, or a longer-lived asset.”

If the student test is incomplete, the honest draft narration is: “The required independent locked test is still outstanding. This example is AI-authored rehearsal.” That disclosure does not satisfy the missing assignment requirement.

## Exact code pointers and limits

- `model.py`: `load()`, `opening()`, `nwc()`, `calculate()`, `npv()`, `analyses()`.
- `test_model.py`: `ModelTests.test_independent_known_answer`, `test_source_reconciliation`, `test_base_and_causal_cases`, `test_directional_predictions`, `test_invalid_inputs_and_failure_recovery`, `test_all_512_control_corners`, `test_terminal_diagnostic_and_recovery`.
- `build_report.py`: `main()` runs `analyses()` and writes the visible HTML, unrounded JSON, forecast CSV, and freeze hashes. It also regenerates the draft decision memo.
- `app.py` serves the local interface in `static/index.html`; it calls the same model rather than maintaining a second set of valuation formulas.
- The synthetic known-answer test is not evidence that the required course training case was completed. Likewise, self-reproduction is not a partner cold run. Show those separate records only when actually available.
- Current tests allow a boundary combination to fail safely by withholding valuation; “512 combinations tested” does not mean all 512 produce valid valuations.

After recording, produce a corrected transcript of what you actually said, use actual timestamps in the video index, and record the submitted file/commit version. Do not submit this prospective script as a transcript.

## New terminal-input demonstration

The dashboard now includes a separate **Terminal-input diagnostic** panel and **Test invalid terminal inputs** button. `model.terminal_failure_demo()` uses WACC and growth of 3% to trigger the real `calculate()` guard; the model returns no value, and Reset restores the base. This tests a mathematical boundary, not the highest-risk economic claim or the student's locked prediction. Backend checks pass; rehearse actual browser behavior before recording.
