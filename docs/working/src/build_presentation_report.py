"""Builds the presentation report as a PDF (HTML to Chrome) and as a Word file.

Run: ~/slides-venv/bin/python docs/working/src/build_presentation_report.py OUT_DIR
Needs python-docx and Pillow. Images are in docs/working/src/report_img.
One content list feeds both outputs, so the PDF and the Word copy say the same.
"""
import ast
import html
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, 'report_img')
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'out_report')
os.makedirs(OUT, exist_ok=True)

TITLE = 'Smart University Website'
SUB = 'Presentation Report, Project I'
COURSE = 'IT Project I and II (BC362916 and BC362914), Krirk University'
INSTRUCTOR = 'Dr. Aftab Alam Janisar'
DATE = '20 October 2026'
MEMBERS = [('Pyae Sone', '67111336'), ('Wai Yan Lynn', '67111411'),
           ('Myat Hsu Hnin', '68111423'), ('Nang Ying Noom Lao', '67111378')]
LINKS = [
    ('Presentation slides (Canva)', 'https://canva.link/m4d5yphk4qiojt4'),
    ('Clickable prototype (Figma)', 'https://www.figma.com/design/nDM8Bg8Or66Nk5j0d2CB4m/Thales-University-Prototype?node-id=0-1&t=krdn838rmwVghV5m-1'),
    ('Project repository (GitHub)', 'https://github.com/SaiWaiYanLynn/smart-university-website'),
]


def survey_data():
    src = open(os.path.join(HERE, 'build_feasibility_v3.py')).read()
    tree = ast.parse(src)
    out = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], 'id', '') == 'SURVEY':
            out[node.targets[0].id] = ast.literal_eval(node.value)
    survey = out['SURVEY']
    tot = [sum(1 for _, m, _ in survey if m[i] == 'Y') for i in range(7)]
    assert tot == [13, 3, 11, 15, 0, 0, 0], tot
    return survey, tot


def git_facts():
    root = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
    try:
        n = subprocess.check_output(['git', '-C', root, 'rev-list', '--count', 'HEAD'], text=True).strip()
        d = subprocess.check_output(['git', '-C', root, 'log', '--reverse', '--format=%ad', '--date=format:%-d %B %Y'], text=True).splitlines()[0]
        return n, d
    except Exception:
        return None, None


SURVEY, TOT = survey_data()
NCOMMITS, FIRSTDATE = git_facts()

B = []  # blocks


def h1(t): B.append(('h1', t))
def h2(t): B.append(('h2', t))
def p(t): B.append(('p', t))
def ul(items): B.append(('ul', items))
def table(head, rows, w=None, small=False): B.append(('table', dict(head=head, rows=rows, w=w, small=small)))
def img(f, cm, cap): B.append(('img', f, cm, cap))
def grid(items): B.append(('grid', items))
def pb(): B.append(('pb',))
def quote(t): B.append(('quote', t))


# ---------------------------------------------------------------- 1
h1('1. Summary')
p('Group S presented the Smart University Website for IT Project I on ' + DATE + '. The project is a student services assistant for a university. '
  'A student, instructor, staff member or administrator asks in a web chat, on LINE or on Telegram. '
  'The assistant answers from the rules of the university and names the section it used. '
  'It completes bookings and requests after the user says yes, and it hands the chat to a person when it is not sure.')
p('The midterm needs no code. The talk used slides, diagrams and a clickable Figma prototype. '
  'This report records what we presented, how the prototype works, the question we were asked, and what we do next.')
table(['Item', 'Value'], [
    ['University websites surveyed', '17 (12 in Thailand, 5 abroad), checked on 5 and 6 October 2026'],
    ['Websites with an assistant that cites its own rules, completes a request in the chat, or reaches all services from one place', '0 of 17'],
    ['Prototype', '270 frames in 12 stories, in light and dark versions, all clickable'],
    ['Requirements', '33 functional and 5 non-functional'],
    ['Data model', '44 entities'],
    ['Diagrams', '12 (architecture, data, routing, states, use cases and more)'],
], [58, 42])

# ---------------------------------------------------------------- 2
h1('2. The presentation')
p('The midterm needs no code. We built the talk around three things: slides in Canva, diagrams, and a clickable Figma prototype. '
  'The slides came first, and the Figma prototype followed. Questions came at the end.')
table(['Part of the talk', 'Main message'], [
    ['Background', 'Universities put services online, but in separate places. A student needs three systems and three logins for three tasks.'],
    ['Survey', 'We checked 17 university websites on seven capabilities. Basic services are common. Three capabilities are missing everywhere.'],
    ['Problem statement', 'A student cannot finish a university task in one place. Services are split apart, hard to find and hard to share.'],
    ['Objectives', 'One general objective and five specific ones. Each one answers a problem.'],
    ['Users and stakeholders', 'Six user groups, and a table of interest and influence.'],
    ['Requirements', 'The functional and non-functional requirements.'],
    ['Chatbot comparison', 'An ordinary bot and our assistant answer the same messages side by side.'],
    ['Technology stack', 'Each choice, and the reason for it.'],
    ['Architecture', 'A simple level 0 diagram, then the full architecture diagram.'],
    ['Use cases', 'Five roles, two outside systems and 29 use cases in seven groups.'],
    ['Data', '44 tables. One slot has one reservation. Documents keep their source. Every agent step is stored.'],
    ['Supervisor routing', 'One supervisor sends each message to the right agent. A write needs a yes.'],
    ['Scope', 'What the system will and will not do.'],
    ['Conclusion', 'Where we are, and what comes next.'],
], [26, 74])
p('The diagram slides show small pictures. During the talk we opened the full diagrams in draw.io and came back to the slides.')

