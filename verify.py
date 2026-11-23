import re
with open(r'C:\Users\nexus\.gemini\antigravity\scratch\jymmys-barber\index.html', 'r', encoding='utf-8') as f:
    html = f.read()
scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', html, re.DOTALL)
for idx, js in enumerate(scripts):
    s = js.strip()
    if not s:
        continue
    ob = s.count('{')
    cb = s.count('}')
    op = s.count('(')
    cp = s.count(')')
    print(f'Script {idx+1}: braces {ob}/{cb} diff={ob-cb}, parens {op}/{cp} diff={op-cp}')
print(f'Total file size: {len(html)} bytes')
print('Has mqtt.min.js:', 'mqtt.min.js' in html)
print('Has touch-action pan-y:', 'pan-y' in html)
print('Has overflow-x hidden:', 'overflow-x' in html)
