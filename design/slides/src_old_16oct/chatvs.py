"""Option 1 comparison: two chat windows drawn in the same style and the same channel skin.
Left, an ordinary bot (illustrative mock). Right, our assistant, with action lines for what the backend did.
Nothing here is a screenshot. All ordinary-bot text is made up for contrast."""
import lib
from lib import C, wrap, text_w
from kit import hdr

MOCK_TAG = 'Illustrative mock, not a real bot'

SKINS = {
    'web': dict(name='Web portal', head='#FFFFFF', head_text=C['ink'], title='Thales Assistant', body=C['alt'],
                user=C['teal'], user_text=C['white'], bot=C['white'], bot_text=C['text'], bot_stroke=C['border'],
                btn_fill=C['white'], btn_text=C['ink'], btn_stroke=C['border_strong'], head_border=True),
    'line': dict(name='LINE', head='#06C755', head_text=C['white'], title='Thales University', body='#8CABD9',
                 user='#8DE055', user_text=C['ink'], bot=C['white'], bot_text=C['text'], bot_stroke=None,
                 btn_fill=C['white'], btn_text=C['ink'], btn_stroke=None, head_border=False),
    'tg': dict(name='Telegram', head='#3390EC', head_text=C['white'], title='Thales University', body='#D7E4EE',
               user='#EFFDDE', user_text=C['ink'], bot=C['white'], bot_text=C['text'], bot_stroke=None,
               btn_fill='#E8F2FB', btn_text='#2481CC', btn_stroke=None, head_border=False),
}

FS = 23      # chat text
AS = 21      # action text


def _bubble(s, sk, x, y, w, who, text, size=FS):
    bw = w * 0.90
    lines = wrap(text, (bw - 40) * 0.975, size, 400)
    tw = min(bw, max(text_w(l, size, 400) for l in lines) + 48)
    hh = len(lines) * size * 1.3 + 28
    if who == 'u':
        bx, fill, col, st = x + w - tw, sk['user'], sk['user_text'], None
    else:
        bx, fill, col, st = x, sk['bot'], sk['bot_text'], sk['bot_stroke']
    s.rect(bx, y, tw, hh, fill=fill, stroke=st, sw=2, r=18)
    s.text(bx + 20, y + 14, (tw - 40) / 0.975 + 4, text, size=size, color=col, lh=1.3, fit=False)
    return y + hh


def _buttons(s, sk, x, y, w, labels, size=21):
    cx, cy = x, y
    for i, lb in enumerate(labels):
        tw = text_w(lb, size, 600) + 40
        if cx + tw > x + w and cx > x:
            cx, cy = x, cy + 56
        primary = (i == 0 and sk is SKINS['web'])
        s.rect(cx, cy, tw, 46, fill=C['teal'] if primary else sk['btn_fill'], stroke=None if primary else sk['btn_stroke'], sw=2, r=23)
        s.text(cx + 20, cy + 10, tw, lb, size=size, weight=600, color=C['white'] if primary else sk['btn_text'], lh=1.2, fit=False)
        cx += tw + 12
    return cy + 46


def _action(s, x, y, w, agent, text):
    lines = wrap(text, (w - 40) * 0.975, AS, 400)
    hh = 38 + len(lines) * AS * 1.28 + 14
    s.rect(x, y, w, hh, fill=C['teal_tint'], stroke=C['teal_200'], sw=2, r=14)
    s.rect(x, y + 12, 6, hh - 24, fill=C['teal'], r=3)
    s.text(x + 22, y + 10, w - 40, agent.upper(), size=20, weight=700, color=C['teal'], tracking=1, lh=1.2, fit=False)
    s.text(x + 22, y + 38, w - 40, text, size=AS, color=C['teal_dark'], lh=1.28, fit=False)
    return y + hh


def _photo(s, x, y, w, caption):
    pw, ph = 300, 130
    s.rect(x + w - pw, y, pw, ph, fill=C['white'], stroke=C['border'], sw=2, r=14)
    s.rect(x + w - pw + 20, y + 20, pw - 40, 34, fill=C['green_tint'], r=8)
    s.text(x + w - pw + 32, y + 26, pw - 60, caption, size=20, weight=600, color=C['green'], lh=1.2, fit=False)
    for i, ww in enumerate((0.55, 0.8)):
        s.rect(x + w - pw + 20, y + 74 + i * 26, (pw - 40) * ww, 12, fill=C['panel'], r=6)
    return y + ph


