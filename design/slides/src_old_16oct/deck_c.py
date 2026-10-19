"""Option C: the story deck. One student, one week. The architecture appears piece by piece, when the story needs it."""
import lib
from lib import C
import kit
from kit import hdr, note_bar, section_slide
import modules as M
import journeys as J


def week_slide(d):
    s = d.add(notes='This is the whole story on one slide. The student is Wai Yan Lynn, third year ICT. Everything happens in one week of the 2026 calendar. Each event is a frame in the prototype, and each one shows a different part of the system. We walk through them in order.')
    y = hdr(s, 'One student, one week', 'The story')
    days = [
        ('Wed 14 Oct', [('10:05', 'Plans her graduation'), ('11:34', 'Books a study room'), ('14:22', 'Asks about a scholarship'), ('14:31', 'Requests a transcript'), ('16:06', 'Sends a payment slip')]),
        ('Thu 15 Oct', [('08:04', 'Asks everything on LINE'), ('09:41', 'Staff accept the slip'), ('12:19', 'Asks on Telegram')]),
        ('Fri 16 Oct', [('09:12', 'Transcript is ready')]),
        ('Mon 19 Oct', [('17:40', 'Asks about withdrawing')]),
        ('Tue 20 Oct', [('08:50', 'Continues the chat'), ('09:13', 'Staff approve it'), ('11:05', 'Missed a midterm')]),
    ]
    widths = [440, 330, 250, 330, 378]
    x = 96
    gap = 0
    for (day, evs), w in zip(days, widths):
        s.rect(x, y, w - 8, 58, fill=C['charcoal'])
        s.text(x, y + 12, w - 8, day, size=28, weight=700, color=C['white'], align='c', lh=1.1, fit=False)
        yy = y + 78
        for tm, ev in evs:
            s.rect(x, yy, w - 8, 112, fill=C['teal_tint'], stroke=C['teal_200'], r=12)
            s.text(x + 18, yy + 12, w - 44, tm, size=26, weight=700, color=C['teal_dark'], fit=False)
            s.text(x + 18, yy + 52, w - 44, ev, size=26, color=C['ink'], lh=1.2, h=56, minsize=22)
            yy += 126
        x += w
    s.text(96, 1000 - 40, 1728, 'Wai Yan Lynn, 67111411, third year ICT. All dates follow the 2026 calendar.', size=24, color=C['muted'])
    return s


