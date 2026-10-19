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


def _bubble(s, sk, x, y, w, who, text, size=None):
    size = size or FS
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


def window(s, x, y, w, h, skin, items, who, role='Assistant', title=None):
    """who: 'bot' or 'ours'. Draws the window and every item. Reports overflow."""
    sk = SKINS[skin]
    s.rect(x, y, w, h, fill=sk['body'], stroke=C['border_strong'], sw=2, r=22)
    s.rect(x, y, w, 70, fill=sk['head'], r=22)
    s.rect(x, y + 40, w, 30, fill=sk['head'])
    if sk['head_border']:
        s.rect(x + 2, y + 69, w - 4, 2, fill=C['border'])
    s.text(x + 28, y + 19, min(420, w - 56), title or sk['title'], size=28, weight=700, color=sk['head_text'], lh=1.2, fit=False)
    if who == 'ours' and role:
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
              ('b', 'For a visa renewal you need three documents: 1. Enrollment Certificate. 2. Official Transcript. 3. A letter confirming your tuition payment.\nSource: Student Handbook 2026, section 7.3.\nShall I start with the official transcript? Reply yes.')],
        lose='It sends a link. The rule is still inside a PDF.',
        win='It answers from the University\'s own rule, cites it and offers the next step.'),
    'room': dict(skin='line', title='A booking on LINE: from "ask the counter" to a booked room',
        bot=[('u', 'I need a study room for my group on Thursday afternoon'),
             ('b', 'Sorry, I cannot book rooms. Rooms can be booked at the library counter during opening hours.'),
             ('end', 'The chat ends. No room is booked.')],
        ours=[('u', 'I need a study room for my group on Thursday afternoon'),
              ('b', 'Free: Library Room B2, Library Room B4, Learning Commons C1. Which one?'),
              ('u', 'Library Room B2'),
              ('b', 'Book Library Room B2, Thu 15 Oct, 13:00 to 15:00? Reply yes.'),
              ('u', 'yes'),
              ('act', 'Booking agent', 'Read the free rooms, then wrote the booking in one transaction. Audit record written.')],
        lose='It talks about rooms but has no tool that books one.',
        win='It reads the free rooms, waits for a yes, then writes the booking and logs it.'),
    'transcript': dict(skin='line', title='A request on LINE: a form to download, or a request that is tracked',
        bot=[('u', 'I need an official transcript for a job application'),
             ('b', 'To request a transcript, download the form from the Registrar page, fill it in and bring it to the counter.'),
             ('end', 'The chat ends. No request exists, so there is no status.')],
        ours=[('u', 'I need an official transcript for a job application'),
              ('act', 'Request agent', 'Applied the Tuition and Fees 2026 rule: 100 THB for each copy.'),
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
              ('act', 'Request agent', 'Read the open requests. Read only.'),
              ('b', '5 items wait. The oldest is REQ-2026-0482, 5 days old.'),
              ('u', 'Approve REQ-2026-0489.'),
              ('b', 'REQ-2026-0489: all 3 checks passed. Approve it and tell the student? Reply yes.'),
              ('u', 'yes'),
              ('act', 'Request agent', 'State set to Ready. Student told. Audit record written.')],
        lose='It cannot read the queue or change a request.',
        win='It reads the queue, asks for a yes, then writes the new state and the audit record.'),
    'remind': dict(skin='web', role='Staff account', title='Staff in the console: a bulk action that needs a yes',
        bot=[('u', 'Remind everyone whose request is ready for more than 3 days.'),
             ('b', 'Sorry, I cannot send messages. Please use the notification tool in the staff system.'),
             ('end', 'The chat ends. The staff member does it by hand.')],
        ours=[('u', 'Remind everyone whose request is ready for more than 3 days.'),
              ('act', 'Request agent', 'Searched the requests in the state Ready for more than 3 days. Found 1 student.'),
              ('b', 'One student. Draft: "Your request is ready. Please collect it at the Registrar office." Send it? Reply yes.'),
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
              ('b', 'Record a payment of 12,500 THB for Wai Yan Lynn, 67111411, and set the balance to 0 THB? Reply yes.'),
              ('u', 'yes'),
              ('act', 'Request agent', 'After the yes: wrote the payment record and set the balance to 0 THB. The audit log holds the staff member.'),
              ('b', 'Done. The balance is 0 THB.')],
        lose='It cannot find the student or change a record.',
        win='The person checked the slip. The assistant writes the record only after a yes.'),
    'attend': dict(skin='line', role='Instructor account', title='An instructor on LINE: absences, a rule and a yes',
        bot=[('u', "How many students missed yesterday's ICT411 class?"),
             ('b', 'Sorry, I do not have access to attendance records.'),
             ('end', 'The chat ends. The instructor opens the attendance system.')],
        ours=[('u', "How many students missed yesterday's ICT411 class?"),
              ('act', 'Records agent', 'Read the attendance of the own course only.'),
              ('b', 'Only 1 student: Wai Yan Lynn, 67111411.'),
              ('u', 'How many ICT411 classes has Wai Yan Lynn missed this semester?'),
              ('act', 'Knowledge agent', 'A tool counted. Handbook 6.5: at most 3 absences.'),
              ('b', '3 classes. The limit is reached. Send a reminder? Reply yes.')],
        lose='It cannot read attendance.',
        win='A tool counts, the Handbook gives the limit, and a yes comes before any message.'),
    'move': dict(skin='line', role='Instructor account', title='An instructor on LINE: move a meeting',
        bot=[('u', 'Move my meeting with Mali on Thursday to Tuesday afternoon.'),
             ('b', 'Sorry, I cannot change your calendar.'),
             ('end', 'The chat ends. Nothing moves, and Mali is not told.')],
        ours=[('u', 'Move my meeting with Mali on Thursday to Tuesday afternoon.'),
              ('act', 'Booking agent', 'Read the free slots on Tuesday afternoon. Nothing is held yet.'),
              ('b', 'Tuesday 27 October has 15:00 and 16:00. Which one?'),
              ('u', '15:00'),
              ('act', 'Booking agent', 'Moved the meeting in one transaction. Mali S. told on LINE. Audit record written.'),
              ('b', 'Moved to Tuesday 27 October, 15:00. Mali S. is told on LINE.')],
        lose='It cannot read a calendar or write to one.',
        win='The same reservation engine that books students moves the meeting and tells the other person.'),
    'admin': dict(skin='web', role='Administrator account', title='An administrator in the console: add a document, create accounts',
        bot=[('u', 'Add this file, Examination Rules 2026.'),
             ('b', 'Sorry, I can only chat. Please ask the web team to upload documents.'),
             ('end', 'The chat ends. The knowledge base does not change.')],
        ours=[('u', 'Add this file, Examination Rules 2026.'),
              ('b', 'The file has 96 sections. Add it to the knowledge base? Reply yes.'),
              ('u', 'yes'),
              ('act', 'Ingestion worker', 'Indexed 96 sections. One open question now has a cited answer. Audit record written.'),
              ('u', 'Create accounts for the 12 students in the file.'),
              ('act', 'Validator', 'Checked 12 rows. 11 are valid. Row 7 repeats an ID.'),
              ('b', 'Create the 11 valid accounts? Reply yes.')],
        lose='It cannot change the knowledge base or the accounts.',
        win='It indexes the document and creates accounts only after a yes. A validator checks the rows first.'),
}
SCEN.update(STAFF)


