import lib
from lib import C


def make():
    d = lib.Deck('smoke', 'Smoke test')
    s = d.add(kind='dark', bg=C['charcoal'], footer=False, number=False)
    s.rect(96, 96, 140, 12, fill=C['lime'])
    s.text(96, 320, 1500, 'Smart University Website', size=96, weight=700, color=C['white'], lh=1.05)
    s.text(96, 520, 1400, 'One assistant for rules, records, bookings and requests', size=40, color='#D4D4D8')
    s = d.add(notes='note one')
    s.title('Bullets, a table and a screenshot', overline='Test')
    s.bullets(96, 220, 800, [('Bold lead.', 'The rest of the sentence runs across the line and wraps to a second line to test wrapping.'), 'Plain item two', 'Plain item three that is a little longer than item two'], size=30)
    s.table(96, 560, [300, 250, 250], [['Name', 'A', 'B'], ['Row one', 'yes', 'no'], ['Row two is long text that wraps in the cell', 'x', 'y']], size=24)
    s.device('j1_3.png', 1000, 200, 800, caption='J1.3 answer with citation')
    for i, k in enumerate('yn~'):
        s.mark(k, 1100 + i * 80, 900)
    s.pill(96, 940, 'Pill label')
    return d
