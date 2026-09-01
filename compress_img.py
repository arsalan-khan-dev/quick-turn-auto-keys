from PIL import Image
import os

filepath = r'assets\images\logo\og-image.png'
outpath = r'assets\images\logo\og-image.jpg'
try:
    img = Image.open(filepath)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save(outpath, 'JPEG', quality=85)
    print("Saved as JPEG.")
except Exception as e:
    print(f"Error: {e}")