"""Reusable slide patterns built on lib.py."""
from lib import C, text_w, wrap, Slide
from PIL import Image
import os, lib


# ---- auto crop of prototype frames so the screenshot shows the part that matters ----
WEB_CHAT = {'j1_3', 'j1_4', 'j2_2', 'j2_4', 'j3_2', 'j3_4', 'j4_3', 'j4_4', 'j4_5', 'j5_1', 'j5_3', 'j5_4', 'j5_5', 'j8_2', 'j8_3', 'j11_2', 'j11_3'}
CONSOLE = {'sc1', 'sc2', 'r5_1', 'r3_1', 'r7_1', 'a3_2', 'a4_2', 'r8_1', 'r8_2', 'r8_3', 'r1_3', 'sc8', 'r1_1'}
PHONE = {'j10_2', 'j10_4', 'j10_5', 'j12_1', 'j12_4', 'j13_1', 'j14_1', 'j15_1', 'j16_1', 'j17_2', 'j19_1', 'j20_1', 'j20_3', 'j20_4', 'j24_2', 'j21_2', 'j22_1', 'j22_2', 'j22_3'}


def auto_crop(name):
    key = name.replace('.png', '')
    box = None
    if key == 'j1_3':
        box = (20, 64, 1440, 900)
    elif key == 'j1_4':
        box = (20, 64, 1440, 900)
    elif key in WEB_CHAT:
        box = (110, 64, 1330, 900)
    elif key in CONSOLE:
        box = (260, 0, 1440, 900)
    elif key in PHONE:
        box = (330, 0, 1350, 998)
    if not box:
        return name
    os.makedirs(os.path.join(lib.IMG, 'crops'), exist_ok=True)
    out = f'crops/{key}.png'
    full = os.path.join(lib.IMG, out)
    src = os.path.join(lib.IMG, name)
    if not os.path.exists(full) or os.path.getmtime(full) < os.path.getmtime(src):
        im = Image.open(src)
        im.crop((box[0], box[1], min(box[2], im.size[0]), min(box[3], im.size[1]))).save(full)
    return out


def hdr(s, title, overline=None, size=52):
    """Standard header. Returns y where content can start."""
    end = s.title(title, overline=overline, size=size, y=56)
    return end + 36


def box(s, x, y, w, h, title, sub=None, fill=None, stroke=None, tcolor=None, scolor=None, tsize=26, ssize=22, r=14,
        sw=2, align='c', tweight=700, pad=16, lh=1.22):
    s.rect(x, y, w, h, fill=fill or C['bg'], stroke=stroke or C['border'], sw=sw, r=r)
    tl = wrap(title, (w - 2 * pad) * 0.975, tsize, tweight)
    th = len(tl) * tsize * lh
    sh = 0
    sl = []
    if sub:
        sl = wrap(sub, (w - 2 * pad) * 0.975, ssize, 400)
        sh = len(sl) * ssize * lh + 6
    total = th + sh
    yy = y + (h - total) / 2
    if total > h - 8:
        s.issues.append(f'box overflow: "{title[:30]}" needs {total:.0f} has {h}')
    s.text(x + pad, yy, w - 2 * pad, title, size=tsize, weight=tweight, color=tcolor or C['ink'], align=align, lh=lh, fit=False)
    if sub:
        s.text(x + pad, yy + th + 6, w - 2 * pad, sub, size=ssize, color=scolor or C['muted'], align=align, lh=lh, fit=False)


def arrow(s, x1, y1, x2, y2, color=None, w=3):
    s.line(x1, y1, x2, y2, color=color or C['border_strong'], w=w, arrow=True)


def chain(s, x, y, w, items, gap=60, h=150, size=24, tsize=26, fills=None, numbered=True):
    """Horizontal chain of boxes with arrows. items: list of (title, sub)."""
    n = len(items)
    bw = (w - gap * (n - 1)) / n
    for i, (t, sub) in enumerate(items):
        bx = x + i * (bw + gap)
        f = (fills[i] if fills else C['bg'])
        box(s, bx, y, bw, h, t, sub, fill=f, tsize=tsize, ssize=size, stroke=C['border_strong'] if f == C['bg'] else C['teal'])
        if numbered:
            s.ellipse(bx - 14, y - 18, 40, 40, fill=C['teal'])
            s.text(bx - 14, y - 12, 40, str(i + 1), size=22, weight=700, color=C['white'], align='c', lh=1.1)
        if i < n - 1:
            arrow(s, bx + bw + 8, y + h / 2, bx + bw + gap - 8, y + h / 2)


def big_number(s, x, y, w, num, label, color=None, nsize=120, lsize=26, fill=None):
    if fill:
        s.rect(x, y, w, nsize * 1.15 + 20 + 90, fill=fill, r=16)
    s.text(x, y, w, num, size=nsize, weight=700, color=color or C['teal'], align='c', lh=1.0, fit=False)
    s.text(x + 20, y + nsize * 1.08, w - 40, label, size=lsize, color=C['muted'], align='c', lh=1.25)