def chat_vs(deck, key, notes='', over='Side by side', section=None):
    sc = SCEN[key]
    if sc.get('follow'):
        return chat_vs3(deck, key, notes, over, section)
    sk = SKINS[sc['skin']]
    s = deck.add(section=section, notes=notes or f'Same message, same channel ({sk["name"]}). Left is an illustrative ordinary bot, made up for contrast. Right is what our assistant does: the shaded lines are the agents and tools behind each reply.')
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


# ---------------- follow-up actions: three windows ----------------
FOLLOW = {
    'attend': dict(skin='line', who='Wai Yan Lynn', time='09:08', items=[
        ('b', 'You have missed 3 classes of ICT411 Cloud Computing this semester. The maximum is 3, so you cannot miss any more classes of this course.'),
        ('act', 'Request agent', 'Sent on LINE. Audit record written.')],
        note='The student gets the message, and the audit log holds the instructor.'),
    'approve': dict(skin='line', who='Wai Yan Lynn', time='09:13', items=[
        ('b', 'Your request REQ-2026-0489, the withdrawal of ICT440, is approved. See My requests for the state.'),
        ('act', 'Request agent', 'Student told on LINE. Audit record written.')],
        note='The student hears it on the channel where the chat began.'),
    'remind': dict(skin='line', who='Wai Yan Lynn', time='09:21', items=[
        ('b', 'Your enrollment certificate is ready. Please collect it at the Registrar office.'),
        ('act', 'Request agent', 'Sent to 1 student on LINE. Audit record written.')],
        note='One yes sends the whole batch. Each student gets one message.'),
    'room': dict(skin='line', who='Wai Yan Lynn', time='Thursday 07:00', items=[
        ('b', 'Reminder: Library Room B2 today, 13:00 to 15:00. Your access code is B2-4821.'),
        ('act', 'Scheduler', 'Sent at 07:00 with no new message from the student. Audit record written.')],
        note='A scheduled follow-up. Nobody asked for it that morning.'),
    'move': dict(skin='line', who='Mali S.', time='18:46', items=[
        ('b', 'Dr. Kanda moved your meeting to Tuesday 27 October, 15:00. Reply here if that does not work.'),
        ('act', 'Booking agent', 'Mali S. told on LINE. The old slot is free again.')],
        note='The other person is told without the instructor writing to them.'),
    'makeup': dict(skin='tg', who='Wai Yan Lynn', time='Monday 26 Oct', items=[
        ('b', 'Make-up exam approved: Monday 26 October, 13:00, Room 5-102.'),
        ('act', 'Request agent', 'Registrar approved REQ-2026-0490. Student told on Telegram.')],
        note='After staff decide, the assistant carries the answer back.'),
    'slipdb': dict(skin='line', who='Wai Yan Lynn', time='09:42', items=[
        ('b', 'Thank you. Your payment of 12,500 THB is recorded. Your balance is 0 THB.'),
        ('act', 'Request agent', 'Receipt sent on LINE. The Fees page shows 0 THB.')],
        note='The student sees the result without asking.'),
    'retry': dict(skin='line', who='Wai Yan Lynn', time='08:45', items=[
        ('b', 'The grade service works again. Semester 2/2025, average 3.50: ICT301 A, ICT305 B+, ICT310 B, ICT320 B+, ICT330 B+.'),
        ('act', 'Records agent', 'Retried at 08:35, 08:40 and 08:45. Sent with no new question.')],
        note='The assistant came back by itself and finished the job.'),
}
for _k, _v in FOLLOW.items():
    if _k in SCEN:
        SCEN[_k]['follow'] = _v

