import re

# Update service-areas.html
filepath = r"C:\Users\97ars\.gemini\antigravity-ide\scratch\quick-turn-auto-keys\service-areas.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add links to main regions
regions = [
    ("Central London", "central-london"),
    ("North London", "north-london"),
    ("South London", "south-london"),
    ("East London", "east-london"),
    ("West London", "west-london"),
]

for name, slug in regions:
    link_html = f'<a href="locations/{slug}.html" class="text-link" style="margin-top:14px;">View {name} <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>'
    # Find the paragraph for this region and append the link
    pattern = re.compile(f'(<h3>{name}</h3>\n\\s*<p>.*?</p>)')
    content = pattern.sub(f'\\1\n        {link_html}', content)

# Add links to surrounding areas
content = content.replace("Surrey", '<a href="locations/surrey.html" style="text-decoration: underline; color: inherit;">Surrey</a>')
content = content.replace("Kent", '<a href="locations/kent.html" style="text-decoration: underline; color: inherit;">Kent</a>')
content = content.replace("Essex", '<a href="locations/essex.html" style="text-decoration: underline; color: inherit;">Essex</a>')
content = content.replace("Hertfordshire", '<a href="locations/hertfordshire.html" style="text-decoration: underline; color: inherit;">Hertfordshire</a>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# Update sitemap.xml
sitemap_path = r"C:\Users\97ars\.gemini\antigravity-ide\scratch\quick-turn-auto-keys\sitemap.xml"
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap = f.read()

new_urls = []
for slug in ["central-london", "north-london", "south-london", "east-london", "west-london", "surrey", "kent", "essex", "hertfordshire"]:
    new_urls.append(f"""
  <url>
    <loc>https://auttokeys.com/locations/{slug}.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>""")

insert_idx = sitemap.rfind('</urlset>')
if insert_idx != -1:
    sitemap = sitemap[:insert_idx] + "".join(new_urls) + "\n" + sitemap[insert_idx:]

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap)

print("Updated service-areas.html and sitemap.xml successfully.")
