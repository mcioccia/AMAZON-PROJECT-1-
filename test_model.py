"""AI-assisted educational tests, not investment advice or a student AI-off exercise."""
import itertools
import math
import unittest
from model import calculate, load, npv, analyses, terminal_failure_demo

class ModelTests(unittest.TestCase):
    def test_npv_rejects_missing_discount_time(self):
        with self.assertRaises(ValueError): npv([10,1000],.10,[1])

    def test_terminal_diagnostic_and_recovery(self):
        r=terminal_failure_demo()
        self.assertFalse(r['valid'])
        self.assertIsNone(r['value'])
        self.assertEqual(r['diagnostic_inputs'],{'wacc':.03,'terminal_growth':.03})
        self.assertIn('WACC must exceed',r['checks'][0]['name'])
        self.assertEqual(r['years'],[])
        self.assertTrue(calculate()['valid'])

    def test_independent_known_answer(self):
        # A perpetuity paying 10 from year 1 at 10% is 100.
        # Split explicitly into three payments and a year-3 terminal value.
        self.assertAlmostEqual(npv([10,10,110], .10, [1,2,3]),100)

    def test_source_reconciliation(self):
        h=load()['history']
        self.assertEqual(sum(h['segment_sales']),716924)
        self.assertEqual(sum(h['segment_ebit']),79975)
        self.assertEqual(h['cash']+h['securities'],123029)

    def test_base_and_causal_cases(self):
        a=analyses()
        for r in [a['base'],*a['scenarios'].values()]:
            self.assertTrue(r['valid'])
            self.assertTrue(all(c['passed'] for c in r['checks']))
        self.assertLess(a['scenarios']['Downside']['value']['per_share'],a['base']['value']['per_share'])
        self.assertGreater(a['scenarios']['Upside']['value']['per_share'],a['base']['value']['per_share'])

    def test_directional_predictions(self):
        # Predictions are authored by AI, not a student's locked prediction.
        base=calculate()['value']['per_share']
        self.assertLess(calculate({'wacc':.11})['value']['per_share'],base)
        self.assertLess(calculate({'capex_2026':220000})['value']['per_share'],base)
        self.assertGreater(calculate({'aws_predep_margin':.62})['value']['per_share'],base)
        self.assertGreater(calculate({'terminal_growth':.035})['value']['per_share'],base)

    def test_invalid_inputs_and_failure_recovery(self):
        for x in [float('nan'),float('inf'),True,.99]:
            with self.assertRaises(ValueError): calculate({'wacc':x})
        broken=calculate(break_cash=True)
        self.assertFalse(broken['valid'])
        self.assertIsNone(broken['value'])
        self.assertTrue(calculate()['valid'])

    def test_all_512_control_corners(self):
        controls=load()['controls']; keys=list(controls)
        for bounds in itertools.product(['min','max'],repeat=len(keys)):
            r=calculate({k:controls[k][b] for k,b in zip(keys,bounds)})
            if r['valid']:
                self.assertTrue(math.isfinite(r['value']['per_share']))
                self.assertTrue(all(c['passed'] for c in r['checks']))
            else:
                self.assertIsNone(r['value'])
                self.assertTrue(any(not c['passed'] for c in r['checks']))

if __name__=='__main__': unittest.main(verbosity=2)
