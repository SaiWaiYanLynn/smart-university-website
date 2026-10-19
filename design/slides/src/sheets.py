import sys, glob, os
from PIL import Image
root = os.path.join(os.path.dirname(__file__), '..', 'out')
for name in sys.argv[1:]:
    d = os.path.join(root, name + '_png')
    files = sorted(glob.glob(d + '/s-*.png'), key=lambda f: int(os.path.basename(f).split('-')[1].split('.')[0]))
    for old in glob.glob(d + '/sheet_*.png'):
        os.remove(old)
    for k in range(0, len(files), 4):
        sheet = Image.new('RGB', (1920, 1080), '#999')
        for j, f in enumerate(files[k:k + 4]):
            sheet.paste(Image.open(f).convert('RGB'), ((j % 2) * 960, (j // 2) * 540))
        sheet.save(f'{d}/sheet_{k // 4 + 1:02d}.png')
    print(name, len(files), 'slides', (len(files) + 3) // 4, 'sheets')
