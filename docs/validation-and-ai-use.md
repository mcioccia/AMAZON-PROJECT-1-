# Validation and AI Use - Amazon Project 1

Final submission draft | October 19, 2026

AI-assisted educational coursework; not financial or investment advice. This record reports completed checks and openly identifies evidence not supplied. A final document version is not an assertion of full submission readiness.

**AI contribution**

AI researched public filings, transcribed inputs, proposed assumptions, wrote Python and HTML, prepared reports and scripts, and generated automated tests. The source comparison in the research presentation was also AI-assisted. The original local META Edition A contains its own AI-use disclosure and has been preserved unchanged. The later Amazon note is not portrayed as a pre-model checkpoint.

**Completed calculation checks**

Eight automated test methods passed on October 19, 2026. Coverage includes a known-answer perpetuity identity, stored historical-total reconciliation, base and joint scenarios, directional sensitivities, invalid inputs, missing discount-time rejection, deliberate cash-error rejection/recovery, terminal-domain rejection/recovery, and evaluation of 512 bounded-control corners.

The base run passes 29 checks. Separately summing discounted forecast cash flows, calculating terminal cash flow from NOPAT and growth/ROIC reinvestment, and applying the equity bridge reproduces $73.3057085 per share with no difference at the displayed precision. This recomputation uses the model's existing cash flows and assumptions; it is not an independent economic forecast.

**Failure behavior and observed student execution**

The cash-error demonstration adds $1,000 million to first-year cash without a corresponding flow. Reconciliation checks fail and valuation is None. A clean recalculation returns a valid result. The terminal diagnostic sets WACC and growth to 3%, causing rejection before valuation.

Student-provided terminal screenshots show eight passing tests, a rebuilt $73.31 base report with 29/29 checks, the injected cash failure, and recovery. This establishes visible execution evidence. It does not establish a pre-run AI-off prediction, a partner cold run, or instructor repository access.

**Limits of validation**

Source-total tests check transcribed arithmetic, not independent retrieval of filings. The perpetuity test is synthetic and does not satisfy a separate course training-case reconciliation. All-corner tests check numerical behavior and accounting consistency, not the plausibility of every scenario. Model outputs remain conditional on uncalibrated margins, WACC, investment/lease treatment, and terminal assumptions.

**Evidence not yet supplied or verified**

The student's AI-off highest-risk claim and three failures; a locked changed-input prediction with pre-run timestamp, frozen version, observed outcome and reconciliation; the required independent source check; course training-case reconciliation; partner/fresh-environment reproduction; and complete reviewer access evidence. These are not fabricated or inferred from AI-generated tests.

**Recordings and repository**

Three local final recordings exist: Video 1 3:16.467, Video 2 4:57.267, Video 3 4:50.609. Full content and transcripts have not been verified by the assistant. Video 1 exceeds the previously reviewed three-minute limit; confirm the current handout or obtain an applicable exception before treating it as compliant.

Student-supplied repository: https://github.com/mcioccia/AMAZON-PROJECT-1-

The reviewed downloaded repository ZIP placed required files at the top level, leaving data/inputs.json and static/index.html absent. Running that copy failed with FileNotFoundError. The local working project retains the expected structure. A newly uploaded ZIP must be checked before marking remote reproduction repaired. Private/public visibility and instructional-team access are unverified.

**Submission audit interpretation**

The last official audit reported mechanical gaps in all 11 required rows, including missing access confirmations for existing documents. Its exit code was zero despite these gaps. Finalize locations, corrected transcripts, timestamp indexes, access evidence and frozen identifiers, then rerun and read the audit output. Never treat a zero exit code or a populated field as proof of substantive completion.
