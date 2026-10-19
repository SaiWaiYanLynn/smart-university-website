"""Journey slides built from prototype frames. Every text below matches the text in the frame it shows."""
from kit import journey_slide, two_frames


def j1a(d, over='Walkthrough', piece=None):
    return journey_slide(d, 'J1: a policy answer, with the rule behind it', over, 'j1_3.png',
        [('Knowledge agent', 'Searches the Student Handbook 2026 and finds section 7.3.'),
         ('The answer', 'Three documents. It offers to start with the official transcript.'),
         ('The citation', 'Handbook 2026, section 7.3, shown under the answer.')],
        quote_text='What documents do I need from the university for my student visa renewal?', who='The student asks', caption='Frame J1.3: answer with citation', piece=piece,
        notes='Click the answer. Say: the Knowledge agent retrieved a passage, wrote the answer from it, and attached the citation. None of the 17 universities shows the rule behind an answer.')


def j1b(d, over='Walkthrough', piece=None):
    return journey_slide(d, 'J1: the student opens the source', over, 'j1_4.png',
        [('The source panel', 'It shows the real paragraph: section 7.3, page 42.'),
         ('The sentence', 'The sentence that answers the question is highlighted.'),
         ('Why it matters', 'The student can check the rule. Nobody has to trust the model.')],
        caption='Frame J1.4: source expanded', piece=piece,
        notes='Optional, skip if time is short. Click View source. The panel shows the passage the answer came from. This is requirement FR-04: every answer carries the document and the section.')


def j2(d, over='Walkthrough', piece=None):
    return two_frames(d, 'J2: no rule found, so refuse and hand over', over, 'j2_2.png', 'Frame J2.2: the assistant refuses to guess', 'sc2.png', 'Frame SC2: staff take over, the assistant is paused',
        'No passage found: the assistant says so, offers a person, and stays silent while staff reply. The staff member sees the whole chat.',
        notes='Click Yes, pass it on. The conversation goes to Student Services at 14:22. In the staff console the assistant is paused and the staff member sees the whole conversation, so the student does not explain it twice. This is our third problem.')


def j3(d, over='Walkthrough', piece=None):
    return journey_slide(d, 'J3: own record yes, someone else\'s no', over, 'j3_4.png',
        [('Records agent', 'It reads the signed-in student\'s record only.'),
         ('The token', 'The student ID comes from the token, never from the message text.'),
         ('The audit log', 'The refused attempt is recorded.')],
        quote_text='What about student 67999999, how much do they owe?', who='The student asks', caption='Frame J3.4: access refused', piece=piece,
        notes='Say it out loud: the student identifier comes from the signed-in session token, never from the message text. This is the slide where we say that.')


def j4a(d, over='Walkthrough', piece=None):
    return journey_slide(d, 'J4: booking a study room, step one', over, 'j4_3.png',
        [('Booking agent', 'Reads the free rooms for Thursday afternoon. Read only.'),
         ('No slot held', 'Nothing is held until the student picks one.'),
         ('Three rooms', 'Library Room B2, Library Room B4 and Learning Commons C1.')],
        quote_text='I need a study room for my group on Thursday afternoon', who='The student asks', caption='Frame J4.3: rooms offered', piece=piece,
        notes='The agent asked how many people, then read the free slots. It holds nothing yet.')


def j4b(d, over='Walkthrough', piece=None):
    return two_frames(d, 'J4: a yes before anything is written', over, 'j4_4.png', 'Frame J4.4: confirm the booking', 'j4_5.png', 'Frame J4.5: booked',
        'Nothing is written without a yes. The booking runs in one transaction, leaves an audit record and sends a reminder to the linked LINE account.',
        notes='Before it writes anything, the agent always asks for confirmation. After the yes the reservation is written in one transaction with an audit record.')


def j5a(d, over='Walkthrough', piece=None):
    return journey_slide(d, 'J5: a transcript request, step one', over, 'j5_3.png',
        [('Request agent', 'Applies the rules: 100 THB for each copy.'),
         ('Confirm first', 'Nothing is submitted until the student confirms.'),
         ('The fee', '200 THB for two copies, payable on collection.')],
        quote_text='I need an official transcript for a job application', who='The student asks (frame J5.1)', caption='Frame J5.3: confirm the request', piece=piece,
        notes='The agent asked for two details: how many copies and collect or post. Then it shows the summary and waits for the confirmation. Be ready for one question: Student Handbook section 7.3 says 150 THB and Tuition and Fees 2026 says 100 THB. This is the deliberate conflict that the administrator sees in frame A3.1. The prototype uses 100 THB per copy.')


def j5b(d, over='Walkthrough', piece=None):
    return two_frames(d, 'J5: four states, and a message at each change', over, 'j5_4.png', 'Frame J5.4: submitted, with the timeline', 'j5_5.png', 'Frame J5.5: ready for collection',
        'The student gets a message on the same channel when the state changes. Only 3 of 17 universities show any status. None of the 12 Thai ones do.',
        notes='The reference is REQ-2026-0481. The state machine has four states: Submitted, Under review, Ready, Collected. A staff member moves it forward and the student is messaged where the request began.')


