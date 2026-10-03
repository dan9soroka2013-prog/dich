import numpy as np
from PIL import Image, ImageFilter, ImageDraw

width, height = 612, 459
mask = Image.new('L', (width, height), 0)
draw = ImageDraw.Draw(mask)

# 1
draw.rectangle([165, 270, 275, 310], fill=255)
draw.rectangle([205, 110, 260, 270], fill=255)
draw.rectangle([165, 110, 205, 150], fill=255)

# 2
draw.rectangle([305, 110, 415, 150], fill=255)
draw.rectangle([360, 150, 415, 210], fill=255)
draw.rectangle([305, 210, 415, 250], fill=255)
draw.rectangle([305, 250, 360, 270], fill=255)
draw.rectangle([305, 270, 415, 310], fill=255)

# .
draw.rectangle([460, 290, 480, 310], fill=255)

glow = mask.filter(ImageFilter.GaussianBlur(radius=25))
glow_intense = mask.filter(ImageFilter.GaussianBlur(radius=8))

final_img = Image.new('RGB', (width, height), 'black')
glow_rgb = Image.merge('RGB', (glow, glow, glow))
glow_intense_rgb = Image.merge('RGB', (glow_intense, glow_intense, glow_intense))
sharp_rgb = Image.merge('RGB', (mask, mask, mask))

arr_glow = np.array(glow_rgb).astype(float) * 0.4
arr_intense = np.array(glow_intense_rgb).astype(float) * 0.5
arr_sharp = np.array(sharp_rgb).astype(float)

arr_final = np.clip(arr_glow + arr_intense + arr_sharp, 0, 255).astype(np.uint8)
output_image = Image.fromarray(arr_final)

import os
os.makedirs('/tmp/generated', exist_ok=True)
output_image.save('/tmp/generated/12_retro_glow.png')
print("Saved successfully to /tmp/generated/12_retro_glow.png")