def note_bar(s, y, text, fill=None, color=None, size=30, h=None, x=96, w=1728, weight=600, stroke=None):
    lines = wrap(text, (w - 80) * 0.975, size, weight)
    hh = h or (len(lines) * size * 1.3 + 40)
    s.rect(x, y, w, hh, fill=fill or C['teal_tint'], stroke=stroke or C['teal_200'], r=14)
    s.text(x + 40, y + (hh - len(lines) * size * 1.3) / 2, w - 80, text, size=size, weight=weight, color=color or C['teal_dark'], lh=1.3, fit=False)
    return y + hh


def quote(s, x, y, w, who, msg, size=28, fill=None):
    """A chat-bubble style quote."""
    lines = wrap(msg, (w - 56) * 0.975, size, 500)
    hh = len(lines) * size * 1.3 + 44
    s.rect(x, y, w, hh, fill=fill or C['teal'], r=18)
    s.text(x + 28, y + 22, w - 56, msg, size=size, weight=500, color=C['white'], lh=1.3, fit=False)
    return y + hh


def journey_slide(deck, title, overline, frame, callouts, quote_text=None, who=None, caption=None, notes='', imgw=1040, src=None,
                  bottom=None, csize=26, piece=None):
    s = deck.add(notes=notes)
    y0 = hdr(s, title, overline)
    ix, iy = 96, y0
    frame = auto_crop(frame)
    im = Image.open(os.path.join(lib.IMG, frame))
    ih = imgw * im.size[1] / im.size[0]
    maxh = 1000 - iy - (60 if caption else 0)
    if ih > maxh:
        imgw = maxh * im.size[0] / im.size[1]
        ih = maxh
    s.image(frame, ix, iy, imgw, ih, fit='contain', r=14, border=C['border'], shadow=True)
    if caption:
        s.text(ix, iy + ih + 14, imgw, caption, size=22, color=C['muted'], align='c', lh=1.2)
    rx = ix + imgw + 56
    rw = 1824 - rx
    yy = y0
    if quote_text:
        s.text(rx, yy, rw, (who or 'The student').upper(), size=20, weight=700, color=C['teal'], tracking=2)
        yy = quote(s, rx, yy + 32, rw, who, quote_text, size=26) + 28
    s.text(rx, yy, rw, 'WHAT THE SYSTEM DOES UNDERNEATH', size=20, weight=700, color=C['teal'], tracking=2)
    yy += 40
    for i, (t, b) in enumerate(callouts, 1):
        yy = s.callout(rx, yy, rw, i, t, b, size=csize) + 22
    if piece:
        ph = 150
        py = max(yy + 6, 1000 - ph)
        s.rect(rx, py, rw, ph, fill=C['teal_tint'], stroke=C['teal_200'], r=14)
        s.text(rx + 24, py + 14, rw - 48, 'ARCHITECTURE PIECE', size=20, weight=700, color=C['teal'], tracking=2)
        s.text(rx + 24, py + 46, rw - 48, piece, size=26, weight=600, color=C['teal_dark'], lh=1.25, h=ph - 56, minsize=22)
    s.title_text = title
    return s


def two_frames(deck, title, overline, f1, c1, f2, c2, takeaway, notes='', w=840, sub1=None, sub2=None):
    s = deck.add(notes=notes)
    y0 = hdr(s, title, overline)
    for i, (f, c) in enumerate(((f1, c1), (f2, c2))):
        x = 96 + i * (w + 48)
        f = auto_crop(f)
        im = Image.open(os.path.join(lib.IMG, f))
        h = w * im.size[1] / im.size[0]
        s.image(f, x, y0, w, h, fit='contain', r=14, border=C['border'], shadow=True)
        s.text(x, y0 + h + 14, w, c, size=24, color=C['muted'], align='c', lh=1.25)
    yb = 1000 - 96
    note_bar(s, yb, takeaway, size=28, h=96)
    return s


def section_slide(deck, number, label, sub=None, notes=''):
    s = deck.add(kind='dark', bg=C['charcoal'], footer=False, number=True, notes=notes)
    s.rect(96, 360, 140, 12, fill=C['lime'])
    s.text(96, 400, 1500, label, size=92, weight=700, color=C['white'], lh=1.05)
    if sub:
        s.text(96, 400 + 110 * (1 + (len(wrap(label, 1500, 92, 700)) - 1)), 1400, sub, size=38, color='#D4D4D8', lh=1.3)
    if number is not None:
        s.text(96, 250, 400, f'{number:02d}', size=64, weight=700, color=C['teal_200'], lh=1.0)
    return s
