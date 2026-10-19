"""AI-assisted educational model. Not investment advice. USD millions throughout."""
from __future__ import annotations
import copy
import datetime as dt
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOTICE = 'AI-assisted coursework draft. Educational purposes only; not investment advice.'

def load():
    return json.loads((ROOT / 'data' / 'inputs.json').read_text(encoding='utf-8'))

def npv(flows, rate, times):
    if len(flows) != len(times):
        raise ValueError('Each cash flow must have exactly one discount time.')
    if rate <= -1:
        raise ValueError('Discount rate must exceed -100%.')
    return sum(c / (1 + rate)**t for c, t in zip(flows, times))

def opening(h):
    return {
        'cash':h['cash'], 'securities':h['securities'], 'inventory':h['inventory'],
        'receivables':h['receivables'], 'ppe':h['ppe'], 'rou':h['rou'],
        'goodwill':h['goodwill'], 'other_assets':h['other_assets'],
        'trade_payables':h['payables']-h['capex_payable'], 'capex_payable':h['capex_payable'],
        'operating_accruals':h['accruals']-h['current_debt']-h['current_leases']-h['short_debt']-h['current_financing'],
        'unearned':h['unearned'], 'operating_leases':h['operating_leases'],
        'debt':h['long_debt']+h['current_debt']+h['short_debt'],
        'finance_leases':h['finance_leases'], 'financing_obligations':h['financing_obligations'],
        'other_liabilities':h['other_liabilities']-(h['financing_obligations']-h['current_financing']),
        'equity':h['equity']
    }

ASSETS = ['cash','securities','inventory','receivables','ppe','rou','goodwill','other_assets']
LIABS = ['trade_payables','capex_payable','operating_accruals','unearned','operating_leases','debt','finance_leases','financing_obligations','other_liabilities']

def balance(b):
    return sum(b[k] for k in ASSETS)-sum(b[k] for k in LIABS)-b['equity']

def nwc(b):
    return b['inventory']+b['receivables']-b['trade_payables']-b['operating_accruals']-b['unearned']