# ---------------------------------------------------------------- 3
h1('3. The problem and the evidence')
h2('3.1 Three problems')
table(['Problem', 'What a student meets', 'Evidence from the survey'], [
    ['Services are split apart', 'A transcript, a room and a library book mean three systems with three logins.', '13 of 17 universities keep document requests in a separate system.'],
    ['Information is hard to find', 'The rule is inside a PDF handbook, so the student asks a senior instead.', '0 of 17 have an assistant that answers from the university\'s own regulations.'],
    ['Cases are hard to share', 'A case sits in one staff member\'s inbox. When that person is away, help stops.', 'Only 3 of 17 show the state of a request. None of the 12 Thai universities does.'],
], [24, 40, 36])
h2('3.2 The survey')
p('We checked the public pages of 17 universities, 12 in Thailand and 5 abroad, on 5 and 6 October 2026. We used no logins. '
  'Each university was checked on the same seven capabilities. We counted a capability only when we found clear public evidence.')
table(['Capability', 'Universities'], [
    ['C1  Submit a request online through a real form', '13 of 17'],
    ['C2  See the state of the request afterwards', '3 of 17'],
    ['C3  Book a room online', '11 of 17'],
    ['C4  Reach an assistant or an official chat channel', '15 of 17'],
    ['C5  The assistant answers from the university\'s own rules and shows the rule', '0 of 17'],
    ['C6  The assistant completes a request or booking in the chat', '0 of 17'],
    ['C7  These services are reachable from one place', '0 of 17'],
], [78, 22])
p('Universities have the basic services. The gap is in C5, C6 and C7. The full table, with notes for each university, is in the research report that comes with this report.')
h2('3.3 Chatbots that already exist')
p('Fifteen of the 17 universities have an assistant or an official chat channel. Some Thai universities have published LINE chatbots, such as NN Bot at KMUTNB and a chatbot at Buriram Rajabhat. '
  'These bots follow fixed intents, so they cover only the questions and flows that a developer wrote in advance. '
  'We do not claim that nobody has built a conversational university service. Our claim is about the kind of system. '
  'It retrieves from the university\'s own documents, covers several services, acts through tools, cites its source and tracks state.')

# ---------------------------------------------------------------- 4
h1('4. Our solution')
h2('4.1 What the assistant does')
ul(['Answers from the rules. It searches the university\'s own handbooks and cites the section.',
    'Does the task in the chat. A student books an advisor appointment or a study room, renews a loan, or asks for a document and then tracks it.',
    'Hands over to a person. A staff member takes the chat when the student asks or when the assistant is unsure. While a person owns the chat, the assistant stops replying.',
    'Works for every role. The signed-in account sets the role, and the role sets the tools.',
    'Asks before it writes. Every change needs a yes from the user and leaves an audit record.',
    'Uses plain text on chat apps. LINE and Telegram carry text only, with no buttons and no cards.'])
h2('4.2 One supervisor and four agents')
table(['Agent', 'Job', 'Rights'], [
    ['Supervisor', 'Reads the message and the role, splits the message into tasks and calls the right agent as a tool.', 'Routes only'],
    ['Knowledge', 'Finds passages in the university documents and returns an answer with its source.', 'Read'],
    ['Records', 'Returns the own record, timetable, fees and loans, the catalogue, and attendance of an own course.', 'Read only'],
    ['Booking', 'Lists free slots and books or changes an advisor appointment or a study room.', 'Write, after a yes'],
    ['Request', 'Handles document requests, loan renewals, payment records, approvals and bulk jobs.', 'Write, after a yes'],
], [16, 62, 22])
h2('4.3 Rules for every action')
ul(['Check the role and the rows that the role may read.', 'Cite the source document for a policy answer.',
    'Confirm with the user before any write.', 'Write an audit record for every write, every personal read and every blocked call.'])
p('A person decides every payment slip. The assistant never reads the slip image and never decides on money.')
h2('4.4 How people reach it')
img('channels_and_roles.png', 16.5, 'Figure 1. People write on LINE, Telegram or the web chat. Chatwoot passes the message to the agentic backend. Keycloak supplies the role.')
p('Students, instructors, staff and administrators write on LINE, on Telegram or in the web chat. Chatwoot owns these channels and the human handoff, and it calls the backend. '
  'Keycloak signs every user in and holds the role. The backend checks the role before any tool runs. Guests use the public website only and never use the assistant.')

# ---------------------------------------------------------------- 5
h1('5. Architecture and technology')
ul(['The REST layer checks the token with Keycloak and reads the role.',
    'The supervisor calls one of four sub-agents as tools. A role middleware filters the tools and the rows by role.',
    'A validator checks the arguments. The tool layer takes the subject from the token and never from the message text.',
    'The audit writer records every write, every personal read and every blocked call.',
    'A model adapter holds the key and the model name for OpenRouter, and it retries and queues on a rate limit.',
    'Scheduler and workers send reminders, retry failed questions and read uploaded documents.'])
