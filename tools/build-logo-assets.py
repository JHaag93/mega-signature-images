"""Rebuild the Mega logo files from source/mega-logo-original.png (megapayments.com/mega-logo.png).

Usage: python3 tools/build-logo-assets.py <brand-folder>

Writes, into the brand folder:
  mega-logo-tile.png         white rounded tile, 234 x 90  (shown at 78 x 30)  - email signature
  mega-logo-tile-header.png  white rounded tile, 360 x 138 (shown at 120 x 46) - email headers
  mega-logo-navy.png         navy logo, no background     - web pages and PDFs on LIGHT backgrounds only
  mega-logo-white.png        white logo, no background    - web pages and PDFs on NAVY backgrounds only
"""
import os, sys
from PIL import Image, ImageDraw, ImageFilter

def clean_logo(path):
    """Keep only the five big shapes (m, e, g, a, chevron); drop the stray specks the original has."""
    src = Image.open(path).convert('RGBA'); w, h = src.size; px = src.load()
    seen, keep = set(), Image.new('L', (w, h), 0); kp = keep.load()
    for y in range(h):
        for x in range(w):
            if px[x, y][3] > 20 and (x, y) not in seen:
                stack, pts = [(x, y)], []; seen.add((x, y))
                while stack:
                    cx, cy = stack.pop(); pts.append((cx, cy))
                    for nx, ny in ((cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)):
                        if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in seen and px[nx, ny][3] > 20:
                            seen.add((nx, ny)); stack.append((nx, ny))
                if len(pts) > 500:
                    for p in pts: kp[p] = 255
    keep = keep.filter(ImageFilter.MaxFilter(5))
    src.putalpha(Image.composite(src.getchannel('A'), Image.new('L', (w, h), 0), keep))
    return src.crop(keep.getbbox())

def tile(logo, disp_w, disp_h, pad_x, pad_y, radius, scale=3):
    """Logo flattened onto a white rounded tile. The white is part of the picture, so email dark mode can't remove it."""
    flat = Image.new('RGBA', logo.size, (255, 255, 255, 255)); flat.alpha_composite(logo)
    tw, th = disp_w * scale, disp_h * scale
    lw = tw - 2 * pad_x * scale; lh = round(flat.height * lw / flat.width)
    if lh > th - 2 * pad_y * scale:
        lh = th - 2 * pad_y * scale; lw = round(flat.width * lh / flat.height)
    flat = flat.resize((lw, lh), Image.LANCZOS)
    mask = Image.new('L', (tw * 4, th * 4), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, tw * 4 - 1, th * 4 - 1], radius=radius * scale * 4, fill=255)
    out = Image.composite(Image.new('RGBA', (tw, th), (255, 255, 255, 255)),
                          Image.new('RGBA', (tw, th), (255, 255, 255, 0)), mask.resize((tw, th), Image.LANCZOS))
    out.alpha_composite(flat, ((tw - lw) // 2, (th - lh) // 2))
    return out

def padded(img, frac=0.06):
    m = round(img.height * frac); out = Image.new('RGBA', (img.width + 2 * m, img.height + 2 * m), (0, 0, 0, 0))
    out.alpha_composite(img, (m, m)); return out

if __name__ == '__main__':
    d = sys.argv[1]
    logo = clean_logo(os.path.join(d, 'source', 'mega-logo-original.png'))
    tile(logo, 78, 30, 7, 6, 4).save(os.path.join(d, 'mega-logo-tile.png'), optimize=True)
    tile(logo, 120, 46, 9, 8, 6).save(os.path.join(d, 'mega-logo-tile-header.png'), optimize=True)
    padded(logo).save(os.path.join(d, 'mega-logo-navy.png'), optimize=True)
    white = logo.copy(); white.putdata([(255, 255, 255, a) for (_, _, _, a) in logo.getdata()])
    padded(white).save(os.path.join(d, 'mega-logo-white.png'), optimize=True)
    for f in ('mega-logo-tile.png', 'mega-logo-tile-header.png', 'mega-logo-navy.png', 'mega-logo-white.png'):
        print(f, Image.open(os.path.join(d, f)).size)
