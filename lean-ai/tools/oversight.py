"""Recompute the invented figures of lean-ai.md section 4, The owner's hours (v0.2.0, 25 November 2026, KST).

Standard library only. No sources, no network, no model call. Rewrites evidence/oversight-illustration.json
and exits 1 if any figure the module displays does not reproduce. The figures are invented to show the
arithmetic of The Boundary and the Limit, Section 8; they are not a measurement.
"""
import json
import sys
from decimal import Decimal as D, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'evidence' / 'oversight-illustration.json'

def r(x, places='0.01'):
    return D(x).quantize(D(places), rounding=ROUND_HALF_UP)

# The month of section 4's illustration: ten cases, eight accepted, 300 minutes at 1.40, 26.00 of charges.
rate, charges, accepted = D('1.40'), D('26.00'), 8
minutes = {  # W16's five mutually exclusive categories, invented
    'preparation and first-pass work': 40,
    'production or AI interaction': 80,
    'initial review': 100,
    'correction and re-review including fallback': 50,
    'final approval and case-specific administration': 30,
}
oversight_keys = ['initial review', 'correction and re-review including fallback',
                  'final approval and case-specific administration']
total_min = sum(minutes.values())
oversight_min = sum(minutes[k] for k in oversight_keys)
case_processing = charges + rate * total_min
oversight_cost = rate * oversight_min
standing_hours, available_hours = D('1'), D('3.5')   # s and O, invented
demanded = D(oversight_min) / 60 + standing_hours     # D
load = demanded / available_hours
governed = min(D(1), available_hours / demanded)

figures = {
    'total minutes': total_min,
    'oversight minutes': oversight_min,
    'case-processing cost': str(r(case_processing)),
    'case-processing cost per accepted outcome': str(r(case_processing / accepted)),
    'oversight effort': str(r(oversight_cost)),
    'oversight share of case-processing cost': str(r(oversight_cost / case_processing * 100, '0.1')) + '%',
    'oversight per accepted outcome': str(r(oversight_cost / accepted)),
    'cost per accepted outcome with no model charges': str(r((case_processing - charges) / accepted)),
    'hours demanded D': str(r(demanded, '0.1')),
    'hours available O': str(available_hours),
    'oversight load D/O': str(r(load)),
    'governed share O/D': str(r(governed * 100, '0.1')) + '%',
    'designed oversight not performable': str(r((1 - governed) * 100, '0.1')) + '%',
}
displayed = {  # as printed in lean-ai.md v0.2.0
    'total minutes': 300, 'oversight minutes': 180,
    'case-processing cost': '446.00', 'case-processing cost per accepted outcome': '55.75',
    'oversight effort': '252.00', 'oversight share of case-processing cost': '56.5%',
    'oversight per accepted outcome': '31.50', 'cost per accepted outcome with no model charges': '52.50', 'hours demanded D': '4.0', 'hours available O': '3.5',
    'oversight load D/O': '1.14', 'governed share O/D': '87.5%',
    'designed oversight not performable': '12.5%',
}
mismatch = {k: (figures[k], displayed[k]) for k in displayed if figures[k] != displayed[k]}
module = ROOT.parent / 'lean-ai.md'
text = module.read_text(encoding='utf-8')
start = text.find("### The owner's hours")
end = text.find('### ', start + 4)
section = text[start:end] if start >= 0 and end > start else ''
absent = sorted({str(v) for v in displayed.values()} - {str(v) for v in displayed.values() if str(v) in section})
if not section:
    absent = ['the subsection The owner\'s hours was not found in lean-ai.md']
result = {
    'date': '2026-11-25 (KST)',
    'status': 'invented figures; arithmetic only; not a measurement',
    'source': 'lean-ai.md v0.2.0, section 4, The owner\'s hours; The Boundary and the Limit v1.4, Section 8',
    'minutes by W16 category': minutes,
    'figures': figures,
    'all displayed figures reproduce': not mismatch,
    'mismatches': mismatch,
    'displayed figures absent from the module': absent,
}
OUT.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))
sys.exit(1 if mismatch or absent else 0)
