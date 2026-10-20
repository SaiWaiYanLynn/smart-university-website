"""Slides that make the decks follow the 17 suggested sections of the Project Proposal (Week 7 slides).
Each function adds one slide and returns it. The text comes from feasibility report v3."""
import lib
from lib import C
import modules as M
from kit import hdr, box, arrow, note_bar

SECTION_NAMES = {
    1: 'Project title', 2: 'Background', 3: 'Problem statement', 4: 'Objectives', 5: 'Target users', 6: 'Stakeholders',
    7: 'Requirements', 8: 'Scope, constraints, assumptions', 9: 'Proposed solution', 10: 'Architecture', 11: 'System models',
    12: 'Technology stack', 13: 'Development methodology', 14: 'Project timeline', 15: 'Risks and mitigations',
    16: 'Project I deliverables', 17: 'Project II continuation plan',
}
# Which slide covers which section: a keyword that must appear in the slide title (lower case).
SECTION_KEYS = {
    2: ['background:'], 3: ['problem statement'], 4: ['objectives:'], 5: ['target users'], 6: ['stakeholders'],
    7: ['functional and 5 non-functional', 'non-functional requirements:'], 8: ['scope: what is in', 'constraints, assumptions'],
    9: ['proposed solution'], 10: ['the system in one picture', 'what happens to one message'], 11: ['system models'],
    12: ['technology stack'], 13: ['development method'], 14: ['timeline and milestones'], 15: ['risks we know'],
    16: ['seven deliverables'], 17: ['project ii plan'],
}


def _tile(s, x, y, w, h, number, label, color, fill):
    s.rect(x, y, w, h, fill=fill, stroke=C['border'], r=16)
    s.text(x + 24, y + 38, 250, number, size=52, weight=700, color=color, lh=1.0, fit=False)
    s.text(x + 24 + 250, y + 30, w - 24 - 250 - 20, label, size=26, color=C['text'], lh=1.28, h=h - 48)


def m_background(d, notes=None):
    s = d.add(notes=notes or 'Context first. Universities have put their services online, and chat is normal for students. What is missing is the join between them.')
    y = hdr(s, 'Background: services are online, but split and one-way', 'Proposal 2  ·  Background')
    cw = (1728 - 2 * 28) / 3
    s.text(96, y, 1728, 'What universities already offer', size=34, weight=700, color=C['teal_dark'])
    y1 = y + 56
    for i, (n, t) in enumerate([('13 of 17', 'take a request online'), ('11 of 17', 'let a student book a room online'), ('15 of 17', 'run an assistant or an official chat channel')]):
        _tile(s, 96 + i * (cw + 28), y1, cw, 150, n, t, C['teal'], C['teal_tint'])
    y2 = y1 + 150 + 40
    s.text(96, y2, 1728, 'What is missing', size=34, weight=700, color=C['red'])
    y3 = y2 + 56
    for i, (n, t) in enumerate([('3 of 17', 'show the student the state of a request'), ('0 of 17', 'cite the University\'s own rules or finish a request in chat'), ('0 of 17', 'offer the services from one place')]):
        _tile(s, 96 + i * (cw + 28), y3, cw, 150, n, t, C['red'], C['red_tint'] if 'red_tint' in C else C['panel'])
    note_bar(s, y3 + 150 + 30, 'Thai universities already run LINE bots, such as NN Bot at KMUTNB and the Buriram Rajabhat chatbot. They follow intents that a developer wrote in advance. Source: our survey of 17 websites, 5 and 6 October 2026.', size=26)
    return s


