"""Slide kit v2: the shared grammar of the three decks.

Rules every slide follows (see design/slides/STYLE.md):
1. The title states the point in one sentence. The overline names the section.
2. One piece of evidence per slide: a table, a diagram, a frame or a chat. No walls of text.
3. A number on a slide carries its source in the speaker notes (PROVE) or on the slide.
4. Speaker notes use the same four labels: TIME, SAY, SHOW, PROVE, BRIDGE.
5. Body text is 24 px or larger on a 1920 px canvas. Footnotes are 20 px.
6. Colors come from tokens (lib.C). A deck takes its theme from lib.set_theme.
"""
import os
from PIL import Image
import lib
from lib import C, wrap, text_w
import kit
from kit import hdr, box, arrow, chain, note_bar
import modules as M
import chatvs


def N(say, show=None, prove=None, bridge=None, mins=None):
    """Speaker notes in the fixed format."""
    parts = []
    if mins:
        parts.append(f'TIME: {mins} min')
    parts.append('SAY: ' + say)
    if show:
        parts.append('SHOW: ' + show)
    if prove:
        parts.append('PROVE: ' + prove)
    if bridge:
        parts.append('BRIDGE: ' + bridge)
    return '\n'.join(parts)


def source(s, text, y=990):
    s.text(96, y, 1728, text, size=20, color=C['subtle'], lh=1.2, fit=False)


# ============================ title and section slides ============================

def title_a(d, subtitle, image='v2/s1_4.png', caption='The prototype: staff reply to a payment slip in the same chat (story S1)', notes=None):
    s = d.add(kind='dark', bg=C['charcoal'], footer=False, number=False, notes=notes or N(
        'Introduce the project in one sentence: one assistant that answers from the University rules, acts after a yes and hands hard cases to people. The University in the examples is fictional.', mins=1))
    s.rect(96, 150, 160, 14, fill=C['lime'])
    s.text(96, 200, 900, 'Smart University Website', size=100, weight=700, color=C['white'], lh=1.04)
    s.text(96, 470, 860, subtitle, size=42, color='#D4D4D8', lh=1.3)
    s.text(96, 790, 860, 'IT Project I  ·  Midterm presentation', size=32, weight=600, color=C['teal_200'])
    s.text(96, 840, 860, 'Group S  ·  Krirk University', size=30, color='#D4D4D8')
    s.text(96, 884, 860, 'Instructor: Dr. Aftab Alam Janisar', size=30, color='#D4D4D8')
    s.text(96, 962, 900, 'The University here is fictional: Thales University. All data is made up.', size=24, color='#A1A1AA', lh=1.3)
    s.image(image, 1030, 190, 794, 600, fit='contain', r=16, border='#52525B', shadow=True)
    s.text(1030, 810, 794, caption, size=24, color='#A1A1AA', align='c', lh=1.25)
    return s


