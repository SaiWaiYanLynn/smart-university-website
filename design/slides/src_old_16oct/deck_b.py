"""Option B: the walkthrough deck. The slides carry the prototype, frame by frame, with what the system does underneath."""
import lib
from lib import C
import kit
import modules as M
import journeys as J


def make():
    d = lib.Deck('Option_B_Walkthrough_Deck', 'Smart University Website: walkthrough deck')
    M.m_title(d, 'One assistant for rules, records, bookings and requests', frame='j4_5.png')
    M.m_team(d)
    rows = [['5', 'The problem, led by a survey of 17 universities, and how an agent differs', 'Survey report'],
            ['3', 'Objectives, requirements and scope', 'Feasibility report, updated'],
            ['7', 'Architecture and the system models', '12 diagrams'],
            ['15', 'The prototype, frame by frame, and what it changes', 'Figma prototype'],
            ['4', 'How we build it: stack, plan, risks, decisions, how we measure', 'Feasibility report, updated'],
            ['3', 'Where we are, and Project II', 'Seven deliverables'],
            ['3', 'Questions', 'Everyone']]
    assert sum(int(r[0]) for r in rows) == 40
    M.m_agenda(d, rows, notes='Forty minutes. Every journey in the middle is a slide, so nothing depends on a live click. If time allows, open the real prototype for two of the journeys. The slides are the backup and the main path.')
    # problem and evidence
    M.m_problem(d)
    M.m_method(d)
    M.m_heatmap(d)
    M.m_bars(d)
    M.m_cmp_table(d)
    M.m_two_answers(d)
    # objectives, requirements, scope
    M.m_objectives(d)
    M.m_requirements(d)
    M.m_scope(d)
    # architecture, short
    M.m_arch(d)
    M.m_flow(d)
    M.m_agents(d)
    M.m_engines(d)
    M.m_roles(d)
    M.m_safety(d)
    M.m_channels_tests(d)
    # walkthrough
    M.m_proto(d)
    kit.section_slide(d, 1, 'Walkthrough', 'The prototype, frame by frame. Each slide says what the system does underneath.',
                      notes='From here every slide is one frame of the prototype. The right column says what the system does underneath, because that is the criterion. The student is Wai Yan Lynn, third year ICT. All the dates follow the 2026 calendar.')
    J.j1a(d)
    J.j1b(d)
    J.j2(d)
    J.j3(d)
    J.j4a(d)
    J.j4b(d)
    J.j5a(d)
    J.j5b(d)
    J.j8(d)
    J.j10(d)
    J.j11(d)
    J.chan(d)
    J.staff_assist(d)
    J.staff_prep(d)
    J.instr(d)
    J.admin(d)
    # what it changes
    M.m_roles_change(d)
    M.m_steps(d)
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