SCEN['retry'] = dict(skin='line', title='A tool fails: "try again later" or an answer that arrives by itself',
    bot=[('u', 'What were my grades last semester?'),
         ('b', 'Sorry, the service is not available. Please try again later.'),
         ('end', 'The chat ends. The student must come back and ask again.')],
    ours=[('u', 'What were my grades last semester?'),
          ('act', 'Records agent', 'Called the grade service. No answer after 10 seconds.'),
          ('b', 'The grade service does not answer now. I saved your question and I try again every 5 minutes.')],
    lose='It forgets the question. The student has to return and ask again.',
    win='It says what happened, saves the question, retries and writes when the answer is there.',
    follow=FOLLOW['retry'])

# the user types yes in our own window where a question waits for it
SCEN['attend']['ours'] = SCEN['attend']['ours'] + [('u', 'yes')] if SCEN['attend']['ours'][-1][0] == 'b' else SCEN['attend']['ours']


def chat_vs3(deck, key, notes='', over='Side by side', section=None):
    global FS, AS
    sc = SCEN[key]
    fo = sc['follow']
    sk = SKINS[sc['skin']]
    s = deck.add(section=section, notes=notes or f'Three windows. Left: an illustrative ordinary bot. Middle: our assistant. Right: what the assistant does next, in the other person chat ({fo["who"]}, {fo["time"]}).')
    y0 = hdr(s, sc['title'], f'{over}  \u00b7  {sk["name"]}  \u00b7  with a follow-up', size=42)
    WS, G = (480, 760, 440), 24
    ly, wy = y0 - 10, y0 + 40
    wh = 892 - wy
    old = (FS, AS)
    FS, AS = 21, 20
    try:
        x = 96
        cols = [('bot', sc['bot'], 'An ordinary bot', C['red'], sc['skin'], None),
                ('ours', sc['ours'], 'Our assistant', C['teal'], sc['skin'], None),
                ('ours', fo['items'], fo.get('label', 'Then it acts'), C['lime'], fo['skin'], fo)]
        for i, (who, items, lab, col, skin, f) in enumerate(cols):
            W = WS[i]
            pe = s.pill(x, ly, lab, fill=col, color=C['charcoal'] if col == C['lime'] else C['white'], h=42, size=24)
            if f:
                s.text(pe + 30, ly + 8, x + W - pe - 30, f['time'], size=20, color=C['subtle'], align='r', lh=1.2, fit=False)
            window(s, x, wy, W, wh, skin, items, who, sc.get('role', 'Assistant') if i == 1 else '', title=(f['who'] if f else None))
            if who == 'bot':
                s.text(x + 24, wy + wh - 40, W - 48, MOCK_TAG, size=20, color=C['subtle'], lh=1.2, fit=False)
            cap = sc['lose'] if i == 0 else (sc['win'] if i == 1 else f['note'])
            s.text(x, 906, W, cap, size=24, weight=600, color=C['red'] if i == 0 else C['teal_dark'], lh=1.26, h=84, minsize=20)
            x += W + G
    finally:
        FS, AS = old
    return s