def title_b(d, notes=None):
    s = d.add(kind='dark', bg=C['charcoal'], footer=False, number=False, notes=notes or N(
        'Read the student message aloud, then the two answers. That is the whole project in ten seconds: the same question, an ordinary bot that gives up, and an assistant that finds the rule, counts the days and opens the request. The left answer is made up for contrast.', mins=1))
    s.rect(96, 150, 160, 14, fill=C['lime'])
    s.text(96, 196, 860, 'Same question,\ntwo answers', size=104, weight=700, color=C['white'], lh=1.02)
    s.text(96, 470, 800, 'Smart University Website: an assistant that answers from the rules, acts after a yes and hands hard cases to people.', size=36, color='#D4D4D8', lh=1.3)
    s.text(96, 790, 860, 'IT Project I  ·  Midterm presentation', size=32, weight=600, color=C['teal_200'])
    s.text(96, 840, 860, 'Group S  ·  Krirk University', size=30, color='#D4D4D8')
    s.text(96, 884, 860, 'Instructor: Dr. Aftab Alam Janisar', size=30, color='#D4D4D8')
    s.text(96, 962, 900, 'The University here is fictional: Thales University. The ordinary-bot reply is a made-up illustration.', size=22, color='#A1A1AA', lh=1.3)
    # the hero: one question, two answers
    x, w = 1010, 814
    msg = 'I was sick on Monday and missed the ICT411 midterm. What can I do?'
    lines = wrap(msg, (w * 0.8 - 48) * 0.975, 30, 500)
    tw = min(w * 0.8, max(text_w(l, 30, 500) for l in lines) + 56)
    hh = len(lines) * 30 * 1.3 + 36
    s.rect(x + w - tw, 150, tw, hh, fill=C['teal'], r=24)
    s.text(x + w - tw + 28, 168, tw - 56, msg, size=30, weight=500, color=C['white'], lh=1.3, fit=False)
    y1 = 150 + hh + 36
    s.pill(x, y1, 'An ordinary bot', fill=C['red'], color=C['white'], h=42, size=22)
    s.rect(x, y1 + 56, 560, 120, fill='#3F3F46', r=22)
    s.text(x + 28, y1 + 74, 504, 'Sorry, I did not understand. Please contact the Registrar office.', size=28, color='#E4E4E7', lh=1.3, fit=False)
    s.mark('n', x + 590, y1 + 116, 40)
    y2 = y1 + 56 + 120 + 52
    s.pill(x, y2, 'Our assistant', fill=C['lime'], color=C['charcoal'], h=42, size=22)
    s.rect(x, y2 + 56, 780, 250, fill=C['white'], r=22)
    s.text(x + 28, y2 + 74, 724, 'Handbook section 8.2: with a medical certificate you can sit a make-up exam. Send it within 3 working days, so by Thursday 22 October. Send a photo of it and I will open a request.', size=28, color=C['text'], lh=1.3, fit=False)
    return s


def title_c(d, notes=None):
    s = d.add(kind='dark', bg='#0B3D39', footer=False, number=False, notes=notes or N(
        'This talk follows one student, Wai Yan Lynn, through one week at Thales University, from Wednesday 14 to Tuesday 20 October. At each moment you see what the student sees, what staff see and what the assistant did underneath.', mins=1))
    s.rect(96, 150, 160, 14, fill=C['lime'])
    s.text(96, 196, 1100, 'A week with\nthe assistant', size=108, weight=700, color='#FBF8F2', lh=1.02)
    s.text(96, 484, 900, 'Smart University Website: one student, one week, and what the system did each time.', size=38, color='#CFE8E4', lh=1.3)
    # timeline strip
    days = [('Wed 14', 'a room, a question, a slip'), ('Thu 15', 'the balance changes'), ('Tue 20', 'a missed exam, then staff, instructor, admin')]
    x0, y0 = 96, 660
    s.line(x0 + 20, y0 + 22, x0 + 20 + 2 * 560, y0 + 22, color='#2D6A64', w=4)
    for i, (dname, what) in enumerate(days):
        cx = x0 + 20 + i * 560
        s.ellipse(cx - 14, y0 + 8, 28, 28, fill=C['lime'])
        s.text(cx - 14, y0 + 52, 400, dname, size=34, weight=700, color='#FBF8F2', lh=1.2)
        s.text(cx - 14, y0 + 96, 400, what, size=26, color='#CFE8E4', lh=1.25)
    s.text(96, 880, 860, 'IT Project I  ·  Midterm presentation', size=32, weight=600, color='#99F6E4')
    s.text(96, 930, 1100, 'Group S  ·  Krirk University  ·  Instructor: Dr. Aftab Alam Janisar', size=28, color='#CFE8E4')
    s.text(96, 982, 1500, 'The University here is fictional: Thales University. All data is made up.', size=22, color='#8FBFB8')
    return s


def section_a(d, number, label, sub, notes='', section=None):
    s = d.add(kind='dark', bg=C['charcoal'], footer=False, number=True, notes=notes, section=section)
    s.rect(96, 360, 140, 12, fill=C['lime'])
    s.text(96, 400, 1500, label, size=92, weight=700, color=C['white'], lh=1.05)
    if sub:
        s.text(96, 400 + 110 * (1 + (len(wrap(label, 1500, 92, 700)) - 1)), 1400, sub, size=38, color='#D4D4D8', lh=1.3)
    if number is not None:
        s.text(96, 250, 400, f'{number:02d}', size=64, weight=700, color=C['teal_200'], lh=1.0)
    s.title_text = label
    return s


