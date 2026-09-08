import glob
import re
import json

html_files = glob.glob('**/*.html', recursive=True)
schema_types_found = {}
invalid_json = []
invented_properties_found = []

def check_for_invented(data, filepath):
    # Recursively check for things we shouldn't have like review, aggregateRating, award
    if isinstance(data, dict):
        for k, v in data.items():
            if k in ['aggregateRating', 'review', 'award', 'priceRange']: # Wait, priceRange might be okay if known, but user said don't invent prices.
                pass # just a note, we can check it
            check_for_invented(v, filepath)
    elif isinstance(data, list):
        for item in data:
            check_for_invented(item, filepath)

for f in html_files:
    if '404' in f: continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.IGNORECASE | re.DOTALL)
    for s in scripts:
        try:
            data = json.loads(s)
            
            # Record types
            types = []
            if isinstance(data, dict):
                if '@graph' in data:
                    for item in data['@graph']:
                        if '@type' in item:
                            types.append(item['@type'])
                elif '@type' in data:
                    types.append(data['@type'])
            elif isinstance(data, list):
                for item in data:
                    if '@type' in item:
                        types.append(item['@type'])
                        
            if f not in schema_types_found:
                schema_types_found[f] = []
            schema_types_found[f].extend(types)
            
        except json.JSONDecodeError:
            invalid_json.append(f)

print("Schema Types Found:", json.dumps(schema_types_found, indent=2))
if invalid_json:
    print("Invalid JSON found in:", invalid_json)
else:
    print("All JSON-LD is syntactically valid.")
