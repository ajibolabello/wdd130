from PIL import Image
import os

img_path = "images/profile.jpg"
img = Image.open(img_path)

# Resize to a web-friendly dimension (e.g., max 600px width/height)
img.thumbnail((600, 600))

# Reduce quality until the file size drops below 125 KB
quality = 85
while quality > 10:
    img.save(img_path, "JPEG", quality=quality)
    if os.path.getsize(img_path) < 125 * 1024:
        break
print(f"Success! Final size: {os.path.getsize(img_path) / 1024:.1f} KB")