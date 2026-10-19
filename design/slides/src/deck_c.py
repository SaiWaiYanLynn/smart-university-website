"""Deck C, The Week. One student, one week. Each moment shows what the student sees, what a person does and what the system did. Theme C (warm paper)."""
import lib
from lib import C
import kit
import modules as M
import chatvs
import v2
import proposal as P
from v2 import N

SECTIONS = ['The week', 'Wed 14', 'Tue 20', 'Under the hood', 'Plan']


def setn(s, text, section=None):
    s.notes = text
    if section:
        s.section = section
    return s


def moment(d, section, title, over, img, callouts, caption, say, prove=None, mins=1.5, imgw=900, quote=None, who=None):
    return v2.frame_callouts(d, title, over, img, callouts, caption, notes=N(say, show='The frame on the left, then the three numbered lines.', prove=prove, mins=mins), section=section, imgw=imgw, quote=quote, who=who)


def make():
    d = lib.Deck('Deck_C_The_Week', 'Smart University Website: The Week', theme='C', sections=SECTIONS)
    v2.title_c(d)
    setn(M.m_team(d), N('Four members, one course. Wai Yan Lynn is also our demo student, so the week you will see is the week of the demo student.', mins=1), 'The week')
    v2.week_overview(d, 'The week')
    v2.exec_summary(d, 'The week', kicker='Why this week matters')
    setn(P.m_background(d), N('Context first. Universities have put their services online and students use chat every day. What is missing is the join between them. Say the numbers once and move on.', prove='Survey report and feasibility report v3, section 1.', mins=1), 'The week')
    setn(M.m_problem(d), N('Before the week starts: why a student needs this. Three problems, each with its source. We did not survey students.', prove='Survey: 13 of 17 take online requests, 3 of 17 show a status.', mins=1.5), 'The week')
    setn(M.m_heatmap(d), N('The survey in one picture. The last three columns, citing rules, acting in the chat and one place, have no full tick for any of the 17 universities.', prove='Full ticks: 13, 3, 11, 15, 0, 0, 0.', mins=1.5), 'The week')
    v2.how_to_read(d, 'The week')
    # ---------------- Wed 14
    v2.section_c(d, 'Wednesday 14 October', 'A room, a question, a slip', 'Three moments in one afternoon.', notes=N('Wednesday afternoon.', mins=0), section='Wed 14')
    moment(d, 'Wed 14', 'Wednesday 11:34. The group needs a room', 'Moment 1', v2.fcrop('v2/s5_2.png', v2.PHONE), [
        ('Booking agent', 'Read the free rooms for Thursday afternoon. Nothing is held yet.'),
        ('Plain text on LINE', 'One line for each room. The student answers in words.'),
        ('A yes, then one transaction', 'The booking and its audit record are written together.')],
        'S5.2: the assistant lists the rooms on LINE', 'The student writes on LINE. The assistant reads the free rooms, lists them as plain text, waits for a choice and for a yes, then writes the booking in one transaction.', prove='Planned test: 200 concurrent requests on one slot, one success.', imgw=700, quote='I need a study room for my group on Thursday afternoon', who='Wai Yan Lynn, 11:34')
    chatvs.chat_vs(d, 'room', section='Wed 14', over='Same message', notes=N('The same message to an ordinary bot: it can talk about rooms but cannot book one.', prove='Ordinary-bot reply is made up.', mins=1))
    chatvs.chat_vs(d, 'handoff', section='Wed 14', over='Wednesday 14:22', notes=N('The student asks for a person about a leave of absence. An ordinary bot gives a phone number. Ours passes the whole chat on and stays silent, and the staff member opens a summary and a draft reply instead of a blank page. This is our third problem: case records that cannot be shared.', prove='Design: handoff in diagram 03. The ordinary-bot reply, the summary and the draft are a mock. The prototype shows the staff console conversation in frame S1.4.', mins=1.5))
    v2.lanes_s1(d, 'Wed 14', kicker='Wednesday 16:06. The payment slip')
    moment(d, 'Wed 14', 'The student sends the slip, and the assistant steps back', 'Moment 3, steps 1 and 2', v2.fcrop('v2/s1_2.png', v2.PHONE), [
        ('A photo, plain text', 'LINE carries the photo and the words. No buttons.'),
        ('The assistant does not read the slip', 'It does not decide on money.'),
        ('A person gets the chat', 'The assistant is paused while Student Services handle it.')],
        'S1.2: the assistant hands the chat to staff', 'The student sends the slip as a photo. The assistant does not read it and does not decide. It passes the conversation to Student Services and stays silent.', prove='Decision of 16 October 2026: a slip goes to staff in a normal chat.', imgw=700, quote='I paid my tuition. Here is the slip.', who='Wai Yan Lynn, 16:06')
    moment(d, 'Wed 14', 'A staff member checks the slip and replies by hand', 'Moment 3, steps 3 to 5', v2.fcrop('v2/s1_4.png', (285, 112, 1070, 745)), [
        ('A normal inbox chat', 'The slip is in the conversation, where the staff member can see it.'),
        ('A person checks it', 'Amount, name, date and reference, by eye.'),
        ('The reply is human', 'The student reads it in the same LINE chat.')],
        'S1.4: Siriporn K. replies in the same chat', 'In the staff inbox the slip sits in a normal chat. Siriporn checks it and replies by hand. The assistant stays silent. The student reads the reply on LINE the next morning.', imgw=900)
    moment(d, 'Wed 14', 'Then the staff member asks the assistant to record it', 'Moment 3, steps 6 and 7', v2.fcrop('v2/s1_6.png', (285, 130, 1070, 470)), [
        ('Records agent', 'Reads the open balance of student 67111411: 12,500 THB.'),
        ('A yes first', 'The assistant says what it will write and waits for a yes.'),
        ('Request agent', 'Writes the payment record and the audit entry in one transaction.')],
        'S1.6: a different chat, with the assistant', 'This is a different chat from the one with the student. The staff member says the student paid and asks for the database update. The assistant reads the balance, asks for a yes, writes the record and the audit entry.', prove='Frames S1.6 and S1.7.', imgw=900, quote="Wai Yan Lynn, ID 67111411, paid this semester's fee. Update the database.", who='Siriporn K., Student Services')
    moment(d, 'Wed 14', 'Thursday 15. The student sees the balance as paid', 'Moment 3, step 8', v2.fcrop('v2/s1_8.png', (150, 100, 1290, 880)), [
        ('The Fees page', 'Amount due 0 THB. Paid on 15 October.'),
        ('One record', 'The portal shows what the staff member wrote.'),
        ('A person decided', 'The audit log holds the staff member and the time.')],
        'S1.8: the Fees page after the update', 'The portal now shows a balance of 0 THB. A person decided. The assistant did the bookkeeping, with a yes and an audit record.', imgw=900)
    chatvs.chat_vs(d, 'watch', section='Wed 14', over='The request, two days later', notes=N('Back to the transcript request of Wednesday. The student asked to be told when it is ready. On Friday morning a staff member sets the state to Ready and the assistant writes first.', show='Third window: Friday 09:12.', prove='Design: WATCH entity in diagram 02. The ordinary-bot reply is a made-up illustration. The prototype shows the message itself in story S7, on Telegram. The watch is design.', mins=1))
    # ---------------- Tue 20
    v2.section_c(d, 'Tuesday 20 October', 'A missed exam, then the University side', 'A rule nobody scripted, then staff, an instructor and an administrator.', notes=N('Tuesday.', mins=0), section='Tue 20')
    chatvs.chat_vs(d, 'makeup', section='Tue 20', over='Same message', notes=N('On Tuesday morning the student writes that the ICT411 midterm was missed on Monday. The ordinary bot falls back to a stock sentence. Ours finds Handbook 8.2, counts the working days in code, opens a request with the photo of the certificate, and staff decide.', prove='A comparison mock built on a fictional Handbook rule (section 8.2). The prototype has no frame for this story.', mins=1.5))
    chatvs.chat_vs(d, 'gap', section='Tue 20', over='Administrator', notes=N('The administrator asks which questions had no answer, adds a document after a yes, and the next day a student gets a cited answer.', prove='Design: UNANSWERED_QUESTION in diagram 02. The ordinary-bot reply is a made-up illustration. The prototype has no frame for it.', mins=1))
    chatvs.chat_vs(d, 'blocked', section='Tue 20', over='A refused call', notes=N('A student session asks for the staff queue. The role decides which tools exist. The refusal is written to the audit log.', prove='Planned test: 10 staff-tool attempts, none may succeed. The ordinary-bot reply is a made-up illustration. This scenario is a comparison mock; the prototype has no frame for it.', mins=1))
    chatvs.chat_vs(d, 'approve', section='Tue 20', over='Staff', notes=N('Staff read the queue on Telegram and approve a request. A yes comes first, the state changes, the student is told on LINE, and the audit log holds the staff member.', mins=1))
    chatvs.chat_vs(d, 'attend', section='Tue 20', over='Instructor, 29 October', notes=N('A week later, an instructor asks who missed yesterday class. A tool counts the absences, the Handbook gives the limit, and a reminder is sent only after a yes.', mins=1))
    chatvs.chat_vs(d, 'admin', section='Tue 20', over='Administrator', notes=N('An administrator adds a document and creates accounts from a file. A validator checks the rows first, and accounts are created only after a yes.', mins=1))
    # ---------------- under the hood
    v2.section_c(d, 'Behind every moment', 'Under the hood', 'Four rules in code make the week true.', notes=N('The architecture.', mins=0), section='Under the hood')
    v2.ground_rules(d, 'Under the hood')
    setn(P.m_solution(d), N('The proposed solution in one line: a person writes on any channel, the supervisor picks a sub-agent, a tool reads or writes after a yes, and the reply returns on the same channel. A person takes over when needed.', prove='Feasibility report v3, sections 1.5 and 6.1, and diagram 01.', mins=1), 'Under the hood')
    setn(P.m_trace(d), N('Every objective traces to requirements, to a component and to a test. This is why each part of the architecture exists.', prove='Feasibility report v3, sections 1.3, 4.2 and 4.3.', mins=1), 'Under the hood')
    setn(M.m_arch(d), N('One picture behind every moment. People, two entry points, one application with one supervisor, data and services below.', prove='Diagram 01.', mins=1.5), 'Under the hood')
    setn(M.m_flow(d), N('What happened to each message in the week: who is writing, is a person on this chat, split, pick a tool, three checks, read or write after a yes, one reply.', prove='Diagram 03.', mins=1.5), 'Under the hood')
    setn(M.m_agents(d), N('The supervisor calls four sub-agents as tools. A role middleware filters the tools on every model call.', mins=1), 'Under the hood')
    setn(M.m_safety(d), N('The token decides who, the role decides what exists, a yes comes before a write, no source means refusal, and a person decides money.', mins=1), 'Under the hood')
    setn(M.m_engines(d), N('Two engines cover every feature: one reservation engine and one four-state request machine.', mins=1), 'Under the hood')
    setn(M.m_channels_tests(d), N('We tested Chatwoot live. Nine of eleven checks passed. Cards failed, so every channel uses plain text.', prove='11 checks, 9 passed.', mins=1), 'Under the hood')
    setn(P.m_models(d), N('We picked the diagrams that carry the design and skipped the rest. The Figma prototype is the wireframe set: 305 frames in 14 stories.', prove='Diagrams in design/diagrams, 12 files, and the Figma prototype.', mins=1), 'Under the hood')
    # ---------------- plan
    v2.parts_map(d, 'Plan')
    setn(M.m_objectives(d), N('Seven objectives for the build.', mins=1), 'Plan')
    setn(P.m_users(d), N('Who it is for: six kinds of person and what each one needs. The office is small and the questions come in peaks.', prove='Feasibility report v3, section 1.4.', mins=0.5), 'Plan')
    setn(P.m_stakeholders(d), N('The stakeholder register. Students and staff are the primary users and have high influence, because the system has no value if either group does not use it. The model service is a single point of failure.', prove='Feasibility report v3, section 4.1.', mins=0.5), 'Plan')
    setn(M.m_requirements(d), N('Thirty three functional and five non functional requirements, each with a test. Nineteen are core and fourteen are extended. Say three of them out loud: 200 concurrent requests on one slot, exactly one succeeds; zero successful cross account attempts; 80 and 90 percent accuracy scored by two raters.', prove='Feasibility report v3, requirements table.', mins=1), 'Plan')
    setn(P.m_nfr(d), N('The five non functional requirements, each with a test. The speed targets are proposals for the hosted model until the week two test measures them.', prove='Feasibility report v3, section 4.3. Targets are proposals until measured.', mins=0.5), 'Plan')
    setn(M.m_scope(d), N('Scope is frozen. The payment slip is in as you saw it. Payment processing is out.', mins=1), 'Plan')
    setn(P.m_constraints(d), N('Constraints, assumptions and limits, stated and not hidden. The assumption that a free model is good enough at tool calling is checked in week two, not assumed.', prove='Feasibility report v3, section 6.3.', mins=0.5), 'Plan')
    setn(M.m_stack(d), N('Every tool is free or open source.', mins=0.5), 'Plan')
    setn(P.m_devmethod(d), N('We work in short iterative cycles with a prioritized backlog. The core requirements come first and the extended ones after. Every track has a yes or no milestone each week. Track owners are not assigned yet.', prove='Feasibility report v3, sections 2.2 and 2.3, and the git log.', mins=0.5), 'Plan')
    setn(M.m_timeline(d), N('Ten weeks, with week ten as a buffer.', mins=0.5), 'Plan')
    setn(M.m_risks(d), N('Known risks and what we do about each.', mins=0.5), 'Plan')
    setn(M.m_decisions(d), N('Decided, and open on purpose.', mins=0.5), 'Plan')
    setn(M.m_eval(d), N('Targets, not results.', mins=0.5), 'Plan')
    setn(M.m_tests(d), N('Eleven channel checks, nine passed.', mins=0.5), 'Plan')
    setn(M.m_deliverables(d), N('Seven deliverables of Project I.', mins=0.5), 'Plan')
    setn(M.m_proj2(d), N('Project II adds more of the same on the same two engines.', mins=0.5), 'Plan')
    slot = P.m_propmap_slot(d, notes=N('Close the proposal. Every one of the 17 suggested sections has a slide. Offer the checklist to the instructor.', prove='Week 7 slides: the 17 suggested sections of the proposal.', mins=0.5))
    slot.section = 'Plan'
    M.m_thanks(d, notes=N('Thank the room. Offer to open the prototype on any frame.', mins=3))
    v2.section_a(d, None, 'Appendix', 'Reference slides.', notes='Reference.', section=None)
    for k in ['visa', 'record', 'slip', 'transcript', 'remind', 'scope', 'slipdb', 'move', 'advisor', 'cross', 'conflict', 'query']:
        chatvs.chat_vs(d, k, over='Appendix', section=None, notes=N('Reference slide. The left side is an illustration.'))
    M.m_appx_img(d, 'Appendix: use case diagram', 'dg_12_use_case.png', 'Source: 12_use_case.drawio')
    M.m_appx_img(d, 'Appendix: entity relationship diagram', 'dg_02_er.png', f'{len(M.ER_ENTITIES)} entities. Source: 02_er.mmd')
    M.m_appx_sources(d)
    P.fill_propmap(d, slot)
    v2.add_prove(d)
    v2.fit_time(d)
    return d
