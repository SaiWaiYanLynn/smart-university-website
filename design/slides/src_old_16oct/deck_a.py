"""Option A: the classic deck. Slides frame the talk, and the Figma click-through takes the middle 12 minutes."""
import lib
from lib import C
import kit
from kit import hdr, note_bar
import modules as M


def make():
    d = lib.Deck('Option_A_Classic_Deck', 'Smart University Website: classic deck')
    M.m_title(d, 'One assistant for rules, records, bookings and requests', frame='j1_3.png')
    M.m_team(d)
    rows = [['4', 'The problem, led by a survey of 17 universities', 'Survey report'],
            ['3', 'Objectives, requirements and scope', 'Feasibility report, updated'],
            ['8', 'Architecture and the system models', '12 diagrams'],
            ['11', 'The prototype, and a click-through of six journeys', 'Figma prototype'],
            ['3', 'What it changes: three comparisons', 'Survey, prototype'],
            ['5', 'How we build it: stack, plan, risks, decisions, how we measure', 'Feasibility report, updated'],
            ['3', 'Where we are, and Project II', 'Seven deliverables'],
            ['3', 'Questions', 'Everyone']]
    assert sum(int(r[0]) for r in rows) == 40
    M.m_agenda(d, rows, notes='Forty minutes. Four on the problem, four on objectives and scope, eight on architecture, twelve in the prototype, five on how we build it, three on status and Project II, four for questions. Keep this slide to ten seconds.')
    # problem and evidence
    M.m_problem(d)
    M.m_method(d)
    M.m_heatmap(d)
    M.m_bars(d)
    M.m_cmp_table(d)
    # objectives, requirements, scope
    M.m_objectives(d)
    M.m_requirements(d)
    M.m_scope(d)
    # architecture
    M.m_arch(d)
    M.m_flow(d)
    M.m_agents(d)
    M.m_roles(d)
    M.m_engines(d)
    M.m_safety(d)
    M.m_channels_tests(d)
    # prototype
    M.m_proto(d)
    click_through_plan(d)
    # comparisons after the click-through
    M.m_two_answers(d)
    M.m_roles_change(d)
    M.m_steps(d)
    # how we build it
    M.m_stack(d)
    M.m_timeline(d)
    M.m_risks(d)
    M.m_decisions(d)
    M.m_eval(d)
    M.m_tests(d)
    M.m_deliverables(d)
    M.m_proj2(d)
    M.m_thanks(d)
    # appendix
    kit.section_slide(d, None, 'Appendix', 'Reference slides. Open them only if asked.', notes='Reference slides.')
    M.m_handoff(d)
    M.m_data(d)
    M.m_deploy(d)
    M.m_appx_img(d, 'Appendix: use case diagram', 'dg_12_use_case.png', 'Six actors and their use cases. Source: design/diagrams/12_use_case.drawio')
    M.m_appx_img(d, 'Appendix: deployment diagram', 'dg_10_deployment.png', 'Docker Compose services and what sits outside the host. Source: design/diagrams/10_deployment.mmd')
    M.m_appx_img(d, 'Appendix: entity relationship diagram', 'dg_02_er.png', f'{len(M.ER_ENTITIES)} entities. Source: design/diagrams/02_er.mmd')
    M.m_appx_requirements(d)
    M.m_appx_sources(d)
    return d


def click_through_plan(d):
    s = d.add(notes='Switch to Figma now. Run the six journeys in this order, about ten minutes in all and say what the system does underneath at every step, because that is the criterion. J1: the answer carries its source. J2: refusal and handoff, staff sees the whole chat. J3: the student ID comes from the token, never from the text. J4: nothing is written without a yes. J5: status is pushed to the student. J8: the assistant never decides on money. Backup: this slide and the PDF export of the frames.')
    y = hdr(s, 'The click-through: six journeys, 10 minutes', 'The prototype')
    items = [('J1', '1.5 min', 'j1_3.png', 'A policy answer with its source', 'The Knowledge agent retrieves Handbook section 7.3 and shows it.'),
             ('J2', '1.5 min', 'j2_4.png', 'No rule found: refuse and hand over', 'No guess. Staff see the whole chat. The assistant goes silent.'),
             ('J3', '1 min', 'j3_4.png', 'Own record yes, someone else\'s no', 'The ID comes from the token, never from the message.'),
             ('J4', '2 min', 'j4_4.png', 'Book a study room', 'Slots are read first. A yes comes before any write.'),
             ('J5', '2.5 min', 'j5_4.png', 'Request a transcript and track it', 'Four states. The student is messaged on the same channel.'),
             ('J8', '1.5 min', 'j8_3.png', 'Pay with a slip: a person decides', 'The model never sees the image. Staff confirm the payment.')]
    cw = (1728 - 2 * 40) / 3
    ch = 420
    for i, (j, mins, img, t, b) in enumerate(items):
        x = 96 + (i % 3) * (cw + 40)
        yy = y - 6 + (i // 3) * ch
        ih = cw * 0.5
        s.image(kit.auto_crop(img), x, yy, cw, ih, fit='contain', r=12, border=C['border'], shadow=True, bgfill=C['alt'])
        ty = yy + ih + 12
        s.pill(x, ty, f'{j}  ·  {mins}', fill=C['teal'], color=C['white'], size=20, h=34)
        s.text(x + 190, ty + 2, cw - 190, t, size=24, weight=700, color=C['ink'], lh=1.15, h=64, minsize=22)
        s.text(x, ty + 70, cw, b, size=22, color=C['muted'], lh=1.22, h=58, minsize=20)
    return s
