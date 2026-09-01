from PIL import Image
import os

filepath = r'assets\images\logo\og-image.png'
img = Image.open(filepath)
print(f"Dimensions: {img.size}")