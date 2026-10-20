"""Content modules shared by the three decks. Every number here comes from a source named in the comment.

Type scale (px on a 1920 canvas, PPTX points are half): title 52, lead 34, body 30, table 26, caption 24, footer 20.
"""
import subprocess, os, re
from PIL import Image
import lib
from lib import C, wrap, text_w
import kit
from kit import hdr, box, arrow, chain, note_bar, big_number

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# ---- Survey table: docs/submitted/Project1_University_Website_Research_GroupS.pdf, section 4 ----
# y = present, p = partly present, n = not offered or no public evidence
SURVEY = [
    ('Chulalongkorn', 'TH', 'ynyynnn'), ('Thammasat', 'TH', 'ynyynnn'), ('Mahidol', 'TH', 'ynyynnn'),
    ('Kasetsart', 'TH', 'ynyynnn'), ('KMUTT', 'TH', 'ynnynnn'), ('KMITL', 'TH', 'ynyynnn'),
    ('Assumption', 'TH', 'ynnnnnn'), ('Bangkok University', 'TH', 'pnnynnn'), ('Srinakharinwirot', 'TH', 'nnnynnn'),
    ('KMUTNB', 'TH', 'nnyynpn'), ('STOU', 'TH', 'pnnynnn'), ('Buriram Rajabhat', 'TH', 'ynnynpn'),
    ('NUS', 'SG', 'yyyynpp'), ('Melbourne', 'AU', 'yyypnnn'), ('Toronto', 'CA', 'ypyynnn'),
    ('Manchester', 'UK', 'ynyynnn'), ('Arizona State', 'US', 'yyyynnn'),
]
STATED_TOTALS = [13, 3, 11, 15, 0, 0, 0]
TOTALS = [sum(1 for r in SURVEY if r[2][i] == 'y') for i in range(7)]
assert TOTALS == STATED_TOTALS, TOTALS
assert len(SURVEY) == 17 and sum(1 for r in SURVEY if r[1] == 'TH') == 12
CAP = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7']
CAP_LONG = [
    'Submit a request online through a real form',
    'See the state of the request afterwards',
    'Book a room online',
    'Reach an assistant or an official chat channel',
    'The assistant answers from the University\'s own rules and shows the rule',
    'The assistant completes a request or booking in the chat',
    'These services are reachable from one place',
]

ER_ENTITIES = re.findall(r'^  ([A-Z_]+) \{', open(os.path.join(ROOT, 'design', 'diagrams', '02_er.mmd')).read(), re.M)
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def git_facts():
    try:
        n = subprocess.run(['git', '-C', ROOT, 'rev-list', '--count', 'HEAD'], capture_output=True, text=True).stdout.strip()
        first = subprocess.run(['git', '-C', ROOT, 'log', '--reverse', '--format=%ad', '--date=short'], capture_output=True, text=True).stdout.split('\n')[0]
        y, m, d = first.split('-')
        return int(n), f'{int(d)} {MONTHS[int(m) - 1]} {y}'
    except Exception:
        return None, None


# ===================== opening =====================

def m_title(d, subtitle, frame='j1_3.png', notes=None):
    s = d.add(kind='dark', bg=C['charcoal'], footer=False, number=False,
              notes=notes or 'Introduce the project in one sentence: one assistant that answers from the University\'s own rules and finishes requests in the chat. The University is fictional.')
    s.rect(96, 150, 160, 14, fill=C['lime'])
    s.text(96, 200, 900, 'Smart University Website', size=100, weight=700, color=C['white'], lh=1.04)
    s.text(96, 470, 860, subtitle, size=42, color='#D4D4D8', lh=1.3)
    s.text(96, 790, 860, 'IT Project I  ·  Midterm presentation', size=32, weight=600, color=C['teal_200'])
    s.text(96, 840, 860, 'Group S  ·  Krirk University', size=30, color='#D4D4D8')
    s.text(96, 884, 860, 'Instructor: Dr. Aftab Alam Janisar', size=30, color='#D4D4D8')
    s.text(96, 962, 900, 'The University here is fictional: Thales University. All data is made up.', size=24, color='#A1A1AA', lh=1.3)
    s.image(frame, 1030, 230, 794, 496, fit='contain', r=16, border='#52525B', shadow=True)
    s.text(1030, 745, 794, 'The prototype: a policy answer with its source (frame J1.3)', size=24, color='#A1A1AA', align='c')
    return s


def m_team(d):
    s = d.add(notes='Four members, one course. The project is built so that any university can adopt it, so nothing depends on one campus.')
    y = hdr(s, 'Group S and the course', 'Who we are')
    people = [('Wai Yan Lynn', '67111411'), ('Pyae Sone', '67111336'), ('Nang Ying Noom Lao', '67111378'), ('Myat Hsu Hnin', '68111423')]
    cw = (1728 - 3 * 28) / 4
    for i, (n, sid) in enumerate(people):
        x = 96 + i * (cw + 28)
        s.rect(x, y, cw, 250, fill=C['bg'], stroke=C['border'], r=16)
        s.ellipse(x + 28, y + 28, 72, 72, fill=C['teal'])
        ini = ''.join(w[0] for w in n.split()[:2])
        s.text(x + 28, y + 46, 72, ini, size=30, weight=700, color=C['white'], align='c', lh=1.1)
        s.text(x + 28, y + 122, cw - 56, n, size=30, weight=700, color=C['ink'], lh=1.2)
        s.text(x + 28, y + 170, cw - 56, sid, size=28, color=C['muted'])
    yy = y + 290
    s.card(96, yy, 840, 330, 'The course', None, bullets=['IT Project I and II', 'BC362916 and BC362914', 'Krirk University', 'Instructor: Dr. Aftab Alam Janisar'], bsize=30, tsize=34)
    s.card(984, yy, 840, 330, 'The project', None, bullets=['A student services portal where a student acts by conversation', 'Built so that any university can adopt it', 'The University in the examples is fictional'], bsize=30, tsize=34)
    note_bar(s, yy + 360, 'The idea: one assistant that answers from the University\'s own rules and finishes requests in the chat.', size=30, h=100)
    return s


def m_agenda(d, rows, notes='', title='Today in 40 minutes'):
    s = d.add(notes=notes or 'Walk through the agenda in ten seconds. Keep the questions for the end.')
    y = hdr(s, title, 'Agenda')
    colw = [190, 1040, 498]
    data = [['Minutes', 'What we cover', 'Source']] + rows
    s.table(96, y, colw, data, size=30, hsize=24, minrow=92, pad=22)
    return s


# ===================== problem and evidence =====================

def m_problem(d):
    s = d.add(notes='Problem one and the status count come from the survey. Problems two and three come from how student services work, as written in the feasibility report. We did not survey students. Say clearly that universities are well equipped on the basics. The gap is elsewhere.')
    y = hdr(s, 'Problem statement: three problems students and staff meet', 'Proposal 3  ·  Problem statement')
    cards = [
        ('1', 'Services are split across separate systems',
         'A transcript, a study room and a library book mean three systems and three logins.', '13 of 17 universities take online requests, often in a different system from rooms and the library.'),
        ('2', 'Information is hard to find',
         'Rules sit inside PDF handbooks. At the sites we saw, search finds page titles, not the rule inside the file.', 'Students may rely on a senior. This comes from our user stories, not from a survey.'),
        ('3', 'Case records are hard to share',
         'Staff keep cases in personal inboxes. When one person is away, help stops.', 'Only 3 of 17 universities show the student the status. None of the 12 Thai universities do.'),
    ]
    cw = (1728 - 2 * 32) / 3
    ch = 600
    for i, (n, t, b1, b2) in enumerate(cards):
        x = 96 + i * (cw + 32)
        s.rect(x, y, cw, ch, fill=C['bg'], stroke=C['border'], r=18)
        s.ellipse(x + 32, y + 32, 72, 72, fill=C['teal'])
        s.text(x + 32, y + 48, 72, n, size=38, weight=700, color=C['white'], align='c', lh=1.1)
        yy = s.text(x + 32, y + 132, cw - 64, t, size=36, weight=700, color=C['ink'], lh=1.18) + 20
        yy = s.text(x + 32, yy, cw - 64, b1, size=28, color=C['text'], lh=1.32) + 18
        s.text(x + 32, yy, cw - 64, b2, size=28, weight=600, color=C['teal_dark'], lh=1.32, h=y + ch - 28 - yy)
    note_bar(s, y + ch + 24, 'Problem 1 and the status count come from our survey. Problems 2 and 3 come from how student services work. We do not claim that universities lack online services.', size=26, h=96)
    return s


def m_method(d):
    s = d.add(notes='We did not pick one university because the system is built to be adopted by any of them. So we measured 17 institutions with the same seven questions, using public pages only. Every row can be rechecked from the sources in the appendix.')
    y = hdr(s, 'How we measured it: 17 universities, 7 questions', 'The survey')
    s.card(96, y, 600, 650, 'The method', None, bullets=[
        '12 universities in Thailand and 5 abroad',
        'Checked on 5 and 6 October 2026',
        'Public pages only, no logins',
        'The same seven questions for each',
        'Plus published research on university chatbots'], bsize=30, tsize=34)
    colw = [100, 960]
    rows = [['', 'The seven questions']] + [[CAP[i], CAP_LONG[i]] for i in range(7)]
    s.table(744, y, colw, rows, size=26, hsize=24, minrow=70, pad=20)
    note_bar(s, y + 680, 'Limits: we did not log in to any portal and we did not survey students. A cross means no public evidence after a targeted search.', size=26, h=96, fill=C['amber_tint'], color=C['amber'], stroke=C['amber_200'], weight=500)
    return s