def _cite(s, x, y, w, text):
    tw = min(w * 0.8, text_w(text, 21, 600) + 70)
    s.rect(x, y, tw, 52, fill=C['white'], stroke=C['border'], sw=2, r=12)
    s.rect(x, y + 6, 6, 40, fill=C['teal'], r=3)
    s.text(x + 22, y + 13, tw - 30, text, size=21, weight=600, color=C['ink'], lh=1.2, fit=False)
    return y + 52


def _end(s, x, y, w, text):
    s.mark('n', x + 22, y + 24, 30)
    lines = wrap(text, (w - 60) * 0.975, 22, 600)
    s.text(x + 52, y + 8, w - 60, text, size=22, weight=600, color=C['red'], lh=1.25, fit=False)
    return y + max(48, len(lines) * 22 * 1.25 + 16)


def window(s, x, y, w, h, skin, items, who, role='Assistant'):
    """who: 'bot' or 'ours'. Draws the window and every item. Reports overflow."""
    sk = SKINS[skin]
    s.rect(x, y, w, h, fill=sk['body'], stroke=C['border_strong'], sw=2, r=22)
    s.rect(x, y, w, 70, fill=sk['head'], r=22)
    s.rect(x, y + 40, w, 30, fill=sk['head'])
    if sk['head_border']:
        s.rect(x + 2, y + 69, w - 4, 2, fill=C['border'])
    s.text(x + 28, y + 19, 420, sk['title'], size=28, weight=700, color=sk['head_text'], lh=1.2, fit=False)
    if who == 'ours':
        s.pill(x + w - 40 - text_w(role, 20, 600), y + 14, role, fill=C['teal_tint'] if skin == 'web' else C['white'], color=C['teal'], h=42, size=20)
    s.pill(x + 24, y + h + 12, 'x', fill=None) if False else None
    ix, iw = x + 24, w - 48
    yy = y + 70 + 12
    prev = None
    for it in items:
        k = it[0]
        gap = 14 if prev in ('act', 'btns', 'cite') or k in ('act', 'btns', 'cite') else 14
        if prev is None:
            gap = 0
        yy += gap
        if k in ('u', 'b'):
            yy = _bubble(s, sk, ix, yy, iw, k, it[1])
        elif k == 's':
            s.text(ix + 6, yy, iw, it[1], size=20, weight=700, color=C['teal'], lh=1.2, fit=False)
            yy = _bubble(s, sk, ix, yy + 26, iw, 'b', it[2])
        elif k == 'act':
            yy = _action(s, ix, yy, iw, it[1], it[2])
        elif k == 'btns':
            yy = _buttons(s, sk, ix, yy, iw, it[1])
        elif k == 'photo':
            yy = _photo(s, ix, yy, iw, it[1])
        elif k == 'cite':
            yy = _cite(s, ix, yy, iw, it[1])
        elif k == 'end':
            yy = _end(s, ix, yy + 6, iw, it[1])
        prev = k
    if yy > y + h - 14:
        s.issues.append(f'chat window overflow ({who}): bottom {yy:.0f} limit {y + h - 14:.0f}')
    return yy


