import glob
import re
import json
import os

files_to_check = [
    'index.html',
    'quote.html'
]
files_to_check.extend(glob.glob('services/*.html'))
files_to_check.extend(glob.glob('brands/*.html'))

results = {}
for file in files_to_check:
    if not os.path.exists(file): continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else ''
    
    desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]+)">', content, re.IGNORECASE)
    desc = desc_match.group(1).strip() if desc_match else ''
    
    results[file] = {'title': title, 'description': desc}

with open('meta_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)

print("Done extracting metadata")
