# -*- coding: UTF-8 -*-

import sys
import re

pattern = re.compile(r'([\d\.]+)亿元')

candi = []

while True:
    line=sys.stdin.readline()
    if line == '':
        break
    parts = line.split(';;')
    if parts[4] == '[]' or parts[5] == '[]\n':
        continue
    name = parts[0][2:-2]
    url = parts[1]
    shouyi = parts[2][2:-3]
    guimo = float(pattern.findall(parts[4])[0])

    a=[float(o)/108.0 for o in eval(parts[5])]
    bili = a[-1]

    if guimo >= 100 and guimo <= 400 and bili >= 0.6:
        # print (name + ' ' + shouyi + ' ' + url)
        candi.append((name, shouyi, url, bili, guimo))

print ('|名称|6个月收益|资金规模|散户比例|天天基金url|')
print ('|---|---|---|---|---|')
candi = sorted(candi, key=lambda x:x[1], reverse=True)
for o in candi:
    print ('|{}|{}|{}|{}|{}|'.format(o[0], o[1], o[4], o[3], o[2]))

buf = ''
buf += r'\begin{array}[b] {|c|c|} '
buf += r'\hline 名称 & 6个月收益 & 资金规模 & 散户比例 & 天天基金页面 \\ '
for o in candi:
    buf += r'\hline {} & {} & {} & {} & {} \\ '.format(o[0], o[1], o[4], o[3], o[2].replace('http://','http:\/\/'))

buf += r'\hline \end{array}\\'
print (buf)