SCEN = {
    'visa': dict(skin='web', title='A rule question: a link, or the rule itself',
        bot=[('u', 'What documents do I need for my student visa renewal?'),
             ('b', 'For visa information, please visit the International Office page: thales.example/international'),
             ('end', 'The chat ends. The student opens a PDF and looks for the rule.')],
        ours=[('u', 'What documents do I need for my student visa renewal?'),
              ('act', 'Knowledge agent', 'Searched the Student Handbook 2026. Found section 7.3.'),
              ('b', 'For a visa renewal you need three documents: 1. Enrollment Certificate. 2. Official Transcript. 3. A letter confirming your tuition payment. Shall I start with the official transcript?'),
              ('cite', 'Student Handbook 2026, section 7.3'),
              ('btns', ['Yes, start with the transcript', 'Not now'])],
        lose='It sends a link. The rule is still inside a PDF.',
        win='It answers from the University\'s own rule, cites it and offers the next step.'),
    'room': dict(skin='line', title='A booking on LINE: from "ask the counter" to a booked room',
        bot=[('u', 'I need a study room for my group on Thursday afternoon'),
             ('b', 'Sorry, I cannot book rooms. Rooms can be booked at the library counter during opening hours.'),
             ('end', 'The chat ends. No room is booked.')],
        ours=[('u', 'I need a study room for my group on Thursday afternoon'),
              ('act', 'Booking agent', 'Read the free rooms for Thursday. Nothing is held.'),
              ('b', 'Three rooms are free: Library Room B2, Library Room B4 and Learning Commons C1. Which one?'),
              ('u', 'Library Room B2'),
              ('b', 'Book Library Room B2, Thursday 15 October, 13:00 to 15:00? Reply yes.'),
              ('u', 'yes'),
              ('act', 'Booking agent', 'One transaction, one audit record.')],
        lose='It talks about rooms but has no tool that books one.',
        win='It reads the free rooms, waits for a yes, then writes the booking and logs it.'),
    'transcript': dict(skin='line', title='A request on LINE: a form to download, or a request that is tracked',
        bot=[('u', 'I need an official transcript for a job application'),
             ('b', 'To request a transcript, download the form from the Registrar page, fill it in and bring it to the counter.'),
             ('end', 'The chat ends. No request exists, so there is no status.')],
        ours=[('u', 'I need an official transcript for a job application'),
              ('act', 'Request agent', 'Applied the fee rule: 100 THB for each copy. Asked for the copies and the way to collect.'),
              ('b', 'Transcript, 2 copies, collect in person, 200 THB. Reply yes to submit the request.'),
              ('u', 'yes'),
              ('act', 'Request agent', 'Wrote REQ-2026-0481 in the state Submitted.'),
              ('b', 'Friday 16 October, 09:12. REQ-2026-0481 is ready. Collect it at the Registrar.')],
        lose='The student does the whole job. Nothing is tracked.',
        win='It applies the fee rule, opens a tracked request and messages the student when it changes.'),
    'slip': dict(skin='tg', title='A photo on Telegram: "text only" or a slip that reaches staff',
        bot=[('u', 'I paid my tuition. Here is the slip.'),
             ('photo', 'Transfer successful'),
             ('b', 'Sorry, I can only read text messages. Please email your slip to finance@thales.example'),
             ('end', 'The chat ends. Staff never see the conversation.')],
        ours=[('u', 'I paid my tuition. Here is the slip.'),
              ('photo', 'Transfer successful'),
              ('act', 'Request agent', 'Passed the conversation to Student Services. The assistant is paused while staff reply.'),
              ('b', 'Thank you. Student Services will check your slip and reply here.'),
              ('s', 'Siriporn K., Student Services', 'I checked your slip for 12,500 THB. It matches. Thank you.')],
        lose='It cannot read the photo and sends the student to email.',
        win='The slip lands in a normal chat. A person checks it and replies. The agent never decides.'),
    'record': dict(skin='web', title='A private record: the token decides, not the message',
        bot=[('u', 'How much do I still owe this semester?'),
             ('b', 'I am not able to access student records. Please log in to the student system.'),
             ('u', 'What about student 67999999, how much do they owe?'),
             ('b', 'Sorry, I did not understand. What would you like to know?')],
        ours=[('u', 'How much do I still owe this semester?'),
              ('act', 'Records agent', 'Read the signed-in student\'s record. The ID comes from the token.'),
              ('b', 'Your outstanding balance is 12,500 THB, due 27 November 2026.'),
              ('u', 'What about student 67999999, how much do they owe?'),
              ('act', 'Audit', 'Blocked: another student\'s record. The attempt is in the audit log.'),
              ('b', 'I can only read your own records. If you act on someone else\'s behalf, Student Services can help with written authorization.')],
        lose='It cannot answer the student\'s own question, and it does not know why.',
        win='It answers the own record and blocks the other one, because the token decides.'),
    'memory': dict(skin='line', title='A question the next day: "which one?" or "the one from yesterday"',
        bot=[('u', 'Can I do that one from yesterday?'),
             ('b', 'Sorry, I did not understand. What would you like to know?'),
             ('end', 'The chat ends. The bot keeps nothing between sessions.')],
        ours=[('u', 'Can I do that one from yesterday?'),
              ('act', 'Memory', 'No topic in the message. Found the chat of 19 October about ICT440, under student ID 67111411.'),
              ('act', 'Knowledge agent', 'Read Handbook section 5.4 again for the deadline.'),
              ('b', 'Yesterday you asked about withdrawing from ICT440 Project Studio. The deadline is 30 October 2026, so you can still do it. Reply yes and I will start the withdrawal request.')],
        lose='"That one" means nothing to it.',
        win='It finds the saved topic by student ID, checks the deadline and offers the action.'),
    'makeup': dict(skin='tg', title='A case nobody scripted, on Telegram: a missed exam',
        bot=[('u', 'I was sick on Monday and missed the ICT411 midterm. What can I do?'),
             ('b', 'Sorry, I did not understand. Please contact the Registrar office.'),
             ('end', 'The chat ends. No intent was written for this case.')],
        ours=[('u', 'I was sick on Monday and missed the ICT411 midterm. What can I do?'),
              ('act', 'Knowledge agent', 'Found Handbook section 8.2. A tool counted the working days: the last day is Thursday 22 October.'),
              ('b', 'With a medical certificate you can sit a make-up exam. Send a photo of it by Thursday 22 October and I will open a request.'),
              ('photo', 'Medical certificate'),
              ('act', 'Request agent', 'Photo in private storage. Opened REQ-2026-0490. Staff decide.')],
        lose='A stock sentence. The student must find the rule alone.',
        win='It finds the rule, counts the days in code, opens a request and leaves the decision to staff.'),
}