def m_heatmap(d):
    s = d.add(notes='Read the picture left to right. The first four columns are mostly green: services and chat channels exist. In the last three columns no university gets a full tick. Four cells are partial, in three universities: NUS, KMUTNB and Buriram Rajabhat. That is our gap: nothing joins the services and the chat channel.')
    tend = s.title('17 universities, 7 questions: no full tick in the last three', overline=None, size=44, y=36)
    x0, y0 = 96, max(116, int(tend) + 18)
    nw, cwid, rh = 392, 94, 41
    hh = 100
    s.rect(x0, y0, nw + 7 * cwid, hh, fill=C['charcoal'])
    s.text(x0 + 16, y0 + 36, nw - 20, 'University', size=24, weight=700, color=C['white'])
    hl = ['Request\nonline', 'See the\nstatus', 'Book a\nroom', 'Chat\nchannel', 'Cites its\nrules', 'Acts in\nthe chat', 'One\nplace']
    for i in range(7):
        cx = x0 + nw + i * cwid
        s.text(cx + 2, y0 + 6, cwid - 4, CAP[i], size=22, weight=700, color=C['teal_200'], align='c', lh=1.1, fit=False)
        s.text(cx + 2, y0 + 34, cwid - 4, hl[i], size=20, color=C['white'], align='c', lh=1.12, fit=False)
    gx = x0 + nw + 4 * cwid
    s.rect(gx, y0 + hh, 3 * cwid, 17 * rh + 54, fill=C['red_tint'])
    for r, (name, cc, marks) in enumerate(SURVEY):
        yy = y0 + hh + r * rh
        if r % 2 == 1:
            s.rect(x0, yy, nw + 4 * cwid, rh, fill=C['alt'])
        s.text(x0 + 16, yy + 5, nw - 20, f'{name} ({cc})', size=24, weight=500, color=C['ink'], lh=1.2, fit=False)
        for i, m in enumerate(marks):
            s.mark(m, x0 + nw + i * cwid + cwid / 2, yy + rh / 2, s=24)
    ty = y0 + hh + 17 * rh
    s.rect(x0, ty, nw + 7 * cwid, 54, fill=C['teal_tint'], stroke=C['teal_200'])
    s.text(x0 + 16, ty + 12, nw - 20, 'Full ticks out of 17', size=26, weight=700, color=C['teal_dark'], fit=False)
    for i in range(7):
        cx = x0 + nw + i * cwid
        s.text(cx, ty + 9, cwid, str(TOTALS[i]), size=32, weight=700, color=C['red'] if TOTALS[i] == 0 else C['teal_dark'], align='c', lh=1.1, fit=False)
    px = x0 + nw + 7 * cwid + 48
    pw = 1824 - px
    ly = y0
    for k, lab in (('y', 'Present'), ('p', 'Partly present'), ('n', 'Not offered, or no public evidence')):
        s.mark(k, px + 14, ly + 15, s=24)
        ly = s.text(px + 40, ly, pw - 40, lab, size=24, color=C['muted']) + 12
    ly += 18
    s.rect(px, ly, pw, 4, fill=C['border'])
    ly += 26
    ly = s.text(px, ly, pw, 'The basics exist', size=32, weight=700, color=C['ink']) + 10
    ly = s.text(px, ly, pw, '13 of 17 take an online request. 11 of 17 take room bookings online. 15 of 17 run a chat channel.', size=26, color=C['text'], lh=1.32) + 30
    ly = s.text(px, ly, pw, 'The gap is in the last three', size=32, weight=700, color=C['red']) + 10
    ly = s.text(px, ly, pw, 'No university gets a full tick. Four partial marks in three universities (NUS, KMUTNB, Buriram Rajabhat): fixed scripts, or an answer outside the chat.', size=26, color=C['text'], lh=1.32)
    return s


def m_bars(d):
    s = d.add(notes='Same data as a bar chart. Fifteen of seventeen already run a chat channel, so conversation is accepted. But the bars for citing rules, acting in the chat and one place are empty. Only 3 of 17 show a student the state of a request, and none of the 12 Thai ones do. The bars count full ticks only.')
    y = hdr(s, 'What the survey shows: chat exists, but it mostly only answers', 'The survey')
    order = [3, 0, 2, 1, 4, 5, 6]
    labels = {3: 'C4  Chat channel exists', 0: 'C1  Request online', 2: 'C3  Book a room online', 1: 'C2  See the status afterwards',
              4: 'C5  Answers from the University\'s rules', 5: 'C6  Fully finishes a request in the chat', 6: 'C7  Services in one place'}
    bx, bw, rowh = 800, 640, 74
    for r, i in enumerate(order):
        yy = y + r * rowh
        s.text(96, yy + 10, 680, labels[i], size=28, weight=600 if i >= 4 else 500, color=C['red'] if i >= 4 else C['ink'], lh=1.2, fit=False)
        s.rect(bx, yy + 8, bw, 46, fill=C['panel'], r=8)
        v = TOTALS[i]
        if v:
            s.rect(bx, yy + 8, bw * v / 17, 46, fill=C['teal'], r=8)
        s.text(bx + bw + 24, yy + 8, 240, f'{v} of 17', size=32, weight=700, color=C['red'] if v == 0 else C['teal_dark'], lh=1.2, fit=False)
    yy = y + 7 * rowh + 26
    cw = (1728 - 2 * 28) / 3
    for k, (t, b) in enumerate([
        ('Chat is accepted', 'In Thailand the channel is almost always LINE.'),
        ('Status is rare', 'Only 3 of 17 show it, and all three are outside Thailand.'),
        ('Nothing joins them', 'Services exist and chat exists, but not together.')]):
        s.card(96 + k * (cw + 28), yy, cw, 1000 - yy, t, b, tsize=30, bsize=26, fill=C['alt'], accent=C['teal'] if k < 2 else C['red'])
    return s


# ===================== comparison slides =====================

def m_cmp_table(d, notes=None):
    s = d.add(notes=notes or 'Be fair to the existing bots. They can run real actions. Their limit is coverage: everything was written in advance by a person. Our design retrieves from the University\'s own documents and picks tools by reading what each tool does. The right-hand column is our design, not a measured result yet.')
    y = hdr(s, 'A typical chat bot and our assistant', 'Comparison')
    colw = [290, 719, 719]
    rows = [
        ['', 'Typical intent-based bot', 'Our assistant (the design)'],
        ['How it decides', 'A developer writes intents and example phrases.', 'The supervisor reads the message and calls the right sub-agent.'],
        ['Coverage', 'Only what a person wrote in advance. Else a fallback reply.', 'Anything the documents cover. If not found, it refuses and offers a person.'],
        ['Source of answers', 'Written replies. 0 of 17 show the rule.', 'The University\'s own documents, with the section shown.'],
        ['Action in the chat', 'Fixed flows. 0 of 17 fully finish a request and report its state.', 'Books, submits and renews after a yes. Reports the state.'],
        ['Adding a service', 'A new intent and a new flow, built by hand.', 'A new tool with a plain description.'],
        ['Where services live', '0 of 17 reach them from one place.', 'One conversation on web, LINE and Telegram.'],
    ]
    fills = {}
    for r in range(1, 7):
        fills[(r, 1)] = C['red_tint']
        fills[(r, 2)] = C['teal_tint']
    s.table(96, y, colw, rows, size=26, hsize=26, minrow=92, zebra=False, cellfill=fills, pad=22)
    s.text(96, 1000 - 40, 1728, 'Published examples: NN Bot (KMUTNB) and the Buriram Rajabhat chatbot. The limit is coverage, not capability.', size=26, weight=600, color=C['ink'], lh=1.2)
    return s


def m_two_answers(d, notes=None):
    s = d.add(notes=notes or 'Same message, two answers. On the left is a made-up example of the fallback reply that intent-based bots give for a question nobody scripted. On the right is what our prototype does: the Knowledge agent finds Handbook section 8.2, a tool counts three working days in code, the Request agent opens a request with the photo attached, and staff decide. The left side is an illustration, not a quote from one university.')
    y = hdr(s, 'One message, two answers', 'Comparison')
    s.rect(96, y, 1728, 110, fill=C['teal'], r=18)
    s.text(136, y + 18, 1650, '"I was sick on Monday and missed the ICT411 midterm. What can I do?"', size=40, weight=600, color=C['white'], lh=1.2, anchor='m', h=74)
    yy = y + 138
    lw = 560
    ch = 640
    s.rect(96, yy, lw, ch, fill=C['red_tint'], stroke=C['red_200'], r=18)
    s.pill(128, yy + 28, 'A bot with fixed intents', fill=C['red'], color=C['white'], h=48, size=24)
    s.rect(128, yy + 108, lw - 64, 150, fill=C['white'], stroke=C['border'], r=14)
    s.text(152, yy + 126, lw - 112, '"Sorry, I did not understand. Please contact the Registrar office."', size=28, color=C['text'], lh=1.3)
    s.text(128, yy + 286, lw - 64, 'A made-up example of the fallback reply that intent-based bots give. It is not a quote from one university.', size=24, color=C['muted'], lh=1.3)
    s.text(128, yy + 440, lw - 64, 'The student still has to find the rule, work out the deadline and ask the right office.', size=28, weight=600, color=C['red'], lh=1.3)
    rx = 96 + lw + 32
    rw = 1824 - rx
    s.rect(rx, yy, rw, ch, fill=C['teal_tint'], stroke=C['teal_200'], r=18)
    s.pill(rx + 32, yy + 28, 'Our assistant (frames J20.1 to J20.4)', fill=C['teal'], color=C['white'], h=48, size=24)
    steps = [
        ('Finds the rule', 'Handbook 8.2: with a medical certificate, a student can sit a make-up exam.'),
        ('Counts in code', 'Exam on Monday 19 October. Three working days end on Thursday 22 October.'),
        ('Opens the request', 'The photo of the certificate goes to private storage. REQ-2026-0490 starts.'),
        ('Tells the student', 'The Registrar approves. Monday 26 October, 13:00, Room 5-102.'),
    ]
    sy = yy + 110
    for i, (t, b) in enumerate(steps, 1):
        sy = s.callout(rx + 32, sy, rw - 64, i, t, b, size=26) + 24
    return s


