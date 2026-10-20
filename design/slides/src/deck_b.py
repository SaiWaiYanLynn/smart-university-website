"""Deck B, The Gap. Comparison-led: every claim is shown as an ordinary bot against our assistant. Theme B (grey and charcoal)."""
import lib
from lib import C
import modules as M
import chatvs
import v2
import proposal as P
from v2 import N

SECTIONS = ['Gap', 'Student', 'Staff', 'Teachers', 'How', 'Plan']


def setn(s, text, section=None):
    s.notes = text
    if section:
        s.section = section
    return s


def cmp(d, key, section, say, prove=None, mins=1, show=None):
    chatvs.chat_vs(d, key, section=section, over='Comparison', notes=N(say, show=show or 'Red window first, then the teal one. Read the shaded line.', prove=prove or 'The ordinary-bot reply is a made-up illustration, not a quote.', mins=mins))


def make():
    d = lib.Deck('Deck_B_The_Gap', 'Smart University Website: The Gap', theme='B', sections=SECTIONS)
    v2.title_b(d)
    setn(M.m_team(d), N('Four members, one course. The project is built so that any university can adopt it. Wai Yan Lynn owns the design and documents, and the other three own the diagrams.', mins=1), 'Gap')
    rows = [['4', 'The gap: what 17 universities offer, and what none does', 'Survey report'],
            ['9', 'Student side by side: ten questions to an ordinary bot and to ours', 'Prototype'],
            ['5', 'Staff, instructors and administrators: actions a bot cannot do', 'Prototype'],
            ['8', 'How it works: the architecture behind the answers', '12 diagrams'],
            ['6', 'Live click-through: one payment slip from student to database', 'Figma prototype'],
            ['5', 'How we build it, where we are, Project II', 'Feasibility report'],
            ['3', 'Questions', 'Everyone']]
    assert sum(int(r[0]) for r in rows) == 40
    setn(M.m_agenda(d, rows, title='Forty minutes, built around one comparison'), N('The whole talk is one comparison: the same message to an ordinary bot and to ours. First the gap in the survey, then the student, staff and teacher sides, then how it works, then a live click-through, then the plan.', mins=0.5), 'Gap')
    v2.exec_summary(d, 'Gap', kicker='The claim')
    # ---- 01 gap
    v2.section_b(d, '01', 'The gap', 'Seventeen universities, seven questions. What exists, and what none of them does.', chips=['Survey of 17', 'Public pages only', '5 and 6 October 2026'], notes=N('Section one: the gap.', mins=0), section='Gap')
    setn(P.m_background(d), N('Context first. Universities have put their services online and students use chat every day. What is missing is the join between them. Say the numbers once and move on.', prove='Survey report and feasibility report v3, section 1.', mins=1), 'Gap')
    setn(M.m_problem(d), N('Three problems, each with its source. We did not survey students. Universities are well equipped on the basics. The gap is elsewhere.', prove='Survey: 13 of 17 take online requests, 3 of 17 show a status, none of the 12 Thai ones.', mins=1.5), 'Gap')
    setn(M.m_heatmap(d), N('Read left to right. The first four columns are mostly green. In the last three no university gets a full tick. Four partial cells run fixed scripts or answer outside the chat. That is the gap.', show='Point at the red band.', prove='Full ticks out of 17: 13, 3, 11, 15, 0, 0, 0.', mins=1.5), 'Gap')
    setn(M.m_cmp_table(d), N('Be fair. Existing bots can run real actions. Their limit is coverage: a person wrote every intent in advance. Our right column is a design, not a measured result.', prove='NN Bot (KMUTNB) and the Buriram Rajabhat chatbot are published intent-based bots.', mins=1), 'Gap')
    v2.how_to_read(d, 'Gap')
    # ---- 02 student
    v2.section_b(d, '02', 'The student', 'Ten questions, each sent to an ordinary bot and to our assistant.', chips=['Web', 'LINE', 'Telegram'], notes=N('Section two: the student side.', mins=0), section='Student')
    cmp(d, 'visa', 'Student', 'A rule question. The ordinary bot matches a keyword and sends a link. Ours retrieves Handbook section 7.3, answers, cites the source and offers the next step.', prove='Survey: 0 of 17 show the rule behind an answer.')
    cmp(d, 'record', 'Student', 'Own record yes, someone else\'s record no. The student ID comes from the token, never from the message. The blocked attempt is written to the audit log.', prove='Planned test: 30 other-student attempts, 30 refusals.')
    cmp(d, 'room', 'Student', 'A booking on LINE in plain text. The assistant lists the rooms, waits for the student to name one and for a yes, then writes the booking in one transaction.', prove='Planned test: 200 concurrent requests on one slot, exactly one succeeds.')
    cmp(d, 'transcript', 'Student', 'A request with a state. The assistant applies the fee rule, asks for a yes, opens REQ-2026-0481 and messages the student when the state changes.', prove='Survey: only 3 of 17 show any status, none of the 12 Thai ones.')
    cmp(d, 'slip', 'Student', 'A payment slip on Telegram. The assistant does not read the photo and does not decide on money. It hands the chat to Student Services and stays silent. A person checks the slip and replies.')
    cmp(d, 'memory', 'Student', 'A question the next day. The assistant finds the saved topic by student ID, not by the LINE account, checks the deadline again and offers to start the withdrawal.')
    cmp(d, 'makeup', 'Student', 'A case nobody scripted. The Knowledge agent finds Handbook 8.2, a tool counts the working days in code, the Request agent opens a request with the photo, and staff decide.', prove='A comparison mock built on a fictional Handbook rule (section 8.2). The prototype has no frame for this story.')
    cmp(d, 'retry', 'Student', 'A tool fails. The ordinary bot forgets the question. Ours saves it and retries every 5 minutes, then writes to the student on its own when the grade service answers.', prove='Prototype story S9: retries at 08:35, 08:40 and 08:45.', show='Third window: a message that arrives with no new question.')
    cmp(d, 'watch', 'Student', 'The student asks to be told when the transcript is ready. The ordinary bot cannot watch anything. Ours saves a watch. Days later the state changes and the assistant writes first.', prove='Design: WATCH entity in diagram 02. The ordinary-bot reply is a made-up illustration. The prototype shows the message itself in story S7, on Telegram. The watch is design.', show='Third window: the message nobody asked for that morning.')
    cmp(d, 'advisor', 'Student', 'An advisor appointment. The ordinary bot gives a phone number. Ours finds the advisor, reads the free slots and books after a yes. A scheduler sends the reminder 24 hours before, and the advisor gets a brief.', prove='Design: the 24 hour timer in diagram 03. The ordinary-bot reply is a made-up illustration. This scenario is a comparison mock; the prototype has no frame for it.')
    # ---- 03 staff
    v2.section_b(d, '03', 'Staff', 'The same assistant for the people who run the University. The role from the sign-in sets the tools.', chips=['Read the queue', 'Approve after a yes', 'Record a payment'], notes=N('Section three: staff.', mins=0), section='Staff')
    cmp(d, 'approve', 'Staff', 'A staff member reads the queue on Telegram and approves a request. The assistant asks for a yes, sets the state, tells the student on LINE and writes the audit record with the staff member.')
    cmp(d, 'slipdb', 'Staff', 'This is the end of the slip story. A person already checked the slip and replied. Now the staff member tells the assistant to record the payment. It reads the balance, asks for a yes, writes the record and the audit entry.', show='Right window: three lines. Read, ask, write.', mins=1.5)
    cmp(d, 'handoff', 'Staff', 'Handoff. An ordinary bot gives a phone number. Ours passes the whole chat on and stays silent, and the staff member starts from a summary and a draft reply.', prove='Design: handoff in diagram 03. The prototype shows the staff console conversation in frame S1.4. The summary and draft are a mock.', show='Third window: summary and draft in the console.')
    cmp(d, 'query', 'Staff', 'A query across records in one sentence. Ours searches the open requests, answers, and writes an assignment only after a yes.', prove='Design: Request agent and tool layer. The ordinary-bot reply is a made-up illustration. This scenario is a comparison mock; the prototype has no frame for it.')
    cmp(d, 'remind', 'Staff', 'A bulk action. The assistant finds the rows with a query, drafts one message, shows the batch size and sends only after a yes.')
    cmp(d, 'scope', 'Staff', 'The role limits the rows. Staff can read conversations passed to Student Services. Private chats stay private, and every read is written to the audit log.')
    # ---- 04 teachers and admin
    v2.section_b(d, '04', 'Instructors and administrators', 'Attendance, meetings, documents and accounts, all limited by role.', chips=['Instructor', 'Administrator'], notes=N('Section four.', mins=0), section='Teachers')
    cmp(d, 'gap', 'Teachers', 'A knowledge gap. The administrator sees the question asked 14 times, adds a document after a yes, and the next day a student gets a cited answer.', prove='Design: UNANSWERED_QUESTION and DOCUMENT_CHUNK in diagram 02. The ordinary-bot reply is a made-up illustration. The prototype has no frame for it.', show='Third window: the gap is closed.')
    cmp(d, 'conflict', 'Teachers', 'Two documents disagree on a fee. The assistant flags the conflict and a person decides which document is the source.', prove='Design: SOURCE_CONFLICT in diagram 02. The ordinary-bot reply is a made-up illustration. This scenario is a comparison mock; the prototype has no frame for it.')
    cmp(d, 'blocked', 'Teachers', 'A student session asks for the staff queue. The role decides which tools exist. The refusal is written to the audit log and can be replayed.', prove='Planned test: 10 staff-tool attempts from a student session, none may succeed. The ordinary-bot reply is a made-up illustration. This scenario is a comparison mock; the prototype has no frame for it.', show='Third window: the audit log.')
    cmp(d, 'attend', 'Teachers', 'An instructor asks who missed a class. A tool counts the absences, the Handbook gives the limit, and a warning goes out only after a yes.')
    cmp(d, 'move', 'Teachers', 'An instructor moves a meeting. The same reservation engine that books students moves it and tells the other person.')
    cmp(d, 'admin', 'Teachers', 'An administrator adds a document and creates accounts from a file. A validator checks the rows first, and accounts are created only after a yes.')
    # ---- 05 how
    v2.section_b(d, '05', 'How it works', 'Four rules in code make the comparisons above true.', chips=['Token', 'Role', 'A yes', 'Audit'], notes=N('Section five: the architecture.', mins=0), section='How')
    v2.ground_rules(d, 'How')
    setn(P.m_solution(d), N('The proposed solution in one line: a person writes on any channel, the supervisor picks a sub-agent, a tool reads or writes after a yes, and the reply returns on the same channel. A person takes over when needed.', prove='Feasibility report v3, sections 1.5 and 6.1, and diagram 01.', mins=1), 'How')
    setn(P.m_trace(d), N('Every objective traces to requirements, to a component and to a test. This is why each part of the architecture exists.', prove='Feasibility report v3, sections 1.3, 4.2 and 4.3.', mins=1), 'How')
    setn(M.m_arch(d), N('One picture. People at the top, one FastAPI application with one supervisor, data and services at the bottom. Chatwoot owns the channels and the handoff. Everyone signs in through Keycloak.', prove='Diagram 01.', mins=1.5), 'How')
    setn(M.m_flow(d), N('The route of one message: who is writing, is a person handling this chat, split into tasks, pick a tool, three checks, read or write after a yes, one reply.', prove='Diagram 03.', mins=1.5), 'How')
    setn(M.m_agents(d), N('One LangChain supervisor, four sub-agents as tools, and a role middleware that filters the tools on every model call.', mins=1), 'How')
    setn(M.m_safety(d), N('Safety lives in code. The token decides who, the role decides what exists, a yes comes before a write, no source means refusal, and a person decides money. 40 attack attempts are planned and none may succeed.', mins=1), 'How')
    setn(M.m_channels_tests(d), N('Chatwoot tests on 15 and 16 October: 9 of 11 passed. Cards failed, so we use plain text on every channel.', prove='11 checks, 9 passed.', mins=1), 'How')
    setn(M.m_roles(d), N('Six kinds of person, four roles. The role decides the tools and the rows.', mins=1), 'How')
    setn(P.m_models(d), N('We picked the diagrams that carry the design and skipped the rest. The Figma prototype is the wireframe set: 270 frames in 12 stories.', prove='Diagrams in design/diagrams, 12 files, and the Figma prototype.', mins=1), 'How')
    # ---- 06 plan: demo first
    v2.section_b(d, '06', 'Show and plan', 'A live click-through, then how we build it and where we are.', chips=['Live', 'Plan', 'Project II'], notes=N('Section six.', mins=0), section='Plan')
    v2.parts_map(d, 'Plan')
    s = d.add(section='Plan', notes=N('Open the Figma prototype on story S1 and press Next. If Figma fails, use the appendix.', show='Figma, Prototype page, presentation view, flow S1.', mins=6))
    y = v2.hdr(s, 'Live: one payment slip, from the student to the database', 'The prototype', size=46)
    s.image(v2.fcrop('v2/s1_6.png', (285, 130, 1070, 470)), 96, y, 1040, 650, fit='contain', r=14, border=C['border'], shadow=True)
    rx = 1190
    yy = y
    for i, (tt, bb) in enumerate([('Open Figma', 'Prototype page, presentation view, flow S1 Payment slip.'), ('Press Next', 'The bar at the bottom of each frame names the actor and the channel.'), ('Follow the actors', 'Student, assistant, staff, assistant, student. The same Next button follows them.'), ('End on the Fees page', 'The balance is 0 THB and the audit log holds the staff member.')], 1):
        yy = s.callout(rx, yy, 1824 - rx, i, tt, bb, size=26) + 26
    v2.source(s, 'Frame shown: S1.6, the staff member asks the assistant to record the payment. Prototype v2.1, 18 October 2026.')
    setn(M.m_objectives(d), N('Seven objectives. Objective five covers staff, instructors and administrators.', mins=1), 'Plan')
    setn(P.m_users(d), N('Who it is for: six kinds of person and what each one needs. The office is small and the questions come in peaks.', prove='Feasibility report v3, section 1.4.', mins=0.5), 'Plan')
    setn(P.m_stakeholders(d), N('The stakeholder register. Students and staff are the primary users and have high influence, because the system has no value if either group does not use it. The model service is a single point of failure.', prove='Feasibility report v3, section 4.1.', mins=0.5), 'Plan')
    setn(M.m_requirements(d), N('Thirty three functional and five non functional requirements, each with a test. Nineteen are core and fourteen are extended. Say three of them out loud: 200 concurrent requests on one slot, exactly one succeeds; zero successful cross account attempts; 80 and 90 percent accuracy scored by two raters.', prove='Feasibility report v3, requirements table.', mins=1), 'Plan')
    setn(P.m_nfr(d), N('The five non functional requirements, each with a test. The speed targets are proposals for the hosted model until the week two test measures them.', prove='Feasibility report v3, section 4.3. Targets are proposals until measured.', mins=0.5), 'Plan')
    setn(M.m_scope(d), N('Scope is frozen. The payment slip is in: a person checks it and the assistant records it after a yes. Payment processing is out.', mins=1), 'Plan')
    setn(P.m_constraints(d), N('Constraints, assumptions and limits, stated and not hidden. The assumption that a free model is good enough at tool calling is checked in week two, not assumed.', prove='Feasibility report v3, section 6.3.', mins=0.5), 'Plan')
    setn(M.m_stack(d), N('Every tool is free or open source. The model moved from a local one to a hosted free tier.', mins=0.5), 'Plan')
    setn(P.m_devmethod(d), N('We work in short iterative cycles with a prioritized backlog. The core requirements come first and the extended ones after. Every track has a yes or no milestone each week. Track owners are not assigned yet.', prove='Feasibility report v3, sections 2.2 and 2.3, and the git log.', mins=0.5), 'Plan')
    setn(M.m_timeline(d), N('Ten weeks. Week ten is a buffer with no new features.', mins=0.5), 'Plan')
    setn(M.m_risks(d), N('Risk one changed: rate limits or a withdrawn free model, not an unreliable local model. LINE is kept for the demo because of the push quota.', mins=0.5), 'Plan')
    setn(M.m_decisions(d), N('Decided on the left, open on purpose on the right.', mins=0.5), 'Plan')
    setn(M.m_eval(d), N('Targets, not results. Two evaluation sets will be written and frozen before any agent code.', mins=0.5), 'Plan')
    setn(M.m_tests(d), N('Eleven channel checks, nine passed. The failed ones, cards, changed the design.', mins=0.5), 'Plan')
    setn(M.m_deliverables(d), N('Seven deliverables. The coded prototype is the big item still ahead.', mins=0.5), 'Plan')
    setn(M.m_proj2(d), N('Project II adds more of the same on the same two engines.', mins=0.5), 'Plan')
    slot = P.m_propmap_slot(d, notes=N('Close the proposal. Every one of the 17 suggested sections has a slide. Offer the checklist to the instructor.', prove='Week 7 slides: the 17 suggested sections of the proposal.', mins=0.5))
    slot.section = 'Plan'
    M.m_thanks(d, notes=N('Thank the room. Offer to open the prototype on any frame.', mins=3))
    # ---- appendix
    v2.section_a(d, None, 'Appendix', 'Reference slides. Open them only if asked.', notes='Reference.', section=None)
    for k in ['transcript_x'] if False else []:
        pass
    for k in ['move']:
        pass
    chatvs.chat_vs(d, 'cross', over='Appendix', section=None, notes=N('Reference slide. Start on the web, continue on Telegram. The left side is an illustration.'))
    for key, a, b, ta, tb, tk in [
        ('s1', 'v2/s1_1.png', 'v2/s1_2.png', 'S1.1 The student sends the slip', 'S1.2 The assistant hands the chat to staff', 'A photo goes in. The assistant does not read it and does not decide.'),
        ('s1b', 'v2/s1_3.png', 'v2/s1_4.png', 'S1.3 Staff see the slip', 'S1.4 Staff reply by hand', 'A normal chat. The assistant is paused.'),
        ('s1c', 'v2/s1_6.png', 'v2/s1_7.png', 'S1.6 Record the payment: a yes first', 'S1.7 Written and audited', 'Nothing is written without a yes.')]:
        v2.frames2(d, 'Fallback frames: ' + key.upper(), 'Appendix', a, ta, b, tb, tk, notes=N('Use only if Figma fails.'), section=None)
    M.m_appx_img(d, 'Appendix: use case diagram', 'dg_12_use_case.png', 'Six actors and their use cases. Source: 12_use_case.drawio')
    M.m_appx_img(d, 'Appendix: supervisor routing', 'dg_03_supervisor.png', 'Diagram 03. Source: 03_supervisor.mmd')
    M.m_appx_img(d, 'Appendix: entity relationship diagram', 'dg_02_er.png', f'{len(M.ER_ENTITIES)} entities. Source: 02_er.mmd')
    M.m_appx_sources(d)
    P.fill_propmap(d, slot)
    v2.add_prove(d)
    v2.fit_time(d, agenda=dict(title='Forty minutes, built around one comparison', rows={
        'Gap': ('The gap: what 17 universities offer, and what none does', 'Survey report'),
        'Student': ('Student side by side: ten questions to an ordinary bot and to ours', 'Prototype'),
        'Staff': ('Staff actions a bot cannot do, with their follow-ups', 'Prototype'),
        'Teachers': ('Instructors and administrators', 'Prototype'),
        'How': ('How it works: the architecture behind the answers', '12 diagrams'),
        'Plan': ('Live click-through, then how we build it and Project II', 'Figma prototype')}))
    return d
