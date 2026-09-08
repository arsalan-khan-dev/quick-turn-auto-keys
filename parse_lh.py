import json

with open('report.json', encoding='utf-8') as f:
    d = json.load(f)

perf = d.get('categories', {}).get('performance', {}).get('score', 0) * 100
lcp = d['audits']['largest-contentful-paint']['displayValue']
tbt = d['audits']['total-blocking-time']['displayValue']
cls = d['audits']['cumulative-layout-shift']['displayValue']
fcp = d['audits']['first-contentful-paint']['displayValue']
si = d['audits']['speed-index']['displayValue']

print(f"Performance Score: {perf}")
print(f"LCP: {lcp}")
print(f"TBT: {tbt}")
print(f"CLS: {cls}")
print(f"FCP: {fcp}")
print(f"Speed Index: {si}")
