# Click-by-click recording walkthrough

AI-assisted educational rehearsal aid; not investment advice. Prepared October 19, 2026. These instructions describe the current provisional model. They do not certify final financial readiness or replace the student's actual independent evidence.

## Step 0 - use the correct files

Press Windows+R and paste this folder path, then press Enter:

```text
C:\Users\mac10\Documents\Codex\2026-10-18\new-chat\Amazon-Project
```

Open `Recording-Pack.html` for the scripts. Keep it beside your recording window as your notes. Open `outputs/visible-result.html` to show the saved calculation. For the source code, open the same project folder in your code editor. For final recording use the actual uploaded repository version, not an unrelated or older copy.

In File Explorer's address bar type `powershell` and press Enter to open a terminal in this folder. Run:

```powershell
python -m unittest -v
python build_report.py
```

The expected model results are eight passing test methods, 29 passing base checks, and approximately $73.31/share. The tests do not prove the financial assumptions correct. Do not call this a fresh-environment or partner cold run unless you actually perform and preserve that separate test.

Choose your screen recorder, enable the microphone and small webcam overlay, record ten seconds, and play it back. Enlarge your editor and browser until text is readable. Have all tabs open before the real take. Avoid opening private mail or credentials while recording. The timed guides provide speaking scripts; the steps below specify the screens.

## Video 1 - target 2:40, hard stop 3:00

1. **0:00-0:20:** Show `outputs/visible-result.html` at the top. Point to Amazon, the historical February 6, 2026 valuation date and forecast horizon. State the decision is whether a fund without an existing position should initiate.
2. **0:20-0:40:** Open `docs/research-evolution.md` in the editor. Show the missing original Edition A disclosure. Say it directly. Do not describe the retrospective starting-point document as the original checkpoint or claim an unverified instructor exception.
3. **0:40-1:10:** Open `docs/assumption-challenges.md`. Find Cash capex and Capacity response. Explain the proposed capital-productivity question: AWS growth must justify the investment needed to deliver it. Treat this as AI-assisted reasoning you have reviewed, not a pre-AI belief.
4. **1:10-1:30:** Open the Amazon February 5 earnings release linked in `data/inputs.json`. Press Ctrl+F and search `200 billion`. Show the passage and date. It is an Amazon-wide capital-expenditure outlook; it is not an AWS-only spending forecast.
5. **1:30-2:10:** Switch to `data/inputs.json`, find `capex_2026`, then `capex_path` and `capacity_elasticity`. Show your own actual source-check record alongside it. Explain your actual accepted/qualified/corrected/rejected finding and its scope. **This segment cannot be completed truthfully until you personally make that check.** The outlook does not itself establish cash-capex versus lease treatment or the later path.
6. **2:10-2:40:** Return to the saved result. Point out approximately $73.31 and 94.2% terminal share as provisional outputs, then state your reviewed position and AI-use disclosure. Use the full Video 1 script in the pack for phrasing.

## Video 2 - target 4:40, hard stop 5:00

1. **0:00-0:25:** Show the real submitted repository URL and README, then the editor folder tree. State the date, units and purpose. If a repository has not been created and shared, rehearse locally but do not claim the repository requirement is met.
2. **0:25-0:55:** Open `data/inputs.json`. Show `history`, `assumptions`, `controls`, `sources`. Explain how actual reported numbers differ from forecasts and judgment calls.
3. **0:55-1:40:** Open `model.py`. Use Ctrl+F for `def opening`, then `def calculate`. Explain one year: segment sales, pre-depreciation operating profit, depreciation, interest, taxes, working capital and investment. Point to `b['ppe']`, `cfo`, `cff` and `b['cash']`. Cash follows cash flows and funding; it is not an unexplained number chosen to force a balance.
4. **1:40-2:15:** Find `fcff=`, `terminal_reinvestment=`, and `bridge=`. Explain FCFF discounted at WACC, the growth/ROIC terminal rule, and additions/subtractions between enterprise and equity value. The ABG tutorial's FCFE/cost-of-equity method should not be mixed with this FCFF/WACC model.
5. **2:15-2:55:** In the terminal run `python -m unittest -v`, then `python build_report.py`. Read the actual output. Switch to the saved HTML and refresh it. Show the check block and statement tables; the source-transcription tests are arithmetic checks, not independent verification of filings.
6. **2:55-4:05:** Show your completed highest-risk validation evidence and locked changed-input record: actual input/units, frozen version, timestamped AI-off prediction, before/after output and your reconciliation. **Only use authentic completed records.** An optional AI-assisted boundary demo is available, but it does not substitute for this evidence. Keep code visible briefly to explain why the check detects the failure.
7. **4:05-4:40:** Show `docs/assumption-challenges.md` and the terminal share in the report. Name a specific remaining limitation and what evidence would resolve it. End on how another analyst reproduces the same output.