def calculate(overrides=None, data=None, break_cash=False, allow_outside=False):
    d=copy.deepcopy(data or load()); h=d['history']; a=d['assumptions']
    if overrides:
        for k,v in overrides.items():
            if k not in d['controls']: raise ValueError('Unknown control: '+k)
            if isinstance(v,bool) or not isinstance(v,(float,int)) or not math.isfinite(v): raise ValueError('Input must be a finite number: '+k)
            c=d['controls'][k]
            if not allow_outside and not c['min']<=v<=c['max']: raise ValueError('Outside permitted range: '+k)
            a[k]=v
    if a['wacc'] <= a['terminal_growth']: raise ValueError('WACC must exceed terminal growth.')
    if a['terminal_roic'] <= a['terminal_growth']: raise ValueError('Terminal ROIC must exceed growth.')
    b=opening(h); initial=copy.deepcopy(b); prev_rev=h['revenue']; seg_rev=h['segment_sales'].copy()
    checks=[{'name':'Historical balance sheet matches filing','residual':balance(b),'passed':abs(balance(b))<.01},
            {'name':'Historical assets match filing','residual':sum(b[k] for k in ASSETS)-h['total_assets'],'passed':abs(sum(b[k] for k in ASSETS)-h['total_assets'])<.01},
            {'name':'Segment revenue reconciles','residual':sum(seg_rev)-h['revenue'],'passed':sum(seg_rev)==h['revenue']},
            {'name':'Segment EBIT reconciles','residual':sum(h['segment_ebit'])-h['ebit'],'passed':sum(h['segment_ebit'])==h['ebit']}]
    records=[]; vintages=[]; additional_debt=0
    for i,year in enumerate(range(2026,2031)):
        old=copy.deepcopy(b)
        growths=[a['retail_growth']-i*.005,a['international_growth']-i*.005,a['aws_growth']-i*.02]
        seg_rev=[r*(1+g) for r,g in zip(seg_rev,growths)]; rev=sum(seg_rev)
        capex=a['capex_2026']*a['capex_path'][i]
        # Capacity scales after 2026 with AWS revenue relative to the reference growth path.
        reference_aws=h['segment_sales'][2]
        for j in range(i+1): reference_aws*=1+d['reference_aws_growth']-j*.02
        if i: capex*= (seg_rev[2]/reference_aws)**a['capacity_elasticity']
        lease_add=a['finance_lease_additions']*(rev/h['revenue'])
        investment=capex+lease_add
        life=a['asset_life']; old_da=h['ppe_da']*a['legacy_da_decay']**i
        da=old_da
        for vintage_year,amount in vintages+[(i,investment)]:
            age=i-vintage_year
            # Half-year convention, with final half-year retirement at the chosen life.
            fraction=.5 if age in (0,life) else (1 if 0<age<life else 0)
            da+=amount/life*fraction
        da=min(da,old['ppe']+investment); vintages.append((i,investment))
        # Pre-PPE-depreciation margins retain SBC, content and operating-lease expense.
        margins=[a['na_predep_margin']+i*.002,a['intl_predep_margin']+i*.002,a['aws_predep_margin']]
        predep=[r*m for r,m in zip(seg_rev,margins)]
        ebit=sum(predep)-da
        sbc=rev*a['sbc_ratio']
        interest=old['debt']*a['debt_cost']+old['finance_leases']*.034+old['financing_obligations']*.029
        interest_income=0 # Excluded cash/investment income; no double count in enterprise value.
        pretax=ebit-interest+interest_income
        taxes=max(pretax,0)*a['tax_rate']; ni=pretax-taxes
        for field in ('inventory','receivables','trade_payables','operating_accruals','unearned'):
            b[field]=initial[field]*rev/h['revenue']
        change_nwc=nwc(b)-nwc(old)
        # Operating rent expense equals payment; new ROU additions offset amortization.
        lease_growth=old['operating_leases']*(rev/prev_rev-1)
        b['operating_leases']+=lease_growth; b['rou']+=lease_growth
        b['ppe']=old['ppe']+investment-da
        cfo=ni+da+sbc-change_nwc
        maturity=a['debt_maturities'][i]
        lease_principal=min(old['finance_leases'],a['finance_lease_principal'])
        obligation_principal=min(old['financing_obligations'],a['financing_principal'])
        cfi=-capex
        before_funding=old['cash']+cfo+cfi-maturity-lease_principal-obligation_principal
        borrowing=max(0,a['cash_floor']-before_funding)
        additional_debt+=borrowing
        cff=borrowing-maturity-lease_principal-obligation_principal
        b['cash']=old['cash']+cfo+cfi+cff
        b['debt']=old['debt']+borrowing-maturity
        b['finance_leases']=old['finance_leases']+lease_add-lease_principal
        b['financing_obligations']=old['financing_obligations']-obligation_principal
        b['equity']=old['equity']+ni+sbc
        if break_cash and i==0: b['cash']+=1000
        # Keep stock compensation as an economic cost: do not add it back to FCFF.
        nopat=ebit-max(ebit,0)*a['tax_rate']
        fcff=nopat+da-investment-change_nwc
        fcff_from_cfo=cfo+interest-(max(ebit,0)*a['tax_rate']-taxes)-sbc-investment
        for name,res in [('Balance sheet',balance(b)),('Cash flow to cash',b['cash']-old['cash']-cfo-cfi-cff),('FCFF to CFO bridge',fcff-fcff_from_cfo)]:
            checks.append({'name':str(year)+' '+name,'residual':res,'passed':abs(res)<.01})
        checks.append({'name':str(year)+' funding ceiling','residual':max(0,additional_debt-a['borrowing_ceiling']),'passed':additional_debt<=a['borrowing_ceiling']})
        checks.append({'name':str(year)+' nonnegative asset and cash-cost balances','residual':None,'passed':min(b[k] for k in ASSETS)>=0 and rev-sum(predep)-sbc>=0})
        records.append({'year':year,'revenue':rev,'segment_sales':seg_rev.copy(),'segment_predep_income':predep,
          'predep_income':sum(predep),'depreciation':da,'ebit':ebit,'interest':interest,'pretax':pretax,'taxes':taxes,'net_income':ni,
          'sbc':sbc,'capex':capex,'finance_lease_additions':lease_add,'investment':investment,'change_nwc':change_nwc,
          'nopat':nopat,'fcff':fcff,'cfo':cfo,'cfi':cfi,'cff':cff,'borrowing':borrowing,'debt_repaid':maturity,
          'lease_principal':lease_principal,'financing_principal':obligation_principal,'balance_sheet':copy.deepcopy(b)})
        prev_rev=rev
    if not all(c['passed'] for c in checks):
        return {'valid':False,'checks':checks,'years':records,'assumptions':a,'value':None,'notice':NOTICE}
    date=dt.date.fromisoformat(d['valuation_date'])
    times=[(dt.date(y['year'],12,31)-date).days/365.25 for y in records]
    terminal_nopat=records[-1]['nopat']*(1+a['terminal_growth'])
    terminal_reinvestment=terminal_nopat*a['terminal_growth']/a['terminal_roic']
    terminal_fcff=terminal_nopat-terminal_reinvestment
    terminal_value=terminal_fcff/(a['wacc']-a['terminal_growth'])
    pv_terminal=terminal_value/(1+a['wacc'])**times[-1]
    pv_flows=npv([y['fcff'] for y in records],a['wacc'],times)
    ev=pv_terminal+pv_flows
    # Debt face values for bridge; book values remain in projected accounting statements.
    bridge={'excess_cash':max(0,h['cash']-a['cash_floor']), 'marketable_securities':h['securities'],
        'anthropic_value_after_haircut_and_tax':h['anthropic_carrying']*a['investment_realization']*(1-a['investment_tax']),
        'debt_face':-h['debt_face']-h['short_debt'],'finance_leases':-h['finance_leases'],
        'financing_obligations':-h['financing_obligations']}
    equity=ev+sum(bridge.values()); per_share=equity/a['diluted_shares']
    upside=per_share/d['market_price']-1
    action='Initiate candidate' if upside>=.2 else ('Do not initiate' if upside<=-.2 else 'Watch / defer')
    warnings=['Scenario assumptions are AI-assisted proposals awaiting student judgment.',
      'December balance sheet is a proxy at February valuation date; interim changes are not measured.',
      'Terminal phase resets investment to growth/ROIC; review the explicit-to-terminal transition.',
      'Borrowing is an assumed funding route, not committed access to capital.']
    if pv_terminal/ev>.75: warnings.append('More than 75% of operating value comes from the terminal period.')
    return {'valid':True,'notice':NOTICE,'valuation_date':d['valuation_date'],'market_price':d['market_price'],
      'assumptions':a,'opening_balance_sheet':initial,'years':records,'checks':checks,'warnings':warnings,
      'value':{'ev':ev,'equity':equity,'per_share':per_share,'upside':upside,'action':action,'bridge':bridge,
      'pv_explicit':pv_flows,'terminal_fcff':terminal_fcff,'terminal_nopat':terminal_nopat,'terminal_reinvestment':terminal_reinvestment,
      'terminal_value':terminal_value,'pv_terminal':pv_terminal,'terminal_share':pv_terminal/ev,'discount_times':times,
      'cumulative_borrowing':additional_debt}}

