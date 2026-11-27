// UI icon index checks. Run: npx tsx scripts/ui-icons.test.ts
import { existsSync } from 'node:fs';
import { icons, iconNames, iconSvg, type IconName } from '../ui/src/index';

const failures: string[] = [];
const expect = (ok: boolean, msg: string) => { if (!ok) failures.push(msg); };

const tabs: IconName[] = ['world', 'discover', 'yuhshi', 'phrasebook', 'profile'];
const forbidden = ['heart', 'like', 'crown', 'trophy', 'flame', 'fire', 'follower', 'rank'];

expect(iconNames.length >= 66, `expected at least 66 icons, got ${iconNames.length}`);
for (const t of tabs) {
  expect(!!icons[t].active, `tab icon "${t}" needs a selected (-active) version`);
  expect(iconSvg(t, true).includes('fill-opacity="0.16"'), `selected "${t}" must use the 16% tint`);
  expect(iconSvg(t, false) === icons[t].svg, `unselected "${t}" must return the outline`);
}
for (const n of iconNames) {
  const e = icons[n];
  expect(existsSync(`ui/svg/${n}.svg`), `ui/svg/${n}.svg missing`);
  expect(e.svg.startsWith('<svg') && e.svg.includes('<title>'), `"${n}" must be an SVG with a <title>`);
  expect(e.svg.includes('stroke-width="1.75"'), `"${n}" must use the 1.75 stroke`);
  expect(!forbidden.some((f) => n.includes(f)), `"${n}" is a popularity symbol; Yuhshi has none`);
}
expect(icons.back.mirrorInRtl && icons.forward.mirrorInRtl, 'back/forward must mirror in RTL');
expect(!icons.search.mirrorInRtl, 'search must not mirror');

if (failures.length) {
  console.error(`${failures.length} UI icon check(s) failed:\n- ${failures.join('\n- ')}`);
  process.exit(1);
}
console.log(`UI icons: all checks passed (${iconNames.length} icons)`);
