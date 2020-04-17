import sys
import re

pattern = re.compile(r'([\d\.]+)亿元')

while True:
    line=sys.stdin.readline()
    if line == '':
        break
    parts = line.split(';;')
    name = parts[0]
    url = parts[1]
    shouyi = parts[2]
    start = parts[3][1:]
    result1 = pattern.findall(parts[4])

    print(parts)
    print(result1)
