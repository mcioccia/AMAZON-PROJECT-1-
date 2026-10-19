# Video 3: live workbench and investment committee decision

AI-assisted rehearsal draft; educational coursework, not investment advice. Target 4:40; maximum 5:00. The recommendation and reasoning below are proposed analysis for the student to review and adopt or revise. This is not evidence of the student's AI-off prediction, independent test, or original reasoning. Record your own delivery and correct the transcript afterward.

## Before recording

1. In the extracted `Amazon-Project` folder run `python app.py`. Open `http://127.0.0.1:8767`. Use the live dashboard, not `outputs/visible-result.html`, because the saved HTML has no live controls. Keep the terminal running.
2. Close irrelevant windows. Use a small webcam view that does not cover values or controls. Set browser zoom so the AWS control, Recalculate, Reset to base, and price are readable. Rehearse scrolling between controls and results before the timed take.
3. Verify base value $73.31 and terminal share 94.2%. Change AWS growth in 2026 from 24 to 28, click Recalculate, and check approximately $88.30. Reset and verify $73.31. These are AI-assisted exploratory results calculated from the current model; your actual recording must show a fresh successful run.
4. Verify the new diagnostic button **Test invalid terminal inputs**. Its labeled diagnostic preset uses WACC = terminal growth = 3%, outside the normal WACC control bounds, to reach the model's mathematical coherence check. Expect **WACC must exceed terminal growth.** No valuation may remain usable. Reset and verify $73.31. This specific UI addition must be present and locally rehearsed before using the script. Do not substitute the older **Demonstrate cash error** button: that injects an accounting discrepancy rather than incoherent economic assumptions.
5. Open `docs/decision-memo.md` and `docs/assumption-challenges.md` in reserve. The main recording should stay on the dashboard. Review the historical cutoff, source checks, cost of capital, and terminal assumptions before endorsing the draft. Browser interaction was not verified by the script author.

## Timed screen plan

| Time | Show and do | Point the audience should understand |
|---|---|---|
| 0:00-0:10 | Base dashboard, company/date banner and price | Historical exercise; proposed decision is defer initiation |
| 0:10-0:30 | AWS growth in 2026: 24 -> 28; Recalculate; show $88.30; Reset to base; show $73.31 | A bounded live input changes output; reset is reproducible |
| 0:30-1:00 | Show Terminal-input diagnostic panel; Test invalid terminal inputs; show WACC=g=3% error and withheld value; Reset | Incoherent inputs are rejected and recovery works |
| 1:00-1:45 | Operating forecast and free cash flow; briefly indicate capex row | Growth creates value only when capacity spending earns adequate returns |
| 1:45-2:25 | Saved-base cases, all three rows | Joint economic cases, not statistical confidence bounds |
| 2:25-3:05 | Saved-base WACC x terminal growth and sensitivity table | Terminal dependence and uncalibrated WACC limit conviction |
| 3:05-3:40 | Market-implied expectation | Conditional reverse DCF explains the gap without claiming investor beliefs |
| 3:40-4:10 | Value bridge, then Sources and limits | Reconcile enterprise to equity and name material conventions |
| 4:10-4:40 | Return to top/base result | Clear committee request and conditions for revisiting it |

Allow clicking pauses. At an ordinary pace the script below should fit with brief navigation; rehearse with a timer. If a live number differs, stop, investigate, and update the script instead of reading the expected number over conflicting evidence.

## Word-for-word rehearsal script

**0:00-1:00 — live demonstration**

“My proposed decision is to defer initiating Amazon. This is a historical exercise as of February sixth, 2026.

“The base model shows seventy-three dollars and thirty-one cents per share. I’ll change initial AWS growth from twenty-four to twenty-eight percent and recalculate. The result rises to eighty-eight dollars and thirty cents. Reset restores the original result.

“Now I’ll test invalid terminal inputs. This diagnostic preset deliberately makes WACC and terminal growth both three percent. It sits outside the normal scenario bounds. The model rejects it because WACC must exceed growth; otherwise the terminal-value denominator is zero. It withholds the valuation. Reset returns us to the valid base. This is a software demonstration, separate from my required independent validation exercise.”