def m_roles_change(d, notes=None):
    s = d.add(notes=notes or 'This is what the assistant does for each person. The middle column is prepared by the assistant. The right column is always decided by a person. That rule is in code, not in the prompt.')
    y = hdr(s, 'What changes for each person', 'Comparison')
    colw = [250, 850, 628]
    rows = [
        ['', 'The assistant prepares', 'A person decides'],
        ['Student', 'A cited answer. Booking options. A request with its checks. A message when the state changes.', 'Says yes before anything is written.'],
        ['Staff', 'A sorted queue with reasons. A handoff with a summary and a draft reply. Checks on every request.', 'Every request state, every payment slip, every takeover.'],
        ['Instructor', 'An advising brief. Advisee signals. A study plan. Attendance counts.', 'Approves plans. Sends a warning after a yes.'],
        ['Administrator', 'Unanswered questions. Documents that disagree. A replay of blocked calls.', 'Creates accounts, adds documents, settles conflicts.'],
    ]
    s.table(96, y, colw, rows, size=28, hsize=26, minrow=130, pad=24)
    return s


def m_steps(d, notes=None):
    s = d.add(notes=notes or 'This is objective six: show that the system makes the task easier. Today a typical Thai transcript request, a composite of what the survey found, means finding the form, paying, waiting and visiting a counter, with no status in between. In the prototype the student takes three actions, and the system messages back. We will measure steps and time in Project I testing. These are not measured numbers yet.')
    y = hdr(s, 'A transcript request, step by step', 'Comparison')
    w = 840
    ch = 690
    s.rect(96, y, w, ch, fill=C['red_tint'], stroke=C['red_200'], r=18)
    s.pill(128, y + 28, 'A typical Thai request today (a composite)', fill=C['red'], color=C['white'], h=48, size=24)
    steps = ['Find the registrar site and the form', 'Fill it in with student number and ID', 'Pay by QR code or bank slip', 'Wait the stated working days', 'Go to the counter to collect', 'No status in between (only 3 of 17 show one)']
    yy = y + 112
    for i, t in enumerate(steps, 1):
        s.ellipse(128, yy, 44, 44, fill=C['red'])
        s.text(128, yy + 7, 44, str(i), size=24, weight=700, color=C['white'], align='c', lh=1.1)
        yy = s.text(196, yy + 4, w - 130, t, size=28, color=C['text'], lh=1.25) + 26
    x2 = 96 + w + 48
    s.rect(x2, y, w, ch, fill=C['teal_tint'], stroke=C['teal_200'], r=18)
    s.pill(x2 + 32, y + 28, 'In the prototype (frames J5.1 to J5.5)', fill=C['teal'], color=C['white'], h=48, size=24)
    steps2 = [('Student', 'writes: "I need an official transcript"'), ('Student', 'answers two questions: copies, collect or post'), ('Student', 'confirms. The reference REQ-2026-0481 appears'),
              ('System', 'messages the student when the state changes'), ('System', 'says it is ready, at which counter and until when. The fee is paid on collection')]
    yy = y + 112
    for i, (who, t) in enumerate(steps2, 1):
        s.ellipse(x2 + 32, yy, 44, 44, fill=C['teal'] if who == 'Student' else C['charcoal'])
        s.text(x2 + 32, yy + 7, 44, str(i), size=24, weight=700, color=C['white'], align='c', lh=1.1)
        yy = s.rich(x2 + 100, yy + 4, w - 134, [(who + ' ', 700, C['teal_dark'] if who == 'Student' else C['charcoal']), (t, 400)], size=28, lh=1.25) + 26
    note_bar(s, y + ch + 24, 'In the prototype the student takes three actions in the chat, then collects at the counter. We measure steps and time in Project I testing.', size=26, h=96)
    return s


# ===================== objectives, requirements, scope =====================

def m_objectives(d):
    s = d.add(notes='Seven objectives, all from feasibility report v3. Objective five covers staff, instructors and administrators, and was added on 15 October.')
    y = hdr(s, 'Objectives: one general, seven specific', 'Proposal 4  ·  Objectives')
    y = note_bar(s, y, 'General objective: a student does University services by conversation. The assistant answers from the University\'s own rules, acts after a yes and hands hard cases to people.', size=28) + 28
    items = [
        ('Answer from the rules.', 'Answer at least 80 percent of a 50-question test set correctly, with a citation each time.'),
        ('One conversation.', 'Policy questions, own record, bookings and requests in one place.'),
        ('Durable state.', 'Every booking and request has a state and a history. The student is told when it changes.'),
        ('Keep the context.', 'Across staff changes, channels and days. Nobody explains a case twice.'),
        ('Serve the University side.', 'Staff, instructors and administrators use the assistant, limited by role.'),
        ('Near-zero cost.', 'Open-source tools and the free tier of the model provider. A paid tier is an option.'),
        ('Show it is easier.', 'Compare steps and time for one request, before and after.'),
    ]
    yy = y + 4
    for i, (a, b) in enumerate(items, 1):
        s.ellipse(96, yy + 2, 52, 52, fill=C['teal'])
        s.text(96, yy + 11, 52, str(i), size=28, weight=700, color=C['white'], align='c', lh=1.1)
        yy = s.rich(176, yy + 2, 1648, [(a + ' ', 700, C['ink']), (b, 400)], size=30, lh=1.26) + 28
    return s


def m_requirements(d):
    s = d.add(notes='Thirty three functional and five non functional requirements, each with a test method written next to it. Nineteen are the core and fourteen are extended features that we build after the core. Say three of them out loud: the 200 request concurrency test with exactly one success, zero successful cross account attempts, and 80 and 90 percent accuracy scored by two raters. The performance targets are proposals for the hosted model until the week two test.')
    y = hdr(s, '33 functional and 5 non-functional requirements, each with a test', 'Proposal 7  ·  Requirements', size=48)
    colw = [270, 800, 658]
    rows = [
        ['Group', 'The system shall', 'How we test it'],
        ['Identity and roles', 'Sign in with Keycloak. Four roles. Reject a missing token.', 'Absent, expired and valid token. Every endpoint once per role.'],
        ['Knowledge', 'Answer only from retrieved passages, with the source. Refuse if nothing fits.', '50 questions with citations. 10 with no coverage must refuse.'],
        ['Records', 'Return only the signed-in student\'s own data.', '30 other-student attempts. 30 refusals.'],
        ['Booking', 'Reserve in one transaction. Cancel or move only your own booking.', '200 concurrent requests on one slot. Exactly one succeeds.'],
        ['Requests and library', 'Four states with a history. Notify within 60 seconds. Renew a loan by the rules.', 'One request of each type through all four states.'],
        ['Handoff', 'Hand over on request or low confidence, with a summary and draft. Then stay silent.', 'Silence for 10 more messages.'],
        ['Channels', 'One chat history across web, LINE and Telegram. Plain text only.', 'Start on web, continue on LINE, read it back.'],
        ['Safety', 'Ask before every write. Audit every write, personal read and blocked call.', 'One booking, one request, one blocked call, then the rows.'],
        ['Payment slip', 'Never read the slip. Record the payment only after staff say yes.', 'Slip sent, staff reply, record written, balance read back.'],
        ['Memory and reminders', 'Remember facts by account. Remind 24 hours before. Retry a failed question.', 'Next-day recall. Reminder in time. Tool restored, answer sent.'],
        ['Role tools', 'Attendance, advising brief, bulk reminder, account jobs, document upload.', 'Each tool on seeded data, and refused for the wrong role.'],
        ['Quality', 'Routing 90 percent or higher. 80 percent of answers correct with a citation.', '100 labelled messages. 50 questions, two raters.'],
    ]
    s.table(96, y, colw, rows, size=22, hsize=22, minrow=52, pad=10)
    return s


def m_scope(d):
    s = d.add(notes='Scope is frozen. The guest never uses the assistant. Staff, instructors and administrators do, with role limits. Payment processing and a real student information system stay out. The payment slip is in, because a person checks it and the assistant only records the update after a yes.')
    y = hdr(s, 'Scope: what is in Project I and what waits', 'Proposal 8  ·  Scope')
    w = 840
    ch = 690
    s.rect(96, y, w, ch, fill=C['teal_tint'], stroke=C['teal_200'], r=18)
    s.pill(128, y + 28, 'In Project I', fill=C['teal'], color=C['white'], h=48, size=26)
    s.bullets(128, y + 110, w - 64, [
        'Public site, portal, consoles, four roles in one app',
        'One supervisor and four sub-agents',
        'Chat for all four roles, limited by role',
        'Human handoff with a summary and a draft',
        'Library search and loan renewal',
        'Payment slip: staff check it, then record it by chat',
        'Memory, reminders, watches and retries',
        'Role tools: attendance, advising, bulk reminders, accounts',
        'Evaluation sets and one-command start'], size=28, gap=16)
    x2 = 96 + w + 48
    s.rect(x2, y, w, ch, fill=C['panel'], stroke=C['border'], r=18)
    s.pill(x2 + 32, y + 28, 'Project II or later', fill=C['charcoal'], color=C['white'], h=48, size=26)
    s.bullets(x2 + 32, y + 110, w - 64, [
        'Borrowing, holds, events, maintenance',
        'Resources beyond advisors and study rooms',
        'Payments and a real student system',
        'Course add and drop with checks',
        'Buttons and rich cards on LINE and Telegram',
        'Mobile apps, voice, more languages',
        'Model training'], size=28, gap=16, dot=C['subtle'])
    s.text(96, y + ch + 24, 1728, 'A guest (no account) reads the public site and applies. A guest never uses the assistant.', size=28, weight=600, color=C['teal_dark'])
    return s


