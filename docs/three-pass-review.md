# Three-pass review - October 19, 2026

AI-assisted educational review, not investment advice. Review scope: current course instructions/transcripts available in this conversation, current model arithmetic, primary source spot checks, and script/UI consistency. This is not a claim of an exhaustive independent financial audit, human student validation, or completed browser test.

## Pass 1 - sources, requirements and provenance

The course specifies separate 3/5/5-minute recordings, corrected transcripts, small webcam view unless accommodated, and a Project 1 live demonstration. Missing Edition A remains missing evidence. Updated wording removes any implication that the user's request constitutes verified instructor approval. The uploaded ABG transcripts use FCFE/cost of equity; Amazon follows the local FCFF/WACC assignment architecture.

Primary checks repeated on Amazon FY2025 10-K and February earnings release: segment EBIT reconciliation, balance-sheet totals, current debt, debt face values/maturities, lease balances, PPE depreciation, capex-payable classification, financing obligations and Anthropic balances. These are assistant checks, not the student's independent evidence. Source: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm .

Management's approximately $200bn outlook applies across Amazon. It does not alone validate the model's cash-capex-plus-lease interpretation or later spending path. Source: https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/ . The February 6 historical $210.32 close was reconfirmed in Yahoo historical data and a separate market report; the model date remains a proposed historical exercise, not a current recommendation.

No fresh exhaustive verification of every peer input, every history field or every source date is claimed. Existing peer consistency qualifications remain open. Three-year historical analysis, complete assumption origin labels, independent source-check evidence and the required course training case remain incomplete.

## Pass 2 - independently reconstructed arithmetic

A separate agent reconstructed first-year arithmetic from raw inputs and recomputed DCF using Decimal arithmetic. Results agree with the current model:

| Measure | Result, USD millions unless per share |
|---|---:|
| 2026 revenue | 804,506.375 |
| 2026 PPE depreciation | 58,847.208 |
| 2026 EBIT | 100,585.880 |
| Opening operating working capital | -67,191.000 |
| 2026 change in working capital | -8,208.328 |
| 2026 FCFF | -56,848.111 |
| PV explicit FCFF | 44,175.523 |
| PV terminal value | 711,091.233 |
| Enterprise value | 755,266.756 |
| Net equity bridge adjustment | +44,199.500 |
| Equity value | 799,466.256 |
| Value per share | 73.30570850 |

Eight automated test methods now pass, including all 512 nine-control corner combinations and a new check preventing mismatched cash-flow/discount-time arrays. All 29 base checks pass. The mismatched-array bug was real but did not affect existing model results because their arrays have equal length.

## Pass 3 - scripts and display behavior

Verified computational rehearsal values: AWS initial growth 24% -> 28% gives $73.31 -> $88.30; joint downside $5.21, upside $179.16; terminal share 94.2%; conditional market-implied terminal EBIT margin 31.3%. WACC 8/10/12% produces approximately $108.68/$73.31/$53.90 with other assumptions fixed.

The terminal-input diagnostic sets WACC=growth=3%, calls the actual validation guard, and withholds value. Recovery recalculates/restores the valid base. Recalculate and Reset buttons were moved above the driver controls to reduce scrolling. All nine initial control values fit their numeric bounds and steps. JavaScript syntax was checked; browser interaction remains unverified in this restricted environment. The guide's diagnostic location is the separate Terminal-input diagnostic panel, not the older cash-error disclosure.

## Material unresolved findings

1. **Margin calibration:** 2026 pre-PPE-depreciation operating income rises 30.82% on revenue growth of 12.22%. Applying the proposed segment margins to 2025 does not reconcile to historical PPE depreciation. These are judgmental margin improvements, not historical estimates.
2. **Investment definition and depreciation:** the $200bn cash-capex mapping, separate lease additions, six-year blended life and legacy depreciation runoff need evidence. Forecast PPE depreciation reaches about $163.78bn by 2030 under these conventions.
3. **Terminal transition:** FCFF drops from $91.12bn in 2030 to $79.39bn in 2031 (-12.87%). Net reinvestment rises from $5.23bn to $19.85bn. Do not describe the base transition as a release of terminal cash. A justified convergence schedule is still needed.
4. **Cost of capital:** 10% is an assumed hurdle. No 60-month beta estimation or date-matched market WACC has been completed.
5. **Timing:** discount exponents are arithmetically correct, but December balances and full-year 2026 flows are not reconciled to the February valuation date. A true stub-period bridge remains due.
6. **Decision evidence:** scripts propose watch/defer because of unresolved calibration. That does not establish an economically defensible valuation range. Quantified monitoring triggers and authentic human evidence remain due.

Result: useful rehearsal materials and an internally consistent computational draft; not certification that the project is ready for final investment presentation or submission.
