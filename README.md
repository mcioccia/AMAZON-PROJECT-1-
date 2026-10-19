# Amazon Project 1 — working draft

AI-assisted educational coursework; not financial or investment advice. This is a new Amazon project. It does not replace or claim an original META or Amazon Edition A submission.

**Status: runnable analytical draft, not submission-ready.** The user selected Amazon; instructor approval, assignment cutoff and Edition A treatment have not been verified. No instructor access, student AI-off work, videos, or submission receipt is claimed.

## Reproduce the visible result

Use Python 3.10+ (tested with Python 3.13). The model and dashboard use the standard library. No API key, account, internet connection, or pip install is needed to reproduce the saved inputs. Start from the extracted `Amazon-Project` folder:

```powershell
python -m unittest -v
python build_report.py
python app.py
```

Open http://127.0.0.1:8767 in your browser. Stop the server with Ctrl+C. A different port can be passed with `python app.py --port 8768` if supported by the command help. The static result is `outputs/visible-result.html`; open it directly without a server. Exact unrounded results are in `outputs/analysis.json`. Rebuilding overwrites generated outputs. Keep a copy before experimenting.

Expected base result: approximately **$73.31 per share**, with **94.2%** of enterprise value from the terminal period. This is a provisional model output, not an established fair value. The historical comparison price is $210.32 on February 6, 2026; it is not today's quote. Any different result requires checking inputs, code and assumptions before use. Automated model checks passed; interactive browser testing was blocked by this preparation environment's local socket restrictions. Test dashboard controls locally before recording the demo.

## Scope and decision

Proposed historical exercise: information cutoff and valuation date February 6, 2026, FY2025 base, annual forecasts 2026–2030. This cutoff is an analyst choice requiring instructor confirmation; later information is intentionally excluded. Proposed fund decision: **watch/defer initiation while validating capital productivity and the cost of capital**. The mechanical value screen differs from this judgment and does not override it.

Source inputs and URLs are in `data/inputs.json`; methodology, historical normalization and limits are in `docs/assumption-challenges.md`. USD millions, shares in millions, per-share prices in dollars. Forecast segment margins are before PPE depreciation, retain stock compensation, and are analyst assumptions rather than reported EBITDA margins. See `model.py` for all transformations.

## Explore and test

Change a bounded driver, click Recalculate, inspect the price and statements, then Reset to base. The cash-error demonstration injects a $1,000 million discrepancy and withholds valuation. Reset recovers the base. An exported exploratory JSON file is evidence of a run, not evidence of an independent student exercise. The saved-base case, sensitivity and reverse-DCF tables stay fixed while controls change.

## Audit and submission

`project_audit.py` is the unchanged course script. It requires **pandas**, unlike the model. In an environment with pandas installed:

```powershell
python project_audit.py project-submission-manifest-template.csv
```

If pandas is missing, install it in your own virtual environment with `python -m pip install pandas`, then rerun. The manifest deliberately leaves unavailable evidence blank. A nonempty field can satisfy this mechanical script without proving access, finance quality, or completion. The script can report gaps and still exit successfully; read its output.

Read `docs/STUDENT_ACTIONS.md` for remaining requirements. Course repository and student handout control the architecture: https://github.com/CinderZhang/FIN43900-Fall2026/tree/main . Damodaran's format and GitHub's README guidance are external references, not replacement submission templates.

## Recording preparation

Open `Recording-Pack.html` for all three timed recording guides and scripts, plus the retrospective research starting point. The latter is AI-assisted and does not replace original Edition A. Student-authored evidence slots remain marked. The dashboard now includes a labeled invalid-terminal-input diagnostic; WACC equals growth at 3%, so valuation is withheld until reset. The eight automated tests include backend rejection/recovery; local browser rehearsal remains necessary.
