import os
import re
import glob

# 1. Minify CSS
css_dir = r"C:\Users\97ars\.gemini\antigravity-ide\scratch\quick-turn-auto-keys\css"
css_files = ["tokens.css", "global.css", "components.css", "responsive.css"]

def minify_css(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([\{\}\:\;\,\>])\s*', r'\1', css)
    css = re.sub(r';}', '}', css)
    return css.strip()

for filename in css_files:
    filepath = os.path.join(css_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    minified = minify_css(content)
    min_filename = filename.replace('.css', '.min.css')
    with open(os.path.join(css_dir, min_filename), 'w', encoding='utf-8') as f:
        f.write(minified)
print("CSS files minified.")

# 2. HTML Updates
html_files = []
base_dir = r"C:\Users\97ars\.gemini\antigravity-ide\scratch\quick-turn-auto-keys"
for root, _, files in os.walk(base_dir):
    if "node_modules" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

font_preload = """
<link rel="preload" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=Inter:wght@400;500;600&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=Inter:wght@400;500;600&display=swap"></noscript>
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update CSS links to .min.css
    content = content.replace('href="css/tokens.css"', 'href="css/tokens.min.css"')
    content = content.replace('href="css/global.css"', 'href="css/global.min.css"')
    content = content.replace('href="css/components.css"', 'href="css/components.min.css"')
    content = content.replace('href="css/responsive.css"', 'href="css/responsive.min.css"')
    
    content = content.replace('href="../css/tokens.css"', 'href="../css/tokens.min.css"')
    content = content.replace('href="../css/global.css"', 'href="../css/global.min.css"')
    content = content.replace('href="../css/components.css"', 'href="../css/components.min.css"')
    content = content.replace('href="../css/responsive.css"', 'href="../css/responsive.min.css"')

    # Preload Fonts (replace existing link)
    old_font_link = '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
    if old_font_link in content:
        content = content.replace(old_font_link, font_preload)

    # Preload LCP Images
    # For index.html
    if filepath.endswith("index.html"):
        hero_img = '<link rel="preload" as="image" href="assets/images/services imgs/data (7).webp">'
        if hero_img not in content:
            content = content.replace('</head>', f'{hero_img}\n</head>')
    
    # For quote.html
    elif filepath.endswith("quote.html"):
        hero_img = '<link rel="preload" as="image" href="assets/images/services imgs/data (4).webp">'
        if hero_img not in content:
            content = content.replace('</head>', f'{hero_img}\n</head>')
            
    # For brands/*.html
    elif "brands\\" in filepath:
        # We need to find the specific hero image for that brand
        match = re.search(r'<img[^>]*src="([^"]+)"[^>]*alt="[^"]*hero[^"]*"', content, re.IGNORECASE)
        # If no explicit hero alt, let's find the first image in the hero section
        if not match:
             match = re.search(r'hero-visual.*?<img[^>]*src="([^"]+)"', content, re.IGNORECASE | re.DOTALL)
             
        if match:
            img_src = match.group(1)
            hero_img = f'<link rel="preload" as="image" href="{img_src}">'
            if hero_img not in content:
                content = content.replace('</head>', f'{hero_img}\n</head>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML files updated with performance optimizations.")
