# Slide style and structure, v2 (17 October 2026)

Three decks come from one engine: Deck A The Case, Deck B The Gap, Deck C The Week. They share one grammar so a reader can move between them.

## Structure
1. Open with the answer: a title slide, the team, the agenda, then the three claims (exec_summary).
2. Evidence before design: the survey, then the comparison with ordinary bots.
3. Design after the demonstration, or before it in Deck A: architecture, safety rules, engines.
4. End with the plan: scope, stack, timeline, risks, decisions, evaluation, tests, deliverables, Project II.
5. Appendix last: fallback frames, extra comparisons, diagrams, requirements, sources.

## Slide rules
1. The title states the point in one sentence. The overline names the section.
2. One piece of evidence per slide: a table, a diagram, a frame or a chat.
3. Body text is 24 px or larger on the 1920 px canvas. Footnotes are 20 px.
4. Colors come from tokens. A deck takes its theme from lib.set_theme (A white, B grey with a charcoal band, C warm paper).
5. A footer tracker shows every section, and the current one is bold.
6. The left side of a comparison slide is an illustration and says so on the slide.

## Speaker notes (fixed labels)
TIME, SAY, SHOW, PROVE, BRIDGE. PROVE names the source of every number.

## Build
cd design/slides/src and run: ~/slides-venv/bin/python build.py deck_a deck_b deck_c
Frame images are in img/v2 (1x screenshots of the prototype). Comparison text is in chatvs.py.