def terminal_failure_demo():
    """Explicit diagnostic preset; exercise the real terminal-domain guard."""
    d=load()
    d['assumptions']['wacc']=.03
    d['assumptions']['terminal_growth']=.03
    try:
        return calculate(data=d)
    except ValueError as exc:
        return {'valid':False,'value':None,'years':[], 'notice':NOTICE,
                'assumptions':d['assumptions'],
                'diagnostic_inputs':{'wacc':.03,'terminal_growth':.03},
                'checks':[{'name':str(exc),'passed':False,'residual':None}]}

def analyses():
    d=load(); base=calculate(); scenarios={}
    for name,overrides in d['scenarios'].items(): scenarios[name]=calculate(overrides)
    sensitivities=[]
    for key,c in d['controls'].items():
        lo=calculate({key:c['min']}); hi=calculate({key:c['max']})
        mid=d['assumptions'][key]; halflo=calculate({key:(mid+c['min'])/2}); halfhi=calculate({key:(mid+c['max'])/2})
        def val(r): return r['value']['per_share'] if r['valid'] else None
        low,high=val(lo),val(hi); hl,hh=val(halflo),val(halfhi)
        sensitivities.append({'driver':key,'label':c['label'],'low_input':c['min'],'high_input':c['max'],
          'low_value':low,'high_value':high,'span':abs(high-low) if low is not None and high is not None else None,
          'half_range_span':abs(hh-hl) if hl is not None and hh is not None else None,
          'low_2030_ebit':lo['years'][-1]['ebit'],'high_2030_ebit':hi['years'][-1]['ebit'],
          'low_2030_fcff':lo['years'][-1]['fcff'],'high_2030_fcff':hi['years'][-1]['fcff']})
    grid=[]
    for w in [.08,.09,.10,.11,.12]:
        grid.append({'wacc':w,'cells':[calculate({'wacc':w,'terminal_growth':g})['value']['per_share'] for g in [.02,.025,.03,.035,.04]]})
    # Conditional reverse DCF: capacity investment responds to AWS growth.
    low,high=.10,.40
    rlo=calculate({'aws_growth':low},allow_outside=True); rhi=calculate({'aws_growth':high},allow_outside=True)
    reverse={'status':'No feasible root in 10%-40% initial AWS growth bracket','aws_growth':None}
    if rlo['valid'] and rhi['valid'] and rlo['value']['per_share']<=d['market_price']<=rhi['value']['per_share']:
        for _ in range(55):
            mid=(low+high)/2; trial=calculate({'aws_growth':mid},allow_outside=True)
            if not trial['valid']: break
            if trial['value']['per_share']<d['market_price']: low=mid
            else: high=mid
        else:
            reverse={'status':'Conditional model solution, not observed market expectations','aws_growth':mid,
              'matched_value':trial['value']['per_share'],'outside_normal_bounds':not d['controls']['aws_growth']['min']<=mid<=d['controls']['aws_growth']['max']}
    v=base['value']; a=base['assumptions']
    target_ev=d['market_price']*a['diluted_shares']-sum(v['bridge'].values())
    implied_terminal_fcff=(target_ev-v['pv_explicit'])*(1+a['wacc'])**v['discount_times'][-1]*(a['wacc']-a['terminal_growth'])
    implied_terminal_nopat=implied_terminal_fcff/(1-a['terminal_growth']/a['terminal_roic'])
    reverse['implied_2031_ebit']=implied_terminal_nopat/(1-a['tax_rate'])
    reverse['implied_2031_margin']=reverse['implied_2031_ebit']/(base['years'][-1]['revenue']*(1+a['terminal_growth']))
    reverse['terminal_method']='Hold explicit cash flows, WACC, growth, ROIC and bridge fixed; solve terminal operating profit needed to match price.'
    return {'base':base,'scenarios':scenarios,'sensitivities':sensitivities,'grid':grid,'reverse_dcf':reverse}

if __name__=='__main__':
    import sys
    print(NOTICE)
    result=calculate(break_cash='--break-cash' in sys.argv)
    print(json.dumps(result,indent=2,allow_nan=False))
    sys.exit(0 if result['valid'] else 1)
