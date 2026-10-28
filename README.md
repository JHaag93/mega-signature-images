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