img('architecture.png', 14, 'Figure 2. The full architecture. The React application and Chatwoot sit on top, the FastAPI application with the supervisor and four agents in the middle, and the data stores at the bottom.')
h2('5.1 Technology stack')
table(['Layer', 'Choice', 'Why'], [
    ['Backend', 'Python 3.12, FastAPI', 'The agent tools are strongest in Python.'],
    ['Agents', 'LangChain, LangGraph', 'One LangChain supervisor calls the sub-agents as tools. A role middleware filters the tools. LangGraph runs underneath.'],
    ['Model', 'OpenRouter, free tier', 'Hosted models follow tool schemas better than a small local model. The exact model is chosen by testing. Free limits count per account.'],
    ['Data', 'PostgreSQL 16, pgvector', 'One engine for records and document vectors.'],
    ['Identity', 'Keycloak, OIDC', 'No passwords in our code. An administrator creates the accounts.'],
    ['Channels', 'Chatwoot, self-hosted', 'Web, LINE, Telegram and human handoff in one service.'],
    ['Frontend', 'React with Vite', 'One app. Keycloak roles gate the routes.'],
    ['Deployment', 'Docker Compose, ngrok', 'One command starts everything. ngrok carries the channel webhooks during development.'],
    ['Testing', 'pytest, Locust', 'Automated tests, and a load test for concurrent chats.'],
    ['Supporting tools', 'GitHub, Figma, Mermaid, draw.io', 'Version control, the prototype and the diagrams.'],
], [16, 26, 58])
h2('5.2 Front-end libraries')
p('React draws the screens, and Vite builds and serves the app. The app also uses TypeScript, Tailwind CSS, React Router for the role-gated routes, TanStack Query for data from the API, and keycloak-js for sign-in.')

# ---------------------------------------------------------------- 6
h1('6. The prototype')
p('The prototype is a clickable Figma file with a small design system: Inter type, Lucide icons, an 8-point grid and text contrast that meets WCAG AA. '
  'It has 270 frames in 12 stories, and the public site, the student portal and the role consoles also have light and dark versions. '
  'Each story frame has a bar at the bottom with the actor, the channel, the step and a Next button. Every chat on LINE, Telegram, the web and the console is plain text.')
table(['Code', 'Story', 'Channels', 'Frames'], [
    ['S1', 'Payment slip, from the student to the database', 'LINE, staff console, web portal', '8'],
    ['S3', 'Own record, not someone else\'s', 'Web portal chat', '4'],
    ['S4', 'Book a study room on the web', 'Web portal chat', '6'],
    ['S5', 'Book a study room on LINE', 'LINE', '3'],
    ['S6', 'Two students, one room', 'LINE and Telegram', '3'],
    ['S8', 'A what-if grade question', 'Telegram', '2'],
    ['S9', 'A tool fails and the assistant recovers', 'LINE', '2'],
    ['T1', 'Staff ask the assistant in the console', 'Staff console, LINE', '4'],
    ['T2', 'Staff send a fee reminder', 'LINE and Telegram', '5'],
    ['T3', 'The registrar sends a Dean list notice', 'Staff console, LINE', '4'],
    ['I1', 'An instructor asks about tomorrow\'s classes', 'LINE', '1'],
    ['I2', 'An instructor sends an absence reminder', 'LINE', '5'],
], [9, 47, 34, 10])
p('The stories show one idea each. S1 follows a payment slip through three people and the database. T2 shows one staff message that reaches two students on two different channels. '
  'T3 shows a registrar who asks for a list and sends a notice after a yes. I2 shows a count done in code, a rule from the handbook, and a reminder sent after a yes.')
grid([('s1_1.png', 'S1.1 A student sends a payment slip on LINE'),
      ('s1_4.png', 'S1.4 Staff reply by hand in the same chat'),
      ('t1_2.png', 'T1.2 An approval waits for a yes'),
      ('t2_3.png', 'T2.3 A reminder goes out after a yes'),
      ('t3_3.png', 'T3.3 A Dean list notice goes to 42 students'),
      ('i2_3.png', 'I2.3 An instructor checks a draft before it is sent')])
h2('6.1 How to open the prototype')
ul(['Open the Figma link in section 10 and go to the Prototype page.',
    'Press Present, then open the Flows list and choose a story.',
    'Click Next at the bottom of each frame. The last frame says Start again.',
    'The sun and moon button in the menu switches a page to its dark version.'])

# ---------------------------------------------------------------- 7
h1('7. The plan in short')
p('We work in one-week cycles with a prioritized backlog. The core requirements (FR-01 to FR-19) come first and the extended ones (FR-20 to FR-33) come after. '
  'Each of four tracks has a yes or no milestone every week: infrastructure and identity, corpus and measurement, the agents and tools, and the React application with the channels.')
p('The build runs for ten weeks. Weeks 1 and 2 set up the foundations. Weeks 3 to 5 build the core. Weeks 6 to 8 add the channels and the role consoles. '
  'Week 9 adds the extended features and the tests. Week 10 is a buffer with no new features. If we fall behind, we cut in this order: study plans and signals, then bulk jobs and account files, then LINE. The team has not confirmed this order yet.')
