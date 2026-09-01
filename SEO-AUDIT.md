# SEO Audit — Quick Turn Auto Keys (auttokeys.com)

**Audit Date:** 2026-09-02
**Domain:** https://auttokeys.com
**Repository:** arsalan-khan-dev/quick-turn-auto-keys (private)

---

## 1. Project Architecture

| Property | Value |
|---|---|
| Framework | None — pure static HTML/CSS/JS |
| Build system | None — no bundler, no npm |
| Deployment | Static hosting — domain auttokeys.com |
| CSS | Custom token-based (tokens.css, global.css, components.css, responsive.css, blog.css) |
| JavaScript | Vanilla JS (main.js, navigation.js, animations.js, hero-slider.js) |
| Fonts | Google Fonts — Space Grotesk + Inter |

### Total Pages: 40 indexable pages
- Root: index, about, services, brands, service-areas, faq, blog, contact, quote, privacy-policy, terms-conditions
- /services/ : 9 pages (car-key-replacement, lost-car-keys, key-fob-repair, car-key-cutting, car-key-programming, emergency-car-lockout, ignition-repair, van-key-replacement, eeprom-programming)
- /brands/ : 14 pages (volkswagen, vauxhall, hyundai, mercedes, bmw, kia, land-rover, audi, ford, nissan, peugeot, renault, skoda, toyota)
- /blog/ : 5 posts

---

## 2. Current SEO — What Is Already Correct (PRESERVE)

- lang="en-GB" on all pages — correct UK locale
- All canonical URLs are unique and self-referencing (correct domain auttokeys.com)
- robots.txt: Allow: / for all bots + sitemap: https://auttokeys.com/sitemap.xml
- 404.html correctly has noindex
- Sitemap includes all 40 indexable URLs
- All pages have unique, well-written titles
- All pages have unique meta descriptions
- Open Graph tags on every page (og:title, og:description, og:type, og:image, og:url)
- Twitter:card set to summary_large_image
- index.html has Locksmith + WebSite schema in @graph (no fake ratings — correct)
- Brand pages have BreadcrumbList + FAQPage schema
- Service pages have BreadcrumbList + Service schema
- Hero image has fetchpriority="high" and explicit width/height
- All images use .webp format
- Mobile nav panel correctly duplicates all links
- Phone CTA tel: link in header

---

## 3. Technical SEO Issues Found

### CRITICAL

**Issue 1: quote.html wrong canonical (points to contact.html)**
- File: quote.html
- Problem: canonical href="https://auttokeys.com/contact.html" — signals to Google that quote.html IS contact.html
- Also: same title and description as contact.html — creates a duplicate content signal
- Risk: HIGH

**Issue 2: quote.html missing from sitemap**
- File: sitemap.xml
- Problem: quote.html is internally linked from every page header but not in sitemap
- Decision needed: either add correct self-referencing canonical + add to sitemap, or add noindex + remove from sitemap

**Issue 3: OG image is 714KB**
- File: assets/images/logo/og-image.png
- Problem: 714KB is extremely oversized for an OG image (recommended: under 200KB, 1200x630px)
- Risk: Performance flag in PageSpeed, slow social card rendering

**Issue 4: Duplicate nav links in desktop brand dropdown**
- File: index.html (and all pages sharing this nav component)
- Problem: The brand dropdown lists ALL brands TWICE (Ford, VW, Toyota, Nissan, Renault, Hyundai, Kia, Peugeot, Land Rover, Mercedes, Vauxhall all appear twice in the same dropdown div)
- Risk: Crawl budget waste, diluted link equity

### MODERATE

**Issue 5: Service title lacks London for car-key-replacement, car-key-cutting, car-key-programming**
- car-key-replacement: "Car Key Replacement Near Me | Mobile Auto Locksmith" — no London
- car-key-cutting: "Car Key Cutting Near Me | Mobile Spare Key Service London" — has London second half
- car-key-programming: "Car Key Programming Near Me | Transponder & Remote Keys London" — has London second half
- Primary issue: car-key-replacement.html title has no London at all