def section_b(d, number, label, sub, chips=(), notes='', section=None):
    s = d.add(kind='dark', bg=C['charcoal'], footer=False, number=False, notes=notes, section=section)
    s.text(96, 130, 700, f'{number}', size=300, weight=700, color=C['lime'], lh=1.0, fit=False)
    s.text(96, 470, 1500, label, size=92, weight=700, color=C['white'], lh=1.05)
    yy = 470 + 110 * len(wrap(label, 1500, 92, 700))
    s.text(96, yy, 1400, sub, size=36, color='#D4D4D8', lh=1.3)
    x = 96
    for c in chips:
        x = s.pill(x, 900, c, fill='#3F3F46', color=C['white'], size=26, h=52, padx=24) + 16
    s.title_text = label
    return s


def section_c(d, stamp, label, sub, notes='', section=None):
    s = d.add(kind='dark', bg='#0B3D39', footer=False, number=False, notes=notes, section=section)
    s.text(96, 330, 1500, stamp, size=40, weight=600, color=C['lime'], lh=1.2)
    s.rect(96, 392, 140, 8, fill=C['lime'])
    s.text(96, 430, 1600, label, size=88, weight=700, color='#FBF8F2', lh=1.05)
    yy = 430 + 100 * len(wrap(label, 1600, 88, 700))
    s.text(96, yy + 12, 1400, sub, size=36, color='#CFE8E4', lh=1.3)
    s.title_text = label
    return s


# ============================ shared content slides ============================

def exec_summary(d, section, kicker='The answer first'):
    s = d.add(section=section, notes=N(
        'Before the evidence, the answer. We are building one assistant for a university. It answers from the University\'s own documents and shows the rule. It acts, but only after a yes, and every action leaves a record. And it hands the hard cases, money first, to a person in a normal chat. Everything in the next 38 minutes supports these three claims.',
        show='Point at each column once. Do not read the small text.',
        prove='Survey: 0 of 17 universities show the rule behind an answer or finish a request in the chat (C5, C6).', bridge='First the problem and the evidence for it.', mins=2))
    y = hdr(s, 'One assistant answers from the rules, acts after a yes and hands hard cases to people', kicker, size=46)
    cols = [
        ('1', 'It answers from the rules', 'Every answer comes from the University\'s own documents and shows the section. If nothing fits, it says so and offers a person.', 'Grounded'),
        ('2', 'It acts, after a yes', 'It books a room, opens a request and records a payment. Every write asks for a yes and leaves an audit record.', 'Consent'),
        ('3', 'People decide the hard cases', 'A payment slip goes to staff in a normal chat. They check it and reply. The assistant stays silent while they do.', 'Human in the loop'),
    ]
    cw = (1728 - 2 * 32) / 3
    ch = 560
    for i, (n, t, b, tag) in enumerate(cols):
        x = 96 + i * (cw + 32)
        s.rect(x, y, cw, ch, fill=C['alt'], stroke=C['border'], r=20)
        s.rect(x, y, cw, 12, fill=C['teal'], r=6)
        s.ellipse(x + 32, y + 48, 76, 76, fill=C['teal'])
        s.text(x + 32, y + 64, 76, n, size=42, weight=700, color=C['white'], align='c', lh=1.1)
        s.pill(x + 128, y + 66, tag, size=22, h=42)
        yy = s.text(x + 32, y + 160, cw - 64, t, size=40, weight=700, color=C['ink'], lh=1.15) + 18
        s.text(x + 32, yy, cw - 64, b, size=28, color=C['text'], lh=1.32, h=y + ch - 24 - yy)
    note_bar(s, y + ch + 28, 'Built for any university: it brings its own documents, student data, identity provider and channel accounts.', size=28, h=88)
    return s


