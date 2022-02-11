import json
import re

w=[]

with open('words.txt') as fh:
    for i in fh:
        if i.startswith('#'):
            continue
        m= re.match(r"(.+) \((.+)\)$", i)
        if m:
            i = m.group(2) + '<br><span class="small">' + m.group(1) + '</span>'

        w.append(i.strip())

w_json = json.dumps(w)

with open('base.html') as fh:
    b = fh.read()

print(re.sub('{w_json}', w_json, b, 1))

