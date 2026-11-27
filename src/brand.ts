// Yuhshi brand module.
// Code names the place a logo appears (a surface); this module picks the file.
// File names follow the theme the logo sits on, not the logo's own colour:
//   light = for light backgrounds (dark ink), dark = for dark backgrounds (white ink).

export type Theme = "light" | "dark";
export type Kind = "logo" | "emblem" | "emblem-small" | "wordmark";
export type Variant = Theme | "contrast-light" | "contrast-dark" | "mono";
export type Format = "svg" | "png";

export type Surface =
  | "web-header"      // site and web-app header
  | "app-header"      // mobile app top bar
  | "browser-tab"     // favicon, 16–24 px
  | "splash"          // launch / onboarding screen
  | "footer"          // page footer
  | "email-header"    // transactional and marketing email (PNG)
  | "social-avatar"   // profile picture on social platforms
  | "document"        // PDFs, invoices, contracts
  | "print-one-colour"; // stamps, embroidery, single-ink print

export interface Options {
  /** Use the high-contrast set (user's OS or in-app high-contrast setting). */
  highContrast?: boolean;
  /** Retina / high-density screens: PNGs use the @2x copy. */
  density?: 1 | 2;
}

export interface LogoFile {
  kind: Kind;
  variant: Variant;
  format: Format;
  /** Path relative to the brand asset root. */
  path: string;
}

/** Below this width the full logo is too small; switch to the emblem. */
export const MIN_LOGO_WIDTH_PX = 96;
/** At or below this size use the simplified small emblem. */
export const SMALL_EMBLEM_MAX_PX = 24;

const SURFACE_KIND: Record<Surface, Kind> = {
  "web-header": "logo",
  "app-header": "logo",
  "browser-tab": "emblem-small",
  "splash": "logo",
  "footer": "logo",
  "email-header": "logo",
  "social-avatar": "emblem",
  "document": "logo",
  "print-one-colour": "logo",
};

const PNG_SURFACES: ReadonlySet<Surface> = new Set<Surface>(["email-header"]);

function pickKind(surface: Surface, width: number): Kind {
  const kind = SURFACE_KIND[surface];
  if (width <= SMALL_EMBLEM_MAX_PX) return "emblem-small";
  if (kind === "logo" && width < MIN_LOGO_WIDTH_PX) return "emblem";
  return kind;
}

function pickVariant(surface: Surface, theme: Theme, opts: Options): Variant {
  if (surface === "print-one-colour") return "mono";
  if (opts.highContrast) return theme === "light" ? "contrast-light" : "contrast-dark";
  return theme;
}

/**
 * Pick the right logo file for a place in the product.
 * @example forSurface("web-header", "dark", 180) → svg/yuhshi-logo-dark.svg
 * @example forSurface("email-header", "light", 240, { density: 2 }) → email/logo-light@2x.png
 */
export function forSurface(
  surface: Surface,
  theme: Theme,
  width: number,
  opts: Options = {},
): LogoFile {
  const kind = pickKind(surface, width);
  const variant = pickVariant(surface, theme, opts);
  if (PNG_SURFACES.has(surface)) {
    const suffix = opts.density === 2 ? "@2x" : "";
    return { kind, variant, format: "png", path: `email/${kind}-${variant}${suffix}.png` };
  }
  return { kind, variant, format: "svg", path: `svg/yuhshi-${kind}-${variant}.svg` };
}

/** The mono files use `currentColor`: set the CSS `color` to the ink you need. */
export const MONO_INKS = { onLight: "#25283A", onDark: "#FFFFFF" } as const;