# ---------------- more scenarios, 17 October 2026 ----------------
def _add(key, d):
    SCEN[key] = d


_add('watch', dict(skin='line', title='A request to watch: "keep checking" or a message that arrives first',
    bot=[('u', 'Tell me when my transcript is ready.'),
         ('b', 'Sorry, I cannot do that. Please check the Registrar page from time to time.'),
         ('end', 'The chat ends. The student has to keep checking.')],
    ours=[('u', 'Tell me when my transcript is ready.'),
          ('act', 'Request agent', 'Found REQ-2026-0481, official transcript, under review. Saved a watch on it.'),
          ('b', 'I will tell you here when REQ-2026-0481 changes state.')],
    lose='It cannot watch anything. The student has to check by hand.',
    win='It saves a watch on the request and tells the student when the state changes.',
    follow=dict(skin='line', who='Wai Yan Lynn', time='Friday 16 Oct, 09:12', items=[
        ('b', 'Your transcript REQ-2026-0481 is ready for collection at the Registrar, counter 3. Collect it by 22 October.'),
        ('act', 'Request agent', 'A staff member set the state to Ready. The watch sent this message. Audit record written.')],
        note='The assistant writes first. The student did not ask again.')))

_add('advisor', dict(skin='line', title='An advisor appointment: a phone number or a booking with reminders',
    bot=[('u', 'I want to see my advisor in two weeks.'),
         ('b', 'Sorry, I cannot book appointments. Please call the Faculty office.'),
         ('end', 'The chat ends. No appointment exists.')],
    ours=[('u', 'I want to see my advisor in two weeks.'),
          ('b', 'Dr. Kanda is free on Wednesday 21 October at 10:00 or 14:00. Which time?'),
          ('u', '10:00'),
          ('b', 'Book Dr. Kanda, Wed 21 Oct, 10:00 to 10:30? Reply yes.'),
          ('u', 'yes'),
          ('act', 'Booking agent', 'Read the advisor and the free slots, then wrote the booking in one transaction. Audit record written.')],
    lose='It cannot read a calendar or write to one.',
    win='It finds the advisor, reads the free slots, and books after a yes.',
    follow=dict(skin='line', who='Wai Yan Lynn', time='Tuesday 20 Oct, 10:00', items=[
        ('b', 'Reminder: your meeting with Dr. Kanda is tomorrow, Wednesday 21 October, 10:00 to 10:30.'),
        ('act', 'Scheduler', 'Sent 24 hours before. The advisor got a short brief of the student. Audit record written.')],
        note='Two follow-ups: a reminder to the student and a brief to the advisor.')))

