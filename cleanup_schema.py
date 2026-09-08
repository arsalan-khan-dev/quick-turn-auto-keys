import glob
import re
import json

keep_full_schema = ['index.html', 'about.html', 'contact.html', 'quote.html']
html_files = glob.glob('**/*.html', recursive=True)

removed_files = []
kept_files = []

# Regex to match the exact Locksmith/WebSite graph script block
# We look for <script type="application/ld+json"> that contains "Locksmith" and "WebSite" in a @graph
script_pattern = re.compile(
    r'<script type="application/ld\+json">\s*\{\s*"@context":\s*"https://schema\.org",\s*"@graph":\s*\[\s*\{\s*"@type":\s*"Locksmith".*?\}\s*\]\s*\}\s*</script>',
    re.IGNORECASE | re.DOTALL
)

for file in html_files:
    if '404' in file: continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    
    # 1. Remove "priceRange": "££" from all Locksmith schemas
    content = re.sub(r'\s*"priceRange":\s*"££",?\n?', '\n', content)
    
    # Clean up any trailing commas that might have been left if priceRange was last (it wasn't, areaServed was next, but just in case)
    # Actually, in the snippet, priceRange is followed by areaServed:
    # "priceRange": "££",
    # "areaServed": [
    # Removing it with the comma is safe.
    
    file_basename = file.replace('\\', '/')
    should_keep = any(file_basename == k for k in keep_full_schema)
    
    if should_keep:
        kept_files.append(file_basename)
    else:
        # 2. Remove redundant Locksmith/WebSite @graph blocks
        # Only remove the script block that contains the specific graph
        new_content = script_pattern.sub('', content)
        if new_content != content:
            removed_files.append(file_basename)
            content = new_content
        else:
            # Maybe the pattern didn't match perfectly, or it wasn't there
            pass
            
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Removed full schema from {len(removed_files)} files:")
for r in removed_files: print(" -", r)

print(f"\nKept full schema in {len(kept_files)} files:")
for k in kept_files: print(" -", k)

