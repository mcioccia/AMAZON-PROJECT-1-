# Assumptions and challenges

AI-assisted educational draft; not investment advice. Every forecast is a proposal requiring student review. No student AI-off claim is written here.

## Sources and timing

Base financial data: Amazon FY2025 Form 10-K, consolidated statements and notes on leases, debt, property, investments and segments: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm . Management's February 5 release: https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/ . Historical unadjusted February 6 close: https://finance.yahoo.com/quote/AMZN/history/?p=AMZN ; cross-check https://www.financecharts.com/stocks/AMZN/summary/price . Inputs were manually transcribed by AI; independent student source checks remain due. The December balance sheet is a proxy at the February valuation date. Full 2026 cash flows are discounted to December year-end without a January-to-February stub adjustment. This approximation needs correction for a precise point-date valuation.

## Historical normalization

FY2025 reported EBIT is $79,975m. Candidate exceptional operating charges are FTC settlement $2,500m, severance $2,700m, impairment $1,300m and tax-dispute and lawsuit settlements $1,100m. Full addback would give $87,575m; this is a sensitivity, not an assertion all costs are nonrecurring. Q4 severance and impairment are included in annual totals and must not be added twice. Recurring restructuring and legal costs challenge full normalization. Forecast operating margins are independently assumed; the model does not mechanically grow adjusted EBIT. Investment gains and interest income do not recur in forecast operating earnings. PPE depreciation ($41,900m, rounded in note) is used instead of the broader cash-flow depreciation/amortization line, which includes other categories.

## Value / basis / challenge / evidence needed

| Driver | Working assumption and basis | Challenge and evidence needed |
|---|---|---|
| AWS growth | 24% initial, fades 2 percentage points annually; recent quarterly growth anchor | Verify backlog conversion, pricing, competition and capacity; revenue growth alone is insufficient if investment rises with it |
| Retail growth | NA 9.5%, international 10%, fade 0.5 points/year | Currency, mix, advertising and mature-market demand need separate tests |
| Pre-PPE depreciation margins | NA 11.5%, international 6.5%, AWS 59%; retail improves 0.2 points/year | Not reported segment EBITDA; allocate actual historical PPE depreciation by segment before relying on these assumptions |
| Cash capex | $200bn in 2026; path 100%,95%,90%,88%,87% | Management outlook is an anchor, but its mapping to cash purchases and lease assets must be reconciled. A decline after 2026 is an analyst assumption |
| Capacity response | Later capex scales with AWS revenue to elasticity 0.65 | Test whether capacity needed per dollar of growth is higher; validate against utilization and infrastructure unit economics |
| PPE depreciation | Six-year blended life, half-year convention; existing depreciation decays 15%/year | Mixed assets have different lives; vintage detail and retirements are simplified |
| Tax | 21% on positive profits, no loss tax benefit | Not a calibrated global effective cash tax forecast |
| WACC | 10% hurdle, range 8–12% | Not yet estimated from date-matched risk-free rate, ERP, beta and capital structure. Complete that work before endorsing valuation |
| Terminal | Growth 3%, incremental ROIC 15% | NOPAT growth/ROIC determines reinvestment. Explicit investment resets at terminal date; test smooth convergence and maintenance spending |
| Liquidity | $25bn cash floor; additional debt ceiling $250bn | Not committed funding. Interest on new debt begins next year. Stress funding access and retained cash policies |
| Share count | 10,905.920870m = January point shares plus FY2025 diluted/basic weighted-average gap | Timing mismatch; replace with date-specific treasury stock/options dilution if available. SBC remains an economic expense in FCFF |
| Private investment | Anthropic carrying $60.6bn ×75% realization ×79% tax factor | Carrying value is not liquidity or market value. Tax factor is a conservative haircut, not tax-basis computation; existing deferred taxes may overlap. Other private assets excluded |

## Statement and valuation conventions

Operating working capital scales with revenue. Capex payables are separated from trade payables and held fixed. Current debt, leases and financing are reclassified out of operating accruals. Finance-lease additions count as investment in FCFF and increase PPE and lease debt; principal repayments belong to financing cash flow. Operating rent remains an operating cost, with no additional operating-lease deduction from EV. ROU and operating-lease liabilities move equally, simplifying new additions/amortization. Other assets, goodwill, securities and other liabilities are held constant; impairment, disposals, foreign-exchange movements and dividends/buybacks are omitted. Equity rolls forward by net income and SBC.

FCFF = EBIT after operating tax + PPE depreciation − cash capex − finance-lease additions − change in operating working capital. Do not add SBC back to FCFF. Enterprise value is discounted FCFF plus terminal value; excess cash, marketable securities and discounted private investment are added, debt at face, finance leases and financing obligations subtracted. Forecast statements use book debt. These simplified linked statements are internally checked, but a balancing result does not establish economic validity.

## External reading critique

Damodaran's Project Format (https://pages.stern.nyu.edu/adamodar/New_Home_Page/eqprojform.htm) encourages an investment view linked to valuation and sensitivity. Its generic format does not establish this course's evidence, replay, AI-use or video requirements. GitHub's About READMEs section and content list (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) help a newcomer find a project's purpose and usage. A runnable command alone cannot verify dated financial inputs or defensible assumptions. This README therefore specifies units, cutoff, expected result, failure behavior and remaining evidence; the local course architecture remains authoritative.
