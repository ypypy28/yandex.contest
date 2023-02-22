import sys


letters = dict()
i = 0
ch = sys.stdin.read(1)
while ch not in ('', '\n'):
    if ch not in letters:
        letters[ch] = []
    letters[ch].append(i)
    ch = sys.stdin.read(1)
    i += 1

size = i
for ch in sorted(letters.keys()):
    val = 0
    for i in letters[ch]:
        val += (i+1)*(size-i)
    print(f"{ch}: {val}")
