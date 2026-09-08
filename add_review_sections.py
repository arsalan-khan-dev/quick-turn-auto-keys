import os

base_dir = r"C:\Users\97ars\.gemini\antigravity-ide\scratch\quick-turn-auto-keys"

review_section = """
<!-- ==================== REVIEWS ==================== -->
<section class="section section--surface-bordered">
  <div class="container">
    <div class="split">
      <div class="reveal split-copy">
        <div class="eyebrow">Customer Feedback</div>
        <h2>Happy with our service? Let others know!</h2>
        <p>As a mobile-only auto locksmith, your public reviews mean the world to us. They help other drivers in emergency situations find reliable and fast assistance.</p>
        <a href="https://share.google/TKAA7RcerROkTsu9L" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="margin-top: 16px; display: inline-flex; align-items: center; gap: 8px;">
          <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M21.35,11.1H12.18V13.83H18.69C18.36,17.64 15.19,19.27 12.19,19.27C8.36,19.27 5,16.25 5,12C5,7.9 8.2,4.73 12.2,4.73C15.29,4.73 17.1,6.7 17.1,6.7L19,4.72C19,4.72 16.56,2 12.1,2C6.42,2 2.03,6.8 2.03,12C2.03,17.05 6.16,22 12.25,22C17.6,22 21.5,18.33 21.5,12.91C21.5,11.76 21.35,11.1 21.35,11.1V11.1Z"/></svg>
          Leave a Review on Google
        </a>
      </div>
      <div class="reveal split-visual" style="display:flex; justify-content:center; align-items:center; background: var(--surface-1); border-radius: var(--radius-lg); padding: 2rem; border: 1px solid var(--border-color);">
        <div style="text-align: center;">
          <h3 style="font-size: 3rem; color: #f59e0b; margin-bottom: 0;">★★★★★</h3>
          <p style="font-weight: 600; margin-top: 8px;">Rate us on Google Maps</p>
        </div>
      </div>
    </div>
  </div>
</section>

"""

files_to_update = ["index.html", "contact.html"]

for filename in files_to_update:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "<!-- ==================== REVIEWS ==================== -->" not in content:
        content = content.replace("<!-- ==================== CTA BAND ==================== -->", review_section + "<!-- ==================== CTA BAND ==================== -->")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"Review section already exists in {filename}")

