"""Deck A, The Case. Evidence first: answer, problem, design, demonstration, plan. Theme A (white and teal)."""
import lib
from lib import C
import modules as M
import chatvs
import v2
import proposal as P
from v2 import N

SECTIONS = ['Opening', 'Problem', 'Answer', 'Architecture', 'Demo', 'Delivery']


def setn(s, text, section=None):
    s.notes = text
    if section:
        s.section = section
    return s


def make():
    d = lib.Deck('Deck_A_The_Case', 'Smart University Website: The Case', theme='A', sections=SECTIONS)
    # ---------- opening ----------
    v2.title_a(d, 'An assistant that answers from the rules, acts after a yes and hands hard cases to people')
    setn(M.m_team(d), N('Four members, one course. The project is built so that any university can adopt it, so nothing depends on one campus. Wai Yan Lynn owns the design and the documents. The other three own the diagrams, and the four build tracks are not assigned yet.', mins=1), 'Opening')
    rows = [['2', 'Opening: the answer first', 'This deck'],
            ['6', 'The problem, led by a survey of 17 universities', 'Survey report'],
            ['4', 'Objectives, requirements and scope', 'Feasibility report'],
            ['8', 'Architecture: how one message becomes an action', '12 diagrams'],
            ['12', 'Demo: ordinary bots against our assistant, then the live prototype', 'Figma prototype'],
            ['5', 'How we build it, where we are, Project II', 'Feasibility report'],
            ['3', 'Questions', 'Everyone']]
    assert sum(int(r[0]) for r in rows) == 40
    setn(M.m_agenda(d, rows), N('Forty minutes. The answer first, then the evidence for the problem, the design, a demonstration, and the plan. Keep questions for the end. The demo is the longest part, and it ends with a live click-through of one story.', mins=0.5), 'Opening')
    v2.exec_summary(d, 'Opening')
    # ---------- problem ----------
    setn(P.m_background(d), N('Context first. Universities have put their services online and students use chat every day. What is missing is the join between them. Say the numbers once and move on.', prove='Survey report and feasibility report v3, section 1.', mins=1), 'Problem')
    setn(M.m_problem(d), N('Three problems, and we say where each one comes from. Problem one and the status count come from our survey. Problems two and three come from how student services work, as written in the feasibility report. We did not survey students. Universities are well equipped on the basics. The gap is elsewhere.',
         prove='Survey of 17 websites, 5 and 6 October 2026: 13 of 17 take online requests, 3 of 17 show a status, none of the 12 Thai universities does.', bridge='So how did we measure it?', mins=1.5), 'Problem')
    setn(M.m_method(d), N('We did not pick one university, because the system is built to be adopted by any of them. We measured 17 institutions with the same seven questions, from public pages only. Say the limits: no logins, no student survey.',
         prove='Every row can be rechecked from the sources in the appendix.', bridge='Here is the result.', mins=1), 'Problem')
    setn(M.m_heatmap(d), N('Read the picture left to right. The first four columns are mostly green: services and chat channels exist. In the last three columns no university gets a full tick. Four cells are partial: NUS, KMUTNB and Buriram Rajabhat run fixed scripts or answer outside the chat. That is the gap: nothing joins the services and the chat channel.',
         show='Point at the red band: C5, C6 and C7.', prove='Full ticks out of 17: 13, 3, 11, 15, 0, 0, 0.', bridge='The same data as bars.', mins=1.5), 'Problem')
    setn(M.m_bars(d), N('Fifteen of seventeen already run a chat channel, so conversation is accepted. But the bars for citing rules, acting in the chat and one place are empty. Only 3 of 17 show a student the state of a request, and none of the 12 Thai ones do.',
         bridge='What does that mean for a typical bot?', mins=1), 'Problem')
    setn(M.m_cmp_table(d), N('Be fair to the existing bots. They can run real actions. Their limit is coverage: everything was written in advance by a person. Our design retrieves from the University\'s own documents and picks tools by reading what each tool does. The right column is our design, not a measured result yet.',
         prove='NN Bot at KMUTNB and the Buriram Rajabhat chatbot are published, intent-based bots.', bridge='So what do we promise to build?', mins=1), 'Problem')
    # ---------- answer ----------
    setn(M.m_objectives(d), N('Seven objectives, all from feasibility report v3. Objective five covers staff, instructors and administrators, and was added on 15 October.', mins=1), 'Answer')
    setn(P.m_users(d), N('Who it is for: six kinds of person and what each one needs. The office is small and the questions come in peaks.', prove='Feasibility report v3, section 1.4.', mins=0.5), 'Answer')
    setn(P.m_stakeholders(d), N('The stakeholder register. Students and staff are the primary users and have high influence, because the system has no value if either group does not use it. The model service is a single point of failure.', prove='Feasibility report v3, section 4.1.', mins=0.5), 'Answer')
    setn(M.m_requirements(d), N('Thirty three functional and five non functional requirements, each with a test written next to it. Nineteen are core and fourteen are extended. Say three of them out loud: 200 concurrent requests on one slot, exactly one succeeds; zero successful cross account attempts; 80 and 90 percent accuracy scored by two raters. The performance targets are proposals for the hosted model until the week two test.',
         prove='Feasibility report v3, requirements table.', mins=1.5), 'Answer')
    setn(P.m_nfr(d), N('The five non functional requirements, each with a test. The speed targets are proposals for the hosted model until the week two test measures them.', prove='Feasibility report v3, section 4.3. Targets are proposals until measured.', mins=0.5), 'Answer')
    setn(M.m_scope(d), N('Scope is frozen. A guest never uses the assistant. Staff, instructors and administrators do, with role limits. Payment processing and a real student information system stay out. The payment slip is in, because a person checks it and the assistant only records the update after a yes.', mins=1), 'Answer')
    setn(P.m_constraints(d), N('Constraints, assumptions and limits, stated and not hidden. The assumption that a free model is good enough at tool calling is checked in week two, not assumed.', prove='Feasibility report v3, section 6.3.', mins=0.5), 'Answer')
    setn(M.m_roles(d), N('One application, six kinds of person: four roles plus the guest and the IT team. The role comes from the Keycloak account, and the tools and the rows follow the role. Staff see conversations that were passed to them, never private chats. The IT team only has the Chatwoot admin screen, with its own login.', mins=0.5), 'Answer')
    setn(P.m_solution(d), N('The proposed solution in one line: a person writes on any channel, the supervisor picks a sub-agent, a tool reads or writes after a yes, and the reply returns on the same channel. A person takes over when needed.', prove='Feasibility report v3, sections 1.5 and 6.1, and diagram 01.', mins=1), 'Answer')
    # ---------- architecture ----------
    setn(P.m_trace(d), N('Every objective traces to requirements, to a component and to a test. This is why each part of the architecture exists.', prove='Feasibility report v3, sections 1.3, 4.2 and 4.3.', mins=1), 'Architecture')
    setn(M.m_arch(d), N('One picture. People at the top, two entry points, one FastAPI application with one supervisor, and the data and services at the bottom. Chatwoot owns the three channels and the human handoff. Everyone signs in through Keycloak, and the REST layer checks the token and reads the role.',
         prove='Diagram 01, architecture.', bridge='Now what happens to one message.', mins=1.5), 'Architecture')
    setn(M.m_flow(d), N('This is the route of one message. First the system resolves who is writing and in which role. If a staff member handles the chat, the assistant stays silent. Otherwise the supervisor splits the message and a sub-agent chooses a tool. Before any tool runs, three checks happen. A write needs a yes and runs in one transaction with an audit record. The reply goes back on the same channel.', prove='Diagram 03, supervisor routing.', mins=1.5), 'Architecture')
    setn(M.m_agents(d), N('The supervisor is one LangChain agent. The four sub-agents are wrapped as tools that it calls. A role middleware filters which tools are visible on each model call, so a student session cannot even see a staff tool. Records only reads. Booking and Request write, and only after a yes.', prove='LangChain agents: tools and middleware (wrap_model_call). The archived langgraph-supervisor library is not used.', mins=1), 'Architecture')
    setn(M.m_safety(d), N('Access control is the part that matters most, so we build as if the data were real. Every tool takes the subject from the verified token. The role decides which tools exist for the model. Nothing is written without a yes, and every write leaves an audit record. The assistant never decides on money. We will attack our own system in a planned test suite: 30 cross account attempts and 10 staff tool attempts from a student session must all fail. The suite is not written yet.', mins=1), 'Architecture')
    setn(M.m_engines(d), N('Two engines cover every feature. One reservation engine with slot locking handles anything bookable. One request state machine with four states handles anything trackable. Each is written once. On the left, two students pick the same slot: the second lock waits, then sees the slot is closed and gets alternatives.', prove='Planned tests: 200 concurrent requests, exactly one success; one request of each type through four states.', mins=1), 'Architecture')
    setn(M.m_handoff(d), N('A new conversation starts with the assistant. A staff member takes over by setting it to open, and the assistant stays silent while it is open. The staff member can release the chat back. We tested that a new chat stays pending and that a failing bot address opens the chat by itself. Staff takeover is design.', mins=0.5), 'Architecture')
    setn(M.m_channels_tests(d), N('Chatwoot is self-hosted and owns the three channels and the human handoff. We tested it live with a LINE official account and a Telegram bot. Text, photos and buttons work on both. Cards do not. So we decided on plain text on LINE and Telegram, and the web chat is plain text too. One behavior on every channel.',
         prove='Chatwoot test notes, 15 and 16 October 2026: 11 checks, 9 passed.', mins=1), 'Architecture')
    setn(M.m_data(d), N('One PostgreSQL database holds both the records and the document vectors. The model has 44 entities in six groups. Say the three groups that matter: requests and money, conversations and memory, and documents with their chunks. The full ER diagram is in the appendix.', prove='Diagram 02, entity relationship.', bridge='Now the demonstration.', mins=0.5), 'Architecture')
    setn(P.m_models(d), N('We picked the diagrams that carry the design and skipped the rest. The Figma prototype is the wireframe set: 305 frames in 14 stories.', prove='Diagrams in design/diagrams, 12 files, and the Figma prototype.', mins=1), 'Architecture')
    # ---------- demo ----------
    v2.parts_map(d, 'Demo')
    v2.ground_rules(d, 'Demo')
    v2.how_to_read(d, 'Demo')
    chatvs.chat_vs(d, 'visa', section='Demo', over='Comparison', notes=N('Student asks a rule question on the web. An ordinary bot matches a keyword and sends a link. Ours retrieves Handbook section 7.3, answers, shows the source and offers the next step.', show='Left red, then right teal. Read the shaded line.', prove='The ordinary-bot reply is a made-up illustration. Survey: 0 of 17 show the rule behind an answer.', mins=1))
    chatvs.chat_vs(d, 'record', section='Demo', over='Comparison', notes=N('Own record yes, someone else\'s record no. The student ID comes from the token, never from the message text. The blocked attempt goes to the audit log.', prove='Planned test: 30 other-student attempts, 30 refusals.', mins=1))
    chatvs.chat_vs(d, 'slip', section='Demo', over='Comparison', notes=N('A student sends a payment slip on Telegram. An ordinary bot cannot read a photo and sends the student to email. Ours hands the chat to Student Services, goes silent, and a person checks the slip and replies in the same chat. The agent never decides on money.', show='Right window: the shaded line, then the staff reply.', mins=1))
    chatvs.chat_vs(d, 'retry', section='Demo', over='Comparison', notes=N('A tool fails. The ordinary bot says try again later and forgets the question. Ours says what happened, saves the question and retries every 5 minutes. When the grade service answers, the assistant writes to the student on its own.', show='Third window: the message that arrives with no new question.', prove='Prototype story S9: the assistant retried at 08:35, 08:40 and 08:45.', mins=1))
    chatvs.chat_vs(d, 'watch', section='Demo', over='Comparison', notes=N('The student asks to be told when the transcript is ready. The ordinary bot cannot watch anything. Ours saves a watch on the request. Days later a staff member sets the state to Ready and the assistant writes first.', show='Third window: the message nobody asked for that morning.', prove='Design: WATCH entity in diagram 02 and the watch branch in diagram 03. The ordinary-bot reply is a made-up illustration. The prototype shows the message itself in story S7, on Telegram. The watch is design.', mins=1))
    chatvs.chat_vs(d, 'handoff', section='Demo', over='Comparison', notes=N('The student asks for a person. An ordinary bot gives a phone number. Ours passes the whole chat on and stays silent, and the staff member opens a summary and a draft reply instead of a blank page.', show='Third window: summary and draft in the staff console.', prove='Design: handoff in diagram 03. The prototype shows the staff console conversation in frame S1.4. The summary and draft are a mock.', mins=1))
    chatvs.chat_vs(d, 'gap', section='Demo', over='Comparison', notes=N('An administrator asks which questions had no answer. The top one was asked 14 times. After a yes the document is indexed and the open questions are tested again. The next day a student gets a cited answer.', show='Third window: the gap is closed.', prove='Design: UNANSWERED_QUESTION and DOCUMENT_CHUNK in diagram 02. The ordinary-bot reply is a made-up illustration. The prototype has no frame for it.', mins=1))
    chatvs.chat_vs(d, 'blocked', section='Demo', over='Comparison', notes=N('A student session asks for the staff queue. The role decides which tools exist, so the call never reaches a tool. The refusal is written to the audit log, and the administrator can replay what was stopped.', show='Third window: the audit log.', prove='Planned test: 10 staff-tool attempts from a student session, none may succeed. The ordinary-bot reply is a made-up illustration. This scenario is a comparison mock; the prototype has no frame for it.', mins=1))
    v2.lanes_s1(d, 'Demo')
    s = d.add(section='Demo', notes=N('Now the live part. Open the Figma prototype on story S1 and press Next. Say what each frame is while you click. If Figma fails, the appendix holds every frame as a slide.', show='Figma, Prototype page, presentation view, flow S1 Payment slip. Next, Next, Next.', prove='All 8 frames exist in light and the web ones in dark.', bridge='Back to the slides for the plan.', mins=6))
    y = v2.hdr(s, 'Live: follow one payment slip from the student to the database', 'Demo', size=46)
    rows = [['Step', 'Frame', 'Say while you click'],
            ['1', 'S1.1 Student sends the slip on LINE', 'A photo, plain text, no buttons.'],
            ['2', 'S1.2 The assistant hands the chat to staff', 'It does not read the slip and does not decide.'],
            ['3 and 4', 'S1.3 and S1.4 Staff inbox', 'A normal chat. A person checks and replies by hand.'],
            ['5', 'S1.5 The student reads the reply', 'The same LINE chat. The assistant stayed silent.'],
            ['6 and 7', 'S1.6 and S1.7 Ask the assistant', 'The staff member says update the record. A yes comes first.'],
            ['8', 'S1.8 The Fees page', 'The balance is 0 THB. The audit log holds the staff member.']]
    s.table(96, y, [150, 760, 818], rows, size=26, hsize=24, minrow=84, pad=20)
    v2.source(s, 'Prototype v2.1, 18 October 2026. Press Next at the bottom right of every frame. Press Start again on the last frame.')
    # ---------- delivery ----------
    setn(M.m_stack(d), N('Every tool is free or open source. The big change since the first feasibility report is the model: we moved from a local model to a hosted free tier, so tool calling is more reliable and no laptop has to carry a model. The supervisor library is archived, so the supervisor is one LangChain agent that calls sub-agents as tools.', mins=0.5), 'Delivery')
    setn(P.m_devmethod(d), N('We work in short iterative cycles with a prioritized backlog. The core requirements come first and the extended ones after. Every track has a yes or no milestone each week. Track owners are not assigned yet.', prove='Feasibility report v3, sections 2.2 and 2.3, and the git log.', mins=0.5), 'Delivery')
    setn(M.m_timeline(d), N('Ten weeks, from the feasibility report, updated for the current design. Week ten is a buffer with no new features. Week two is for measuring: the evaluation sets are written and frozen and the model is chosen by testing. The four interfaces are agreed in week one.', mins=0.5), 'Delivery')
    setn(M.m_risks(d), N('The first risk changed: with a hosted free tier the risk is no longer an unreliable local model. It is rate limits and a model being withdrawn. Prompt injection is covered by tools that take the subject from the token and by an attack test suite. Chatwoot sends LINE messages as push messages and the free quota is not proven, so LINE is kept for the demo.', mins=0.5), 'Delivery')
    setn(M.m_decisions(d), N('Be open about what is decided and what is not. The left column is settled and recorded. The right column is open on purpose: the model is chosen by testing in development, and the database host and the LINE quota fix are decided when we have evidence.', mins=0.5), 'Delivery')
    setn(M.m_eval(d), N('How we will know it works. Two evaluation sets will be written and frozen before any agent code. Two people score the answers separately. We also test the hard things: the concurrency test, the cross account attacks and a usability test with five students. These are targets. We have no measured results yet.', mins=0.5), 'Delivery')
    setn(M.m_tests(d), N('Our first real test results, from 15 and 16 October. We ran a self-hosted Chatwoot behind an ngrok address and connected a LINE official account and a Telegram bot. Everything the design needs worked, and the one thing that failed, cards, changed the design. Eleven checks, nine passed.', mins=0.5), 'Delivery')
    setn(M.m_deliverables(d), N('Where we stand against the seven deliverables. We say plainly what is done and what is planned. The coded prototype is the big item still ahead.', mins=0.5), 'Delivery')
    setn(M.m_proj2(d), N('Project II keeps the two engines and adds more of the same. Everything on this list reuses the reservation engine or the request state machine, which is why it was deferred and not cancelled.', mins=0.5), 'Delivery')
    slot = P.m_propmap_slot(d, notes=N('Close the proposal. Every one of the 17 suggested sections has a slide. Offer the checklist to the instructor.', prove='Week 7 slides: the 17 suggested sections of the proposal.', mins=0.5))
    slot.section = 'Delivery'
    M.m_thanks(d, notes=N('Thank the room. Offer to open the prototype on any frame they ask about.', mins=3))
    # ---------- appendix ----------
    v2.section_a(d, None, 'Appendix', 'Reference slides. Open them only if asked.', notes='Reference slides.', section=None)
    # fallback frames
    v2.frames2(d, 'Fallback: the student side of the slip story', 'Appendix', 'v2/s1_1.png', 'S1.1 The student sends the slip on LINE', 'v2/s1_5.png', 'S1.5 The student reads the staff reply',
               'A photo goes in as a photo. The reply comes from a person, in the same chat.', notes=N('Use only if Figma fails.'), section=None)
    v2.frames2(d, 'Fallback: staff see the slip and reply by hand', 'Appendix', 'v2/s1_3.png', 'S1.3 Staff see the slip in the inbox', 'v2/s1_4.png', 'S1.4 Staff reply by hand in the same chat',
               'A normal chat. The assistant is paused while a person handles it.', notes=N('Use only if Figma fails.'), section=None)
    v2.frames2(d, 'Fallback: the staff member asks the assistant to record it', 'Appendix', 'v2/s1_6.png', 'S1.6 Ask: update the record. A yes comes first', 'v2/s1_7.png', 'S1.7 The record is written and audited',
               'Nothing is written without a yes. The audit log holds the staff member.', notes=N('Use only if Figma fails.'), section=None)
    v2.frames2(d, 'Fallback: the student sees the result', 'Appendix', 'v2/s1_8.png', 'S1.8 The Fees page shows the balance as paid', 'v2/dashboard.png', 'The portal dashboard before the update',
               'The portal shows what the staff member recorded.', notes=N('Use only if Figma fails.'), section=None)
    for k in ['room', 'transcript', 'memory', 'makeup', 'approve', 'remind', 'scope', 'slipdb', 'attend', 'move', 'admin', 'advisor', 'cross', 'conflict', 'query']:
        chatvs.chat_vs(d, k, over='Appendix', section=None, notes=N('Reference slide. The left side is an illustration, not a quote from a real bot.'))
    M.m_appx_img(d, 'Appendix: use case diagram', 'dg_12_use_case.png', 'Six actors and their use cases. Source: design/diagrams/12_use_case.drawio')
    M.m_appx_img(d, 'Appendix: supervisor routing and tool selection', 'dg_03_supervisor.png', 'Diagram 03. A payment slip hands the chat to staff. Source: design/diagrams/03_supervisor.mmd')
    M.m_appx_img(d, 'Appendix: charge and payment record', 'dg_07_state_payment_check.png', 'Diagram 07. The balance changes only when a staff member says yes to the record. Source: 07_state_payment_check.mmd')
    M.m_appx_img(d, 'Appendix: access map', 'dg_11_access_map.png', 'Who reaches what. Source: design/diagrams/11_access_map.mmd')
    M.m_appx_img(d, 'Appendix: deployment diagram', 'dg_10_deployment.png', 'Docker Compose services and what sits outside the host. Source: design/diagrams/10_deployment.mmd')
    M.m_appx_img(d, 'Appendix: entity relationship diagram', 'dg_02_er.png', f'{len(M.ER_ENTITIES)} entities. Source: design/diagrams/02_er.mmd')
    M.m_deploy(d)
    M.m_appx_sources(d)
    P.fill_propmap(d, slot)
    v2.add_prove(d)
    v2.fit_time(d, agenda=dict(title='Today in 40 minutes', rows={
        'Opening': ('Opening: the answer first, and the team', 'This deck'),
        'Problem': ('The problem, led by a survey of 17 universities', 'Survey report'),
        'Answer': ('Objectives, requirements, scope and roles', 'Feasibility report'),
        'Architecture': ('Architecture: how one message becomes an action', '12 diagrams'),
        'Demo': ('Demo: ordinary bots against our assistant, then the live prototype', 'Figma prototype'),
        'Delivery': ('How we build it, where we are, Project II', 'Feasibility report')}))
    return d
