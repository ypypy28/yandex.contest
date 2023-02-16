import sys
from string import ascii_letters, digits


countable = set(ascii_letters) | set(".!?:-,;()") | set(digits)
c = dict()
max_count = 0

ch = sys.stdin.read(1)
while ch != '':
    if ch in countable:
        val = c.get(ch, 0) + 1
        if val > max_count:
            max_count = val
        c[ch] = val
    ch = sys.stdin.read(1)

order = sorted(c.keys(), key=ord)
for i in range(max_count, 0, -1):
    print(''.join((' ', '#')[c[ch] >= i] for ch in order))
print(''.join(order))