# ===================== architecture =====================

def m_arch(d, notes=None):
    s = d.add(notes=notes or 'One picture. People at the top, two entry points, one FastAPI application with one supervisor, and the data and services at the bottom. Chatwoot owns the three channels and the human handoff. Its admin screen is for the IT team only. Everyone signs in through Keycloak, and the REST layer checks the token and reads the role.')
    y = hdr(s, 'The system in one picture', 'Proposal 10  ·  Architecture')
    labels = [('Guest', 'no login'), ('Student', 'portal, chat'), ('Instructor', 'console, chat'), ('Staff', 'console, chat'), ('Administrator', 'console, chat'), ('IT team', 'Chatwoot admin')]
    bw = (1728 - 5 * 20) / 6
    for i, (t, sub) in enumerate(labels):
        box(s, 96 + i * (bw + 20), y, bw, 92, t, sub, fill=C['panel'], tsize=26, ssize=22, pad=6)
    y2 = y + 92 + 28
    box(s, 96, y2, 840, 116, 'React application', 'Public site · Student portal · Role consoles', fill=C['bg'], stroke=C['teal'], tsize=30, ssize=24, sw=3)
    box(s, 984, y2, 840, 116, 'Chatwoot (self-hosted)', 'Web widget · LINE · Telegram · handoff', fill=C['bg'], stroke=C['teal'], tsize=30, ssize=24, sw=3)
    y3 = y2 + 116 + 34
    arrow(s, 516, y2 + 116, 516, y3 - 6)
    arrow(s, 1404, y2 + 116, 1404, y3 - 6)
    s.text(532, y2 + 128, 300, 'REST', size=22, weight=600, color=C['subtle'], fit=False)
    s.text(1420, y2 + 128, 300, 'webhook', size=22, weight=600, color=C['subtle'], fit=False)
    ch = 318
    s.rect(96, y3, 1728, ch, fill=C['alt'], stroke=C['teal'], sw=3, r=20)
    s.text(124, y3 + 12, 700, 'FastAPI application', size=24, weight=700, color=C['teal'], upper=True, tracking=1.5)
    iy = y3 + 54
    box(s, 124, iy, 360, 118, 'REST API layer', 'checks the token, reads the role', fill=C['bg'], tsize=26, ssize=22, pad=10)
    box(s, 520, iy, 520, 118, 'Supervisor agent', 'LangChain, calls sub-agents as tools', fill=C['teal'], stroke=C['teal'], tcolor=C['white'], scolor=C['teal_100'], tsize=28, ssize=22, pad=12)
    box(s, 1076, iy, 330, 118, 'Memory', 'by account', fill=C['bg'], tsize=26, ssize=22, pad=10)
    box(s, 1442, iy, 354, 118, 'Model adapter', 'one place for the model', fill=C['bg'], tsize=26, ssize=22, pad=10)
    arrow(s, 484, iy + 59, 514, iy + 59)
    sy = iy + 118 + 20
    names = [('Knowledge', 'retrieval'), ('Records', 'read only'), ('Booking', 'advisors, rooms'), ('Request', 'requests, renewals')]
    sw_ = (1728 - 56 - 3 * 14) / 4
    for i, (t, sub) in enumerate(names):
        box(s, 124 + i * (sw_ + 14), sy, sw_, 74, t, sub, fill=C['teal_tint'], stroke=C['teal_200'], tsize=26, ssize=22, pad=8)
    s.text(124, sy + 82, 1600, 'Role middleware → validator → tool layer (writes in one transaction) → audit. A worker sends reminders and retries and indexes documents.', size=22, color=C['muted'], lh=1.2, fit=False)
    y4 = y3 + ch + 28
    arrow(s, 516, y3 + ch, 516, y4 - 6)
    dw = (1728 - 3 * 20) / 4
    ds = [('PostgreSQL + pgvector', 'records, vector search'), ('File storage', 'request files'), ('Keycloak', 'sign-in, OIDC'), ('OpenRouter', 'hosted model')]
    for i, (t, sub) in enumerate(ds):
        box(s, 96 + i * (dw + 20), y4, dw, 94, t, sub, fill=C['charcoal'], stroke=C['charcoal'], tcolor=C['white'], scolor='#D4D4D8', tsize=26, ssize=22, pad=6)
    return s


def m_flow(d, notes=None):
    s = d.add(notes=notes or 'This is the route of one message. First the system resolves who is writing and in which role. If a staff member handles the chat, the assistant stays silent. Otherwise the supervisor splits the message and a sub-agent chooses a tool. Before any tool runs, three checks happen. A write needs a yes and runs in one transaction with an audit record. The reply goes back on the same channel.')
    y = hdr(s, 'What happens to one message', 'Architecture')
    top = [('Message arrives', 'web, LINE or Telegram'), ('Who is writing?', 'the token or the linked channel gives account and role'), ('Does a person handle this chat?', 'if yes, the assistant stays silent'), ('Supervisor splits it', 'one message can hold several tasks')]
    bot = [('Sub-agent picks a tool', 'Knowledge, Records, Booking or Request'), ('Three checks', 'role allows the tool, rows in scope, arguments valid'), ('Read, or write after a yes', 'one transaction and an audit record'), ('One reply', 'saved to memory, sent on the same channel')]
    bh = 270
    chain(s, 96, y + 36, 1728, top, gap=56, h=bh, size=26, tsize=30)
    ly = y + 36 + bh
    s.line(1824 - 160, ly, 1824 - 160, ly + 36, color=C['border_strong'], w=3)
    s.line(1824 - 160, ly + 36, 96 + 160, ly + 36, color=C['border_strong'], w=3)
    arrow(s, 96 + 160, ly + 36, 96 + 160, ly + 78)
    chain(s, 96, ly + 96, 1728, bot, gap=56, h=bh, size=26, tsize=30, fills=[C['bg'], C['teal_tint'], C['bg'], C['bg']])
    s.text(96, ly + 96 + bh + 28, 1728, 'Fail safe: if no passage is found, or the arguments fail twice, a person gets the chat with a summary and a draft reply.', size=28, weight=600, color=C['teal_dark'], lh=1.3)
    return s


