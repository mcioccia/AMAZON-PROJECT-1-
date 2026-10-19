# Peer comparison — limited diagnostic

AI-assisted educational draft; not investment advice. Policy: use profitable US-listed digital platforms with FY2025 accounts available by February 6, 2026. Alphabet and Meta provide cloud/platform/advertising checks. Neither reproduces Amazon's retail, logistics or cash-conversion mix. A retail comparator and segment weighting are still needed before using peers to support a recommendation. This policy is documented before the calculations below, but was drafted retrospectively during this work; no contemporaneous student selection record is claimed.

Use February 6 unadjusted share prices, December 31 point shares across all classes (Amazon uses January 28 point shares), FY2025 GAAP EBIT and diluted EPS, face interest-bearing debt plus finance leases/financing, less cash and marketable securities. Price all Alphabet classes at GOOGL and both Meta classes at META; this approximation needs a class-price reconciliation. No operating-lease capitalization, private-investment deduction or operating cash reserve in the standard comparison EV. Thus this EV differs deliberately from the DCF bridge; reconcile that difference before translating a multiple into a target price. Noncontrolling interests are not yet reconciled and peer EV is provisional.

| Input ($m except price/EPS) | AMZN | GOOGL | META |
|---|---:|---:|---:|
| Historical close | 210.32 | 322.86 | 661.46 |
| Point shares (m) | 10,734.920870 | 12,088 | 2,530 |
| Interest debt face | 69,291 | 49,085 | 59,000 |
| Finance lease/financing | 20,444 | 2,500 | 1,184 |
| Cash + marketable securities | 123,029 | 126,843 | 81,592 |
| EBIT | 79,975 | 129,039 | 83,276 |
| Diluted EPS | 7.17 | 10.81 | 23.49 |

Recompute: market cap = price × point shares; EV = market cap + face debt + finance lease/financing − cash/securities; EV/EBIT = EV ÷ reported EBIT; P/E = price ÷ reported diluted EPS. EPS is weighted-average diluted while market cap uses point shares, so P/E is not exactly market cap divided by net income. Generated values appear in outputs/peer-check.json.

Reported earnings contain material distortions: Amazon's investment gains and exceptional operating charges; Alphabet's investment gains; Meta's tax valuation allowance. P/E is a weak cross-check without normalization. EV/EBIT also requires review of recurring legal/restructuring expense. Do not average these multiples mechanically or treat the peers as a target-price engine.

Sources:

- Amazon inputs: data/inputs.json and the FY2025 10-K linked there.
- Alphabet FY2025 10-K, debt/lease/share notes: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm ; earnings: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000012/googexhibit991q42025.htm ; price: https://finance.yahoo.com/quote/GOOGL/history/ .
- Meta FY2025 10-K: https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm ; earnings: https://www.sec.gov/Archives/edgar/data/1326801/000162828026003832/meta-12312025xexhibit991.htm ; price: https://ca.finance.yahoo.com/quote/META/history/ .
