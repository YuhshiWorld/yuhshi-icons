# Yuhshi platform brand assets

Every file here is made from the approved master SVGs in `svg/`. Shapes, colours, letter spacing and the symbol-to-word spacing are identical in every file. Files only differ in size, background and format.

**Naming:** `yuhshi-<asset>-<theme>[-<size>].<ext>`
- `light`: for light backgrounds and light mode (dark ink, white tile).
- `dark`: for dark backgrounds and dark mode (white ink, #171923 tile).
- `mono`: one colour. The platform or CSS tints it.
- `contrast-light` / `contrast-dark`: high-contrast versions (master SVGs and email PNGs).
- Android resource files (`.xml` and folder names) use underscores instead of hyphens, because Android rejects hyphens in resource names.

## Folders

| Folder | What | Files |
|---|---|---|
| `svg/` | Master vectors: full logo, emblem, small emblem, wordmark × light, dark, contrast-light, contrast-dark, mono | `yuhshi-logo-light.svg`, `yuhshi-emblem-dark.svg`, `yuhshi-wordmark-light.svg` … |
| `web/` | Browser tab icons, home-screen icon for iPhone web, Safari pinned tab | `yuhshi-favicon-light.ico` (16, 32, 48), `yuhshi-favicon-light.svg`, `yuhshi-favicon-light-16/32/48.png`, `yuhshi-apple-touch-icon-light-180.png`, `yuhshi-mask-icon-mono.svg` (+ dark) |
| `pwa/` | Installable web app (offline Lite web app) | `yuhshi-pwa-icon-light-192/512.png`, `yuhshi-pwa-maskable-light-192/512.png` (+ dark, + SVG masters) |
| `ios/` | iPhone and iPad app icon, iOS 18 light, dark and tinted | `yuhshi-ios-icon-light-1024.png`, `yuhshi-ios-icon-dark-1024.png`, `yuhshi-ios-icon-tinted-1024.png`, ready-made `AppIcon.appiconset/`, `legacy/` 20–180 px |
| `android/` | Adaptive launcher icon, themed icon (Android 13+), legacy icons, notification icon, Play Store icon | `mipmap-*/yuhshi-android-foreground-light.png`, `mipmap-*/yuhshi-android-monochrome-mono.png`, `drawable-*/yuhshi-android-notification-mono.png`, `yuhshi-play-store-icon-light-512.png`, vector drawables in `drawable/`, `mipmap-anydpi-v26/ic_launcher.xml` |
| `splash/` | App launch screen icon | `yuhshi-splash-icon-light-1024.png` (+ dark) |
| `social/` | Link-share image (WhatsApp, X, LinkedIn, Facebook), profile pictures | `yuhshi-og-image-light-1200x630.png`, `yuhshi-avatar-light-400/800.png` (+ dark) |
| `email/` | PNG logos for emails, 1x and @2x | `logo-light.png`, `logo-light@2x.png`, `emblem-dark@2x.png` … |
| `print/` | Vector PDF and EPS for printers, merchandise, documents | `yuhshi-logo-light.pdf/.eps`, `yuhshi-emblem-mono.pdf` … |
| `code/` | Ready to paste | `head.html` (web), `manifest.webmanifest` (PWA), `expo-app.json` (iOS/Android/web app) |
| `src/brand.ts` | Brand module: code names the place, the module picks the file | `forSurface("web-header", theme, width)` |

## Sizes and safe zones

| Use | Canvas | Emblem width | Why |
|---|---|---|---|
| Favicon | 16, 32, 48 px | 89% | Small emblem, optically centred, fills the tab |
| App tiles: iOS, apple-touch, PWA "any", Play Store, legacy Android | Square | 70% | Platform rounds the corners |
| PWA maskable, splash icon, avatars | Square | 58% | Stays inside the circular crop |
| Android adaptive foreground and themed | 108 dp | 48% | Stays inside the 66 dp safe circle on every launcher shape |
| Android notification | 24 dp | 90% | White silhouette; Android tints it |
| Share image | 1200 × 630 | Full logo at 56% of the width | Readable in chat and feed previews |

The emblem is always optically centred: it sits 3.14% of its height lower than its geometric centre, because it's top-heavy.

## Colours
- Light tile: #FFFFFF. Dark tile: #171923.
- One-colour: #25283A on light, #FFFFFF on dark.
- Accent for tinted system icons: Spirit #5141D7.
