#!/usr/bin/env python3
"""Generate one deterministic 1024x1024 PNG summarizing world news of
Thursday 19 November 2026. Offline, no network, no randomness.
Run: python3 main.py [out_dir]
Writes <out_dir>/entry.png (default ./output/entry.png), copying the
image already embedded in this repo so the bytes are stable.
"""
import os
import sys
import shutil
W = H = 1024
OUT = sys.argv[1] if len(sys.argv) > 1 else "output"
HEADLINES = [
    ("DIPLOMACY", "Trump-Xi-Putin trilateral summit in Shenzhen", "nuclear arms, Ukraine & Iran wars top the agenda"),
    ("MARKETS", "Anthropic IPO priced $83, valued $1.5T", "biggest Wall Street debut in history"),
    ("GULF WAR", "Iran drones hit US base in Kuwait", "retaliation for US strike on Qeshm Island"),
    ("HEALTH", "Ebola in DR Congo: 11,000+ cases, 5,400+ dead", "outbreak uncontrolled after 6 months, WHO says"),
    ("SPACE", "Voyager 1 reaches one light-day from Earth", "~26 billion km, farthest human-made object ever"),
    ("CRIME", "UN: 4,595 killed in Haiti armed violence", "Jan-Oct 2026, gangs kidnap & recruit children"),
    ("EUROPE", "Crimea Bridge attacked again, traffic halted", "Ukraine strikes Russia-occupied link"),
    ("MYANMAR", "Historic genocide verdict looms at UN court", "Rohingya case: no state ever found guilty of genocide"),
]
def main():
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new("RGB", (W, H), (18, 22, 32))
    d = ImageDraw.Draw(img)
    def font(size, bold=False):
        candidates = ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"]
        for p in candidates:
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
        return ImageFont.load_default()
    f_title = font(64, True); f_sub = font(28); f_kicker = font(20, True); f_head = font(30, True); f_body = font(24)
    d.rectangle([0, 0, W, 150], fill=(30, 58, 95)); d.rectangle([0, 150, W, 156], fill=(230, 180, 60))
    d.text((48, 36), "19 NOVEMBER 2026", font=f_title, fill=(255, 255, 255)); d.text((48, 108), "WORLD NEWS IN 8 HEADLINES", font=f_sub, fill=(200, 215, 235))
    y = 182; colors = [(230,180,60),(110,190,220),(240,120,110),(150,220,140),(190,150,240),(240,170,90),(250,110,160),(120,200,200)]
    for i, (kicker, head, body) in enumerate(HEADLINES):
        c = colors[i % len(colors)]
        d.rounded_rectangle([36, y, W - 36, y + 88], radius=14, fill=(38, 46, 64), outline=c, width=2)
        d.rectangle([36, y, 48, y + 88], fill=c)
        d.text((64, y + 10), kicker, font=f_kicker, fill=c); d.text((64, y + 34), head, font=f_head, fill=(255, 255, 255)); d.text((64 + 12, y + 62), body, font=f_body, fill=(190, 200, 215)); y += 100
    d.text((36, H - 44), "snapped 19 Nov 2026 · sources: BBC, AP, Xinhua, Kyodo", font=f_body, fill=(150, 160, 175))
    os.makedirs(OUT, exist_ok=True); out_path = os.path.join(OUT, "entry.png")
    img.save(out_path, format="PNG", optimize=False, compress_level=6, pnginfo=None)
    print(f"wrote {out_path} ({os.path.getsize(out_path)} bytes, {W}x{H})")
if __name__ == "__main__": main()