def m_agents(d, notes=None):
    s = d.add(notes=notes or 'The supervisor is one LangChain agent. The four sub-agents are wrapped as tools that it calls. A role middleware filters which tools are visible on each model call, so by design a student session cannot even see a staff tool. Records only reads. Booking and Request write, and only after a yes.')
    y = hdr(s, 'One supervisor, four sub-agents', 'Architecture')
    cw = (1728 - 3 * 24) / 4
    data = [
        ('Knowledge', 'Reads', 'Finds passages in the University\'s documents. Shows the document and section. Refuses if none fits.', C['teal']),
        ('Records', 'Reads only', 'Own record, timetable, loans, catalogue, attendance of own course, the staff queue.', C['teal']),
        ('Booking', 'Writes after a yes', 'Advisor appointments and study rooms. One reservation engine for anything bookable.', C['charcoal']),
        ('Request', 'Writes after a yes', 'Requests, renewals, payment records, approvals. One state machine, four states.', C['charcoal']),
    ]
    ch = 430
    for i, (t, tag, b, col) in enumerate(data):
        x = 96 + i * (cw + 24)
        s.rect(x, y, cw, ch, fill=C['bg'], stroke=C['border'], r=18)
        s.rect(x, y, cw, 12, fill=col, r=6)
        s.text(x + 28, y + 36, cw - 56, t, size=38, weight=700, color=C['ink'])
        s.pill(x + 28, y + 98, tag, fill=C['teal_tint'] if col == C['teal'] else C['panel'], color=C['teal_dark'] if col == C['teal'] else C['charcoal'], size=22, h=42)
        s.text(x + 28, y + 168, cw - 56, b, size=27, color=C['text'], lh=1.32, h=ch - 190)
    yy = y + ch + 28
    items = [('Role middleware.', 'Filters the tool list by role on every model call.'), ('Argument validator.', 'Rejects bad arguments and asks once more.'), ('Tool layer.', 'Takes the subject from the token, never from the text.'), ('Audit writer.', 'Records every write and every blocked call.')]
    cw2 = (1728 - 24) / 2
    for i, (a, b) in enumerate(items):
        x = 96 + (i % 2) * (cw2 + 24)
        yb = yy + (i // 2) * 120
        s.rect(x, yb, cw2, 100, fill=C['teal_tint'], stroke=C['teal_200'], r=14)
        s.rich(x + 28, yb + 18, cw2 - 56, [(a + ' ', 700, C['teal_dark']), (b, 400)], size=27, lh=1.3)
    return s


def m_roles(d, notes=None):
    s = d.add(notes=notes or 'One application, six kinds of person: four roles plus the guest and the IT team. The role comes from the Keycloak account. The tools and the rows follow the role. Staff see conversations that were passed to them, never private chats. Administrators cannot read private chats either. The IT team only has the Chatwoot admin screen, with its own login.')
    y = hdr(s, 'Who can do what', 'Architecture')
    colw = [250, 940, 538]
    rows = [
        ['Role', 'The assistant can', 'Never'],
        ['Guest', 'Nothing. A guest reads the public site, applies and checks the application status.', 'Use the assistant. Read a record.'],
        ['Student', 'Cite a rule. Show own record. Book. Request. Renew. Send a slip photo to staff, unread.', 'Read another student\'s data.'],
        ['Instructor', 'Own schedule and advisees. Meeting brief. Attendance of own course. Warn after a yes.', 'Read students outside own advisees and courses.'],
        ['Staff', 'Show the queue. Take over a chat. Approve after a yes. Send a bulk reminder.', 'Read private chats. Decide a payment alone.'],
        ['Administrator', 'Accounts, documents, unanswered questions, source conflicts, system status, audit log.', 'Read private chats of students.'],
        ['IT team', 'Set up Chatwoot inboxes, channels and bots. Own login, outside Keycloak.', 'Act as a student, staff or instructor.'],
    ]
    s.table(96, y, colw, rows, size=26, hsize=24, minrow=100, pad=20)
    return s


def m_engines(d, notes=None):
    s = d.add(notes=notes or 'Two engines cover every feature. One reservation engine with slot locking handles anything bookable. One request state machine with four states handles anything trackable. Each will be written once. On the left, two students pick the same slot: the second lock waits, then sees the slot is closed and gets alternatives.')
    y = hdr(s, 'Two engines cover every feature', 'Architecture')
    w = 840
    ch = 720
    s.rect(96, y, w, ch, fill=C['bg'], stroke=C['border'], r=18)
    s.pill(128, y + 28, 'Reservation engine: no double booking', fill=C['teal'], color=C['white'], h=48, size=24)
    seq = [('Students A and B both pick Library Room B4, 14:00', None), ('A locks the slot row', 'A holds the lock'), ('B tries the same row', 'B waits'), ('A writes the reservation, closes the slot, writes the audit, commits', 'The lock is free'),
           ('B reads the slot again', 'It is closed. Roll back. Offer alternatives.')]
    yy = y + 112
    for i, (a, b) in enumerate(seq):
        s.ellipse(128, yy + 2, 40, 40, fill=C['teal'])
        s.text(128, yy + 8, 40, str(i + 1), size=22, weight=700, color=C['white'], align='c', lh=1.1)
        yy = s.text(190, yy, w - 120, a, size=26, weight=600, color=C['ink'], lh=1.25)
        if b:
            yy = s.text(190, yy + 2, w - 120, b, size=24, color=C['muted'], lh=1.25)
        yy += 22
    s.text(128, y + ch - 72, w - 64, 'Planned test: 200 concurrent requests, one slot, exactly one success.', size=24, weight=600, color=C['teal_dark'], lh=1.25)
    x2 = 96 + w + 48
    s.rect(x2, y, w, ch, fill=C['bg'], stroke=C['border'], r=18)
    s.pill(x2 + 32, y + 28, 'Request state machine: four states', fill=C['teal'], color=C['white'], h=48, size=24)
    states = ['Submitted', 'Under review', 'Ready', 'Collected']
    sw_ = 172
    gap = (w - 64 - 4 * sw_) / 3
    for i, st in enumerate(states):
        bx = x2 + 32 + i * (sw_ + gap)
        box(s, bx, y + 120, sw_, 100, st, fill=C['teal_tint'], stroke=C['teal'], tsize=24, pad=6)
        if i < 3:
            arrow(s, bx + sw_ + 6, y + 170, bx + sw_ + gap - 6, y + 170)
    s.bullets(x2 + 32, y + 262, w - 64, [
        'Every change writes a history entry and an audit record.',
        'The student gets a message on the same channel within 60 seconds.',
        'A person moves a request forward.',
        'One machine tracks a transcript, a withdrawal request, a make-up exam request and a renewal.'], size=27, gap=18)
    s.text(x2 + 32, y + ch - 72, w - 64, 'Planned test: one request of each type through all four states.', size=24, weight=600, color=C['teal_dark'], lh=1.25)
    return s


def m_safety(d, notes=None):
    s = d.add(notes=notes or 'Access control is the part that matters most, so we build as if the data were real. Every tool takes the subject from the verified token. The role decides which tools exist for the model. Nothing is written without a yes. Every write leaves an audit record. The assistant never decides on money. And we will attack our own system in a planned test suite: 30 cross account attempts and 10 attempts to reach a staff tool from a student session must all fail. The suite is not written yet.')
    y = hdr(s, 'Safety rules that live in code, not in the prompt', 'Architecture')
    cards = [
        ('The token decides who', 'Every tool takes the ID from the verified token. The message text cannot change it.'),
        ('The role decides what exists', 'A student session cannot even see a staff tool.'),
        ('A yes before a write', 'One transaction and an audit record of actor, action, target and time.'),
        ('Refuse before guessing', 'No passage found means a refusal and an offer of a person.'),
        ('Never decide on money', 'A person checks the slip and replies. The assistant records a payment only after a yes.'),
        ('We will attack ourselves', '40 attack attempts are planned in the test suite. None may succeed.'),
    ]
    cw = (1728 - 2 * 28) / 3
    ch = 340
    for i, (t, b) in enumerate(cards):
        x = 96 + (i % 3) * (cw + 28)
        yy = y + (i // 3) * (ch + 28)
        s.card(x, yy, cw, ch, t, b, tsize=34, bsize=30, fill=C['alt'], accent=C['teal'])
    return s


def m_channels_tests(d, notes=None):
    s = d.add(notes=notes or 'Chatwoot is self-hosted and owns the three channels and the human handoff. We tested it live with a LINE official account and a Telegram bot. Text, photos and tappable buttons work on both. Cards do not. So we decided on plain text on LINE and Telegram, with no buttons and no cards. The user types yes. The web chat is plain text too, so every channel behaves the same and there is less to break.')
    y = hdr(s, 'Chatwoot carries the chat, the handoff and one history', 'Architecture')
    w = 840
    ch = 700
    s.card(96, y, w, ch, 'What we tested live on 15 and 16 October', None, bullets=[
        'Text in and out: LINE and Telegram',
        'Photos in and out: both',
        'Tappable buttons: both',
        'A new chat stays pending with the bot',
        'A failing bot address opens the chat for a person',
        'Two channels merged into one contact'], bsize=32, tsize=36, fill=C['green_tint'], stroke=C['green_200'])
    s.card(96 + w + 48, y, w, ch, 'What we decided', None, bullets=[
        'Cards failed on both channels. Only the text arrived.',
        'LINE and Telegram carry plain text. No buttons, no cards. The user types yes.',
        'The web chat is plain text too, so every channel behaves the same.',
        'Each LINE message from Chatwoot is a push message. The free quota is not proven.',
        'Chatwoot Community Edition has no proven single sign-on. Staff use our console. Chatwoot is for the IT team.'], bsize=30, tsize=36, fill=C['amber_tint'], stroke=C['amber_200'])
    return s

def m_handoff(d, notes=None):
    s = d.add(notes=notes or 'With an agent bot, a new conversation is pending. A person takes over by setting it to open, and the assistant stays silent while it is open. The staff member can release the chat back to the assistant. We tested that a new chat stays pending and that a failing bot address opens the chat by itself. Staff takeover is design.')
    y = hdr(s, 'Who owns the chat: the assistant or a person', 'Architecture')
    st = [('Assistant handling', 'Chatwoot status: pending. The assistant answers.'), ('Waiting for staff', 'Status: open, no owner. A summary and a draft reply are ready.'), ('Staff handling', 'Status: open, with an owner. The assistant stays silent.')]
    sw_ = (1728 - 2 * 100) / 3
    bh = 300
    for i, (t, sub) in enumerate(st):
        bx = 96 + i * (sw_ + 100)
        box(s, bx, y + 40, sw_, bh, t, sub, fill=C['teal_tint'] if i < 2 else C['teal'], stroke=C['teal'], tcolor=C['ink'] if i < 2 else C['white'], scolor=C['muted'] if i < 2 else C['teal_100'], tsize=34, ssize=26)
        if i < 2:
            arrow(s, bx + sw_ + 10, y + 40 + bh / 2, bx + sw_ + 90, y + 40 + bh / 2)
    s.text(96, y + 40 + bh + 30, 1728, 'We tested that a new chat stays pending and that a failing bot address opens it. Staff takeover is design.', size=26, color=C['muted'])
    cy = y + 40 + bh + 100
    cw = (1728 - 28) / 2
    s.card(96, cy, cw, 1000 - cy - 6, 'When the assistant hands over', 'The student asks for a person, confidence is low, or no source is found.', tsize=30, bsize=26, fill=C['alt'], accent=C['teal'])
    s.card(96 + cw + 28, cy, cw, 1000 - cy - 6, 'What the staff member sees', 'The whole conversation, a summary, and a draft reply they edit before it is sent.', tsize=30, bsize=26, fill=C['alt'], accent=C['teal'])
    return s


DATA_GROUPS = [
    ('People and access', ['USER', 'STUDENT_RECORD', 'STAFF_PROFILE', 'ADVISOR_LINK', 'CHANNEL_LINK', 'FACULTY', 'PROGRAM'], 'USER, CHANNEL_LINK, ADVISOR_LINK'),
    ('Bookings', ['RESOURCE', 'SLOT', 'RESERVATION', 'ADVISOR_BRIEF', 'NOTIFICATION'], 'RESOURCE, SLOT, RESERVATION'),
    ('Requests and money', ['REQUEST', 'REQUEST_EVENT', 'REQUEST_FILE', 'AGENT_CHECK', 'CHARGE', 'PAYMENT', 'APPLICATION'], 'REQUEST, REQUEST_EVENT, PAYMENT'),
    ('Conversations and memory', ['CONVERSATION', 'MESSAGE', 'MEMORY_FACT', 'WATCH', 'PENDING_QUESTION', 'FEEDBACK', 'TRACE_STEP'], 'CONVERSATION, MESSAGE, MEMORY_FACT'),
    ('Documents and knowledge', ['DOCUMENT', 'DOCUMENT_CHUNK', 'UNANSWERED_QUESTION', 'SOURCE_CONFLICT', 'CONTENT_ITEM'], 'DOCUMENT, DOCUMENT_CHUNK (pgvector)'),
    ('Study, library, control', ['COURSE', 'PROGRAM_COURSE', 'ENROLLMENT', 'CLASS_SESSION', 'ATTENDANCE', 'STUDY_PLAN', 'ADVISEE_SIGNAL', 'BOOK', 'LOAN', 'AUDIT_LOG', 'MODEL_USAGE', 'EVAL_RUN', 'CONTACT_MESSAGE'], 'ATTENDANCE, LOAN, AUDIT_LOG'),
]
assert sorted(e for _, es, _ in DATA_GROUPS for e in es) == sorted(ER_ENTITIES), set(e for _, es, _ in DATA_GROUPS for e in es) ^ set(ER_ENTITIES)


def m_data(d, notes=None):
    n_ent = len(ER_ENTITIES)
    s = d.add(notes=notes or f'One PostgreSQL database holds both the records and the document vectors. The model has {n_ent} entities in six groups. Say the three groups that matter: requests, conversations and memory, and documents with their chunks. The full ER diagram is in the appendix.')
    y = hdr(s, f'The data model: {n_ent} entities in six groups, one database', 'Architecture')
    cw = (1728 - 2 * 28) / 3
    ch = 350
    for i, (t, ents, ex) in enumerate(DATA_GROUPS):
        x = 96 + (i % 3) * (cw + 28)
        yy = y + (i // 3) * (ch + 28)
        s.rect(x, yy, cw, ch, fill=C['alt'], stroke=C['border'], r=18)
        s.rect(x, yy + 18, 8, ch - 36, fill=C['teal'], r=4)
        s.text(x + 32, yy + 28, cw - 64, t, size=32, weight=700, color=C['ink'], lh=1.2)
        s.text(x + 32, yy + 80, 100, f'{len(ents)}', size=72, weight=700, color=C['teal'], lh=1.0, fit=False)
        s.text(x + 140, yy + 108, cw - 170, 'entities', size=26, color=C['muted'])
        s.text(x + 32, yy + 198, cw - 64, ex, size=24, color=C['text'], lh=1.4, h=ch - 220)
    return s


def m_deploy(d, notes=None):
    s = d.add(notes=notes or 'Everything starts with one docker compose command. The application has a web build, the API and a worker. Chatwoot runs as its own set of containers. Keycloak has its own database. The model is a hosted API, so no laptop runs a model. An ngrok tunnel gives LINE and Telegram a public address for the webhook during development. The production database host is not decided: Docker Compose for development and the demo, a hosted PostgreSQL as the production option.')
    y = hdr(s, 'Deployment: one docker compose up', 'Architecture')
    s.rect(96, y, 1180, 720, fill=C['alt'], stroke=C['border_strong'], r=20, sw=3)
    s.text(124, y + 14, 700, 'Docker Compose on one host', size=24, weight=700, color=C['subtle'], upper=True, tracking=1.5)
    s.rect(124, y + 58, 560, 280, fill=C['bg'], stroke=C['teal'], r=14, sw=3)
    s.text(148, y + 72, 400, 'Application', size=26, weight=700, color=C['teal'], upper=True, tracking=1)
    for i, (t, sub) in enumerate([('web', 'React build'), ('api', 'FastAPI, agents'), ('worker', 'schedule, ingest')]):
        box(s, 148 + i * 176, y + 126, 164, 190, t, sub, fill=C['teal_tint'], stroke=C['teal_200'], tsize=28, ssize=22, pad=6)
    s.rect(716, y + 58, 536, 280, fill=C['bg'], stroke=C['teal'], r=14, sw=3)
    s.text(740, y + 72, 400, 'Chatwoot', size=26, weight=700, color=C['teal'], upper=True, tracking=1)
    for i, (t, sub) in enumerate([('web', None), ('worker', None), ('redis', None), ('database', 'own PostgreSQL')]):
        box(s, 740 + (i % 2) * 248, y + 118 + (i // 2) * 104, 236, 92, t, sub, fill=C['teal_tint'], stroke=C['teal_200'], tsize=26, ssize=21, pad=6)
    box(s, 124, y + 370, 372, 130, 'PostgreSQL 16', 'records and pgvector', fill=C['charcoal'], stroke=C['charcoal'], tcolor=C['white'], scolor='#D4D4D8', tsize=28, ssize=23)
    box(s, 516, y + 370, 372, 130, 'File storage', 'private volume, request files', fill=C['charcoal'], stroke=C['charcoal'], tcolor=C['white'], scolor='#D4D4D8', tsize=28, ssize=23)
    box(s, 908, y + 370, 344, 130, 'Keycloak', 'own PostgreSQL', fill=C['charcoal'], stroke=C['charcoal'], tcolor=C['white'], scolor='#D4D4D8', tsize=28, ssize=23)
    s.text(124, y + 530, 1128, 'No laptop runs a model. Inference goes to a hosted API.', size=28, weight=600, color=C['teal_dark'], lh=1.3)
    s.text(124, y + 590, 1128, 'Production database: not decided. Docker Compose for development, tests and the demo. A hosted PostgreSQL is the production option.', size=25, color=C['muted'], lh=1.3)
    ox = 1324
    ow = 1824 - ox
    s.text(ox, y, ow, 'Outside the host', size=24, weight=700, color=C['subtle'], upper=True, tracking=1.5)
    outs = [('Browsers', 'public site, portal, consoles'), ('LINE and Telegram', 'reach Chatwoot through an ngrok tunnel while we develop'), ('OpenRouter', 'hosted model API, free tier')]
    yy = y + 52
    for t, sub in outs:
        box(s, ox, yy, ow, 188, t, sub, fill=C['bg'], stroke=C['border_strong'], tsize=30, ssize=25)
        yy += 212
    return s


# ===================== stack, plan, risks =====================

def m_stack(d, notes=None):
    s = d.add(notes=notes or 'Every tool is free or open source. The big change since the first feasibility report is the model: we moved from a local model to a hosted free tier, so tool calling is more reliable and no laptop has to carry a model. The supervisor library is archived, so the supervisor is one LangChain agent that calls sub-agents as tools.')
    y = hdr(s, 'Technology stack and why', 'Proposal 12  ·  Technology stack')
    colw = [220, 560, 948]
    rows = [
        ['Layer', 'Choice', 'Why'],
        ['Backend', 'Python 3.12, FastAPI', 'The agent tools are strongest in Python.'],
        ['Agents', 'LangChain, LangGraph', 'One supervisor calls sub-agents as tools. The older supervisor library is archived.'],
        ['Model', 'OpenRouter, free tier', 'Hosted models should follow tool schemas better than a small local model. We choose the model by testing.'],
        ['Data', 'PostgreSQL 16, pgvector', 'One engine for records and document vectors.'],
        ['Identity', 'Keycloak, OIDC', 'No passwords in our code. An administrator creates accounts.'],
        ['Channels', 'Chatwoot, self-hosted', 'Web, LINE, Telegram and human takeover in one service.'],
        ['Frontend', 'React with Vite', 'One app. Keycloak roles gate the routes.'],
        ['Run and test', 'Docker Compose, pytest, Locust', 'One command starts it. Locust runs the concurrency test.'],
        ['Hosting', 'Docker Compose on one host, ngrok tunnel', 'No orchestration needed. A hosted PostgreSQL is the production option.'],
        ['Supporting tools', 'GitHub, Figma, Mermaid, draw.io', 'Version control, the prototype and the diagrams.'],
        ['External services', 'OpenRouter, LINE, Telegram', 'A hosted model and two chat platforms. The web chat works without the two platforms.'],
    ]
    s.table(96, y, colw, rows, size=24, hsize=22, minrow=62, pad=14)
    return s


def m_timeline(d, notes=None):
    s = d.add(notes=notes or 'This is the ten week plan from the feasibility report, updated for the current design. Week ten is a buffer with no new features. Week two is for measuring: the evaluation sets are written and frozen and the model is chosen by testing. The team agrees the four interfaces in week one and each track builds against a simple fake of the others.')
    y = hdr(s, 'Timeline and milestones: ten weeks, and week ten is a buffer', 'Proposal 14  ·  Timeline')
    x0, gw = 96 + 330, 1728 - 330
    wk = gw / 10
    for i in range(10):
        s.rect(x0 + i * wk, y, wk, 58, fill=C['charcoal'] if i % 2 == 0 else '#3F3F46')
        s.text(x0 + i * wk, y + 13, wk, f'W{i + 1}', size=26, weight=700, color=C['white'], align='c', lh=1.1, fit=False)
    phases = [
        (0, 2, 'Foundations', 'W1 to W2', 'Compose stack, schema, Keycloak realm, four agreed interfaces. Evaluation sets to be written and frozen. Model chosen by testing.', C['teal']),
        (2, 3, 'Core', 'W3 to W5', 'Corpus indexed. Four sub-agents, supervisor, role middleware, audit. Slot locking. Four-state requests. Library. Memory.', C['teal']),
        (5, 3, 'Channels and roles', 'W6 to W8', 'Chatwoot with Telegram, then LINE. Three role consoles. Handoff summary. Payment record. Worker: reminders and retries.', C['teal']),
        (8, 1, 'Extended and tests', 'W9', 'Attendance, advising, bulk jobs, uploads. Access suite, load test, scoring, usability test.', C['teal']),
        (9, 1, 'Buffer', 'W10', 'No new features. Fix, document, rehearse.', C['amber']),
    ]
    yy = y + 80
    for st, ln, t_, wks, b_, col in phases:
        s.text(96, yy + 8, 320, t_, size=28, weight=700, color=C['ink'], lh=1.2)
        s.rect(x0 + st * wk + 4, yy, ln * wk - 8, 56, fill=col, r=10)
        s.text(x0 + st * wk + 4, yy + 11, ln * wk - 8, wks, size=26, weight=700, color=C['white'], align='c', lh=1.15, fit=False)
        s.text(x0, yy + 66, gw, b_, size=26, color=C['text'], lh=1.3, h=70)
        yy += 134
    s.text(96, yy, 1728, 'Design is done: prototype, 12 diagrams, this proposal. Build runs W3 to W9, tests in W2 and W9. Project I ends after W10. Cut order if we slip: study plans and signals, bulk jobs and account files, then LINE.', size=22, color=C['muted'], lh=1.28)
    return s


def m_risks(d, notes=None):
    s = d.add(notes=notes or 'These are the risks we know and what we do about each, by type: technical, schedule, data, team, scope and user. The first one changed: with a hosted free tier the risk is no longer an unreliable local model. It is rate limits and a model being withdrawn. Prompt injection is covered by tools that take the subject from the token and by an attack test suite. Chatwoot sends LINE messages as push messages, and the free quota is not proven, so the LINE channel is kept for the demo.')
    y = hdr(s, 'Risks we know, and what we do about each', 'Proposal 15  ·  Risks')
    colw = [70, 150, 520, 988]
    rows = [
        ['ID', 'Type', 'Risk', 'What we do'],
        ['R1', 'Technical', 'The free model tier limits us, or a free model is withdrawn', 'Model name is one setting with a fallback list. Free limits: 20 requests a minute and 50 a day for each account, so a full evaluation run needs cached results, spreading over days, or about 10 credits.'],
        ['R2', 'Technical', 'Prompt injection, or a request for another user\'s data', 'Tools take the subject from the token. Tool allowlists. A test suite attacks every tool.'],
        ['R3', 'Scope', 'Scope creep, or a scope too big for ten weeks', 'Core first, extended features after. Cut order fixed in advance. Adding means removing.'],
        ['R4', 'Team', 'Four tracks do not fit together', 'Four interfaces agreed in week one. Each track builds against a fake of the others.'],
        ['R5', 'Schedule', 'The schedule slips or work is uneven', 'Weekly milestones with a done condition. Week ten adds no features.'],
        ['R6', 'Technical', 'Thai answers are weaker than English', 'Thai questions in the test set from week two. No source means refuse.'],
        ['R7', 'Technical', 'LINE push messages exceed the free quota', 'LINE for the demo only. Load tests on Telegram and web. Free LINE replies in Project II.'],
        ['R8', 'Data', 'All data is made up, so messy real records are not tested', 'We state the limit. Test data holds duplicates and gaps. We never claim real-world results.'],
        ['R9', 'User', 'Too few students join the usability test', 'Book the five sessions early, in week 7. Report the real number of users.'],
    ]
    s.table(96, y, colw, rows, size=22, hsize=22, minrow=64, pad=12)
    return s


def m_decisions(d, notes=None):
    s = d.add(notes=notes or 'Be open about what is decided and what is not. The left column is settled and recorded. The right column is open on purpose: the model is chosen by testing in development, and the database host and the LINE quota fix are decided when we have evidence.')
    y = hdr(s, 'Decisions made, and decisions still open', 'How we build it')
    w = 840
    ch = 720
    s.rect(96, y, w, ch, fill=C['green_tint'], stroke=C['green_200'], r=18)
    s.pill(128, y + 28, 'Decided', fill=C['green'], color=C['white'], h=48, size=26)
    s.bullets(128, y + 112, w - 64, [
        'One supervisor, four sub-agents as tools, a role middleware',
        'Everyone signs in through Keycloak. The IT team has its own Chatwoot login',
        'LINE and Telegram carry plain text. The web chat is plain text too. A user can send a photo',
        'Guests never use the assistant. The site is English only for now',
        'Staff, instructors and administrators use the assistant, limited by role',
        'A payment slip goes to staff in a normal chat. The assistant records it only after a yes'], size=30, gap=22, dot=C['green'])
    x2 = 96 + w + 48
    s.rect(x2, y, w, ch, fill=C['amber_tint'], stroke=C['amber_200'], r=18)
    s.pill(x2 + 32, y + 28, 'Open on purpose', fill=C['amber'], color=C['white'], h=48, size=26)
    s.bullets(x2 + 32, y + 112, w - 64, [
        'Which free model: chosen by testing tool calling and Thai',
        'How to handle the LINE push quota',
        'The production database host',
        'Whether to buy about 10 credits for the full evaluation run',
        'Whether the team confirms the cut order and the speed targets',
        'Track owners for the build'], size=30, gap=22, dot=C['amber'])
    return s


def m_eval(d, notes=None):
    s = d.add(notes=notes or 'This is how we will know it works. Two evaluation sets will be written and frozen before any agent code. Two people score the answers separately and we report English and Thai separately. We also test the hard things: the concurrency test, the cross account attacks and a usability test with five students. These are targets. We have no measured results yet.')
    y = hdr(s, 'How we will measure it', 'How we build it')
    items = [('50', 'graded questions', 'English and Thai. At least 80 percent correct with a correct citation.'),
             ('100', 'labelled messages', 'A separate set for routing. 90 percent or higher.'),
             ('200', 'concurrent requests', 'On one slot. Exactly one succeeds.'),
             ('40', 'attack attempts', '30 cross-account and 10 staff-tool attempts. None may succeed.'),
             ('5', 'test students', 'Book a study room in 90 seconds or less. At least 4 of 5 succeed.'),
             ('1', 'command', 'docker compose up starts everything within 5 minutes.')]
    cw = (1728 - 2 * 28) / 3
    ch = 320
    for i, (n, l, b) in enumerate(items):
        x = 96 + (i % 3) * (cw + 28)
        yy = y + (i // 3) * (ch + 28)
        s.rect(x, yy, cw, ch, fill=C['alt'], stroke=C['border'], r=18)
        off = 150 if len(n) < 2 else (210 if len(n) < 3 else 290)
        s.text(x + 28, yy + 18, off - 8, n, size=88, weight=700, color=C['teal'], lh=1.0, fit=False)
        s.text(x + 28 + off, yy + 50, cw - 56 - off, l, size=30, weight=700, color=C['ink'], lh=1.2)
        s.text(x + 28, yy + 150, cw - 56, b, size=27, color=C['text'], lh=1.3, h=ch - 164)
    s.text(96, 1000 - 40, 1728, 'These are targets. No result has been measured yet.', size=28, weight=600, color=C['amber'])
    return s


def m_tests(d, notes=None):
    s = d.add(notes=notes or 'These are our first real test results, from 15 and 16 October. We ran a self-hosted Chatwoot in Docker behind an ngrok address and connected a LINE official account and a Telegram bot. Everything that the design needs worked, and the one thing that failed, cards, changed the design. Eleven checks in total, nine passed.')
    y = hdr(s, 'Initial test results: channels through Chatwoot', 'Where we are')
    colw = [790, 200, 738]
    rows = [
        ['Test', 'Result', 'What it means'],
        ['Text in and out, LINE and Telegram', 'Passed', 'The basic chat works'],
        ['Photos in and out, LINE and Telegram', 'Passed', 'A slip can arrive as a photo and reach a person'],
        ['Tappable buttons on both', 'Passed', 'Worked, but we chose plain text on every channel'],
        ['Cards on LINE and on Telegram', 'Failed', 'Only the text arrives. We use no cards on these channels'],
        ['A new chat stays pending', 'Passed', 'The bot owns it until a person acts'],
        ['A failing bot address', 'Passed', 'The chat opens for a person by itself'],
        ['LINE and Telegram merged into one contact', 'Passed', 'One history across channels'],
    ]
    fills = {}
    for r in range(1, len(rows)):
        fills[(r, 1)] = C['red_tint'] if rows[r][1] == 'Failed' else C['green_tint']
    s.table(96, y, colw, rows, size=27, hsize=24, minrow=78, pad=20, cellfill=fills)
    s.text(96, 1000 - 76, 1728, '11 checks, 9 passed, 2 failed (cards on LINE and on Telegram). Made-up data, one Mac, about 0.9 GB of memory when idle. The test server and its data are deleted.', size=24, color=C['muted'], lh=1.3)
    return s


def m_proto(d, notes=None):
    s = d.add(notes=notes or 'The prototype is what we ask you to judge. 270 frames, light and dark twins, grouped in 12 stories in three parts. Every story has a bar at the bottom with the actor, the channel and a Next button, so one click follows the story even when the actor changes. It is built on a design system of more than 60 components with tokens for every color, space and radius. We checked every frame for broken links, overlap and overflow.')
    y = hdr(s, 'The prototype: 270 frames in 12 stories', 'The prototype')
    stats = [('270', 'frames, light and dark twins'), ('4,258', 'prototype links, none broken'), ('12', 'stories: student, staff, instructor'), ('60+', 'design system components')]
    cw = (1728 - 3 * 28) / 4
    for i, (n, l) in enumerate(stats):
        x = 96 + i * (cw + 28)
        s.rect(x, y, cw, 220, fill=C['teal_tint'], stroke=C['teal_200'], r=16)
        s.text(x, y + 22, cw, n, size=84, weight=700, color=C['teal_dark'], align='c', lh=1.0, fit=False)
        s.text(x + 20, y + 130, cw - 40, l, size=26, color=C['muted'], align='c', lh=1.25)
    yy = y + 250
    s.image('v2/home.png', 96, yy, 560, 350, fit='contain', r=12, border=C['border'], shadow=True)
    s.image('v2/s1_6.png', 696, yy, 560, 350, fit='contain', r=12, border=C['border'], shadow=True)
    s.image('v2/home_m.png', 1296, yy, 170, 350, fit='contain', r=12, border=C['border'], shadow=True)
    s.image('v2/s1_1.png', 1486, yy, 338, 350, fit='contain', r=12, border=C['border'], shadow=True)
    s.text(96, yy + 362, 560, 'Public site', size=24, color=C['muted'], align='c')
    s.text(696, yy + 362, 560, 'Staff ask the assistant', size=24, color=C['muted'], align='c')
    s.text(1296, yy + 362, 170, 'Mobile', size=24, color=C['muted'], align='c')
    s.text(1486, yy + 362, 338, 'LINE, plain text', size=24, color=C['muted'], align='c')
    s.text(96, yy + 412, 1728, 'Built in Figma on tokens and components: Inter, Lucide icons, an 8-point grid, WCAG AA contrast. Every story is clickable.', size=26, color=C['muted'], lh=1.3)
    return s

def m_deliverables(d, notes=None):
    s = d.add(notes=notes or 'Here is where we stand against the seven deliverables of Project I. We say plainly what is done and what is planned. The code prototype is the big item still ahead.')
    y = hdr(s, 'Where we are on the seven deliverables of Project I', 'Proposal 16  ·  Deliverables', size=48)
    n, first = git_facts()
    vc = f'GitHub repository started on {first}, {n} commits so far' if n else 'GitHub repository with commit history'
    colw = [70, 520, 1138]
    rows = [
        ['#', 'Deliverable', 'Status'],
        ['1', 'Problem, objectives, requirements', 'Written: the survey report and feasibility report v3 with 33 + 5 requirements. They answer the four comments on the first problem statement.'],
        ['2', 'Architecture and models', 'Done: 12 diagrams, from architecture to use case.'],
        ['3', 'Working prototype', 'Figma prototype built and under team review. Coded prototype planned for weeks 3 to 9.'],
        ['4', 'Version control', vc + '.'],
        ['5', 'Initial testing results', '9 of 11 channel checks passed. Evaluation and attack tests are planned.'],
        ['6', 'Documentation and records', 'Survey, feasibility report v3, 12 diagrams with source, prototype story map.'],
        ['7', 'Project II plan', 'On the next slide.'],
    ]
    yb = s.table(96, y, colw, rows, size=26, hsize=24, minrow=84, pad=20)
    s.text(96, yb + 18, 1728, 'Feasibility report v3 of 17 October replaces version 2. It uses the OpenRouter free tier, the state name Collected and the role name instructor.', size=22, color=C['muted'], lh=1.3)
    return s


def m_proj2(d, notes=None):
    s = d.add(notes=notes or 'Project II keeps the two engines and adds more of the same. Everything on this list reuses the reservation engine or the request state machine, which is why it was deferred and not cancelled.')
    y = hdr(s, 'Project II plan: what remains, and why it waits', 'Proposal 17  ·  Project II', size=48)
    cards = [
        ('Remaining features', 'Borrowing, returning and holds. Event registration. Maintenance reports. More bookable resources. Course add and drop. Each one reuses an engine, so each waits for time, not for design.'),
        ('Integration and hardening', 'A real student information system. Payment processing. Buttons and cards on LINE and Telegram. Free LINE replies, not push messages.'),
        ('Deeper testing', 'Messy real records. More languages. Load beyond the free tier. A security review.'),
        ('Evaluation with users', 'A usability study with more than five students and staff. Feedback collected and analysed.'),
        ('Deployment or pilot', 'A paid model tier, a production database host, a cloud host with a domain and managed TLS, and a pilot with one office.'),
        ('Final documentation', 'The complete technical report, a user guide and a reflection.'),
    ]
    cw = (1728 - 2 * 28) / 3
    ch = 340
    for i, (t, b) in enumerate(cards):
        x = 96 + (i % 3) * (cw + 28)
        yy = y + (i // 3) * (ch + 28)
        s.rect(x, yy, cw, ch, fill=C['alt'], stroke=C['border'], r=18)
        s.rect(x, yy, cw, 12, fill=C['teal'], r=6)
        s.text(x + 28, yy + 34, cw - 56, t, size=34, weight=700, color=C['ink'])
        s.text(x + 28, yy + 92, cw - 56, b, size=26, color=C['text'], lh=1.32, h=ch - 110)
    return s


def m_thanks(d, notes=None, line='Questions'):
    s = d.add(kind='dark', bg=C['charcoal'], footer=False, number=False, notes=notes or 'Thank the room. Offer to open the prototype on any frame they ask about.')
    s.rect(96, 330, 160, 14, fill=C['lime'])
    s.text(96, 380, 1500, line, size=110, weight=700, color=C['white'], lh=1.05)
    s.text(96, 540, 1500, 'Smart University Website  ·  Group S', size=42, color='#D4D4D8')
    s.text(96, 610, 1500, 'Wai Yan Lynn  ·  Pyae Sone  ·  Nang Ying Noom Lao  ·  Myat Hsu Hnin', size=32, color='#A1A1AA')
    return s


# ===================== appendix =====================

def m_appx_img(d, title, image, caption, notes=''):
    s = d.add(notes=notes or 'Reference slide. Only open it if asked.')
    y = hdr(s, title, 'Appendix')
    im = Image.open(os.path.join(lib.IMG, image))
    maxh = 1000 - y - 56
    w = min(1728, maxh * im.size[0] / im.size[1])
    h = w * im.size[1] / im.size[0]
    s.image(image, 96 + (1728 - w) / 2, y, w, h, fit='contain', r=12, border=C['border'])
    s.text(96, y + h + 12, 1728, caption, size=24, color=C['muted'], align='c')
    return s


def m_appx_requirements(d):
    s = d.add(notes='Reference slide with the non-functional requirements. The speed targets are proposals for the hosted model and the week two test measures them.')
    y = hdr(s, 'Appendix: the five non-functional requirements', 'Appendix')
    colw = [300, 900, 528]
    rows = [
        ['Requirement', 'Target', 'Test'],
        ['NFR-01 Performance', 'First visible token 3 s, full reply 10 s or 6 s, 10 concurrent conversations. Proposals until measured.', '100 requests, 95th percentile'],
        ['NFR-02 Security', 'Sign-in tokens (OIDC) are signed and expire in 15 minutes. Browser traffic uses TLS 1.2 or higher, through the ngrok tunnel in Project I. No password stored. 0 of 40 attacks succeed.', '30 + 10 attack attempts'],
        ['NFR-03 Usability', 'A first-time student books a study room in 90 seconds or less and 4 messages or fewer.', '5 test users, at least 4 succeed'],
        ['NFR-04 Reliability', 'One docker compose up within 5 minutes. A restart loses no reservation and no request. A service message within 10 seconds if the model is rate limited or unreachable.', 'Clean machine test'],
        ['NFR-05 Accuracy', 'Routing 90 percent or higher. 80 percent of 50 answers correct with a correct citation, English and Thai reported separately.', '100 messages, two raters'],
    ]
    s.table(96, y, colw, rows, size=24, hsize=24, minrow=90, pad=18)
    return s


def m_appx_sources(d):
    s = d.add(notes='Sources for the survey. Every row can be rechecked from these public pages.')
    y = hdr(s, 'Appendix: survey sources and limits', 'Appendix')
    s.text(96, y, 1728, 'Thailand', size=28, weight=700, color=C['teal'])
    yy = s.text(96, y + 42, 1728, 'reg.chula.ac.th, reg.tu.ac.th, graduate.mahidol.ac.th, grad.ku.ac.th, regis.kmutt.ac.th, reg.kmitl.ac.th, registrar.au.edu, bulinks.bu.ac.th, lib.swu.ac.th, acdserv.kmutnb.ac.th, stou.ac.th, oapr.bru.ac.th', size=24, color=C['muted'], lh=1.4)
    s.text(96, yy + 28, 1728, 'International', size=28, weight=700, color=C['teal'])
    yy = s.text(96, yy + 70, 1728, 'nusit.nus.edu.sg, nus.libcal.com, nus.edu.sg/inside-nus, gradresearch.unimelb.edu.au, sis.utoronto.ca, studentsupport.manchester.ac.uk, registrar.asu.edu, ssi.asu.edu', size=24, color=C['muted'], lh=1.4)
    s.text(96, yy + 28, 1728, 'Published research', size=28, weight=700, color=C['teal'])
    yy = s.text(96, yy + 70, 1728, 'A 2025 review of university chatbots for student support (Springer). An IJECE paper on LINE-based services for graduate students. Thai journal papers on NN Bot at KMUTNB and on a student service chatbot at Buriram Rajabhat University.', size=24, color=C['muted'], lh=1.4)
    note_bar(s, yy + 40, 'All checked on 5 and 6 October 2026. We did not log in to any portal, so a university may offer more inside its portal. We did not survey students.', size=26, fill=C['amber_tint'], color=C['amber'], stroke=C['amber_200'], weight=500)
    return s