p('The appendices hold the full timeline, the risks, the deliverables and the plan for Project II.')

# ---------------------------------------------------------------- 8
h1('8. Questions from the audience')
p('Most questions were about topics that the slides already covered, and we answered them during the session. One question needs a fuller answer here, because the answer is a plan and not yet a working feature.')
h2('Question: how can an existing university use this?')
quote('"Your plan, tech stack and schema are good for building a university from scratch. What about a university that already has its own website and database? How would it connect your system to its chatbot or its systems? Do you have connectors?"')
p('Our answer: by design, yes, but we have no ready-made connectors yet. Integration with a real student information system is planned for Project II. '
  'The design below is a proposal. We have not built or tested it.')
table(['Part', 'How an existing university connects it'], [
    ['Website', 'The Chatwoot web widget is one script tag. The university adds the chat to its own site without changing the rest of the site. LINE and Telegram need only the bot accounts of the university.'],
    ['Rules and handbooks', 'The ingestion worker reads the documents. The Knowledge agent works from the first day and needs no access to the database of the university.'],
    ['Login', 'Keycloak can connect to an existing login, through LDAP or Active Directory, or through SAML or OIDC. Students keep their usual accounts, and we map their groups to our roles.'],
    ['Student data', 'Every tool reads and writes through one tool layer. We would replace the data functions of that layer with an adapter to the student system of the university. The adapter would use read-only database views or the API of that system, or a nightly copy into our tables. We would start read-only and pilot one service.'],
    ['Our 44 tables', 'An adopting university would map only the few tables it needs, such as user, student record, course, enrollment and loan.'],
], [22, 78])
p('The main risk is the mapping work, because every university stores its data in a different shape. That is why the plan starts read-only and starts with one office.')

# ---------------------------------------------------------------- 9
h1('9. Next steps')
p('These decisions are still open:')
ul(['Assign an owner to each of the four build tracks.',
    'Confirm the cut order and the performance targets (see Appendix A).',
    'Decide whether to buy about 10 OpenRouter credits for the model tests.',
    'Decide how the backend handles the LINE push-message quota.',
    'Choose the production database host. Docker Compose is the choice for development and the demo.',
    'Write the Project Proposal document of 17 sections, and ask the instructor whether the seven deliverables are due at the midterm or at the end of Project I.',
    'Plan the adapters for an existing university (section 8) as part of Project II.'])

# ---------------------------------------------------------------- 10
h1('10. Links')
table(['Item', 'Link'], [[a, b] for a, b in LINKS], [32, 68])
p('Open the links while signed out of Canva, Figma and GitHub, to check that a reader without an account can see them.')

# ---------------------------------------------------------------- appendices
pb()
h1('Appendix A. Requirements')
h2('Functional requirements')
FR = [
    ('FR-01', 'Sign in through Keycloak. Reject a request without a valid token.'),
    ('FR-02', 'One role per account. Reject a call that the role does not permit.'),
    ('FR-03', 'Route each task to the Knowledge, Records, Booking or Request agent, and store the route.'),
    ('FR-04', 'Answer a policy question only from retrieved passages, with the source title and section.'),
    ('FR-05', 'Refuse and offer a person when no passage scores above the threshold.'),
    ('FR-06', 'Accept English and Thai, and reply in the language of the message.'),
    ('FR-07', 'Return the own timetable, registration, fees and loans. Refuse another student.'),
    ('FR-08', 'List free slots for an advisor appointment or a study room.'),
    ('FR-09', 'Reserve a slot in one transaction. Reject a second reservation of the same slot.'),
    ('FR-10', 'Cancel or reschedule only the own reservation, before the cut-off.'),
    ('FR-11', 'Hold a service request in one of four states: Submitted, Under review, Ready, Collected.'),
    ('FR-12', 'Tell the student on the original channel within 60 seconds of a state change.'),
    ('FR-13', 'Hand a chat to staff on request or on low confidence. Staff reply from the console.'),
    ('FR-14', 'Use the web widget, LINE and Telegram through Chatwoot, with one history per student.'),
    ('FR-15', 'Ask for a yes before every write. Write an audit record.'),
    ('FR-16', 'Search the library catalogue, read only.'),
    ('FR-17', 'Renew a loan when the rules allow it, after a yes.'),
    ('FR-18', 'Payment slip: the student sends it, staff check it, staff ask the assistant to record it after a yes. The assistant never reads the image.'),
    ('FR-19', 'Give each role its own tool set, including staff, instructors and administrators.'),
    ('FR-20', 'Keep facts from a chat and load them in the next conversation, keyed to the account.'),
    ('FR-21', 'Send reminders and tell a watching student when a request changes.'),
    ('FR-22', 'Keep a question when a tool fails. Retry every 5 minutes and send the answer later.'),
    ('FR-23', 'Give staff a summary and a draft reply when they take over a chat.'),
    ('FR-24', 'Record unanswered questions and source conflicts for an administrator.'),
    ('FR-25', 'Upload, split, embed and index a document in the background.'),
    ('FR-26', 'Accept a file or photo for an open request and attach it for staff.'),
    ('FR-27', 'Tell an instructor who missed a class and who is near the absence limit. Send a warning after a yes.'),
    ('FR-28', 'Prepare an advising brief, flag advisees by rules, and store a study plan that the advisor approves.'),
    ('FR-29', 'Send a bulk reminder to a named group after showing the size and a sample, and after a yes.'),
    ('FR-30', 'Manage accounts and roles, create accounts from a file after a yes, and read the system status and the audit log.'),
    ('FR-31', 'Compute grade sums, what-if grades and graduation plans in code, not in the model.'),
    ('FR-32', 'Let a guest read public pages, apply, check an application and send a message, without a login.'),
    ('FR-33', 'Record the route, steps and model use of every reply, and let a user rate a reply.'),
]
table(['ID', 'Requirement, in short'], [list(x) for x in FR], [10, 90], small=True)
h2('Non-functional requirements')
table(['ID', 'Quality', 'Target'], [
    ['NFR-01', 'Performance', 'First visible token in 3 seconds or less, a complete reply in 10 seconds or less for a retrieval answer and 6 seconds or less for a records answer (95th percentile). Ten concurrent chats with no failure.'],
    ['NFR-02', 'Security', 'OpenID Connect with signed tokens that expire within 15 minutes. TLS 1.2 or higher for browser traffic. No password stored by the application.'],
    ['NFR-03', 'Usability', 'A first-time student books a study room in 90 seconds or less and in 4 messages or fewer, with no written instructions.'],
    ['NFR-04', 'Availability', 'The stack starts from one docker compose command within 5 minutes. A restart loses no reservation and no submitted request.'],
    ['NFR-05', 'Accuracy', 'Routing accuracy of 90 percent or higher on 100 labelled messages. At least 80 percent of 50 test questions answered correctly with a valid citation.'],
], [10, 16, 74], small=True)
p('Note on NFR-01. The slide in the talk showed the first targets (4 seconds and 15 seconds). Feasibility report version 3 proposes the tighter targets above, because a hosted model is faster than a local one. The team has not confirmed either set.')

