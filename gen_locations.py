import os
import re

locations = {
    "central-london": {
        "name": "Central London",
        "title": "Auto Locksmith Central London | Mobile Car Key Replacement",
        "description": "Mobile auto locksmith in Central London. Fast car key replacement, programming, and lockout assistance. We cover the Congestion Charge \u0026 ULEZ zones.",
        "hero_desc": "Stranded in the heart of the city? Navigating Central London's busy streets, Congestion Charge zones, and tight parking spaces is no problem for our mobile locksmiths. We come directly to you for fast car key replacement, programming, and non-destructive vehicle entry.",
        "split_desc": "Whether you're parked near a busy commercial district, an underground car park, or stuck roadside, our fully-equipped vans and motorcycles carry the diagnostic tools needed to cut and program keys on the spot. We understand that losing keys in Central London requires a rapid response."
    },
    "north-london": {
        "name": "North London",
        "title": "Auto Locksmith North London | Mobile Car Key Replacement",
        "description": "Mobile auto locksmith in North London. Fast car key replacement, programming, and lockout assistance across all North London boroughs.",
        "hero_desc": "From residential streets in Islington and Camden to the busy A1 and M1 corridors, our mobile auto locksmiths provide comprehensive coverage across North London. If you've lost your car keys or need an urgent spare, we bring the workshop to your location.",
        "split_desc": "You don't need to arrange costly recovery to a dealership. Our technicians arrive with advanced key cutting machinery and dealer-level programming software to replace your lost or broken transponder keys right where your vehicle is parked in North London."
    },
    "south-london": {
        "name": "South London",
        "title": "Auto Locksmith South London | Mobile Car Key Replacement",
        "description": "Mobile auto locksmith in South London. Fast car key replacement, programming, and lockout assistance covering South East \u0026 South West London.",
        "hero_desc": "Covering both South East and South West London, our mobile auto locksmith service ensures you're never left stranded south of the river. From Croydon and Bromley to Wandsworth, we provide rapid on-site car key replacement and emergency lockout assistance.",
        "split_desc": "We know that relying on public transport in parts of South London can be difficult, making your vehicle essential. That's why our mobile vans carry the necessary blank keys and programming equipment to get you back on the road the very same day."
    },
    "east-london": {
        "name": "East London",
        "title": "Auto Locksmith East London | Mobile Car Key Replacement",
        "description": "Mobile auto locksmith in East London. Fast car key replacement, programming, and lockout assistance from Canary Wharf to the Essex borders.",
        "hero_desc": "Whether you're working in Canary Wharf, shopping in Stratford, or living near the Essex borders, our mobile auto locksmiths cover the entirety of East London. We specialise in replacing lost, stolen, or broken car keys directly at your vehicle.",
        "split_desc": "Modern vehicles require sophisticated electronic programming. Our technicians are fully equipped to handle advanced immobiliser systems and smart keys on-site. If you're locked out or need a new key cut in East London, we deliver a hassle-free, dealership-level service."
    },
    "west-london": {
        "name": "West London",
        "title": "Auto Locksmith West London | Mobile Car Key Replacement",
        "description": "Mobile auto locksmith in West London. Fast car key replacement, programming, and lockout assistance along the M4 corridor and Heathrow.",
        "hero_desc": "Serving Ealing, Hounslow, the M4 corridor, and surrounding areas, our West London mobile auto locksmiths are ready to assist. Whether you've lost your keys at Heathrow Airport or snapped them in a local car park, we provide rapid roadside replacement.",
        "split_desc": "Our fully-equipped mobile units carry everything needed to gain non-destructive entry to your vehicle, decode your locks, and program new transponder or proximity keys. We save West London drivers the time and expense of main dealer recovery."
    },
    "surrey": {
        "name": "Surrey",
        "title": "Auto Locksmith Surrey | Mobile Car Key Replacement",
        "description": "Mobile auto locksmith covering Surrey. Fast car key replacement, programming, and emergency lockout assistance at your home, work or roadside.",
        "hero_desc": "Operating extensively across Surrey, our mobile auto locksmiths provide fast, reliable car key replacement and programming. Whether you're in a busy town like Guildford or Woking, or stranded on a rural road, we come directly to your location.",
        "split_desc": "Losing your car keys in Surrey can be incredibly disruptive. Rather than waiting weeks for a dealership appointment and paying for a tow truck, our technicians arrive on-site with dealership-level diagnostic tools to cut and program a brand new key while you wait."
    },
    "kent": {
        "name": "Kent",
        "title": "Auto Locksmith Kent | Mobile Car Key Replacement",
        "description": "Mobile auto locksmith covering Kent. Fast car key replacement, programming, and emergency lockout assistance at your home, work or roadside.",
        "hero_desc": "From the Dartford Crossing to Maidstone and Ashford, our mobile auto locksmiths provide comprehensive coverage across Kent. If you're facing a car key emergency, our fully equipped vans bring the solution directly to your vehicle.",
        "split_desc": "We handle all major vehicle makes and models, offering non-destructive entry, key extraction, and advanced transponder programming. If you've lost your only key in Kent, our technicians can securely bypass the immobiliser and program a replacement on the spot."
    },
    "essex": {
        "name": "Essex",
        "title": "Auto Locksmith Essex | Mobile Car Key Replacement",
        "description": "Mobile auto locksmith covering Essex. Fast car key replacement, programming, and emergency lockout assistance at your home, work or roadside.",
        "hero_desc": "Serving Romford, Chelmsford, and the wider commuter belt, our Essex mobile auto locksmith service is designed for speed and convenience. We specialise in replacing lost car keys, repairing faulty fobs, and resolving ignition issues on-site.",
        "split_desc": "Our mobile units act as fully functioning workshops. We carry high-precision key cutting machinery and the latest OBD diagnostic software. If you're locked out or need a spare key programmed in Essex, we provide a cost-effective alternative to the main dealer."
    },
    "hertfordshire": {
        "name": "Hertfordshire",
        "title": "Auto Locksmith Hertfordshire | Mobile Car Key Replacement",
        "description": "Mobile auto locksmith covering Hertfordshire. Fast car key replacement, programming, and emergency lockout assistance.",
        "hero_desc": "Covering Watford, St Albans, the A1(M) and M1 corridors, our mobile auto locksmiths deliver expert car key services across Hertfordshire. Whether you need an emergency replacement or a spare key cut at your workplace, we come to you.",
        "split_desc": "Modern car keys contain sensitive electronics that require specialized programming. Our Hertfordshire-based technicians have the expertise and equipment to supply, cut, and program standard transponder keys, remote fobs, and smart proximity keys directly at your vehicle."
    }
}

