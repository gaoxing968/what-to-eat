from PIL import Image, ImageDraw, ImageFont
import math, os

base = r'C:\Users\Administrator\what-to-eat\icons'
os.makedirs(base, exist_ok=True)

def make_icon(size, fname):
    img = Image.new('RGBA', (size, size), (15, 15, 26, 255))
    draw = ImageDraw.Draw(img)
    r = size // 2
    cx, cy = r, r
    for y in range(size):
        for x in range(size):
            dist = ((x-cx)**2 + (y-cy)**2) ** 0.5
            if dist <= r:
                t = dist / r
                red = int(231 * (1 - t * 0.6))
                green = int(76 * (1 - t * 0.6))
                blue = int(60 + int(t * 40))
                draw.point((x, y), (red, green, blue, 255))
    emoji = '\U0001F3A1'
    try:
        font = ImageFont.truetype(r'C:\Windows\Fonts\seguiemj.ttf', int(size * 0.5))
    except:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), emoji, font=font)
    ew = bbox[2] - bbox[0]
    eh = bbox[3] - bbox[1]
    draw.text(((size-ew)//2 - bbox[0], (size-eh)//2 - bbox[1]), emoji, font=font)
    path = os.path.join(base, fname)
    img.save(path)
    print(f'Saved {path}')

make_icon(192, 'icon-192.png')
make_icon(512, 'icon-512.png')