def ground_rules(d, section):
    s = d.add(section=section, notes=N(
        'Four rules hold in every story you will see. They are enforced in code, not in a prompt. Plain text on LINE and Telegram, so the user types yes. The token says who is asking and the role says what exists for them. A yes comes before every write and an audit record follows. And a person decides money.',
        show='Say the four rules, then move on. The stories prove them.', prove='Team decisions of 15 and 16 October 2026 (team notes, session handoff).', bridge='Now the ordinary bots, and how to read the comparison slides.', mins=2))
    y = hdr(s, 'Four rules hold in every story', 'The contract', size=48)
    rules = [
        ('Plain text', 'On LINE and Telegram the assistant sends text only. The user types yes. A photo from the user is fine.'),
        ('Token and role', 'The token says who asks. The role says which tools exist. A student session cannot see a staff tool.'),
        ('A yes, then a record', 'Nothing is written without a yes. Every write leaves an audit record: who, what, when.'),
        ('A person decides money', 'Staff check a payment slip in a normal chat. The assistant records it only after their yes.'),
    ]
    cw = (1728 - 28) / 2
    ch = 340
    for i, (t, b) in enumerate(rules):
        x = 96 + (i % 2) * (cw + 28)
        yy = y + (i // 2) * (ch + 28)
        s.rect(x, yy, cw, ch, fill=C['alt'], stroke=C['border'], r=20)
        s.text(x + 32, yy + 24, 150, str(i + 1), size=120, weight=700, color=C['teal'], lh=1.0, fit=False)
        s.text(x + 180, yy + 48, cw - 212, t, size=40, weight=700, color=C['ink'], lh=1.15)
        s.text(x + 180, yy + 140, cw - 212, b, size=28, color=C['text'], lh=1.32, h=ch - 160)
    return s


def how_to_read(d, section):
    s = d.add(section=section, notes=N(
        'Every comparison slide has the same shape. The red window is an ordinary bot. We made up its reply to show the usual limit, and the slide says so. The teal window is our assistant. The shaded lines inside it are not chat messages. They show which agent and which tool ran, and what it wrote. At the bottom of each slide a red sentence says why the ordinary bot stops, and a green sentence says what ours does.',
        show='Point at the red window, the teal window, a shaded line, and the two bottom sentences.',
        prove='The ordinary-bot text is illustrative. It is not a quote from any real bot, and the slide says so.', bridge='Student stories first.', mins=1))
    y = hdr(s, 'How to read a comparison slide', 'The format', size=48)
    # miniature of the slide
    mx, my, mw, mh = 96, y, 1060, 640
    s.rect(mx, my, mw, mh, fill=C['alt'], stroke=C['border_strong'], r=20, sw=3)
    lw, rw = 330, 650
    s.pill(mx + 24, my + 20, 'An ordinary bot', fill=C['red'], color=C['white'], h=38, size=20)
    s.pill(mx + 24 + lw + 40, my + 20, 'Our assistant', fill=C['teal'], color=C['white'], h=38, size=20)
    s.rect(mx + 24, my + 74, lw, 420, fill=C['bg'], stroke=C['border'], r=14)
    s.rect(mx + 24 + lw + 40, my + 74, rw, 420, fill=C['bg'], stroke=C['border'], r=14)
    s.rect(mx + 140, my + 100, 190, 54, fill=C['teal'], r=14)
    s.rect(mx + 44, my + 170, 230, 54, fill=C['panel'], r=14)
    s.mark('n', mx + 58, my + 260, 28)
    s.rect(mx + 24 + lw + 60, my + 100, 300, 54, fill=C['teal'], r=14)
    s.rect(mx + 24 + lw + 60, my + 170, 610, 54, fill=C['teal_tint'], stroke=C['teal_200'], r=10)
    s.rect(mx + 24 + lw + 60, my + 170, 6, 54, fill=C['teal'], r=3)
    s.rect(mx + 24 + lw + 60, my + 240, 420, 90, fill=C['panel'], r=14)
    s.rect(mx + 24 + lw + 60, my + 346, 610, 54, fill=C['teal_tint'], stroke=C['teal_200'], r=10)
    s.rect(mx + 24 + lw + 60, my + 346, 6, 54, fill=C['teal'], r=3)
    s.text(mx + 24, my + 520, lw, 'The chat ends. Why it stops.', size=22, weight=600, color=C['red'], lh=1.25)
    s.text(mx + 24 + lw + 40, my + 520, rw, 'What our backend did, in one sentence.', size=22, weight=600, color=C['teal_dark'], lh=1.25)
    s.rect(mx, my + mh - 64, mw, 64, fill=C['bg'], stroke=C['border'], r=0)
    s.text(mx + 24, my + mh - 46, mw - 48, 'Same message, same channel (web, LINE or Telegram), same skin on both sides', size=22, color=C['muted'], fit=False)
    # legend
    lx = 1196
    lwid = 1824 - lx
    items = [
        (C['red'], 'Red window', 'An ordinary bot. The reply is made up to show the usual limit. It is not a quote from a real bot.'),
        (C['teal'], 'Teal window', 'Our assistant, with a role label. Plain text on every channel.'),
        (C['teal_200'], 'Shaded line', 'Not a chat message. It names the agent and the tool, and what was read or written.'),
        (C['ink'], 'Two sentences below', 'Red: why the ordinary bot stops. Green: what ours does.'),
    ]
    yy = y
    for col, t, b in items:
        s.rect(lx, yy + 6, 16, 120, fill=col, r=6)
        s.text(lx + 36, yy, lwid - 36, t, size=30, weight=700, color=C['ink'], lh=1.2)
        yy = s.text(lx + 36, yy + 42, lwid - 36, b, size=25, color=C['text'], lh=1.3) + 30
    return s


def lanes_s1(d, section, kicker='The story'):
    s = d.add(section=section, notes=N(
        'This is the story we will follow in the prototype. The student sends a payment slip on LINE. The assistant does not read it and does not decide. It hands the chat to Student Services and stays silent. A staff member sees the slip in a normal inbox chat, checks it and replies by hand, and the student reads that reply on LINE. Then the staff member asks the assistant, in a different chat, to record the payment. The assistant asks for a yes, writes the record and the audit entry, and the Fees page shows the balance as paid. A person decided; the assistant did the bookkeeping.',
        show='Trace the eight steps down the three lanes with a finger.',
        prove='Frames S1.1 to S1.8 in the Figma prototype. Decision of 16 October 2026: the slip goes to staff in a normal chat.', bridge='Now the same story, frame by frame.', mins=2))
    y = hdr(s, 'A payment slip travels through three lanes, and a person decides', kicker, size=46)
    lanes = [('Student', 'LINE and the portal', C['teal']), ('Assistant', 'agents, tools, database', C['charcoal']), ('Staff', 'inbox and assistant chat', C['blue'])]
    lx0 = 96
    lw = (1728 - 2 * 24) / 3
    top = y
    for i, (nm, sub, col) in enumerate(lanes):
        x = lx0 + i * (lw + 24)
        s.rect(x, top, lw, 56, fill=col, r=12)
        s.text(x + 20, top + 10, lw - 40, f'{nm}  ·  {sub}', size=24, weight=700, color=C['white'], lh=1.2, fit=False)
        s.rect(x, top + 64, lw, 1000 - top - 64, fill=C['alt'], stroke=C['border'], r=12)
    steps = [
        (0, 'Sends the slip as a photo on LINE'),
        (1, 'Hands the chat to Student Services and goes silent'),
        (2, 'Sees the slip in a normal inbox chat'),
        (2, 'Checks it and replies by hand'),
        (0, 'Reads the reply on LINE'),
        (2, 'Asks the assistant to record the payment'),
        (1, 'Asks for a yes, writes the record and the audit entry'),
        (0, 'Sees the balance as paid on the Fees page'),
    ]
    rh = (1000 - top - 64 - 16) / 8
    prev = None
    for i, (lane, txt) in enumerate(steps):
        x = lx0 + lane * (lw + 24)
        yy = top + 72 + i * rh
        bh = rh - 12
        col = lanes[lane][2]
        s.rect(x + 14, yy, lw - 28, bh, fill=C['bg'], stroke=col, sw=3, r=12)
        s.ellipse(x + 26, yy + (bh - 44) / 2, 44, 44, fill=col)
        s.text(x + 26, yy + (bh - 44) / 2 + 7, 44, str(i + 1), size=24, weight=700, color=C['white'], align='c', lh=1.1)
        s.text(x + 84, yy + 8, lw - 112, txt, size=24, color=C['text'], lh=1.22, anchor='m', h=bh - 16, minsize=21)
        if prev is not None:
            px, py, pl = prev
            cx_prev = lx0 + pl * (lw + 24) + lw / 2
            cx_cur = x + lw / 2
            gy = (py + yy) / 2
            if pl == lane:
                arrow(s, cx_cur, py + 1, cx_cur, yy - 3, w=3)
            else:
                s.line(cx_prev, py + 1, cx_prev, gy, color=C['border_strong'], w=3)
                s.line(cx_prev, gy, cx_cur, gy, color=C['border_strong'], w=3)
                arrow(s, cx_cur, gy, cx_cur, yy - 3, w=3)
        prev = (x, yy + bh, lane)
    return s


def frames2(d, title, overline, f1, c1, f2, c2, takeaway, notes='', section=None, w=840):
    s = d.add(notes=notes, section=section)
    y0 = hdr(s, title, overline, size=46)
    for i, (f, c) in enumerate(((f1, c1), (f2, c2))):
        x = 96 + i * (w + 48)
        im = Image.open(os.path.join(lib.IMG, f))
        h = w * im.size[1] / im.size[0]
        s.image(f, x, y0, w, h, fit='contain', r=14, border=C['border'], shadow=True)
        s.text(x, y0 + h + 14, w, c, size=24, color=C['muted'], align='c', lh=1.25)
    note_bar(s, 1000 - 96 - 4, takeaway, size=28, h=96)
    return s


def frame_callouts(d, title, overline, img, callouts, caption, notes='', section=None, imgw=1040, quote=None, who=None):
    s = d.add(notes=notes, section=section)
    y0 = hdr(s, title, overline, size=46)
    im = Image.open(os.path.join(lib.IMG, img))
    ih = imgw * im.size[1] / im.size[0]
    maxh = 1000 - y0 - 60
    if ih > maxh:
        imgw = maxh * im.size[0] / im.size[1]
        ih = maxh
    s.image(img, 96, y0, imgw, ih, fit='contain', r=14, border=C['border'], shadow=True)
    s.text(96, y0 + ih + 14, imgw, caption, size=22, color=C['muted'], align='c', lh=1.2)
    rx = 96 + imgw + 56
    rw = 1824 - rx
    yy = y0
    if quote:
        s.text(rx, yy, rw, (who or 'The student').upper(), size=20, weight=700, color=C['teal'], tracking=2)
        yy = kit.quote(s, rx, yy + 32, rw, who, quote, size=26) + 28
    s.text(rx, yy, rw, 'WHAT THE SYSTEM DOES UNDERNEATH', size=20, weight=700, color=C['teal'], tracking=2)
    yy += 40
    for i, (t, b) in enumerate(callouts, 1):
        yy = s.callout(rx, yy, rw, i, t, b, size=26) + 22
    return s


def parts_map(d, section, notes=None):
    s = d.add(section=section, notes=notes or N(
        'The prototype has 12 stories in three parts: student, staff and instructor. Every story is a short chain of frames. A bar at the bottom of each frame names the actor, the channel and the step, and a Next button jumps to the next frame. When the story changes actor, the same Next button follows it. That is how you will see one payment slip pass through three people.',
        show='Run a finger down the three columns.', prove='Figma prototype: 270 frames, 4,258 links, 24 flow starts. No broken link, no frame a flow cannot reach.', bridge='Two comparisons first, then the live click-through.', mins=1))
    y = hdr(s, 'Twelve stories, in three parts', 'The prototype', size=48)
    cols = [
        ('Student', C['teal'], ['S1 Payment slip, to the database', 'S3 Own record only', 'S4 Book a room on the web', 'S5 Book a room on LINE', 'S6 Two students, one room', 'S8 A what-if question', 'S9 A tool fails, then recovers']),
        ('Staff', C['blue'], ['T1 Ask the assistant in the console', 'T2 Remind late students on LINE and Telegram', 'T3 Registrar sends a Dean list notice']),
        ('Instructor', C['amber'], ['I1 Classes tomorrow', 'I2 An absence reminder']),
    ]
    widths = [820, 560, 340]
    x = 96
    for (nm, col, items), w in zip(cols, widths):
        s.rect(x, y, w, 60, fill=col, r=12)
        s.text(x + 18, y + 12, w - 36, nm, size=28, weight=700, color=C['white'], lh=1.2, fit=False)
        s.rect(x, y + 68, w, 700, fill=C['alt'], stroke=C['border'], r=12)
        yy = y + 90
        for it in items:
            code, rest = it.split(' ', 1)
            s.text(x + 18, yy, 70, code, size=26, weight=700, color=col, lh=1.2, fit=False)
            yy = s.text(x + 88, yy, w - 106, rest, size=24, color=C['text'], lh=1.22) + 16
        x += w + 12
    s.text(96, y + 790, 1728, 'Every frame has a bar with the actor, the channel and Next. 270 frames, 4,258 links, none broken.', size=26, weight=600, color=C['teal_dark'])
    return s


# ============================ frame crops ============================
def fcrop(name, box, scale=2):
    """Crop part of a prototype frame and upscale it, so chat text stays readable on a slide."""
    os.makedirs(os.path.join(lib.IMG, 'v2', 'crops'), exist_ok=True)
    key = os.path.splitext(os.path.basename(name))[0] + '_' + '_'.join(str(b) for b in box)
    out = f'v2/crops/{key}.png'
    full = os.path.join(lib.IMG, out)
    src = os.path.join(lib.IMG, name)
    if not os.path.exists(full) or os.path.getmtime(full) < os.path.getmtime(src):
        im = Image.open(src).crop(box)
        im.resize((im.width * scale, im.height * scale), Image.LANCZOS).save(full)
    return out


PHONE = (525, 175, 915, 700)       # the message area of a phone frame
PHONE_FULL = (525, 120, 915, 970)  # the whole phone
WEBCHAT = (338, 125, 1094, 560)    # the message area of a web chat frame
CONSOLE_CHAT = (280, 130, 1010, 560)


def week_overview(d, section):
    s = d.add(section=section, notes=N(
        'We follow one student, Wai Yan Lynn, from Wednesday 14 October to Tuesday 20 October. Each stop is one moment: a question, a room, a slip, a missed exam. For each we show what the student sees, what a person does, and what the system did underneath. The ordinary-bot replies in the comparison slides are made up for contrast.',
        show='Point at the five stops.', prove='All dates follow the 2026 calendar and the prototype.', bridge='First the reason this is needed.', mins=1))
    y = hdr(s, 'Five moments in one student week', 'The week', size=48)
    stops = [('Wed 14, 11:34', 'A room for the group', 'Booking on LINE'), ('Wed 14, 14:22', 'A question nobody wrote down', 'A person takes over'), ('Wed 14, 16:06', 'A payment slip', 'Student, staff, assistant, database'),
             ('Tue 20, morning', 'A missed exam', 'A rule, a deadline, a request'), ('Tue 20', 'The University side', 'Staff, instructor, administrator')]
    cw = (1728 - 4 * 20) / 5
    s.line(96, y + 90, 1824, y + 90, color=C['teal_200'], w=6)
    for i, (when, what, sub) in enumerate(stops):
        x = 96 + i * (cw + 20)
        s.ellipse(x + cw / 2 - 18, y + 72, 36, 36, fill=C['teal'])
        s.text(x, y, cw, when, size=28, weight=700, color=C['teal_dark'], align='c', lh=1.2, fit=False)
        s.rect(x, y + 140, cw, 420, fill=C['alt'], stroke=C['border'], r=18)
        s.text(x + 24, y + 168, cw - 48, what, size=34, weight=700, color=C['ink'], lh=1.15)
        s.text(x + 24, y + 340, cw - 48, sub, size=26, color=C['muted'], lh=1.3)
    note_bar(s, y + 600, 'At every stop: what the student sees, what a person does, and what the system did underneath.', size=28, h=88)
    return s


# ============================ time and proof passes ============================
import re as _re

PROVE_MAP = {
    'What the survey shows': 'Survey report, 5 and 6 October 2026: 15, 13, 11, 3, 0, 0, 0 of 17.',
    'Objectives': 'Feasibility report v3, objectives.',
    'Scope': 'Feasibility report v3 and the team scope decisions of 15 and 16 October 2026.',
    'Who can do what': 'Access map, diagram 11.',
    'Technology stack': 'Feasibility report v3 and the team decisions of 11 to 16 October 2026.',
    'Timeline and milestones': 'Feasibility report v3, section 2.3.',
    'Risks we know': 'Feasibility report v3 risk table, updated for OpenRouter. OpenRouter limits: openrouter.ai/docs/api-reference/limits.',
    'How we will measure': 'Feasibility report v3, requirements and test plan. These are targets.',
    'Initial test results': 'Chatwoot spike results, 15 and 16 October 2026: 11 checks, 9 passed.',
    'seven deliverables': 'git log of the repository: commits since 12 October 2026. Diagrams: design/diagrams, 12 files.',
    'Decisions made': 'Team decisions, 11 to 17 October 2026.',
    'Twelve stories': 'Figma prototype audit, 18 October 2026: 270 frames, 4,258 links, 24 flow starts.',
    'The prototype: 270': 'Figma prototype audit, 18 October 2026.',
    'The data model': 'Diagram 02: 44 entities in six groups.',
    'Chatwoot carries': 'Chatwoot spike results, 15 and 16 October 2026.',
    'Project II': 'Feasibility report v3 and the scope decisions.',
    'Group S and the course': 'Course record: BC362916 and BC362914, Krirk University.',
}


def add_prove(d):
    for s in d.slides:
        if not s.notes or 'PROVE:' in s.notes:
            continue
        for k, v in PROVE_MAP.items():
            if k.lower() in (s.title_text or '').lower():
                s.notes = s.notes.rstrip() + '\nPROVE: ' + v
                break


def fit_time(d, agenda=None, total=37.0):
    """Scale the TIME lines of the main slides so they add up to `total` minutes, then rebuild the agenda from the section sums."""
    ai = next((i for i, s in enumerate(d.slides) if s.title_text == 'Appendix'), len(d.slides))
    main = d.slides[:ai]
    rx = _re.compile(r'TIME: ([\d.]+) min')
    fixed = [s for s in main if 'Thank the' in (s.notes or '')]
    var = [s for s in main if s not in fixed and rx.search(s.notes or '')]
    cur = sum(float(rx.search(s.notes).group(1)) for s in var)
    k = total / cur if cur else 1
    for s in var:
        v = float(rx.search(s.notes).group(1)) * k
        v = max(0.5, round(v * 2) / 2)
        s.notes = rx.sub('TIME: ' + (str(int(v)) if v == int(v) else str(v)) + ' min', s.notes, count=1)
    def tv(s):
        return float(rx.search(s.notes).group(1))

    def setv(s, v):
        s.notes = rx.sub('TIME: ' + (str(int(v)) if v == int(v) else str(v)) + ' min', s.notes, count=1)
    guard = 0
    while sum(tv(s) for s in var) > total + 0.01 and guard < 500:
        s = max(var, key=tv)
        if tv(s) <= 0.5:
            break
        setv(s, tv(s) - 0.5)
        guard += 1
    guard = 0
    order_up = sorted(var, key=tv, reverse=True)
    while sum(tv(s) for s in var) < total - 0.01 and guard < 500:
        s = order_up[guard % len(order_up)]
        setv(s, tv(s) + 0.5)
        guard += 1
    sums = {}
    first_sec = d.sections[0] if d.sections else None
    for s in var:
        sec = s.section or first_sec
        sums[sec] = sums.get(sec, 0) + tv(s)
    out = sum(sums.values())
    if agenda:
        rows_f = {sec: sums.get(sec, 0) for sec in agenda['rows']}
        tot = sum(rows_f.values())
        ints = {sec: int(v) for sec, v in rows_f.items()}
        rem = int(round(total)) - sum(ints.values())
        order = sorted(rows_f, key=lambda sec: rows_f[sec] - ints[sec], reverse=(rem > 0))
        for sec in order[:abs(rem)]:
            ints[sec] += 1 if rem > 0 else -1
        rows = [[str(ints[sec]), agenda['rows'][sec][0], agenda['rows'][sec][1]] for sec in agenda['rows']] + [[str(int(round(40 - total))), 'Questions', 'Everyone']]
        assert sum(int(r[0]) for r in rows) == 40, rows
        idx = next(i for i, s in enumerate(d.slides) if s.title_text == agenda['title'])
        old = d.slides[idx]
        new = M.m_agenda(d, rows, notes=old.notes, title=agenda['title'])
        d.slides.pop()
        new.section = old.section
        d.slides[idx] = new
    return out