STAFF = {
    'approve': dict(skin='tg', role='Staff account', title='Staff on Telegram: read the queue, then approve a request',
        bot=[('u', 'How many items wait for me and which is the oldest?'),
             ('b', 'Sorry, I cannot see the request queue. Please log in to the staff system.'),
             ('u', 'Approve REQ-2026-0489.'),
             ('b', 'I can only answer general questions about the University.')],
        ours=[('u', 'How many items wait for me and which is the oldest?'),
              ('act', 'Request agent', 'Read the open requests for Student Services. Read only.'),
              ('b', '5 items. The oldest is REQ-2026-0487, blocked by a fee hold.'),
              ('u', 'Approve REQ-2026-0489.'),
              ('b', 'REQ-2026-0489: all 3 checks passed. Approve it and tell the student on LINE? Reply yes.'),
              ('u', 'yes'),
              ('act', 'Request agent', 'State set to Ready. Student told. The audit log holds the staff member.')],
        lose='It cannot read the queue or change a request.',
        win='It reads the queue, asks for a yes, then writes the new state and the audit record.'),
    'remind': dict(skin='web', role='Staff account', title='Staff in the console: a bulk action that needs a yes',
        bot=[('u', 'Remind everyone whose request is ready for more than 3 days.'),
             ('b', 'Sorry, I cannot send messages. Please use the notification tool in the staff system.'),
             ('end', 'The chat ends. The staff member does it by hand.')],
        ours=[('u', 'Remind everyone whose request is ready for more than 3 days.'),
              ('act', 'Request agent', 'Searched the requests in the state Ready for more than 3 days. Found 1 student.'),
              ('b', 'One student. Draft: "Your request is ready. Please collect it at the Registrar office." Send it?'),
              ('btns', ['Yes, send', 'Edit the draft']),
              ('act', 'Request agent', 'After the yes: sent on the channel where the request began. Audit record written.')],
        lose='It cannot find the students or send anything.',
        win='It finds the rows, drafts the message and sends it only after the yes.'),
    'scope': dict(skin='web', role='Staff account', title='Staff in the console: the role sets which rows can be read',
        bot=[('u', 'Show me everything Wai Yan Lynn asked the assistant this week.'),
             ('b', 'Sorry, I did not understand. What would you like to know?'),
             ('end', 'The chat ends. No answer, and no rule behind it.')],
        ours=[('u', 'Show me everything Wai Yan Lynn asked the assistant this week.'),
              ('act', 'Records agent', 'Role: Student Services staff. Read only the conversations passed to Student Services.'),
              ('b', 'Here are the conversations that were passed to Student Services this week. Other chats stay private.'),
              ('act', 'Audit', 'The read is written to the audit log with the staff member and the student ID.')],
        lose='It has no idea who is asking, so it cannot apply a rule.',
        win='The role from the sign-in sets the tools and the rows. Every read leaves a record.'),
    'slipdb': dict(skin='web', role='Staff account', title='Staff in the console: update the database after checking a slip',
        bot=[('u', 'Wai Yan Lynn, ID 67111411, paid this semester\'s fee. Update the database.'),
             ('b', 'Sorry, I cannot change records. Please use the finance system.'),
             ('end', 'The chat ends. The staff member types the record by hand.')],
        ours=[('u', 'Wai Yan Lynn, ID 67111411, paid this semester\'s fee. Update the database.'),
              ('act', 'Records agent', 'Found student 67111411. Open balance for Semester 1/2026: 12,500 THB.'),
              ('b', 'Record a payment of 12,500 THB for Wai Yan Lynn, 67111411, and set the balance to 0 THB?'),
              ('btns', ['Yes, update', 'Not now']),
              ('act', 'Request agent', 'After the yes: wrote the payment record and set the balance to 0 THB. The audit log holds the staff member.'),
              ('b', 'Done. The balance is 0 THB.')],
        lose='It cannot find the student or change a record.',
        win='The person checked the slip. The assistant writes the record only after a yes.'),
    'attend': dict(skin='line', role='Instructor account', title='An instructor on LINE: attendance, a warning and a yes',
        bot=[('u', 'Who missed ICT411 last Wednesday?'),
             ('b', 'Sorry, I do not have access to attendance records.'),
             ('end', 'The chat ends. The instructor opens the attendance system.')],
        ours=[('u', 'Who missed ICT411 last Wednesday?'),
              ('act', 'Records agent', 'Read the attendance of the own course only.'),
              ('b', '14 October: 38 present, 1 late, 3 absent: Kittipong A., Arthit S. and Chai W.'),
              ('u', 'Is anyone close to the absence limit?'),
              ('act', 'Knowledge agent', 'A tool counted the absences. Handbook 6.5: a warning at 3.'),
              ('b', 'Arthit S. has 3 absences in 9 classes. Send a warning and tell Student Services? Reply yes.')],
        lose='It cannot read attendance.',
        win='A tool counts, the Handbook gives the limit, and a yes comes before any message.'),
    'move': dict(skin='line', role='Instructor account', title='An instructor on LINE: move a meeting',
        bot=[('u', 'Move my meeting with Mali on Thursday to Friday afternoon.'),
             ('b', 'Sorry, I cannot change your calendar.'),
             ('end', 'The chat ends. Nothing moves, and Mali is not told.')],
        ours=[('u', 'Move my meeting with Mali on Thursday to Friday afternoon.'),
              ('act', 'Booking agent', 'Read the free slots on Friday afternoon. Nothing is held yet.'),
              ('b', 'Friday afternoon has 15:00 and 16:00. Which one?'),
              ('u', '15:00'),
              ('act', 'Booking agent', 'Moved the meeting in one transaction. Mali S. told on LINE. Audit record written.'),
              ('b', 'Moved to Friday 15:00. Mali S. is told on LINE.')],
        lose='It cannot read a calendar or write to one.',
        win='The same reservation engine that books students moves the meeting and tells the other person.'),
    'admin': dict(skin='line', role='Administrator account', title='An administrator on LINE: add a document, create accounts',
        bot=[('u', 'Add this file, Examination Rules 2026.'),
             ('b', 'Sorry, I can only chat. Please ask the web team to upload documents.'),
             ('end', 'The chat ends. The knowledge base does not change.')],
        ours=[('u', 'Add this file, Examination Rules 2026.'),
              ('act', 'Knowledge agent', 'Read the file, split it into sections and indexed them.'),
              ('b', '96 sections indexed. One of the 4 open questions now has a cited answer.'),
              ('u', 'Create accounts for the 12 students in the file.'),
              ('act', 'Validator', 'Checked 12 rows. 11 are valid. Row 7 repeats an ID.'),
              ('b', 'Create the 11 valid accounts? Reply yes.')],
        lose='It cannot change the knowledge base or the accounts.',
        win='It indexes the document, checks the rows, and creates accounts only after a yes.'),
}
SCEN.update(STAFF)