**Issue 6: All 14 brand page meta descriptions are template-identical**
- Pattern: "Lost your [BRAND] keys or need a spare? Our mobile auto locksmiths in London offer fast [BRAND] car key replacement, programming, and lockout assistance."
- Problem: Semantically identical — signals thin content

**Issue 7: All 14 brand page H1s are template-identical**
- Pattern: "Specialist mobile [BRAND] auto locksmith in London"
- Problem: No differentiation — weakens relevance signals

**Issue 8: blog.html H1 has typo — missing space**
- Current: "Auto LocksmithKnowledge Base"
- Should be: "Auto Locksmith Knowledge Base"

**Issue 9: faq.html H1 is too generic**
- Current: "Answers to common questions"
- No keyword — zero SEO signal

**Issue 10: about.html H1 is benefit-focused, no keyword**
- Current: "Reliable auto locksmith help, whenever you need it"

**Issue 11: Blog H1s are excessively long**
- All end with "in London and surrounding areas" which adds noise
- Example: "Lost Fleet Keys? A Practical Guide to Managing Vehicle Keys Across a Business Fleet in London and surrounding areas"

**Issue 12: Twitter title and description missing from all pages**
- twitter:card is set but twitter:title and twitter:description are absent
- Relies on OG fallback — works but suboptimal

### LOW / INFORMATIONAL

**Issue 13: quote.html has no H1**

**Issue 14: Blog changefreq="yearly" is too infrequent**
- Recommend: monthly

**Issue 15: faq.html has no FAQPage schema**
- Page has FAQ content but no structured data schema

**Issue 16: Blog posts have no Article schema**

**Issue 17: contact.html has no LocalBusiness schema**

**Issue 18: Brand/service pages could have stronger cross-linking**

---

## 4. Ranking Opportunities

| Query Theme | Existing Page | Gap |
|---|---|---|
| Volkswagen key replacement London | brands/volkswagen.html | Template H1/desc — differentiate |
| Vauxhall car key replacement | brands/vauxhall.html | Template H1/desc — differentiate |
| Hyundai key replacement London | brands/hyundai.html | Template H1/desc — differentiate |
| Mercedes key replacement London | brands/mercedes.html | Template H1/desc — differentiate |
| BMW keys cut London | brands/bmw.html | Template H1/desc — differentiate |
| Kia key replacement London | brands/kia.html | Template H1/desc — differentiate |
| Land Rover key replacement | brands/land-rover.html | Template H1/desc — differentiate |
| Emergency car locksmith London | services/emergency-car-lockout.html | Good — strengthen linking |
| 24 hour auto locksmith London | index.html | H1 already says 24/7 — good |
| Car key replacement London | services/car-key-replacement.html | Add London to title |
| Lost car keys London | services/lost-car-keys.html | Well-targeted |
| Car key programming London | services/car-key-programming.html | Good — add brand cross-links |
| Vauxhall keys cut | brands/vauxhall.html + services/car-key-cutting.html | Cross-link opportunity |

---

## 5. Performance Notes

| Asset | Size | Status |
|---|---|---|
| og-image.png | 714KB | CRITICAL — compress to <200KB |
| logo-mark.png | 41KB PNG | Minor — could be WebP |
| locksmith-van.webp | 129KB | Acceptable |
| locksmith-technician.webp | 76KB | Good |
| Hero slider images | 50-125KB | Acceptable |
| Brand images | 8-127KB | Variable — some large |
| Blog images | 68-137KB | Acceptable |

---

## 6. Schema Summary

| Page | Schema Present | Status |
|---|---|---|
| index.html | Locksmith, WebSite | Good |
| services/* | Service, BreadcrumbList | Good |
| brands/* | FAQPage, BreadcrumbList | Good |
| faq.html | None | Should add FAQPage |
| blog posts | None | Should add Article |
| contact.html | None | Could add LocalBusiness |
| about.html | None | Optional: Organization |