**1:00-1:45 — investment mechanism**

“The central question is whether Amazon can turn infrastructure spending into enough additional operating profit and cash flow. Higher AWS revenue is helpful, but it is not free: this model increases later capital investment when AWS grows faster.

“The base begins with twenty-four percent AWS growth, fading two percentage points annually. North America begins at nine and a half percent, and international at ten. The two-hundred-billion-dollar investment assumption is anchored to management’s outlook; treating that amount as cash investment and assuming its later decline are modeling choices that still need reconciliation. Stock compensation remains an economic expense in free cash flow.”

**1:45-2:25 — cases and interpretation**

“The saved downside, base, and upside cases produce about five dollars, seventy-three dollars, and one hundred seventy-nine dollars per share, compared with the historical two-hundred-ten-dollar closing price.

“The upside combines stronger growth and margins with better capital productivity and a lower discount rate. The downside combines weaker growth and margins with higher spending. These are joint economic scenarios, not probability bounds. Even the upside is below the comparison price, but I would not treat that as a validated sell conclusion: our fund has no position, and key assumptions remain unresolved.”

**2:25-3:05 — sensitivity and limits**

“About ninety-four percent of base enterprise value comes from the terminal period. That makes sustainable margins, reinvestment, and the discount rate especially important.

“The ten-percent WACC is currently a hurdle assumption, not a completed market-based estimate. Terminal growth is three percent, with fifteen-percent incremental return on capital determining required reinvestment. The model changes to that terminal investment rule after the explicit forecast, so I need to test whether the transition is economically credible. Passing the balance-sheet checks does not resolve those judgments.”

**3:05-3:40 — reverse DCF**

“Holding the explicit cash flows and other base assumptions fixed, matching the historical price requires roughly a thirty-one-percent terminal operating margin. That is a conditional model result, not a claim about what investors actually forecast.

“Increasing initial AWS growth alone did not match the price within the tested ten-to-forty-percent bracket. That focuses the research on a combination of margins, capital productivity, and required returns, rather than relying on one optimistic growth number.”

**3:40-4:10 — bridge and evidence**

“The bridge adds excess cash, securities, and a discounted private-investment value, then subtracts debt, finance leases, and financing obligations before dividing by a diluted share proxy. The private-investment haircut and dilution estimate need review.

“The financial source is Amazon’s 2025 ten-K, alongside its February earnings release and a dated historical price. The December balance sheet is a proxy for the February valuation date.”

**4:10-4:40 — committee request**

“My request is to keep Amazon on the watchlist and defer committing capital. I would revisit initiation after independently verifying the inputs, calibrating WACC, reconciling investment and depreciation, and supporting the terminal margin and reinvestment assumptions.

“A defensible value at least twenty percent above the comparison price would pass the model’s initial screen, but would not automatically justify buying. The next decision should depend on corroborated capital productivity and an adequate return cushion. AI assisted the research, code, and this rehearsal draft; the final judgment needs to be mine.”

## Rehearsal numbers and verification provenance

These are model outputs, not independent financial facts. Computed by the assistant from `model.calculate()` and `model.calculate({'aws_growth': .28})` on October 19, 2026:

| Metric | Base (AWS initial growth 24%) | Exploratory change (28%) |
|---|---:|---:|
| Value per share | $73.30570850 | $88.29875792 |
| Difference from base | — | +$14.99304941 |
| 2030 FCFF, USD millions | 91,119.43 | 101,225.30 |
| 2030 cash capex, USD millions | 174,000.00 | 193,577.82 |
| Model accounting/funding checks | Pass | Pass |

The growth example demonstrates the capacity feedback: faster AWS growth raises projected 2030 capital investment as well as FCFF. Do not label this AI-assisted run as the student's locked prediction test. Saved-base scenarios, sensitivity, and reverse-DCF sections remain fixed when live controls change; reset before presenting those sections.

## After recording

Keep the actual recording at or below five minutes, watch it once, and make sure both the value change and failed-check recovery are visible. Create a transcript that matches what you actually said and use actual recording timestamps in the submission manifest. Do not mark the video, transcript, link access, or live test complete until those actions have occurred. Add the instructor-approved delivery link and access verification only after testing it.
