"""Rebuild visible outputs. AI-assisted education only, not investment advice."""
import csv
import datetime
import hashlib
import html
import json
from pathlib import Path
from model import analyses, load, NOTICE

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'outputs'

def table(headers, rows):
    def cell(x): return html.escape(str(x))
    return '<table><thead><tr>'+''.join('<th>'+cell(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+cell(x)+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>'

def fmt(x): return f'{x:,.2f}'

def main():
    OUT.mkdir(exist_ok=True)
    a=analyses(); d=load(); b=a['base']; v=b['value']; years=b['years']
    (OUT/'analysis.json').write_text(json.dumps(a,indent=2,allow_nan=False),encoding='utf-8')
    peer_inputs=[('AMZN',210.32,10734.920870,69291,20444,123029,79975,7.17),('GOOGL',322.86,12088,49085,2500,126843,129039,10.81),('META',661.46,2530,59000,1184,81592,83276,23.49)]
    peers=[]
    for ticker,price,shares,debt,leases,cash,ebit,eps in peer_inputs:
        ev=price*shares+debt+leases-cash
        peers.append({'ticker':ticker,'price':price,'shares':shares,'face_debt':debt,'finance_leases_and_financing':leases,'cash_and_securities':cash,'ebit':ebit,'eps':eps,'ev':ev,'ev_ebit':ev/ebit,'pe':price/eps})
    (OUT/'peer-check.json').write_text(json.dumps({'status':'Provisional; see docs/peer-check.md for exclusions and comparability limits','peers':peers},indent=2),encoding='utf-8')
    with (OUT/'forecast.csv').open('w',newline='',encoding='utf-8') as f:
        keys=['year','revenue','ebit','net_income','depreciation','sbc','capex','finance_lease_additions','change_nwc','fcff','cfo','cfi','cff']
        w=csv.DictWriter(f,fieldnames=keys); w.writeheader();w.writerows({k:y[k] for k in keys} for y in years)
    body='<h1>Amazon — reproducible working result</h1><p>'+NOTICE+'</p><p>Historical valuation: February 6, 2026. Forecast: 2026–2030. Review assumptions before use. Not submission-ready.</p>'
    body+=f'<div class="hero"><strong>${v["per_share"]:.2f}</strong> modeled value per share · {v["upside"]:.1%} vs historical $210.32 · {v["terminal_share"]:.1%} terminal share of EV</div>'
    body+='<h2>Decision status</h2><p>Watch/defer initiation pending margin, investment and WACC validation. The mechanical downside screen is not an independently established investment conclusion.</p>'
    body+='<h2>Cases</h2>'+table(['Case','Value/share','2030 EBIT ($m)','2030 FCFF ($m)'],[[k,fmt(r['value']['per_share']),fmt(r['years'][-1]['ebit']),fmt(r['years'][-1]['fcff'])] for k,r in a['scenarios'].items()])
    body+='<h2>Income and investment ($m)</h2>'+table(['Line',*[y['year'] for y in years]],[[k,*[fmt(y[k]) for y in years]] for k in ['revenue','predep_income','depreciation','ebit','interest','pretax','taxes','net_income','capex','finance_lease_additions','change_nwc','fcff']])
    body+='<h2>Balance sheets ($m)</h2>'+table(['Line',2025,*[y['year'] for y in years]],[[k,fmt(b['opening_balance_sheet'][k]),*[fmt(y['balance_sheet'][k]) for y in years]] for k in b['opening_balance_sheet']])
    body+='<h2>Cash flows ($m)</h2>'+table(['Line',*[y['year'] for y in years]],[[k,*[fmt(y[k]) for y in years]] for k in ['net_income','depreciation','sbc','change_nwc','cfo','cfi','debt_repaid','lease_principal','financing_principal','borrowing','cff']])
    body+='<h2>Valuation bridge ($m)</h2>'+table(['Line','Value'],[[k,fmt(v[k])] for k in ['pv_explicit','pv_terminal','ev']]+[[k,fmt(x)] for k,x in v['bridge'].items()]+[['equity',fmt(v['equity'])],['Diluted shares (m)',fmt(b['assumptions']['diluted_shares'])]])
    body+='<h2>One-at-a-time sensitivities</h2>'+table(['Driver','Low input','High input','Low value','High value','Full span','Half span'],[[r['label'],r['low_input'],r['high_input'],fmt(r['low_value']),fmt(r['high_value']),fmt(r['span']),fmt(r['half_range_span'])] for r in sorted(a['sensitivities'],key=lambda r:r['span'],reverse=True)])
    body+='<h2>WACC / terminal growth</h2>'+table(['WACC','2%','2.5%','3%','3.5%','4%'],[[f'{r["wacc"]:.0%}',*[fmt(x) for x in r['cells']]] for r in a['grid']])
    body+='<h2>Reverse DCF</h2><p>'+html.escape(a['reverse_dcf']['status'])+f'. Holding explicit cash flows and other assumptions fixed, the historical price implies a terminal EBIT margin of {a["reverse_dcf"]["implied_2031_margin"]:.1%}. This is a conditional identity, not observed investor expectations.</p>'
    body+='<h2>Checks</h2>'+table(['Check','Passed','Residual'],[[c['name'],c['passed'],c['residual']] for c in b['checks']])
    body+='<h2>Provisional peer diagnostics</h2>'+table(['Ticker','EV/EBIT','P/E'],[[p['ticker'],fmt(p['ev_ebit']),fmt(p['pe'])] for p in peers])+'<p>GAAP denominators, price-class approximations and incomplete minority-interest reconciliation limit comparison. See ../docs/peer-check.md. No mechanical average or peer target price is used.</p>'
    body+='<h2>Sources</h2>'+''.join('<p>'+html.escape(k)+': <a href="'+html.escape(u,quote=True)+'">'+html.escape(u)+'</a></p>' for k,u in d['sources'].items())
    body+='<p>See ../docs/assumption-challenges.md for normalization, methodology, source caveats and assumptions. See ../docs/STUDENT_ACTIONS.md for remaining requirements.</p>'
    page='<!doctype html><html lang="en"><meta charset="utf-8"><title>Amazon working result</title><style>body{font:15px/1.6 system-ui;color:#213347;max-width:1200px;margin:35px auto;padding:20px;background:#f6f8fa}h1,h2{color:#172a3c}h2{margin-top:35px}table{width:100%;border-collapse:collapse;background:white;font-size:12px}td,th{padding:8px;border-bottom:1px solid #dce3ea;text-align:right}td:first-child,th:first-child{text-align:left}.hero{padding:24px;background:#172a3c;color:white;border-left:6px solid #f6a137}.hero strong{font-size:32px}a{overflow-wrap:anywhere}</style>'+body+'</html>'
    (OUT/'visible-result.html').write_text(page,encoding='utf-8')
    cases='\n'.join(f'- {name}: ${r["value"]["per_share"]:.2f}/share.' for name,r in a['scenarios'].items())
    memo=f'''# Decision memo — provisional draft

{NOTICE}

**Proposed action: watch/defer initiation pending validation.** Fund has no existing position. Historical as-of date February 6, 2026; proposed holding horizon 3–5 years. This is not a current market recommendation.

The model produces ${v['per_share']:.2f}/share against the historical $210.32 close. {v['terminal_share']:.1%} of operating value is terminal value. Do not treat a precise displayed number as a validated price target: segment depreciation allocation, the cash-investment interpretation, WACC and terminal convergence remain unresolved.

Joint scenario values (not probability bounds):

{cases}

Retail and AWS revenue drive operating cash generation; large infrastructure spending reduces early free cash flow. The upside case combines stronger demand and margins with better capital productivity and a lower discount rate. The downside combines weaker conversion, higher spending and a higher required return. Single-driver tables show which chosen ranges dominate, and half-range spans test dependence on those bounds. These are model outputs rather than a student's independent thesis.

At unchanged explicit cash flows, the historical price requires a terminal EBIT margin of {a['reverse_dcf']['implied_2031_margin']:.1%} under the chosen WACC/growth/ROIC. {a['reverse_dcf']['status']}. Neither result identifies investors' actual beliefs.

Revisit initiation only after corroborating sustainable margins and cash investment, calibrating date-matched WACC, reconciling leases and dilution, and checking a defensible return cushion. A model price at least 20% above market is a screening condition, not sufficient evidence to initiate. Defer if data/model uncertainty prevents defending those conditions. The student's own highest-risk claim and three possible failures must be written without AI as required.

Sources, assumptions and historical normalization: assumption-challenges.md. Reproducible tables: ../outputs/visible-result.html and analysis.json. No revenue, accounting or valuation result here substitutes for the required access, provenance, human testing and recordings.
'''
    (ROOT/'docs'/'decision-memo.md').write_text(memo,encoding='utf-8')
    hashes={str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(ROOT.rglob('*')) if p.is_file() and '__pycache__' not in str(p) and p.name!='freeze.json' and p.suffix not in ('.zip',)}
    (OUT/'freeze.json').write_text(json.dumps({'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256':hashes},indent=2),encoding='utf-8')
    print(NOTICE);print(f'Rebuilt outputs. Base ${v["per_share"]:.2f}; {sum(c["passed"] for c in b["checks"])}/{len(b["checks"])} base checks pass.')

if __name__=='__main__': main()
