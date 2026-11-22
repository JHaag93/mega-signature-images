# Mega Payments brand images

The logo files used across Justin Haag's Mega Payments emails, proposals and pages, in one place so
every piece uses the same ones. GitHub Pages serves them at
**https://jhaag93.github.io/mega-signature-images/** so email programs can load them.

The repo's name is left over from the email signature. **Don't rename it**: the picture links would
change and break every email already sent.

## Which file to use

| File | Pixels | Show it at | Use it for |
|---|---|---|---|
| `mega-logo-tile.png` | 234 × 90 | 78 × 30 | Email signature |
| `mega-logo-tile-header.png` | 360 × 138 | 120 × 46 | Top of any email: proposals, announcements, letters |
| `kind-regards-tile.png` | 238 × 123 | 110 × 57 | Signature sign-off |
| `mega-logo-navy.png` | 327 × 104 | up to 110 wide | Web pages and PDFs on a white or light background. **Never in email.** |
| `mega-logo-white.png` | 327 × 104 | up to 110 wide | Web pages and PDFs on a navy or dark background. **Never in email.** |
| `source/mega-logo-original.png` | 327 × 111 | — | The original from megapayments.com, kept as the source |
| `tools/build-logo-assets.py` | — | — | Rebuilds the four logo files from the original |
| `partners/korona-pos-banner.png` | 1200 × 675 | full card width (about 546) | KORONA POS logo and hardware on solid orange, from koronapos.com's own sharing image (Nov 3, 2026). No see-through areas, so it's dark-mode safe |
| `partners/spoton-handheld-2-table.jpg` | 1200 × 991 | full card width (about 546) | A server taking payment at the table on the SpotOn Handheld 2.0, cropped from SpotOn's own handheld sell sheet (Oct 27, 2026). Solid photo, dark-mode safe. Used in the Nov 11 agent update |
| `partners/square-kiosk-21-5.jpg` | 1200 × 675 | full card width (about 550) | The new Square Kiosk (21.5"), front and three-quarter views on their countertop stands, on a built-in light gray background (Square's own product cut-outs from squareup.com). No see-through areas, so it's dark-mode safe. Used in the Nov 20 agent update |
| `products/pays-retail-kit-dejavoo-p1.jpg` | 1200 × 600 | full card width (about 550) | PAYS Retail Kit and Dejavoo P1 side by side on solid white (makers' own product photos), for merchant proposal emails (Nov 7, 2026). Dark-mode safe |
| `products/korona-joy-j14-pax-a80.jpg` | 1200 × 600 | full card width (about 550) | Partner Tech Joy J14 register (KORONA bundle) and PAX A80 terminal on solid white (makers' own product photos), for merchant proposal emails (Nov 7, 2026). Dark-mode safe |
| `seasonal/thanksgiving-2026-pie-chart.png` | 1200 × 600 | full card width (about 550) | Thanksgiving 2026 agent emails: a pumpkin pie drawn as a "Q4 Results" pie chart (Pumpkin Pie 100%, Missing Slice Under Investigation) and "Happy Thanksgiving, Mega Team." Drawn by Claude Nov 21, 2026 (no outside artwork), solid navy and cream background, so dark-mode safe. Source: `source/thanksgiving-2026-pie-chart-source.html`. |
| `seasonal/thanksgiving-2026-turkey-banner.jpg` | 1200 × 960 | full width (about 550) | Thanksgiving 2026 email banner: a cartoon turkey in a navy scarf holding a pumpkin pie, whipped cream centered with the missing slice cut through it, centered on flat cream (#FEF4E6), and "Happy Thanksgiving, / Mega Team." in navy Georgia Bold 64 px below it, set by us (not AI lettering). Art generated Nov 21, 2026 with OpenAI's image model through Codex (Justin picked the turkey, then the centered cut dollop, "version 1"); layout from an outside designer review (no frame, no copper rule, no navy band; JPEG quality 92, 4:4:4). Replaced in place the same day, before any email using it was sent. Original art: `source/thanksgiving-2026-turkey-art.png`. Dark-mode safe. |
| `seasonal/thanksgiving-2026-turkey-card.jpg` | 600 × 600 | 300 × 300 (exactly half) | The same turkey on flat #FEF4E6 with even margins, no words, for the "Leftovers 2.0" card in the Nov 23 agent email (card background #FEF4E6, img `border-radius:8px`). |
| `seasonal/thanksgiving-2026-turkey-card-whole-pie.jpg` | 600 × 600 | 300 × 300 | **Used in the Nov 23 email** (replaces the card above): the turkey holding a WHOLE pie, whipped cream centered (measured within 4 px of the pie's center), no crumbs, for the "Leftovers 2.0" card. Art: `source/thanksgiving-2026-turkey-art-whole-pie.png` (Codex edit, Nov 21, 2026). |
| `seasonal/thanksgiving-2026-turkey-suspect-banner.jpg` | 1200 × 1044 | full width (about 550) | **Used in the Nov 26 email** (replaces the banner above): the same turkey as the suspect (sly side-eye, whistling, crumbs on its beak, fork behind its back), one slice gone with the whipped cream centered and cut through (within 2 px), a copper-outlined evidence tag "MISSING SLICE: UNDER INVESTIGATION" (Futura Condensed ExtraBold 40, navy) and "Happy Thanksgiving, / Mega Team." (Georgia Bold 64, navy) on flat #FEF4E6. Concept from the CMO and an outside creative director, tag layout from an outside designer; Justin approved Nov 21. Art: `source/thanksgiving-2026-turkey-art-suspect.png`. New file names on purpose: Gmail's image proxy may have cached the earlier files. |

The `-tile` files are the logo on a white rounded tile, made at 3× so they stay sharp on phones.

## Dark mode rules (learned October 26–27, 2026)

1. **Email apps change colors in dark mode, never pictures.** The Gmail phone app flips colors both
   ways: a white header turned black and a navy panel turned light blue (iPhone, October 27, 2026).
2. **So every logo in an email carries its own background inside the picture.** Use the `-tile` files.
   A logo without a background (`mega-logo-navy.png`) vanished on the flipped black header.
3. **Don't count on any background color staying put.** Design so the email still reads if it flips.
4. **Check partner logos before using them.** One with a solid background (SpotOn's black-on-white
   logo) is safe; one without a background needs a tile like ours.
5. **Web pages and PDFs aren't flipped by the browser.** There, switch logos with the snippet below,
   or just use the tile.
6. **Test every new email in dark mode:** send it to yourself and open it on an iPhone with dark mode on.

## Copy-paste

Email header logo (the tile has 9 px of white inside each edge, so give its cell 9 px less padding on
the left and the logo lines up with the text below):

```html
<img src="https://jhaag93.github.io/mega-signature-images/mega-logo-tile-header.png" width="120" height="46" alt="Mega Payments" style="display:block;width:120px;height:46px;border:0">
```

Web page logo that follows the reader's light or dark setting:

```html
<picture>
  <source srcset="https://jhaag93.github.io/mega-signature-images/mega-logo-white.png" media="(prefers-color-scheme: dark)">
  <img src="https://jhaag93.github.io/mega-signature-images/mega-logo-navy.png" width="110" height="35" alt="Mega Payments">
</picture>
```

## Never

- Rename, move or delete a published file. Sent emails link to these exact addresses.
- Use `mega-logo-navy.png` or `mega-logo-white.png` in an email.