h1('Appendix B. Scope')
table(['In scope for Project I', 'Out of scope, or deferred to Project II'], [[
    'Public website and role-based portal. Keycloak login with four roles. The supervisor and four agents. Chat for staff, instructors and administrators, limited by role. Human handoff. Three channels with one history. Library search and loan renewal. Payment slip check by staff. An evaluation set of 50 questions and 100 routing messages. Extended features (memory, reminders, retries, handoff summary, uploads, attendance, advising, bulk reminders, account files, guest application). Docker Compose that starts everything.',
    'Final academic decisions and changes to official grades. Replacing staff. Payment processing, tuition payments and refunds. Library borrowing, returning and holds. Event registration and maintenance reports. Course add and drop. Resources other than advisor appointments and study rooms. Any channel beyond web, LINE and Telegram. Mobile apps, voice, and languages beyond English and Thai. Model training. Integration with a real student information system.']], [50, 50], small=True)

h1('Appendix C. Timeline and risks')
table(['Weeks', 'Phase', 'Work'], [
    ['W1 to W2', 'Foundations', 'Compose stack, schema, Keycloak realm, four agreed interfaces. Evaluation sets written and frozen. Model chosen by testing.'],
    ['W3 to W5', 'Core', 'Corpus indexed. Four sub-agents, supervisor, role middleware, audit. Slot locking. Four-state requests. Library. Memory.'],
    ['W6 to W8', 'Channels and roles', 'Chatwoot with Telegram, then LINE. Three role consoles. Handoff summary. Payment record. Reminders and retries.'],
    ['W9', 'Extended and tests', 'Attendance, advising, bulk jobs, uploads. Access tests, load test, scoring, usability test.'],
    ['W10', 'Buffer', 'No new features. Fix, document and rehearse.'],
], [14, 22, 64], small=True)
table(['ID', 'Type', 'Risk', 'What we do'], [
    ['R1', 'Technical', 'The free model tier limits us, or a free model is withdrawn.', 'The model name is one setting with a fallback list. Free limits are 20 requests a minute and 50 a day for each account. A full evaluation run needs cached results, days of spreading, or about 10 credits.'],
    ['R2', 'Technical', 'Prompt injection, or a request for another user\'s data.', 'Tools take the subject from the token. Tool allowlists. A test suite attacks every tool.'],
    ['R3', 'Scope', 'Scope creep, or a scope too big for ten weeks.', 'Core first, extended features after. The cut order is fixed in advance. Adding means removing.'],
    ['R4', 'Team', 'Four tracks do not fit together.', 'Four interfaces are agreed in week one. Each track builds against a fake of the others.'],
    ['R5', 'Schedule', 'The schedule slips or the work is uneven.', 'Weekly milestones with a done condition. Week 10 adds no features.'],
    ['R6', 'Technical', 'Thai answers are weaker than English answers.', 'Thai questions are in the test set from week 2. No source means refuse.'],
    ['R7', 'Technical', 'LINE push messages exceed the free quota.', 'LINE for the demo only. Load tests on Telegram and web. Free LINE replies in Project II.'],
    ['R8', 'Data', 'All data is made up, so messy real records are not tested.', 'We state the limit. Test data holds duplicates and gaps. We never claim real-world results.'],
    ['R9', 'User', 'Too few students join the usability test.', 'Book the five sessions early, in week 7. Report the real number of users.'],
], [6, 12, 36, 46], small=True)

