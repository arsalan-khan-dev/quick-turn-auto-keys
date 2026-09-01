import glob
import re

files = glob.glob('**/*.html', recursive=True)
count = 0
for file in files:
    if '404' in file: continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    # Replace og-image.png with jpg
    content = content.replace('og-image.png', 'og-image.jpg')
    
    # Add twitter:image if missing
    if 'twitter:image' not in content:
        content = content.replace(
            '<meta name="twitter:card" content="summary_large_image">',
            '<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:image" content="https://auttokeys.com/assets/images/logo/og-image.jpg">'
        )
        
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
print(f"Updated {count} HTML files with og-image.jpg and twitter:image")