def j8(d, over='Walkthrough', piece=None):
    return journey_slide(d, 'J8: a payment slip, and a person decides', over, 'j8_2.png',
        [('A fixed reader', 'It checks amount, name, date and a duplicate reference. The model never sees the image.'),
         ('A payment check', 'The Request agent creates it in the state waiting.'),
         ('A person decides', 'Staff confirm in the Payments tab. Only then does the balance change.')],
        quote_text='I paid my tuition. Here is the slip.', who='The student sends a photo', caption='Frame J8.2: slip received', piece=piece,
        notes='The assistant never decides on money. It passes the slip to a person, and the balance changes only after a staff member confirms it.')


def j10(d, over='Walkthrough', piece=None):
    return journey_slide(d, 'J10: the assistant remembers across days', over, 'j10_4.png',
        [('Memory by student ID', 'It finds the saved topic under student ID 67111411, not under the LINE account.'),
         ('The rule again', 'It reads Handbook section 5.4 again for the deadline.'),
         ('The account', 'Deadline of 30 October not passed. No hold. It offers to start the withdrawal.')],
        quote_text='Can I do that one from yesterday?', who='Tuesday 20 October, 08:50', caption='Frame J10.4: the assistant remembers', piece=piece,
        notes='Optional, skip if time is short. On Monday the student asked about withdrawing from ICT440 and said she needed to think. On Tuesday the message has no topic. The assistant finds it in memory by student ID. Memory belongs to the student, not to the channel.')


def j11(d, over='Walkthrough', piece=None):
    return journey_slide(d, 'J11: one message, three tasks', over, 'j11_2.png',
        [('Supervisor', 'Splits the message into three tasks: credits, the rule and a booking.'),
         ('Records and Knowledge', 'Credits: 66 of 132. The rule: Handbook section 6.2.'),
         ('Booking', 'Finds two free slots with the advisor, Dr. Kanda.')],
        quote_text='I want to plan my graduation. How many credits do I still need, and can I see Dr. Kanda about it?', who='The student asks', caption='Frame J11.2: answers from three agents', piece=piece,
        notes='Optional, skip if time is short. One message, three agents. The Agent Trace panel on the right names every agent and tool behind the answer.')


def chan(d, over='Walkthrough', piece=None):
    return two_frames(d, 'The same assistant on LINE and Telegram', over, 'j13_1.png', 'Frame J13.1: the menu on LINE', 'j14_1.png', 'Frame J14.1: the commands on Telegram',
        'The same records answer on every channel. A button tap or a command is read like any other message. The student never has to open the website.',
        notes='Both channels run through Chatwoot. On LINE the University sets a rich menu once. On Telegram a command is a shortcut. The supervisor reads both like any other message, and the Records agent only reads.')


def j20(d, over='Walkthrough', piece=None):
    return two_frames(d, 'J20: a rule, a deadline and a request', over, 'j20_1.png', 'Frame J20.1: a rule with a date', 'j20_4.png', 'Frame J20.4: the outcome',
        'A tool counts the working days. Staff decide. The assistant carries the message to the channel that started the request.',
        notes='Handbook section 8.2, a medical certificate within three working days, so the last day is Thursday 22 October. A tool counts the days, not the model. The photo goes to private storage. The Registrar approves and the assistant sends the date.')


def staff_assist(d, over='Walkthrough', piece=None):
    return journey_slide(d, 'A staff member asks the assistant to approve', over, 'r8_2.png',
        [('Supervisor and Request agent', 'They read the request and its checks. All 3 checks passed.'),
         ('A yes first', 'The approval waits for the staff member to answer.'),
         ('Then', 'The state changes, the student is told on LINE and the audit log holds the staff member.')],
        quote_text='Approve REQ-2026-0489.', who='Siriporn K., Student Services', caption='Frame R8.2: an approval needs a yes', piece=piece,
        notes='Staff use the same assistant inside the staff console. The linked account sets the role, and the role sets the tools. The approval is the same request state machine that a button in the console uses.')


def staff_prep(d, over='Walkthrough', piece=None):
    return two_frames(d, 'The assistant prepares, a person decides', over, 'r5_1.png', 'Frame R5.1: a queue sorted by the assistant', 'r3_1.png', 'Frame R3.1: a handoff with a summary and a draft',
        'The queue comes with a reason for every item. A handoff comes with a summary and a draft reply. The staff member edits and decides.',
        notes='Optional, skip if time is short. The consoles stay simple because the student-side agents prepare the work. A person still decides every state, every slip and every takeover.')


def instr(d, over='Walkthrough', piece=None):
    return two_frames(d, 'The instructor: a plan to approve, an absence to check', over, 'r7_1.png', 'Frame R7.1: a study plan to approve', 'j24_2.png', 'Frame J24.2: the absence limit',
        'A tool counts the absences. The Handbook gives the limit. The instructor approves the plan and decides on the warning.',
        notes='Optional, skip if time is short. The instructor reads the attendance of the own course only. A tool counts the absences and the Handbook gives the limit in section 6.5. The instructor says yes before a warning is sent.')


def admin(d, over='Walkthrough', piece=None):
    return two_frames(d, 'The administrator: conflicts and blocked calls', over, 'a3_2.png', 'Frame A3.2: two passages side by side', 'a4_2.png', 'Frame A4.2: replay of a blocked call',
        'Documents that disagree and calls that were blocked are shown to the administrator, who decides. Nothing is settled in silence.',
        notes='Optional, skip if time is short. When two documents give different facts, the assistant keeps one as the source and tells the administrator. A blocked call can be replayed step by step: the supervisor, the agent, the checker that stopped it, and the audit write.')