h1('Appendix D. Deliverables and Project II')
vc = (f'GitHub repository started on {FIRSTDATE}, {NCOMMITS} commits so far.' if NCOMMITS else 'GitHub repository with commit history.')
table(['#', 'Deliverable of Project I', 'Status on ' + DATE], [
    ['1', 'Problem, objectives and requirements', 'Written: the survey report and feasibility report version 3, with 33 functional and 5 non-functional requirements.'],
    ['2', 'Architecture and models', 'Done: 12 diagrams, from architecture to use cases.'],
    ['3', 'Working prototype', 'The Figma prototype is built and was shown. A coded prototype is planned for weeks 3 to 9.'],
    ['4', 'Version control', vc],
    ['5', 'Initial testing results', '9 of 11 channel checks passed in a test of Chatwoot with LINE and Telegram. The evaluation and attack tests are planned.'],
    ['6', 'Documentation and records', 'Survey report, feasibility report version 3, 12 diagrams with source, and the prototype story map.'],
    ['7', 'Project II plan', 'See the table below.'],
], [6, 30, 64], small=True)
table(['Project II area', 'What it holds'], [
    ['Remaining features', 'Borrowing, returning and holds. Event registration. Maintenance reports. More bookable resources. Course add and drop. Each one reuses the reservation engine or the request state machine.'],
    ['Integration and hardening', 'A real student information system, with the adapters in section 8. Payment processing. Buttons and cards on LINE and Telegram. Free LINE replies instead of push messages.'],
    ['Deeper testing', 'Messy real records. More languages. Load beyond the free tier. A security review.'],
    ['Evaluation with users', 'A usability study with more than five students and staff members. Feedback collected and analysed.'],
    ['Deployment or pilot', 'A paid model tier, a production database host, a cloud host with a domain and managed TLS, and a pilot with one office.'],
    ['Final documentation', 'The complete technical report, a user guide and a reflection.'],
], [26, 74], small=True)

h1('Appendix E. Diagrams')
table(['No.', 'Diagram', 'No.', 'Diagram'], [
    ['1', 'Architecture', '7', 'State of a payment check'],
    ['2', 'Entity relationship (44 entities)', '8', 'State of a conversation'],
    ['3', 'Supervisor routing and tool selection', '9', 'State of a reservation'],
    ['4', 'Sequence of one message', '10', 'Deployment'],
    ['5', 'Sequence of a booking', '11', 'Access map'],
    ['6', 'State of a request', '12', 'Use cases (overview and seven groups)'],
], [7, 43, 7, 43], small=True)
img('er_overview.png', 17, 'Figure 3. The entity relationship diagram, overview. The full diagram is in the GitHub repository, in the folder design/diagrams.')
pb()
img('supervisor.png', 12.5, 'Figure 4. Supervisor routing and tool selection.')


# ================================================================ HTML
CSS = """
@page { size: A4; margin: 16mm 15mm 18mm 15mm; @bottom-center { content: counter(page); font: 9pt Helvetica, Arial, sans-serif; color: #666; } }
@page :first { @bottom-center { content: ''; } }
* { box-sizing: border-box; }
body { font-family: Georgia, 'Times New Roman', serif; font-size: 10.5pt; line-height: 1.45; color: #1a1a1a; margin: 0; }
h1 { font-family: Helvetica, Arial, sans-serif; font-size: 16pt; margin: 20pt 0 6pt; color: #0F766E; border-bottom: 1.5px solid #0F766E; padding-bottom: 3pt; break-after: avoid; }
h2 { font-family: Helvetica, Arial, sans-serif; font-size: 12pt; margin: 12pt 0 4pt; color: #222; break-after: avoid; }
p { margin: 0 0 7pt; }
ul { margin: 0 0 7pt; padding-left: 16pt; } li { margin-bottom: 3pt; }
table { border-collapse: collapse; width: 100%; font-family: Helvetica, Arial, sans-serif; font-size: 9pt; margin: 4pt 0 9pt; }
table.small { font-size: 8.4pt; }
th { background: #0F766E; color: #fff; text-align: left; padding: 4pt 5pt; font-weight: 600; }
td { border-bottom: 1px solid #d8d8d8; padding: 4pt 5pt; vertical-align: top; }
tr { break-inside: avoid; }
tbody tr:nth-child(even) td { background: #f6f9f8; }
blockquote { margin: 6pt 0 9pt; padding: 6pt 12pt; border-left: 3px solid #A3E635; background: #f6f9f8; font-style: italic; }
figure { margin: 8pt 0 10pt; text-align: center; break-inside: avoid; }
figure img { max-width: 100%; }
figcaption { font-family: Helvetica, Arial, sans-serif; font-size: 8.5pt; color: #444; margin-top: 3pt; }
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8pt; margin: 8pt 0; }
.grid figure { margin: 0; } .grid img { border: 1px solid #ccc; }
.cover { height: 255mm; display: flex; flex-direction: column; justify-content: center; break-after: page; }
.cover .bar { width: 60pt; height: 6pt; background: #A3E635; margin-bottom: 18pt; }
.cover h1 { font-size: 32pt; border: 0; color: #0F766E; margin: 0 0 4pt; }
.cover .sub { font-family: Helvetica, Arial, sans-serif; font-size: 16pt; color: #333; margin-bottom: 26pt; }
.cover table { width: auto; font-size: 10.5pt; } .cover td { border: 0; padding: 3pt 14pt 3pt 0; background: none !important; }
.cover td.k { color: #666; width: 95pt; }
a { color: #0F766E; word-break: break-all; }
.pb { break-before: page; }
"""


