import os
import re

blog_dir = 'blog'
posts = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

links = [
    (r'(?i)\b(replacement car key)\b', '../services/car-key-replacement.html'),
    (r'(?i)\b(lost keys?)\b', '../services/lost-car-keys.html'),
    (r'(?i)\b(key fob repair)\b', '../services/key-fob-repair.html'),
    (r'(?i)\b(car key programming)\b', '../services/car-key-programming.html'),
    (r'(?i)\b(locked out)\b', '../services/emergency-car-lockout.html'),
    (r'(?i)\b(car key cut)\b', '../services/car-key-cutting.html')
]

for post in posts:
    filepath = os.path.join(blog_dir, post)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract article body
    article_match = re.search(r'(<article class="article-content.*?>)(.*?)(</article>)', content, re.DOTALL)
    if not article_match:
        continue
        
    prefix = article_match.group(1)
    body = article_match.group(2)
    suffix = article_match.group(3)
    
    # Apply links at most once per keyword
    for pattern, url in links:
        # Ignore matches that are already inside a tag
        # A simple hack for not replacing inside tags:
        # Split by <...>, replace in text, join back
        parts = re.split(r'(<[^>]*>)', body)
        replaced = False
        for i in range(0, len(parts), 2): # Even indices are text outside tags
            if not replaced and re.search(pattern, parts[i]):
                parts[i] = re.sub(pattern, rf'<a href="{url}" class="text-link">\1</a>', parts[i], count=1)
                replaced = True
        body = "".join(parts)
        
    new_content = content[:article_match.start()] + prefix + body + suffix + content[article_match.end():]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Done applying contextual links to blog posts.")