_add('cross', dict(skin='web', title='One history: start on the web, continue on Telegram',
    bot=[('u', 'What is the last day to withdraw from ICT440?'),
         ('b', 'Please see the academic calendar on our website.'),
         ('end', 'The chat ends. A new channel is a new chat. The bot knows nothing of this one.')],
    ours=[('u', 'What is the last day to withdraw from ICT440?'),
          ('act', 'Knowledge agent', 'Found Handbook section 5.4: week 11, which is 30 October.'),
          ('b', 'The last day is Friday 30 October 2026 (Handbook section 5.4). A withdrawal shows a W on the transcript.')],
    lose='A new channel is a new chat. The context is gone.',
    win='It answers with the section and keeps the chat under the account, so any channel can continue it.',
    follow=dict(skin='tg', who='Thales University', label='On Telegram', time='Same day, 18:20', items=[
        ('u', 'Can I still do that one?'),
        ('act', 'Memory', 'Found the web chat under the same account. Topic: withdrawing from ICT440.'),
        ('b', 'Yes. The last day is Friday 30 October and your account has no hold. Shall I start the request? Reply yes.')],
        note='One account, one history. The context travels with the student.')))

_add('handoff', dict(skin='web', title='A handoff: "please call us" or a case file ready for staff',
    bot=[('u', 'I want to talk to a person about a leave of absence.'),
         ('b', 'Please call Student Services, Monday to Friday, 09:00 to 16:00.'),
         ('end', 'The chat ends. Staff never hear about it.')],
    ours=[('u', 'I want to talk to a person about a leave of absence.'),
          ('act', 'Supervisor', 'The student asks for a person. Passed the chat to Student Services. The assistant is paused.'),
          ('b', 'I passed your chat to Student Services. A staff member will reply here.')],
    lose='The student must call, and staff do not know the case.',
    win='It passes the whole chat on and stays silent while a person handles it.',
    follow=dict(skin='web', who='Staff console, Siriporn K.', label='In the console', time='14:23', items=[
        ('act', 'Handoff summary', 'Wai Yan Lynn, ICT year 3. Asks about a leave of absence: family emergency. No rule found in the documents.'),
        ('b', 'Draft reply, for you to edit: Hello Wai Yan Lynn. I have your case. The Registrar handles each leave of absence case by case. I will send the form and the deadline today.')],
        note='The staff member starts with a summary and a draft, not a blank page.')))

