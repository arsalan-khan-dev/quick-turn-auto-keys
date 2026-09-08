import os
import re

base_dir = r"C:\Users\97ars\.gemini\antigravity-ide\scratch\quick-turn-auto-keys"

# 1. Update css/components.css to center CTA band
css_path = os.path.join(base_dir, "css", "components.css")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

# Replace .cta-band .container rules
old_cta_css = """.cta-band .container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 32px;
  flex-wrap: wrap;
}"""

new_cta_css = """.cta-band .container {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  text-align: center;
  gap: 24px;
}"""

if old_cta_css in css_content:
    css_content = css_content.replace(old_cta_css, new_cta_css)
elif "justify-content: space-between;" in css_content and ".cta-band .container" in css_content:
    # Use regex if spacing differs
    css_content = re.sub(
        r'\.cta-band \.container\s*\{[^}]*\}',
        new_cta_css,
        css_content
    )

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content)


# 2. Update index.html to center the checklist block
index_path = os.path.join(base_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

# Change the text-align:left of the container to text-align:center
old_container = '<div class="testimonial-pending" style="text-align:left; max-width: 600px; margin: 0 auto; padding: 2rem;">'
new_container = '<div class="testimonial-pending" style="text-align:center; max-width: 600px; margin: 0 auto; padding: 2rem;">'
index_html = index_html.replace(old_container, new_container)

# Wrap the ul with a flex container to center the left-aligned list
old_ul = '<ul class="checklist" style="list-style:none; padding:0; margin:0; text-align:left;">'
new_ul = '<div style="display: flex; justify-content: center;">\n            <ul class="checklist" style="list-style:none; padding:0; margin:0; text-align:left;">'
index_html = index_html.replace(old_ul, new_ul)

# Find the end of the ul and close the div
old_ul_close = '</ul>\n        </div>\n      </div>\n    </section>'
new_ul_close = '</ul>\n          </div>\n        </div>\n      </div>\n    </section>'

# Let's do it safer with regex
if '<div style="display: flex; justify-content: center;">' in new_ul:
    index_html = re.sub(r'(</ul>\s*)(</div>\s*</div>\s*</section>)', r'\1</div>\n        \2', index_html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)

print("CSS and HTML updated for center alignments.")
