import os
import re
import glob

base_dir = r"C:\Users\97ars\.gemini\antigravity-ide\scratch\quick-turn-auto-keys"

# 1. Generate reviews.html
about_path = os.path.join(base_dir, "about.html")
with open(about_path, "r", encoding="utf-8") as f:
    about_html = f.read()

# Extract head and footer
match_head = re.search(r'(.*?)(<main id="main">)', about_html, re.DOTALL)
match_footer = re.search(r'(</main>.*)', about_html, re.DOTALL)

if match_head and match_footer:
    head_and_nav = match_head.group(1)
    footer = match_footer.group(1)
    
    # Update title and meta
    head_and_nav = re.sub(r'<title>.*?</title>', '<title>Customer Reviews | Quick Turn Auto Keys</title>', head_and_nav, flags=re.DOTALL)
    head_and_nav = re.sub(r'<meta name="description"\s*content=".*?">', '<meta name="description" content="Read our customer reviews or leave a review on Google for Quick Turn Auto Keys.">', head_and_nav, flags=re.DOTALL)
    head_and_nav = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Customer Reviews | Quick Turn Auto Keys">', head_and_nav)
    head_and_nav = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="Read our customer reviews or leave a review on Google for Quick Turn Auto Keys.">', head_and_nav)
    head_and_nav = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://auttokeys.com/reviews.html">', head_and_nav)
    head_and_nav = head_and_nav.replace('"name": "About",\n      "item": "https://auttokeys.com/about.html"', '"name": "Reviews",\n      "item": "https://auttokeys.com/reviews.html"')

    main_body = """<main id="main">

<div class="container">
  <nav class="breadcrumbs" aria-label="Breadcrumb">
    <a href="index.html">Home</a>
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
    <span class="current">Reviews</span>
  </nav>
</div>

<!-- ==================== PAGE HERO ==================== -->
<section class="hero hero--padded">
  <div class="container">
    <div class="hero-copy max-w-720">
      <div class="eyebrow">Customer Feedback</div>
      <h1>Rate our <span class="accent-word">mobile locksmith</span> service</h1>
      <p class="max-w-600">At Quick Turn Auto Keys, we take pride in delivering fast, reliable, and professional mobile locksmith services. As a mobile-only business, your feedback helps us reach more drivers in need of emergency assistance.</p>
      
      <div style="background: var(--surface-2); padding: 2rem; border-radius: var(--radius-lg); margin-top: 2rem; border: 1px solid var(--border-color);">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">Leave us a review on Google</h2>
        <p style="margin-bottom: 1.5rem; color: var(--text-muted);">Have we helped you with a replacement key or lockout? We'd love to hear about your experience.</p>
        <a href="https://share.google/TKAA7RcerROkTsu9L" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="display: inline-flex; align-items: center; gap: 8px;">
          <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M21.35,11.1H12.18V13.83H18.69C18.36,17.64 15.19,19.27 12.19,19.27C8.36,19.27 5,16.25 5,12C5,7.9 8.2,4.73 12.2,4.73C15.29,4.73 17.1,6.7 17.1,6.7L19,4.72C19,4.72 16.56,2 12.1,2C6.42,2 2.03,6.8 2.03,12C2.03,17.05 6.16,22 12.25,22C17.6,22 21.5,18.33 21.5,12.91C21.5,11.76 21.35,11.1 21.35,11.1V11.1Z"/></svg>
          Review on Google Maps
        </a>
      </div>

    </div>
  </div>
</section>

</main>
"""
    
    reviews_html = head_and_nav + main_body + footer
    with open(os.path.join(base_dir, "reviews.html"), "w", encoding="utf-8") as f:
        f.write(reviews_html)
    print("reviews.html created.")


# 2. Update sitemap.xml
sitemap_path = os.path.join(base_dir, "sitemap.xml")
if os.path.exists(sitemap_path):
    with open(sitemap_path, "r", encoding="utf-8") as f:
        sitemap = f.read()
    
    if "reviews.html" not in sitemap:
        review_url = """
  <url>
    <loc>https://auttokeys.com/reviews.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>"""
        insert_idx = sitemap.rfind('</urlset>')
        if insert_idx != -1:
            sitemap = sitemap[:insert_idx] + review_url + "\n" + sitemap[insert_idx:]
            with open(sitemap_path, "w", encoding="utf-8") as f:
                f.write(sitemap)
            print("sitemap.xml updated.")


# 3. Update all HTML files (Nav and Footer links)
html_files = []
for root, _, files in os.walk(base_dir):
    if "node_modules" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

for filepath in html_files:
    rel_depth = filepath.replace(base_dir, "").count(os.sep) - 1
    prefix = "../" * rel_depth if rel_depth > 0 else ""
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Desktop Nav
    nav_search = f'<li><a href="{prefix}faq.html">FAQ</a></li>'
    nav_replace = f'<li><a href="{prefix}faq.html">FAQ</a></li>\n        <li><a href="{prefix}reviews.html">Reviews</a></li>'
    if nav_search in content and f'href="{prefix}reviews.html"' not in content:
        content = content.replace(nav_search, nav_replace)

    # Footer Nav
    footer_search = f'<li><a href="{prefix}faq.html">FAQs</a></li>'
    footer_replace = f'<li><a href="{prefix}faq.html">FAQs</a></li>\n          <li><a href="{prefix}reviews.html">Reviews</a></li>'
    if footer_search in content:
        content = content.replace(footer_search, footer_replace)

    # Contact page specific CTA update
    if filepath.endswith("contact.html"):
        contact_cta = """
      <div class="contact-box" style="margin-top: 2rem;">
        <h3>Rate our Service</h3>
        <p>If we've helped you get back on the road, please consider leaving a public review.</p>
        <a href="https://share.google/TKAA7RcerROkTsu9L" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="margin-top: 1rem; width: 100%; display: flex; justify-content: center;">Review on Google Maps</a>
      </div>
"""
        if "Rate our Service" not in content:
            # Inject after the first contact-box or before the contact-form
            # Let's find <div class="contact-form">
            content = content.replace('<div class="contact-form">', contact_cta + '\n      <div class="contact-form">')
            
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("All HTML files updated.")
