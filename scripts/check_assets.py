"""Asset checks for yuhshi-icons. Fails (exit 1) on any problem.

- Every .svg parses as XML and has a viewBox.
- Every .png has a valid PNG signature and its pixel size matches any -<N> or -<W>x<H> size in its name.
- Every .json / .webmanifest parses.
- UI icons: regenerating from ui/tools/icons.py reproduces ui/svg exactly.
- UI icons: only currentColor is used (no hard-coded colours), on a 24 x 24 viewBox.
"""
import filecmp, json, os, re, struct, subprocess, sys, tempfile
import xml.dom.minidom

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []
counts = {'svg': 0, 'png': 0, 'json': 0}


def png_size(path):
    with open(path, 'rb') as f:
        head = f.read(24)
    if head[:8] != b'\x89PNG\r\n\x1a\n':
        return None
    return struct.unpack('>II', head[16:24])


for dirpath, dirnames, files in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in ('.git', 'node_modules')]
    for name in files:
        path = os.path.join(dirpath, name)
        rel = os.path.relpath(path, ROOT)
        if name.endswith('.svg'):
            counts['svg'] += 1
            try:
                doc = xml.dom.minidom.parse(path)
                if not doc.documentElement.getAttribute('viewBox'):
                    errors.append(f'{rel}: missing viewBox')
            except Exception as e:
                errors.append(f'{rel}: invalid SVG ({e})')
        elif name.endswith('.png'):
            counts['png'] += 1
            size = png_size(path)
            if size is None:
                errors.append(f'{rel}: not a valid PNG')
                continue
            m = re.search(r'-(\d+)x(\d+)(?:@\dx)?\.png$', name)
            if m and (int(m.group(1)), int(m.group(2))) != size:
                errors.append(f'{rel}: is {size[0]}x{size[1]}, name says {m.group(1)}x{m.group(2)}')
            m = re.search(r'-(\d+)\.png$', name)
            if m and size[0] != int(m.group(1)) and size[1] != int(m.group(1)):
                errors.append(f'{rel}: is {size[0]}x{size[1]}, name says {m.group(1)}')
        elif name.endswith(('.json', '.webmanifest')):
            counts['json'] += 1
            try:
                json.load(open(path))
            except Exception as e:
                errors.append(f'{rel}: invalid JSON ({e})')

# UI icons: reproducible from source and colour-neutral
ui = os.path.join(ROOT, 'ui')
if os.path.isdir(ui):
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([sys.executable, os.path.join(ui, 'tools', 'build.py'), tmp], check=True, capture_output=True)
        cmp = filecmp.dircmp(os.path.join(tmp, 'svg'), os.path.join(ui, 'svg'))
        for n in cmp.left_only:
            errors.append(f'ui/svg/{n}: generated but not committed (run ui/tools/build.py)')
        for n in cmp.right_only:
            errors.append(f'ui/svg/{n}: committed but not generated from ui/tools/icons.py')
        for n in cmp.diff_files:
            errors.append(f'ui/svg/{n}: differs from generated output (edit ui/tools/icons.py, not the SVG)')
        if not filecmp.cmp(os.path.join(tmp, 'src', 'index.ts'), os.path.join(ui, 'src', 'index.ts'), shallow=False):
            errors.append('ui/src/index.ts: differs from generated output (run ui/tools/build.py)')
    for n in os.listdir(os.path.join(ui, 'svg')):
        t = open(os.path.join(ui, 'svg', n)).read()
        if re.search(r'#[0-9a-fA-F]{3,8}\b|rgb\(', t):
            errors.append(f'ui/svg/{n}: hard-coded colour; UI icons must use currentColor only')
        if 'viewBox="0 0 24 24"' not in t:
            errors.append(f'ui/svg/{n}: must use the 24 x 24 grid')

print(f"Checked {counts['svg']} SVG, {counts['png']} PNG, {counts['json']} JSON files")
if errors:
    print(f'{len(errors)} problem(s):')
    for e in errors:
        print('  -', e)
    sys.exit(1)
print('All asset checks passed')
