import os, sys, subprocess, importlib, shutil, glob
sys.path.insert(0, os.path.dirname(__file__))
import lib

ROOT = lib.ROOT
OUT = os.path.join(ROOT, 'out')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'


def dump_text(deck, path):
    out = [f'# {deck.title}', '']
    for i, s in enumerate(deck.slides, 1):
        out.append(f'## Slide {i}: {s.title_text or "(no title)"}')
        items = []
        for e in s.els:
            if e['t'] == 'text':
                items.append((e['y'], e['x'], e['raw'].replace('\n', ' / ')))
            elif e['t'] == 'rich':
                items.append((e['y'], e['x'], ' '.join(w[0] for ln in e['lines'] for w in ln)))
            elif e['t'] == 'image':
                items.append((e['y'], e['x'], '[image: ' + os.path.basename(e['path']) + ']'))
        for y, x, tx in sorted(items):
            out.append('- ' + tx)
        if s.notes:
            out.append('')
            out.append('Speaker notes: ' + s.notes)
        out.append('')
    open(path, 'w').write('\n'.join(out))


def build(modname, pdf=True, pptx=True, previews=True):
    mod = importlib.import_module(modname)
    importlib.reload(mod)
    deck = mod.make()
    os.makedirs(OUT, exist_ok=True)
    base = os.path.join(OUT, deck.name)
    issues = deck.report()
    print(f'{deck.name}: {len(deck.slides)} slides, {issues} layout issues')
    dump_text(deck, base + '_text.md')
    lib.render_html(deck, base + '.html')
    if pdf:
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', '--run-all-compositor-stages-before-draw',
                        f'--print-to-pdf={base}.pdf', 'file://' + base + '.html'], check=True, capture_output=True, timeout=300)
    if pptx:
        lib.render_pptx(deck, base + '.pptx')
    if previews and pdf:
        pd = base + '_png'
        shutil.rmtree(pd, ignore_errors=True)
        os.makedirs(pd)
        subprocess.run(['pdftoppm', '-r', '48', '-png', base + '.pdf', pd + '/s'], check=True)
    return deck


if __name__ == '__main__':
    for m in sys.argv[1:]:
        build(m)