def linkify(t):
    t = html.escape(t)
    return re.sub(r'(https?://[^\s<]+)', r'<a href="\1">\1</a>', t)


def render_html():
    o = ['<!doctype html><html lang="en"><head><meta charset="utf-8"><title>' + TITLE + ' - ' + SUB + '</title><style>' + CSS + '</style></head><body>']
    o.append('<div class="cover"><div class="bar"></div><h1>' + TITLE + '</h1><div class="sub">' + SUB + '</div><table>')
    o.append('<tr><td class="k">Course</td><td>' + html.escape(COURSE) + '</td></tr>')
    o.append('<tr><td class="k">Instructor</td><td>' + html.escape(INSTRUCTOR) + '</td></tr>')
    o.append('<tr><td class="k">Group</td><td>Group S</td></tr>')
    o.append('<tr><td class="k">Members</td><td>' + '<br>'.join(f'{n}, {i}' for n, i in MEMBERS) + '</td></tr>')
    o.append('<tr><td class="k">Date</td><td>' + DATE + '</td></tr>')
    for a, b in LINKS:
        o.append('<tr><td class="k">' + html.escape(a.split(' (')[0]) + '</td><td>' + linkify(b) + '</td></tr>')
    o.append('</table></div>')
    for b in B:
        k = b[0]
        if k == 'h1': o.append('<h1>' + html.escape(b[1]) + '</h1>')
        elif k == 'h2': o.append('<h2>' + html.escape(b[1]) + '</h2>')
        elif k == 'p': o.append('<p>' + html.escape(b[1]) + '</p>')
        elif k == 'quote': o.append('<blockquote>' + html.escape(b[1]) + '</blockquote>')
        elif k == 'ul': o.append('<ul>' + ''.join('<li>' + html.escape(x) + '</li>' for x in b[1]) + '</ul>')
        elif k == 'pb': o.append('<div class="pb"></div>')
        elif k == 'table':
            d = b[1]
            cg = ''.join(f'<col style="width:{w}%">' for w in d['w']) if d['w'] else ''
            o.append(f'<table class="{"small" if d["small"] else ""}"><colgroup>{cg}</colgroup><thead><tr>' + ''.join('<th>' + html.escape(h) + '</th>' for h in d['head']) + '</tr></thead><tbody>')
            for r in d['rows']:
                o.append('<tr>' + ''.join('<td>' + linkify(c) + '</td>' for c in r) + '</tr>')
            o.append('</tbody></table>')
        elif k == 'img':
            o.append(f'<figure><img src="file://{IMG}/{b[1]}" style="width:{b[2]}cm"><figcaption>{html.escape(b[3])}</figcaption></figure>')
        elif k == 'grid':
            o.append('<div class="grid">' + ''.join(f'<figure><img src="file://{IMG}/{f}"><figcaption>{html.escape(c)}</figcaption></figure>' for f, c in b[1]) + '</div>')
    o.append('</body></html>')
    return '\n'.join(o)


