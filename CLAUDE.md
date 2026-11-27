# yuhshi-icons — rules for every session

1. Before starting, read `claude/build-log.md` in the YUHSHI project. Logo rules: Master Blueprint 16.15 and `claude/logo-files.md`.
2. Work on a branch, never directly on `main`. Open a pull request; `main` only accepts changes whose CI checks pass.
3. Before opening or merging a pull request, run `npm ci && npm run check`. It must pass.
4. Logo and platform assets are generated from the master SVGs in `svg/`; never alter master shapes, colours or spacing without owner approval.
5. UI icons are generated: edit `ui/tools/icons.py`, then run `python3 ui/tools/build.py ui` (from the repo root) and `python3 ui/tools/preview.py ui/svg ui/preview.svg` and commit the results. Never hand-edit `ui/svg/` or `ui/src/index.ts`.
6. UI icons use `currentColor` only, the 24 px grid and 1.75 stroke. No popularity symbols (hearts, likes, crowns, trophies).
7. After meaningful progress, append a dated entry to the build log's "Session updates".
8. Living documents: when you add, change or remove a feature, data use, fee or safety tool, update every document it affects in the same pull request or the build log entry (Community Guidelines, Terms, Privacy Policy, safety risk assessment, pricing plan, names register, Master Blueprint). Note in the PR which documents changed, or "none affected".
9. Improvements during the build (L12): any improvement you realise while building is implemented, in the same pull request or its own. Add a row to the build log's Improvements register (Section 8): what, where (PR, files, documents) and why, and say so in the PR. Improvements that change a locked decision (blueprint, pricing, names, logo, colours, fonts, tagline) go to the owner first.