base_file = r"C:\Users\97ars\.gemini\antigravity-ide\scratch\quick-turn-auto-keys\services\car-key-replacement.html"
output_dir = r"C:\Users\97ars\.gemini\antigravity-ide\scratch\quick-turn-auto-keys\locations"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(base_file, 'r', encoding='utf-8') as f:
    base_html = f.read()

# Split base HTML into Head, Nav, and Footer
match_head = re.search(r'(.*?)(<main id="main">)', base_html, re.DOTALL)
match_footer = re.search(r'(</main>.*)', base_html, re.DOTALL)

if not match_head or not match_footer:
    print("Failed to parse base HTML.")
    exit(1)

head_and_nav = match_head.group(1)
footer = match_footer.group(1)

for slug, data in locations.items():
    # 1. Update metadata in head
    new_head = head_and_nav
    new_head = re.sub(r'<title>.*?</title>', f'<title>{data["title"]}</title>', new_head, flags=re.DOTALL)
    new_head = re.sub(r'<meta name="description"\s*content=".*?">', f'<meta name="description" content="{data["description"]}">', new_head, flags=re.DOTALL)
    new_head = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{data["title"]}">', new_head)
    new_head = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{data["description"]}">', new_head)
    new_head = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="https://auttokeys.com/locations/{slug}.html">', new_head)
    new_head = re.sub(r'"url":\s*"https://auttokeys.com/services/car-key-replacement.html"', f'"url": "https://auttokeys.com/locations/{slug}.html"', new_head)
    
    # 2. Update Breadcrumbs in head
    new_head = new_head.replace('"name": "Services",\n      "item": "https://auttokeys.com/services.html"', '"name": "Locations",\n      "item": "https://auttokeys.com/service-areas.html"')
    new_head = new_head.replace('"name": "Car Key Replacement",\n      "item": "https://auttokeys.com/services/car-key-replacement.html"', f'"name": "{data["name"]}",\n      "item": "https://auttokeys.com/locations/{slug}.html"')

    # 3. Build Main Body
    main_body = f"""<main id="main">

<div class="container">
  <nav class="breadcrumbs" aria-label="Breadcrumb">
    <a href="../index.html">Home</a>
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
    <a href="../service-areas.html">Locations</a>
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
    <span class="current">{data['name']}</span>
  </nav>
</div>

<!-- ==================== HERO ==================== -->
<section class="hero hero--padded">
  <div class="container">
    <div class="reveal hero-copy">
      <div class="eyebrow">Mobile Locksmith {data['name']}</div>
      <h1>Mobile Auto Locksmith in <span class="accent-word">{data['name']}</span></h1>
      <p>{data['hero_desc']}</p>

      <div class="hero-ctas">
        <a href="tel:+447446980720" class="btn btn-primary">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          Call 07446 980720
        </a>
        <a href="../quote.html" class="btn btn-outline">Request a Free Quote</a>
      </div>

      <ul class="checklist" style="margin-top:6px;">
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Mobile service — we come to you</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Lost car keys replaced on-site</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Non-destructive vehicle entry</li>
      </ul>
    </div>

    <div class="reveal hero-visual aspect-4-5">
      <img width="1400" height="1120" src="../assets/images/services imgs/data (2).webp" alt="Auto locksmith in {data['name']}" loading="lazy" style="width:100%;height:100%;object-fit:cover;border-radius:var(--radius-card);display:block;">
    </div>
  </div>
</section>

<!-- ==================== MOBILE AT YOUR LOCATION ==================== -->
<section class="section pt-0">
  <div class="container">
    <div class="split">
      <div class="reveal split-copy">
        <div class="eyebrow">Local Service</div>
        <h2>Fast response throughout {data['name']}</h2>
        <p>{data['split_desc']}</p>
        <p style="margin-top:16px;">We work with different types of vehicle key systems, including traditional keys, transponder keys, remote fobs and modern keyless-entry systems across all major vehicle brands.</p>
      </div>
      <div class="reveal split-visual">
        <img width="1400" height="933" src="../assets/images/services imgs/data (1).webp" alt="Mobile car key replacement {data['name']}" loading="lazy" style="width:100%;height:100%;object-fit:cover;border-radius:var(--radius-card);display:block;">
      </div>
    </div>
  </div>
</section>

<!-- ==================== WHICH SERVICE DO YOU NEED ==================== -->
<section class="section section--surface-bordered">
  <div class="container">
    <div class="reveal section-head">
      <div class="eyebrow">Core Services</div>
      <h2>How we can help</h2>
    </div>

    <div class="feature-grid">
      <div class="reveal feature-item">
        <div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="8" cy="12" r="4"/><path d="M11 12h11M17 12v4M20 12v3"/></svg></div>
        <h3>Lost Car Keys</h3>
        <p>If every key has been lost, we can decode your vehicle's locks, cut a brand new key from scratch, and program it securely to the immobiliser system.</p>
        <a href="../services/lost-car-keys.html" class="text-link" style="margin-top:14px;">View Lost Car Key Replacement <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
      </div>
      <div class="reveal feature-item">
        <div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="7" y="3" width="10" height="16" rx="3"/><circle cx="12" cy="8" r="1.4"/></svg></div>
        <h3>Broken Car Keys</h3>
        <p>A damaged casing, worn key blade, or faulty buttons can make your vehicle key unreliable. We assess the condition and can repair or replace the key on-site.</p>
        <a href="../services/car-key-replacement.html" class="text-link" style="margin-top:14px;">View Key Replacement <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
      </div>
      <div class="reveal feature-item">
        <div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg></div>
        <h3>Emergency Lockout</h3>
        <p>Locked your keys inside the car? Our technicians use specialist, non-destructive tools to safely pick the lock and get you back into your vehicle in minutes.</p>
        <a href="../services/emergency-car-lockout.html" class="text-link" style="margin-top:14px;">View Emergency Lockout <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
      </div>
    </div>
  </div>
</section>

<!-- ==================== CTA BAND ==================== -->
<section class="cta-band section">
  <div class="container">
    <div class="reveal cta-band-text">
      <h2>Need a car locksmith in {data['name']}?</h2>
      <p>Get in touch with your vehicle details and location, and we'll dispatch a mobile technician to assist you.</p>
    </div>
    <div class="cta-band-actions">
      <a href="tel:+447446980720" class="btn btn-primary">Call 07446 980720</a>
      <a href="../quote.html" class="btn btn-outline">Request a Free Quote</a>
    </div>
  </div>
</section>
"""

    full_html = new_head + main_body + "\n" + footer
    
    with open(os.path.join(output_dir, f"{slug}.html"), 'w', encoding='utf-8') as f:
        f.write(full_html)

print("Generated 9 location pages successfully.")