def make():
    d = lib.Deck('Option_C_Story_Deck', 'Smart University Website: story deck')
    M.m_title(d, 'One assistant for rules, records, bookings and requests', frame='j1_3.png')
    M.m_team(d)
    rows = [['5', 'The problem students meet, and the survey of 17 universities', 'Survey report'],
            ['3', 'Objectives, requirements and scope', 'Feasibility report, updated'],
            ['18', 'One student, one week: the assistant at work, and the system underneath', 'Figma prototype, 12 diagrams'],
            ['4', 'The whole picture, and what it changes', '12 diagrams'],
            ['4', 'How we build it: stack, plan, risks, decisions, how we measure', 'Feasibility report, updated'],
            ['3', 'Where we are, and Project II', 'Seven deliverables'],
            ['3', 'Questions', 'Everyone']]
    assert sum(int(r[0]) for r in rows) == 40
    M.m_agenda(d, rows, notes='Forty minutes. We start with the problem, then follow one student for a week. The architecture is not a block of its own. Each piece appears when the story needs it, and one slide shows the whole picture at the end.')
    week_slide(d)
    # the problem
    M.m_problem(d)
    M.m_method(d)
    M.m_heatmap(d)
    M.m_bars(d)
    M.m_cmp_table(d)
    M.m_objectives(d)
    M.m_requirements(d)
    M.m_scope(d)
    M.m_proto(d)
    # part 1
    section_slide(d, 1, 'Wednesday 14 October', 'Five things happen in one day.',
                  notes='Part one. Five events in one day: a graduation plan, a room, a scholarship question, a transcript and a payment slip.')
    J.j1a(d, over='Wed 14 Oct', piece='The Knowledge agent retrieves a passage and shows the section.')
    J.j11(d, over='Wed 14 Oct, 10:05', piece='The supervisor splits one message into tasks and calls the sub-agents.')
    M.m_agents(d, notes='Now the first piece of the architecture. One supervisor agent, four sub-agents wrapped as tools. A role middleware filters the tools by the role in the token.')
    J.j4a(d, over='Wed 14 Oct, 11:34')
    J.j4b(d, over='Wed 14 Oct, 11:34', piece=None)
    M.m_engines(d, notes='The piece behind the booking and the transcript: two engines. A reservation engine with slot locking, and a request state machine with four states. Each is written once and serves every feature.')
    J.j2(d, over='Wed 14 Oct, 14:22')
    M.m_handoff(d, notes='The piece behind the handoff: a conversation is pending while the assistant answers, open while a person handles it. The assistant stays silent while it is open.')
    J.j5a(d, over='Wed 14 Oct, 14:31')
    J.j5b(d, over='Wed 14 Oct, 14:31 to Fri 16 Oct, 09:12')
    J.j8(d, over='Wed 14 Oct, 16:06')
    M.m_safety(d, notes='The piece behind the slip and behind everything else: the safety rules. They live in code, not in the prompt.')
    # part 2
    section_slide(d, 2, 'Thursday 15 October', 'The student does not open the website.',
                  notes='Part two. The next morning the student asks on LINE, and at lunch on Telegram. The transcript request from Wednesday is ready on Friday 16 October, shown earlier.')
    J.chan(d, over='Thu 15 Oct, 08:04 and 12:19')
    M.m_channels_tests(d, notes='The piece behind the channels: Chatwoot. We tested it live with a LINE official account and a Telegram bot. Text, photos and buttons work on both. Cards do not, so cards stay in the web portal.')
    # part 3
    section_slide(d, 3, 'Monday 19 and Tuesday 20 October', 'The assistant remembers, and the University side uses it too.',
                  notes='Part three. The assistant remembers across days, and staff, instructors and administrators use the same assistant with their own tools.')
    J.j10(d, over='Mon 19 Oct, 17:40 and Tue 20 Oct, 08:50', piece='Memory is kept under the student ID in PostgreSQL, not under the channel.')
    J.staff_assist(d, over='Tue 20 Oct, 09:11 to 09:13', piece='The role comes from the account. The role decides the tools and the rows.')
    M.m_roles(d, notes='The piece behind the staff scene: roles. One application, six kinds of person. The role comes from the Keycloak account, and the tools and the rows follow the role.')
    M.m_two_answers(d, notes='Tuesday, 11:05. The student missed a midterm. Same message, two answers. On the left the fallback reply that the research describes. On the right what our prototype does. The left side is an illustration, not a quote from one university.')
    J.instr(d, over='Tue 20 Oct')
    J.admin(d, over='Tue 20 Oct')
    # the whole picture
    section_slide(d, 4, 'The whole picture', 'Now all the pieces together.', notes='Now we put every piece on one slide and then look at the route of one message.')
    M.m_arch(d)
    M.m_flow(d)
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
    section_slide(d, None, 'Appendix', 'Reference slides. Open them only if asked.', notes='Reference slides.')
    M.m_data(d)
    M.m_deploy(d)
    M.m_proto(d)
    M.m_appx_img(d, 'Appendix: use case diagram', 'dg_12_use_case.png', 'Six actors and their use cases. Source: design/diagrams/12_use_case.drawio')
    M.m_appx_img(d, 'Appendix: deployment diagram', 'dg_10_deployment.png', 'Docker Compose services and what sits outside the host. Source: design/diagrams/10_deployment.mmd')
    M.m_appx_img(d, 'Appendix: entity relationship diagram', 'dg_02_er.png', f'{len(M.ER_ENTITIES)} entities. Source: design/diagrams/02_er.mmd')
    M.m_appx_requirements(d)
    M.m_appx_sources(d)
    return d
