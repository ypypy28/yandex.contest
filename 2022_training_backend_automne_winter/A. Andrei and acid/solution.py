import sys


n = int(input())
if n == 1:
    print(0)
    sys.exit(0)

repr_num = []
tmp = sys.stdin.read(1)
diff = cur = prev = 0
while tmp != ' ':
    repr_num.append(tmp)
    tmp = sys.stdin.read(1)
prev = int(''.join(repr_num))
repr_num.clear()

while tmp != '':
    repr_num.append(tmp)
    tmp = sys.stdin.read(1)
    if tmp == ' ':
        cur = int(''.join(repr_num))
        repr_num.clear()
        if cur < prev or (cur != prev and diff != 0):
            print(-1)
            sys.exit(0)
        elif cur > prev:
            diff = cur - prev
        prev = cur
cur = int(''.join(repr_num))
if cur < prev or (cur != prev and diff != 0):
    print(-1)
    sys.exit(0)
if cur > prev:
    diff = cur - prev
print(diff)
