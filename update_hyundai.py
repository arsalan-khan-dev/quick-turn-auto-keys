import os

filepath = r"C:\Users\97ars\.gemini\antigravity-ide\scratch\quick-turn-auto-keys\brands\hyundai.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero replacement
hero_old = """<p>Hyundai's range — from the popular i10, i20 and i30 to the Tucson, Santa Fe and the latest IONIQ electric vehicles — uses transponder and smart key systems that require specialist programming equipment. Our mobile team handles Hyundai key replacement, fob repair and lockout services on-site, for petrol, hybrid and fully electric models.</p>"""
hero_new = """<p>Hyundai's range — from the popular i10, i20 and i30 to the Tucson, Santa Fe and the latest IONIQ electric vehicles — uses transponder and smart key systems that require specialist programming equipment. Our mobile team handles Hyundai key replacement, fob repair and lockout services on-site, for petrol, hybrid and fully electric models. Whether you're stranded at home, at work, or on the roadside anywhere in Greater London, our fully equipped mobile vans arrive with the blank keys, transponder chips, and programming software required to get you back on the road the very same day. We pride ourselves on rapid response times and non-destructive entry methods.</p>"""

content = content.replace(hero_old, hero_new)

# 2. Why a specialist replacement
spec_old = """<p style="margin-top:16px;">Hyundai owners may need a specialist rather than a general key cutter when a key is lost, a key is damaged, or a key stops responding.</p>"""
spec_new = """<p style="margin-top:16px;">Modern Hyundai vehicles, particularly the newer i-range and electric IONIQ series, utilize highly advanced rolling-code immobilisers and smart proximity systems. If you lose your only key, a standard high-street key cutter cannot generate a new one because the vehicle's ECU (Engine Control Unit) must be accessed directly to authorize a new transponder. Our mobile auto locksmiths carry dealership-level diagnostic equipment tailored specifically for Korean domestic and European-market Hyundai models. This allows us to securely bypass active immobilisers, extract the necessary PIN codes, and program a new key fob on the roadside—saving you the expense and weeks of waiting associated with main dealer recovery.</p>
        <p style="margin-top:16px;">Hyundai owners may need a specialist rather than a general key cutter when a key is lost, a key is damaged, or a key stops responding.</p>"""

content = content.replace(spec_old, spec_new)

# 3. New section
new_section = """<!-- ==================== COMMON ISSUES ==================== -->
<section class="section">
  <div class="container">
    <div class="reveal section-head center">
      <div class="eyebrow">Hyundai Key Problems</div>
      <h2>Common Hyundai Key &amp; Lock Issues We Resolve</h2>
      <p>We see a wide variety of Hyundai key faults across London. Here are the most common issues our mobile locksmiths fix on a daily basis:</p>
    </div>
    
    <div class="feature-grid">
      <div class="reveal feature-item">
        <h3>Ignition Barrel Wear on Older Models</h3>
        <p>Older models like the early Hyundai i10 or Getz often suffer from worn ignition barrels or degraded physical key blades. If your key is sticking, refusing to turn, or won't pull out of the ignition, our technicians can repair or replace the barrel on-site, re-pinning it to match your existing door locks.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Smart Key De-synchronisation</h3>
        <p>Proximity keys for the Tucson, Santa Fe, and IONIQ ranges can occasionally lose sync with the vehicle due to flat batteries or RF interference. We provide mobile re-synchronisation and diagnostic testing to ensure your push-to-start functions work flawlessly.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Broken Key Shells and Snapped Blades</h3>
        <p>Hyundai flip keys (commonly used on the i20 and i30) are prone to the hinge mechanism snapping or the rubber buttons degrading over time. Instead of charging you for a full replacement, we can often transfer your existing internal circuit board into a brand-new, reinforced aftermarket shell and cut a fresh blade.</p>
      </div>
    </div>
  </div>
</section>

<!-- ==================== MOBILE SERVICES ==================== -->"""

content = content.replace("<!-- ==================== MOBILE SERVICES ==================== -->", new_section)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Hyundai content updated successfully.")
