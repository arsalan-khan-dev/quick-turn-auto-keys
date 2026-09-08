import os
import re

filepath = r"C:\Users\97ars\.gemini\antigravity-ide\scratch\quick-turn-auto-keys\brands\skoda.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

hero = " Whether you're stranded at home, at work, or on the roadside anywhere in Greater London, our fully equipped mobile vans arrive with the blank keys, transponder chips, and VAG-specific programming software required to get you back on the road the very same day. We pride ourselves on rapid response times and non-destructive entry methods."
specialist = "Modern Skoda vehicles utilize highly advanced immobilisers, sharing the MQB and MLB platforms with the rest of the Volkswagen Audi Group. If you lose your only key, a standard high-street key cutter cannot generate a new one because the vehicle's dashboard cluster or ECU must be accessed to authorize a new transponder. Our mobile auto locksmiths carry dealership-level diagnostic equipment tailored specifically for VAG vehicles. This allows us to securely bypass active immobilisers, extract the necessary Component Security (CS) codes, and program a new key fob on the roadside—saving you the expense and weeks of waiting associated with main dealer recovery."
issues = """<!-- ==================== COMMON ISSUES ==================== -->
<section class="section">
  <div class="container">
    <div class="reveal section-head center">
      <div class="eyebrow">Skoda Key Problems</div>
      <h2>Common Skoda Key &amp; Lock Issues We Resolve</h2>
      <p>We see a wide variety of Skoda key faults across London. Here are the most common issues our mobile locksmiths fix on a daily basis:</p>
    </div>
    
    <div class="feature-grid">
      <div class="reveal feature-item">
        <h3>Ignition Barrel Sticking (Octavia &amp; Fabia)</h3>
        <p>Many Skoda models suffer from steering lock housing or ignition barrel failure, where the key becomes difficult to turn or gets trapped inside. We can safely extract the key, repair the barrel, and replace the housing if necessary on-site.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Broken Flip Key Shells</h3>
        <p>Skoda flip keys are prone to the hinge snapping or the rubber buttons degrading and falling out over time. Instead of replacing the entire key, we can transfer your existing circuit board and transponder into a reinforced aftermarket shell and cut a fresh blade.</p>
      </div>
      <div class="reveal feature-item">
        <h3>KESSY (Keyless Entry) Range Issues</h3>
        <p>Modern Skodas equipped with the KESSY smart key system can suffer from reduced range or failure due to drops and water damage. We provide rapid diagnostic testing and replacement smart keys programmed directly to your vehicle's profile.</p>
      </div>
    </div>
  </div>
</section>

"""

# 1. Hero Addition
match_hero = re.search(r'(<div class="reveal hero-copy">.*?)(</p>)', content, re.DOTALL)
if match_hero:
    content = content[:match_hero.start(2)] + hero + content[match_hero.start(2):]

# 2. Why a Specialist Addition
match_split = re.search(r'(<div class="reveal split-copy">.*?)(<p[^>]*>.*?</p>)\s*(</div>)', content, re.DOTALL)
if match_split:
    split_content = match_split.group(1) + f'<p style="margin-top:16px;">{specialist}</p>\n            ' + match_split.group(2) + match_split.group(3)
    content = content[:match_split.start()] + split_content + content[match_split.end():]

# 3. New Section
match_mobile = re.search(r'<!-- ==================== SERVICE AVAILABILITY', content)
if match_mobile:
    content = content[:match_mobile.start()] + issues + content[match_mobile.start():]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Skoda fixed.")
