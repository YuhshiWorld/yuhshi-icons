import { forSurface } from "./brand";
const cases: [Parameters<typeof forSurface>, string][] = [
  [["web-header","light",180], "svg/yuhshi-logo-light.svg"],
  [["web-header","dark",180], "svg/yuhshi-logo-dark.svg"],
  [["web-header","dark",64], "svg/yuhshi-emblem-dark.svg"],
  [["browser-tab","light",16], "svg/yuhshi-emblem-small-light.svg"],
  [["email-header","light",240,{density:2}], "email/logo-light@2x.png"],
  [["web-header","light",180,{highContrast:true}], "svg/yuhshi-logo-contrast-light.svg"],
  [["print-one-colour","dark",300], "svg/yuhshi-logo-mono.svg"],
  [["social-avatar","dark",400], "svg/yuhshi-emblem-dark.svg"],
  [["splash","dark",240], "svg/yuhshi-logo-dark.svg"],
];
let bad=0; const fs=require("fs");
for (const [a,exp] of cases){ const p=forSurface(...a).path; const ok=p===exp && fs.existsSync(__dirname+"/../"+p); if(!ok){bad++;console.log("FAIL",a,p)} }
console.log(bad?`${bad} failed`:`all ${cases.length} passed`); process.exit(bad?1:0);