## Video 3 - target 4:40, hard stop 5:00

First launch the actual app in the project terminal:

```powershell
python app.py
```

Leave that terminal running. Open `http://127.0.0.1:8767` in your browser. The saved `visible-result.html` cannot perform live changes. This environment has not verified the app in a browser, so complete this local rehearsal before recording.

1. **Before the take:** Find the AWS field near the top of the left driver panel. Locate Recalculate and Reset to base above the controls. Locate the always-visible **Terminal-input diagnostic** panel in the main column. Browser Ctrl+F can jump to these labels if scrolling takes too long. Rehearse the navigation so the opening demo fits roughly one minute.
2. **0:00-0:10:** Show the app header/date and base value. State your proposed decision briefly: defer initiation while the outstanding assumptions are validated.
3. **0:10-0:30:** In **AWS growth in 2026**, replace `24` with `28`. Click **Recalculate**. Show the result of approximately **$88.30**. Click **Reset to base** and show approximately **$73.31**. Explain the direction and note that later capex also responds to growth. These are AI-assisted rehearsal numbers; read your actual result.
4. **0:30-1:00:** Click **Test invalid terminal inputs** in the separate **Terminal-input diagnostic** panel. Show the displayed WACC 3% / growth 3% preset, red failure and withheld valuation. Explain that WACC minus growth would be zero. Click **Reset to base** and confirm recovery. Do not use the separate cash-error button for this economic-input demonstration.
5. **1:00-1:45:** Keep the tool visible. Show the operating forecast, especially AWS sales, capex and FCFF. Explain the capital-productivity argument in terms of linked outputs, not just revenue growth.
6. **1:45-2:25:** Show **Saved-base cases**. Identify downside $5.21, base $73.31, upside $179.16 against the historical $210.32 price. These are provisional joint scenarios, not probabilities or a validated investment range. Explain the economic story, including how multiple inputs change together.
7. **2:25-3:05:** Show **Saved-base WACC x terminal growth**, then **Which assumptions move the result?** Discuss terminal dependence and chosen sensitivity ranges. Explicitly state that the current 10% WACC has not been calibrated from market inputs.
8. **3:05-3:40:** Show **Market-implied expectation**. The fixed-explicit-cash-flow calculation implies about a 31.3% terminal EBIT margin to match the historical price. Call it a conditional model calculation, not the market's literal forecast. The AWS reverse-search result is bounded by its tested assumptions.
9. **3:40-4:10:** Show **Value bridge** and **Sources and limits**. Briefly explain debt, leases, cash, private-investment and dilution conventions. Point to the limits rather than implying these judgments are facts.
10. **4:10-4:40:** Return to the top/base result. Make a clear committee request and state what evidence would change it. Final investment triggers need your defended, quantified assumptions; generic promises to validate later do not turn this draft into a finished investment case.

## After each recording

Watch it and verify the required screen evidence is visible. Keep within 3/5/5 minutes. Correct the transcript of the actual recording; scripts are not transcripts. Add actual timestamp indexes, duration and accessible provider URLs to the manifest. Student source checks, AI-off work, repository access and submission receipts stay incomplete until genuinely done.

## Readiness limitation

This review confirms specified calculations and code behavior, not final valuation quality. A measured cost of capital, stronger historical normalization/driver calibration, terminal convergence and complete independent evidence remain unresolved. Rehearsal can proceed; final recording should use the completed, internally consistent final project.
