import json
import re

with open('faq.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract questions
questions = []
answers = []

q_pattern = re.compile(r'<button class="faq-question"[^>]*>(.*?)\s*<svg', re.DOTALL)
a_pattern = re.compile(r'<div class="faq-answer-inner">(.*?)</div>', re.DOTALL)

for q in q_pattern.finditer(content):
    questions.append(q.group(1).strip())
for a in a_pattern.finditer(content):
    answers.append(a.group(1).strip())

mainEntity = []
for q, a in zip(questions, answers):
    mainEntity.append({
        "@type": "Question",
        "name": q,
        "acceptedAnswer": {
            "@type": "Answer",
            "text": a
        }
    })

schema_obj = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": mainEntity
}

schema_json = json.dumps(schema_obj, indent=2, ensure_ascii=False)
schema_script = f'<script type="application/ld+json">\n{schema_json}\n</script>'

# Replace in faq.html
# The current FAQPage schema is from lines 26 to 48. Let's find it.
old_schema_pattern = re.compile(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema\.org",\s*"@type": "FAQPage",.*?</script>', re.DOTALL)
new_content, count = old_schema_pattern.subn(schema_script, content)

if count > 0:
    with open('faq.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Success! Found {len(questions)} Q&As and updated FAQPage schema.")
else:
    print("Failed to replace FAQPage schema block.")
