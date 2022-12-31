import string


n = int(input())
last = n - 1

for j in range(n):
    f, i, o, d, m, y = input().split(',')
    stage_1 = len(set(f + i + o))
    stage_2 = sum(sum([int(ch) for ch in num]) for num in (d, m)) * 64
    stage_3 = (string.ascii_uppercase.index(f[0].upper()) + 1) * 256
    code = f"{hex(stage_1 + stage_2 + stage_3).upper()[-3:]:0>3}"
    if j != last:
        print(code, end=' ')
    else:
        print(code)