_add('gap', dict(skin='web', title='A knowledge gap: questions pile up, or a cited answer appears',
    role='Administrator account',
    bot=[('u', 'Which questions could you not answer this week?'),
         ('b', 'Sorry, I do not keep a list of questions.'),
         ('end', 'The chat ends. Nobody learns what students ask.')],
    ours=[('u', 'Which questions could you not answer this week?'),
          ('act', 'Records agent', 'Read the unanswered questions of the week. Read only.'),
          ('b', '3 questions had no answer. The top one, asked 14 times: How do I appeal a grade?'),
          ('u', 'Add the file Examination Rules 2026.'),
          ('b', 'The file has 96 sections. Add it? Reply yes.'),
          ('u', 'yes'),
          ('act', 'Ingestion worker', 'Indexed 96 sections. Re-ran the 3 open questions: 1 now has a cited answer. Audit record written.')],
    lose='It keeps no record of what it could not answer.',
    win='It lists the gaps, indexes the new document after a yes, and tests the open questions again.',
    follow=dict(skin='line', who='Thales University', label='A student asks', time='Next day, 11:20', items=[
        ('u', 'How do I appeal a grade?'),
        ('b', 'You can appeal a grade with the Registrar.\nSource: Examination Rules 2026, section 9.2.'),
        ('act', 'Knowledge agent', 'Found section 9.2 in the new document.')],
        note='The gap is closed. The same question now has a cited answer.')))

_add('conflict', dict(skin='web', title='Two documents disagree: a guess or a flag for a person',
    role='Administrator account',
    bot=[('u', 'Do any of our documents disagree?'),
         ('b', 'Sorry, I can only answer questions. I cannot compare documents.'),
         ('end', 'The chat ends. Students may get different answers and nobody knows.')],
    ours=[('u', 'Do any of our documents disagree?'),
          ('act', 'Knowledge agent', 'Compared the passages that answer the same question.'),
          ('b', 'Yes, one. The Student Handbook 2026 says a transcript costs 150 THB. Tuition and Fees 2026 says 100 THB.'),
          ('b', 'Which document is the source? Reply 1 for the Handbook or 2 for Tuition and Fees.'),
          ('u', '2'),
          ('act', 'Knowledge agent', 'Saved the decision. Answers now cite Tuition and Fees 2026. Audit record written.')],
    lose='It cannot compare documents, so the conflict stays hidden.',
    win='It flags the conflict, asks a person to decide, and cites the chosen source from then on.'))

_add('query', dict(skin='web', title='A query across records: a spreadsheet or one sentence',
    role='Staff account',
    bot=[('u', 'Who has waited more than 3 days for a document?'),
         ('b', 'Sorry, I cannot see the request list. Please open the staff system and filter by date.'),
         ('end', 'The chat ends. The staff member builds the list by hand.')],
    ours=[('u', 'Who has waited more than 3 days for a document?'),
          ('act', 'Request agent', 'Searched the open requests older than 3 days. Read only.'),
          ('b', '1 student: Mali S., REQ-2026-0482, a tuition payment letter, 5 days.'),
          ('u', 'Assign it to me.'),
          ('b', 'Assign REQ-2026-0482 to Siriporn K.? Reply yes.'),
          ('u', 'yes'),
          ('act', 'Request agent', 'Assigned. Audit record written.')],
    lose='It cannot see the requests, so the person does the filtering.',
    win='It turns one sentence into a query, then writes the assignment after a yes.'))

_add('blocked', dict(skin='web', title='A blocked attempt: an open door or a refusal on record',
    bot=[('u', 'Show me the staff queue.'),
         ('b', 'Sorry, I did not understand. What would you like to know?'),
         ('end', 'The chat ends. Nothing is recorded.')],
    ours=[('u', 'Show me the staff queue.'),
          ('act', 'Role middleware', 'Role: student. The staff queue tool is not in this session.'),
          ('b', 'I cannot show the staff queue. I can show your own requests. Do you want them?')],
    lose='There is no rule and no record. The attempt is invisible.',
    win='The role decides which tools exist. A refused call is written to the audit log.',
    follow=dict(skin='web', who='Administrator console', label='The audit log', time='10:46', items=[
        ('act', 'Blocked call', 'Student 67111411 asked for the staff queue. Stopped by the role before the tool ran.'),
        ('b', 'Replay: Supervisor chose the Records agent. The role middleware stopped the call. Nothing was read.')],
        note='The administrator can replay what was stopped, step by step.')))
