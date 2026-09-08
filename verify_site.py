import os
import glob
import re
from collections import Counter
from urllib.parse import urlparse

base_dir = r"C:\Users\97ars\.gemini\antigravity-ide\scratch\quick-turn-auto-keys"

html_files = []
for root, _, files in os.walk(base_dir):
    if "node_modules" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

all_files = set([os.path.relpath(os.path.join(root, file), base_dir).replace('\\', '/')
                 for root, _, files in os.walk(base_dir) for file in files])

broken_links = 0
duplicate_ids = 0

print("Starting Verification...")

for filepath in html_files:
    rel_path = os.path.relpath(filepath, base_dir).replace('\\', '/')
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Check for duplicate IDs
    ids = re.findall(r'id="([^"]+)"', content)
    counts = Counter(ids)
    duplicates = [id for id, count in counts.items() if count > 1]
    if duplicates:
        print(f"Warning: Duplicate IDs found in {rel_path}: {duplicates}")
        duplicate_ids += 1

    # 2. Check for broken internal links
    links = re.findall(r'href="([^"]+)"', content)
    for link in links:
        # Ignore external links, anchor links, phone numbers, mailtos, preloads
        if link.startswith(('http', 'https', 'tel:', 'mailto:', '#', 'javascript:', 'data:')):
            continue
        # Strip anchors and query params
        parsed = urlparse(link)
        clean_link = parsed.path
        if not clean_link:
            continue
        
        # Calculate target path relative to base_dir
        current_dir = os.path.dirname(rel_path)
        target_path = os.path.normpath(os.path.join(current_dir, clean_link)).replace('\\', '/')
        
        if target_path not in all_files:
            # Special case for directories (like /blog/ which might look for index.html)
            if target_path + "/index.html" in all_files:
                continue
            if target_path + "index.html" in all_files:
                continue
            print(f"Broken Link: {link} in {rel_path} (Target {target_path} not found)")
            broken_links += 1

if broken_links == 0 and duplicate_ids == 0:
    print("Verification Passed: No broken internal links or duplicate IDs found.")
else:
    print(f"Verification Failed: {broken_links} broken links, {duplicate_ids} files with duplicate IDs.")