# ================================================================ DOCX
def render_docx(path):
    from docx import Document
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Pt, RGBColor

    TEAL = RGBColor(0x0F, 0x76, 0x6E)
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(2.0)
    sec.top_margin, sec.bottom_margin = Cm(2.0), Cm(2.0)
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(11)
    st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
    st.paragraph_format.space_after = Pt(6)
    for name, size in (('Heading 1', 17), ('Heading 2', 13)):
        s = doc.styles[name]
        s.font.name = 'Calibri'
        s.font.size = Pt(size)
        s.font.bold = True
        s.font.color.rgb = TEAL if name == 'Heading 1' else RGBColor(0x22, 0x22, 0x22)
        s.paragraph_format.space_before = Pt(14 if name == 'Heading 1' else 10)
        s.paragraph_format.space_after = Pt(5)
        s.paragraph_format.keep_with_next = True

    def hyperlink(par, url, text):
        part = par.part
        rid = part.relate_to(url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True)
        h = OxmlElement('w:hyperlink')
        h.set(qn('r:id'), rid)
        r = OxmlElement('w:r')
        rp = OxmlElement('w:rPr')
        c = OxmlElement('w:color'); c.set(qn('w:val'), '0F766E'); rp.append(c)
        u = OxmlElement('w:u'); u.set(qn('w:val'), 'single'); rp.append(u)
        r.append(rp)
        t = OxmlElement('w:t'); t.text = text; t.set(qn('xml:space'), 'preserve'); r.append(t)
        h.append(r)
        par._p.append(h)

    def add_text(par, text, size=None, bold=False):
        parts = re.split(r'(https?://\S+)', text)
        for x in parts:
            if not x:
                continue
            if x.startswith('http'):
                hyperlink(par, x, x)
            else:
                r = par.add_run(x)
                if size: r.font.size = Pt(size)
                r.bold = bold

    def shade(cell, hexcol):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = OxmlElement('w:shd')
        shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), hexcol)
        tcPr.append(shd)

    def set_widths(tbl, widths):
        total = 17.0
        tbl.autofit = False
        for row in tbl.rows:
            for i, c in enumerate(row.cells):
                c.width = Cm(total * widths[i] / 100)

    def footer_numbers():
        par = sec.footer.paragraphs[0]
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = par.add_run()
        for tag, txt in (('begin', None), (None, 'PAGE'), ('end', None)):
            if tag:
                f = OxmlElement('w:fldChar'); f.set(qn('w:fldCharType'), tag); r._r.append(f)
            else:
                it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = txt; r._r.append(it)
        r.font.size = Pt(9)

    # cover
    for _ in range(5):
        doc.add_paragraph()
    pr = doc.add_paragraph()
    r = pr.add_run(TITLE); r.font.size = Pt(32); r.bold = True; r.font.color.rgb = TEAL
    pr = doc.add_paragraph()
    r = pr.add_run(SUB); r.font.size = Pt(16)
    doc.add_paragraph()
    rows = [('Course', COURSE), ('Instructor', INSTRUCTOR), ('Group', 'Group S'),
            ('Members', '\n'.join(f'{n}, {i}' for n, i in MEMBERS)), ('Date', DATE)]
    rows += [(a.split(' (')[0], b) for a, b in LINKS]
    t = doc.add_table(rows=0, cols=2)
    for k, v in rows:
        cells = t.add_row().cells
        cells[0].width, cells[1].width = Cm(3.2), Cm(13.8)
        pr = cells[0].paragraphs[0]; rr = pr.add_run(k); rr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
        add_text(cells[1].paragraphs[0], v)
    doc.add_page_break()
    footer_numbers()

    for b in B:
        k = b[0]
        if k == 'h1':
            doc.add_heading(b[1], level=1)
        elif k == 'h2':
            doc.add_heading(b[1], level=2)
        elif k == 'p':
            par = doc.add_paragraph(); add_text(par, b[1])
        elif k == 'quote':
            par = doc.add_paragraph(); par.paragraph_format.left_indent = Cm(0.8)
            rr = par.add_run(b[1]); rr.italic = True
        elif k == 'ul':
            for x in b[1]:
                par = doc.add_paragraph(style='List Bullet'); add_text(par, x)
        elif k == 'pb':
            doc.add_page_break()
        elif k == 'table':
            d = b[1]
            size = 9 if d['small'] else 10
            t = doc.add_table(rows=1, cols=len(d['head']))
            t.style = 'Table Grid'
            t.alignment = WD_TABLE_ALIGNMENT.CENTER
            for i, h in enumerate(d['head']):
                c = t.rows[0].cells[i]
                shade(c, '0F766E')
                c.paragraphs[0].text = ''
                rr = c.paragraphs[0].add_run(h); rr.bold = True; rr.font.size = Pt(size); rr.font.color.rgb = RGBColor(255, 255, 255)
            for ri, r_ in enumerate(d['rows']):
                cells = t.add_row().cells
                for i, v in enumerate(r_):
                    add_text(cells[i].paragraphs[0], v, size=size)
                    cells[i].paragraphs[0].paragraph_format.space_after = Pt(2)
                    if ri % 2 == 1: shade(cells[i], 'F2F7F6')
            if d['w']: set_widths(t, d['w'])
            # repeat header row
            trPr = t.rows[0]._tr.get_or_add_trPr(); th = OxmlElement('w:tblHeader'); th.set(qn('w:val'), 'true'); trPr.append(th)
            doc.add_paragraph().paragraph_format.space_after = Pt(2)
        elif k == 'img':
            par = doc.add_paragraph(); par.alignment = WD_ALIGN_PARAGRAPH.CENTER
            par.add_run().add_picture(os.path.join(IMG, b[1]), width=Cm(min(b[2], 16.5)))
            cp = doc.add_paragraph(); cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
            rr = cp.add_run(b[3]); rr.font.size = Pt(9); rr.italic = True
        elif k == 'grid':
            items = b[1]
            t = doc.add_table(rows=0, cols=2)
            for i in range(0, len(items), 2):
                cells = t.add_row().cells
                for j in range(2):
                    if i + j < len(items):
                        f, cap = items[i + j]
                        par = cells[j].paragraphs[0]; par.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        par.add_run().add_picture(os.path.join(IMG, f), width=Cm(8.1))
                        cp = cells[j].add_paragraph(); cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        rr = cp.add_run(cap); rr.font.size = Pt(8.5); rr.italic = True
            doc.add_paragraph()
    doc.core_properties.title = TITLE + ' - ' + SUB
    doc.core_properties.author = 'Group S'
    doc.save(path)


if __name__ == '__main__':
    base = 'Smart University Website - Presentation Report'
    open(os.path.join(OUT, 'report.html'), 'w').write(render_html())
    chrome = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    subprocess.run([chrome, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                    f'--print-to-pdf={os.path.join(OUT, base + ".pdf")}', 'file://' + os.path.join(OUT, 'report.html')],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    render_docx(os.path.join(OUT, base + '.docx'))
    print('built', OUT)
