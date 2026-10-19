"""Comparison slides: the same student message to an ordinary bot (illustrative mock) and to our agent (a prototype frame).
The ordinary-bot text is made up for contrast. Every slide says so."""
import os
from PIL import Image
import lib
from lib import C, wrap, text_w
from kit import hdr, auto_crop

MOCK_TAG = 'Illustrative mock. Not a quote from any real bot.'

# Each scenario: frame, what the student writes, what an ordinary bot says, why that bot stops, what our backend does.
SCEN = {
    'j1': dict(
        title='A rule question: a link, or the rule itself',
        frame='j1_3.png', fname='Frame J1.3',
        ask='What documents do I need from the university for my student visa renewal?',
        bot=['For visa information, please visit the International Office page: thales.example/international'],
        why='The bot matches a keyword and sends a link. The student still has to open a PDF and find the rule.',
        ours=[('Retrieves', 'Searches the Student Handbook 2026 and finds section 7.3.'),
              ('Answers', 'Three documents, and an offer to start the official transcript.'),
              ('Cites', 'Handbook 2026, section 7.3, with the source one tap away.')]),
    'j3': dict(
        title='A private record: the token decides, not the message',
        frame='j3_4.png', fname='Frame J3.4',
        ask='What about student 67999999, how much do they owe?',
        bot=['I am not able to access student records. Please log in to the student system.'],
        why='The bot has no link to the student account, so it cannot answer even the student\'s own question.',
        ours=[('Own record', 'The Records agent reads the signed-in student only.'),
              ('The token', 'The student ID comes from the token, never from the message.'),
              ('Audit', 'The refused attempt is written to the audit log.')]),
    'j4': dict(
        title='A booking: from "ask the counter" to a confirmed room',
        frame='j4_4.png', fname='Frame J4.4',
        ask='I need a study room for my group on Thursday afternoon',
        bot=['Sorry, I cannot book rooms.', 'Rooms can be booked at the library counter during opening hours.'],
        why='The bot can talk about rooms but it has no tool that writes a booking.',
        ours=[('Reads', 'The Booking agent reads the free rooms for Thursday afternoon.'),
              ('Asks first', 'Nothing is written until the student says yes.'),
              ('Writes', 'One transaction, an audit record and a reminder on LINE.')]),
    'j5': dict(
        title='A request: a form to download, or a request that is tracked',
        frame='j5_4.png', fname='Frame J5.4',
        ask='I need an official transcript for a job application',
        bot=['To request a transcript, download the form from the Registrar page, fill it in and bring it to the counter.'],
        why='The student does the whole job. Nothing is tracked, so nobody can see the status.',
        ours=[('Applies the rules', '100 THB for each copy. It asks how many and how to collect.'),
              ('Opens a request', 'REQ-2026-0481 after a yes. Four states, from Submitted to Collected.'),
              ('Messages back', 'The student is told on the same channel when the state changes.')]),
    'j8': dict(
        title='A photo: "I cannot read images" or a slip that reaches staff',
        frame='j8_2.png', fname='Frame J8.2',
        ask='I paid my tuition. Here is the slip. [photo]',
        bot=['Sorry, I can only read text messages.', 'Please email your payment slip to finance@thales.example'],
        why='The bot ends the chat and sends the student to email. Staff never see the conversation.',
        ours=[('A fixed reader', 'Checks amount, name, date and duplicate reference. The model never sees the image.'),
              ('A payment check', 'The Request agent creates it in the state waiting.'),
              ('A person decides', 'Staff confirm in the Payments tab. Only then does the balance change.')]),
    'j10': dict(
        title='A next-day question: "which one?" or "the one from yesterday"',
        frame='j10_4.png', fname='Frame J10.4',
        ask='Can I do that one from yesterday?',
        bot=['Sorry, I did not understand. What would you like to know?'],
        why='The bot keeps no memory between sessions, so "that one" means nothing to it.',
        ours=[('Memory', 'Finds the saved topic under student ID 67111411, not the LINE account.'),
              ('The rule again', 'Reads Handbook section 5.4 again for the deadline.'),
              ('The account', 'Deadline not passed, no hold. Offers to start the withdrawal.')]),
    'j11': dict(
        title='Three questions in one message',
        frame='j11_2.png', fname='Frame J11.2',
        ask='I want to plan my graduation. How many credits do I still need, and can I see Dr. Kanda about it?',
        bot=['I can answer one question at a time. Please ask about credits or appointments.'],
        why='One bot, one intent per message. The student has to split the question and start twice.',
        ours=[('Splits', 'The supervisor makes three tasks: credits, the rule and a booking.'),
              ('Three agents', 'Credits 66 of 132. Handbook section 6.2. Two free slots.'),
              ('One answer', 'The student reads one reply, with the Agent Trace beside it.')]),
    'j20': dict(
        title='A situation nobody scripted: a make-up exam',
        frame='j20_1.png', fname='Frame J20.1',
        ask='I was sick on Monday and missed the ICT411 midterm. What can I do?',
        bot=['Sorry, I did not understand. Please contact the Registrar office.'],
        why='No intent was written for this case, so the bot falls back to a stock sentence.',
        ours=[('Finds the rule', 'Handbook 8.2: a medical certificate within three working days.'),
              ('Counts in code', 'A tool, not the model, finds Thursday 22 October as the last day.'),
              ('Opens a request', 'The photo goes to private storage. Staff decide. The student is told.')]),
}


CROPS = {
    'j1_3': (365, 308, 870, 606), 'j3_4': (365, 464, 1080, 650), 'j4_4': (365, 245, 800, 620),
    'j5_4': (149, 240, 560, 625), 'j8_2': (785, 242, 1080, 590), 'j10_4': (520, 225, 920, 600),
    'j11_2': (149, 308, 907, 602), 'j20_1': (520, 278, 920, 600),
}