def m_users(d, notes=None):
    s = d.add(notes=notes or 'Who the system is for. Six kinds of person, with what each one needs. The environment is a small student services office with peaks at registration, fee deadlines and result days.')
    y = hdr(s, 'Target users and their environment', 'Proposal 5  ·  Target users')
    cards = [
        ('Student', 'Uses a phone and chat apps, often after office hours, in English or Thai. Wants an answer and a finished task. Does not read a manual.'),
        ('Staff, Student Services', 'Works from a shared inbox and office software. Is not a developer. Wants the whole case in one place, and routine updates in one sentence.'),
        ('Instructor and advisor', 'Teaches and advises. Wants no calendar work: appointments, advisees and attendance by one question.'),
        ('Administrator', 'Technical. Owns accounts, roles, documents and the deployment.'),
        ('Guest or applicant', 'Reads the public site, applies and checks the application status. Never uses the assistant.'),
        ('IT team', 'Runs the platform and the Chatwoot admin screen. Is not a role in the application.'),
    ]
    cw = (1728 - 2 * 28) / 3
    ch = 285
    for i, (t, b) in enumerate(cards):
        x = 96 + (i % 3) * (cw + 28)
        yy = y + (i // 3) * (ch + 24)
        s.rect(x, yy, cw, ch, fill=C['alt'], stroke=C['border'], r=18)
        s.rect(x, yy, cw, 12, fill=C['teal'] if i < 4 else C['charcoal'], r=6)
        s.text(x + 28, yy + 32, cw - 56, t, size=32, weight=700, color=C['ink'])
        s.text(x + 28, yy + 84, cw - 56, b, size=25, color=C['text'], lh=1.32, h=ch - 100)
    note_bar(s, y + 2 * ch + 24 + 24, 'Environment: a student services office of 3 to 6 staff, open on weekdays. Questions rise at registration, fee deadlines and result days.', size=26)
    return s


def m_stakeholders(d, notes=None):
    s = d.add(notes=notes or 'The stakeholder register. Students and staff are the primary users and have high influence, because the system has no value if either group does not use it. The model service is a single point of failure.')
    y = hdr(s, 'Stakeholders: interest and influence', 'Proposal 6  ·  Stakeholders')
    colw = [250, 460, 850, 168]
    rows = [
        ['Class', 'Who', 'Interest', 'Influence'],
        ['Primary users', 'Students. Student Services staff.', 'Students want a correct answer and a finished task without a counter. Staff want fewer repeat questions and every case with its history.', 'High'],
        ['Secondary users', 'Instructors who advise. Facility and library staff. The head of student services.', 'One booking for each published slot. Attendance and advising in one place. Volume and turnaround, and the decision to deploy.', 'Medium'],
        ['Administrators', 'The IT administrator', 'Accounts and roles, the container stack, the documents the assistant answers from.', 'High'],
        ['Platform', 'The IT team', 'Chatwoot inboxes, channels and the bot. Has its own login.', 'Medium'],
        ['External actors', 'OpenRouter. LINE. Telegram. Applicants.', 'The model service writes every reply, so it is a single point of failure. The web chat works without LINE and Telegram. Applicants only read the public site.', 'Low to high'],
    ]
    s.table(96, y, colw, rows, size=24, hsize=22, minrow=70, pad=14)
    return s


def m_nfr(d, notes=None):
    s = d.add(notes=notes or 'The five non functional requirements, each with a test. The speed targets are proposals for the hosted model, and the week two test measures them.')
    y = hdr(s, 'Non-functional requirements: five targets, each with a test', 'Proposal 7  ·  Requirements', size=48)
    colw = [300, 900, 528]
    rows = [
        ['Requirement', 'Target', 'Test'],
        ['NFR-01 Performance', 'First visible token 3 s, full reply 10 s or 6 s, 10 concurrent conversations. Proposals until measured.', '100 requests, 95th percentile'],
        ['NFR-02 Security', 'Sign-in tokens (OIDC) are signed and expire in 15 minutes. Browser traffic uses TLS 1.2 or higher. No password stored. 0 of 40 attacks succeed.', '30 + 10 attack attempts'],
        ['NFR-03 Usability', 'A first-time student books a study room in 90 seconds or less and 4 messages or fewer.', '5 test users, at least 4 succeed'],
        ['NFR-04 Reliability', 'One docker compose up within 5 minutes. A restart loses no reservation and no request. A service message within 10 seconds if the model is rate limited or unreachable.', 'Clean machine test'],
        ['NFR-05 Accuracy', 'Routing 90 percent or higher. 80 percent of 50 answers correct with a correct citation, English and Thai reported separately.', '100 messages, two raters'],
    ]
    s.table(96, y, colw, rows, size=24, hsize=24, minrow=90, pad=18)
    return s


def m_constraints(d, notes=None):
    s = d.add(notes=notes or 'Constraints, assumptions and limits, stated and not hidden. The assumption that a free model is good enough at tool calling is checked in week two, not assumed.')
    y = hdr(s, 'Constraints, assumptions and limitations', 'Proposal 8  ·  Scope')
    cols = [
        ('Constraints', C['charcoal'], ['Ten working weeks, four people, and no new features in week 10', 'A build budget of zero, with one optional purchase of about 10 credits', 'Docker Compose on one host, no orchestration', 'Free tier: 20 requests a minute, 50 a day, until credits are bought']),
        ('Assumptions', C['teal'], ['A free hosted model follows tool schemas well enough. We test it in week 2', 'Documents we write from public handbooks are close to real ones', 'Students use a chat without training', 'Resource owners publish availability digitally', 'The interfaces frozen in week 1 stay stable']),
        ('Limitations we state', C['amber'], ['The demo needs the internet and one laptop with a tunnel', 'All data is made up, so messy real records are not tested', 'Thai quality is expected below English. We measure the gap', 'The usability test has 5 users, too few to represent everyone', 'We write the test set, so two people score it']),
    ]
    cw = (1728 - 2 * 28) / 3
    for i, (t, col, bl) in enumerate(cols):
        x = 96 + i * (cw + 28)
        s.rect(x, y, cw, 760, fill=C['alt'], stroke=C['border'], r=18)
        s.rect(x, y, cw, 12, fill=col, r=6)
        s.text(x + 28, y + 36, cw - 56, t, size=36, weight=700, color=C['ink'])
        s.bullets(x + 28, y + 108, cw - 56, bl, size=26, gap=20, dot=col)
    return s


def m_solution(d, notes=None):
    s = d.add(notes=notes or 'The proposed solution in one picture. A person writes on any channel. The supervisor reads the role and picks a sub-agent. A tool reads or writes, after a yes for any write. The reply returns on the same channel, and a person takes over when needed.')
    y = hdr(s, 'Proposed solution: one assistant on the web, LINE and Telegram', 'Proposal 9  ·  Proposed solution')
    bw = (1728 - 3 * 56) / 4
    steps = [('A person writes', 'A student, instructor, staff member or administrator, on web, LINE or Telegram.'),
             ('The supervisor decides', 'The role comes from the account. One of four sub-agents takes each task.'),
             ('A tool reads or writes', 'A write needs a yes and leaves an audit record.'),
             ('The reply returns', 'On the same channel. A person takes over when needed.')]
    for i, (t, b) in enumerate(steps):
        x = 96 + i * (bw + 56)
        box(s, x, y, bw, 210, t, b, fill=C['teal_tint'] if i != 1 else C['teal'], stroke=C['teal'], tcolor=C['white'] if i == 1 else None,
            scolor=C['teal_100'] if i == 1 else None, tsize=30, ssize=24, pad=18)
        if i < 3:
            arrow(s, x + bw + 6, y + 105, x + bw + 50, y + 105)
    cards = [
        ('For students', ['Answers with the rule and its source', 'Rooms, appointments, requests and renewals in the chat', 'The state of every request, told by message']),
        ('For staff, instructors and administrators', ['The queue, attendance, approvals and account jobs in one sentence', 'A summary and a draft when a chat is handed over', 'Every write after a yes, with an audit record']),
        ('For a university that adopts it', ['Brings its own documents, student data, identity provider and channel accounts', 'Two engines cover every feature', 'No model runs on campus hardware']),
    ]
    cw = (1728 - 2 * 28) / 3
    y2 = y + 210 + 40
    for i, (t, bl) in enumerate(cards):
        x = 96 + i * (cw + 28)
        s.rect(x, y2, cw, 470, fill=C['alt'], stroke=C['border'], r=18)
        s.rect(x, y2, cw, 12, fill=C['teal'], r=6)
        s.text(x + 28, y2 + 34, cw - 56, t, size=32, weight=700, color=C['ink'], lh=1.2)
        s.bullets(x + 28, y2 + 130, cw - 56, bl, size=26, gap=22)
    return s


def m_models(d, notes=None):
    s = d.add(notes=notes or 'We picked the diagrams that carry the design and skipped the rest. Each model answers one question. The Figma prototype is the wireframe set: 270 frames in 12 stories.')
    y = hdr(s, 'System models: the diagrams we chose, and why', 'Proposal 11  ·  System models')
    colw = [430, 700, 598]
    rows = [
        ['Model', 'What it shows', 'Why we chose it'],
        ['Use case (diagram 12)', 'Six actors and what each can do', 'Keeps the scope visible'],
        ['Architecture (diagram 01)', 'Components, boundaries and outside services', 'Shows what is inside the system'],
        ['Supervisor flow (diagram 03)', 'How a message becomes a tool call, with the checks', 'The core logic of the product'],
        ['Entity relationship (diagram 02)', f'{len(M.ER_ENTITIES)} entities in one PostgreSQL database', 'The data the prototype uses'],
        ['State diagrams (06 to 09)', 'Request, charge, conversation and reservation', 'The two engines, each written once'],
        ['Sequence diagrams (04, 05)', 'One message from LINE to the reply. Two students, one slot', 'Prove the order of steps and the lock'],
        ['Wireframes: the Figma prototype', '270 frames in 12 stories, light and dark', 'Shows the user journeys before code'],
    ]
    yb = s.table(96, y, colw, rows, size=24, hsize=22, minrow=64, pad=12)
    note_bar(s, yb + 24, 'Not drawn: data flow, activity and class diagrams. The supervisor flow already shows the process, and more diagrams would add noise.', size=26)
    return s


def m_devmethod(d, notes=None):
    s = d.add(notes=notes or 'We work in short iterative cycles with a prioritized backlog. The core requirements come first and the extended ones after. Every track has a yes or no milestone each week. The track owners are not assigned yet.')
    y = hdr(s, 'Development method: short cycles, a backlog and a done condition', 'Proposal 13  ·  Methodology')
    w = (1728 - 28) / 2
    s.rect(96, y, w, 640, fill=C['alt'], stroke=C['border'], r=18)
    s.rect(96, y, w, 12, fill=C['teal'], r=6)
    s.text(96 + 28, y + 34, w - 56, 'How we work', size=36, weight=700, color=C['ink'])
    s.bullets(96 + 28, y + 100, w - 56, [
        'Iterative cycles of one week, each with a visible result',
        'A weekly integration check of the four tracks',
        'A prioritized backlog: core FR-01 to FR-19 first, extended FR-20 to FR-33 after',
        'A definition of done: the milestone is yes or no, and the tests of its requirements pass',
        'Version control on GitHub, with the commits visible since 12 October 2026'], size=27, gap=20)
    x2 = 96 + w + 28
    s.rect(x2, y, w, 640, fill=C['alt'], stroke=C['border'], r=18)
    s.rect(x2, y, w, 12, fill=C['charcoal'], r=6)
    s.text(x2 + 28, y + 34, w - 56, 'Four tracks behind agreed interfaces', size=36, weight=700, color=C['ink'])
    s.bullets(x2 + 28, y + 100, w - 56, [
        'Track 1: infrastructure and identity',
        'Track 2: corpus, test set and measurement',
        'Track 3: supervisor, sub-agents and tools',
        'Track 4: React application, consoles and channels',
        'Each track builds against a simple fake of the others until the real one is ready'], size=27, gap=20, dot=C['charcoal'])
    note_bar(s, y + 640 + 24, 'Track owners are not assigned yet. If we slip, we cut in a fixed order and we never cut the core.', size=26)
    return s


def m_trace(d, notes=None):
    s = d.add(notes=notes or 'Every objective traces to requirements, to a component and to a test. This is the answer to the question of why each part of the architecture exists.')
    y = hdr(s, 'From objective to test: every part of the design has a reason', 'Proposal 10  ·  Architecture', size=48)
    colw = [360, 330, 450, 588]
    rows = [
        ['Objective', 'Requirements', 'Component', 'Test'],
        ['1 Answer from the rules', 'FR-04, FR-05', 'Knowledge agent, pgvector', '50 questions, 80 percent correct. 10 with no coverage must refuse'],
        ['2 One conversation', 'FR-03, FR-08, FR-09, FR-17', 'Supervisor, Booking and Request agents', '200 requests on one slot, exactly one succeeds'],
        ['3 Durable state', 'FR-11, FR-12, FR-21', 'Request state machine, worker', 'One request through four states. A message within 60 seconds'],
        ['4 Keep the context', 'FR-13, FR-14, FR-20', 'Chatwoot, memory', 'Silence for 10 messages. One history on three channels'],
        ['5 Serve the University side', 'FR-02, FR-19, FR-27 to FR-30', 'Role middleware, row check', '10 calls of another role\'s tool, none succeeds'],
        ['6 Near-zero cost', 'NFR-01, NFR-04', 'OpenRouter adapter, Docker Compose', 'One compose up in 5 minutes. Cached evaluation runs'],
        ['7 Show it is easier', 'NFR-03', 'Portal and assistant', '5 test users, at least 4 succeed in 90 seconds'],
    ]
    s.table(96, y, colw, rows, size=24, hsize=22, minrow=70, pad=14)
    return s


def m_propmap_slot(d, notes=None):
    """A slide that is filled at the end of the build, when the slide numbers are known."""
    s = d.add(notes=notes or 'Close the proposal. Every one of the 17 suggested sections has a slide. Offer the checklist to the instructor.')
    return s


def fill_propmap(d, s):
    y = hdr(s, 'Proposal checklist: the 17 sections and the slides that cover them', 'The proposal', size=46)
    ai = next((i for i, x in enumerate(d.slides) if x.title_text == 'Appendix'), len(d.slides))
    where = {1: [1]}
    for n, keys in SECTION_KEYS.items():
        hits = []
        for i, x in enumerate(d.slides[:ai], 1):
            t = (x.title_text or '').lower()
            if any(k in t for k in keys):
                hits.append(i)
        where[n] = hits
    missing = [n for n, h in where.items() if not h]
    assert not missing, ('sections without a slide', missing)
    groups = [(1, 6), (7, 12), (13, 17)]
    cw = (1728 - 2 * 28) / 3
    for gi, (a, b) in enumerate(groups):
        x = 96 + gi * (cw + 28)
        s.rect(x, y, cw, 790, fill=C['alt'], stroke=C['border'], r=18)
        yy = y + 24
        for n in range(a, b + 1):
            s.ellipse(x + 24, yy + 2, 46, 46, fill=C['teal'])
            s.text(x + 24, yy + 10, 46, str(n), size=24, weight=700, color=C['white'], align='c', lh=1.1)
            s.text(x + 86, yy, cw - 86 - 24, SECTION_NAMES[n], size=27, weight=700, color=C['ink'], lh=1.2)
            sl = 'Slide ' if len(where[n]) == 1 else 'Slides '
            s.text(x + 86, yy + 36, cw - 86 - 24, sl + ', '.join(str(i) for i in where[n]), size=24, color=C['teal_dark'], lh=1.2)
            yy += 126
    return where