def chat_vs(deck, key, notes='', over='Side by side'):
    sc = SCEN[key]
    sk = SKINS[sc['skin']]
    s = deck.add(notes=notes or f'Same message, same channel ({sk["name"]}). Left is an illustrative ordinary bot, made up for contrast. Right is what our assistant does: the shaded lines are the agents and tools behind each reply.')
    y0 = hdr(s, sc['title'], f'{over}  ·  {sk["name"]}', size=42)
    WS, G = (640, 1040), 48
    ly, wy = y0 - 10, y0 + 40
    wh = 892 - wy
    for i, (who, items, lab, col) in enumerate((('bot', sc['bot'], 'An ordinary bot', C['red']), ('ours', sc['ours'], 'Our assistant', C['teal']))):
        W = WS[i]
        x = 96 + (0 if i == 0 else WS[0] + G)
        s.pill(x, ly, lab, fill=col, color=C['white'], h=42, size=24)
        if who == 'bot':
            s.text(x + 236, ly + 8, W - 236, MOCK_TAG, size=20, color=C['subtle'], align='r', lh=1.2, fit=False)
        window(s, x, wy, W, wh, sc['skin'], items, who, sc.get('role', 'Assistant'))
        s.text(x, 906, W, sc['lose'] if who == 'bot' else sc['win'], size=25, weight=600, color=C['red'] if who == 'bot' else C['teal_dark'], lh=1.28, h=84, minsize=21)
    return s