def vs_crop(name):
    """Tight crop of the chat part of a frame, upscaled 2x so it stays sharp on the slide."""
    key = name.replace('.png', '')
    os.makedirs(os.path.join(lib.IMG, 'crops'), exist_ok=True)
    out = f'crops/vs_{key}.png'
    full = os.path.join(lib.IMG, out)
    src = os.path.join(lib.IMG, name)
    if not os.path.exists(full) or os.path.getmtime(full) < max(os.path.getmtime(src), os.path.getmtime(__file__)):
        im = Image.open(src).crop(CROPS[key])
        im.resize((im.width * 2, im.height * 2), Image.LANCZOS).save(full)
    return out


def chat_mock(s, x, y, w, ask, replies, size=28):
    """Draw a small chat: the student on the right, an ordinary bot on the left. Returns the bottom y."""
    yy = y
    bw = w * 0.86
    lines = wrap(ask, (bw - 48) * 0.975, size, 500)
    tw = min(bw, max(text_w(l, size, 500) for l in lines) + 64)
    hh = len(lines) * size * 1.3 + 32
    s.rect(x + w - tw, yy, tw, hh, fill=C['teal'], r=22)
    s.text(x + w - tw + 24, yy + 16, (tw - 48) / 0.975 + 4, ask, size=size, weight=500, color=C['white'], lh=1.3, fit=False)
    yy += hh + 22
    for rep in replies:
        lines = wrap(rep, (bw - 48) * 0.975, size, 400)
        tw = min(bw, max(text_w(l, size, 400) for l in lines) + 64)
        hh = len(lines) * size * 1.3 + 32
        s.rect(x, yy, tw, hh, fill=C['panel'], stroke=C['border'], r=22)
        s.text(x + 24, yy + 16, (tw - 48) / 0.975 + 4, rep, size=size, color=C['text'], lh=1.3, fit=False)
        yy += hh + 16
    return yy


def versus(deck, key, notes='', over='Side by side'):
    sc = SCEN[key]
    s = deck.add(notes=notes or f'Same message, two bots. Left: an illustrative ordinary bot, made up for contrast. Right: our prototype, {sc["fname"]}.')
    y0 = hdr(s, sc['title'], over, size=48)
    # left: ordinary bot
    lx, lw = 96, 560
    ph = 1000 - y0 + 20
    s.rect(lx, y0, lw, ph - 20, fill=C['bg'], stroke=C['border'], sw=2, r=20)
    s.pill(lx + 28, y0 + 24, 'An ordinary bot', fill=C['red'], color=C['white'], h=46, size=24)
    yy = chat_mock(s, lx + 28, y0 + 96, lw - 56, sc['ask'], sc['bot'])
    yy = max(yy + 18, y0 + 330)
    s.rect(lx + 28, yy, lw - 56, 4, fill=C['red_200'], r=2)
    s.text(lx + 28, yy + 26, lw - 56, sc['why'], size=26, weight=600, color=C['red'], lh=1.3)
    s.text(lx + 28, y0 + ph - 20 - 52, lw - 56, MOCK_TAG, size=20, color=C['subtle'], lh=1.2)
    # right: our agent
    rx = lx + lw + 40
    rw = 1824 - rx
    s.rect(rx, y0, rw, ph - 20, fill=C['teal_tint'], stroke=C['teal_200'], sw=2, r=20)
    s.pill(rx + 28, y0 + 24, f'Our assistant, {sc["fname"]}', fill=C['teal'], color=C['white'], h=46, size=24)
    n0 = len(s.els)
    fr = vs_crop(sc['frame'])
    im = Image.open(os.path.join(lib.IMG, fr))
    ar = im.size[0] / im.size[1]
    top = y0 + 92
    if ar > 1.6:
        iw = min(rw - 56, 440 * ar)
        ih = iw / ar
        s.image(fr, rx + 28, top, iw, ih, fit='contain', r=14, border=C['border'], shadow=True)
        cy = top + ih + 28
        cw = (rw - 56 - 2 * 24) / 3
        for i, (t, b) in enumerate(sc['ours']):
            cx = rx + 28 + i * (cw + 24)
            s.ellipse(cx, cy, 44, 44, fill=C['teal'])
            s.text(cx, cy + 7, 44, str(i + 1), size=24, weight=700, color=C['white'], align='c', lh=1.1)
            ty = s.text(cx + 56, cy + 2, cw - 56, t, size=26, weight=700, color=C['ink'], lh=1.2)
            s.text(cx, max(ty, cy + 54) + 8, cw, b, size=24, color=C['muted'], lh=1.3, h=1000 - 20 - (max(ty, cy + 54) + 8), minsize=20)
    else:
        ih = min(ph - 20 - 92 - 24, 580)
        iw = ih * ar
        s.image(fr, rx + 28, top, iw, ih, fit='contain', r=14, border=C['border'], shadow=True)
        cx = rx + 28 + iw + 36
        cw = 1824 - 28 - cx
        cy = top + 4
        for i, (t, b) in enumerate(sc['ours'], 1):
            cy = s.callout(cx, cy, cw, i, t, b, size=24) + 24
    # centre the right-hand block in its panel
    body = s.els[n0:]
    top_y = min(e['y'] for e in body if e['t'] != 'line')
    bot_y = max(e['y'] + e.get('h', 0) for e in body if e['t'] != 'line')
    delta = ((y0 + (ph - 20) + (y0 + 92)) / 2) - (top_y + bot_y) / 2
    delta = max(0, delta - 10)
    for e in body:
        if e['t'] == 'line':
            e['y1'] += delta
            e['y2'] += delta
        else:
            e['y'] += delta
    return s
