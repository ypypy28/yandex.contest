A, B = (input() for _ in range(2))

plagiarisms = set()
not_sure = dict()
for i, ch_a in enumerate(A):
    if ch_a == B[i]:
        plagiarisms.add(i)
    else:
        not_sure[ch_a] = not_sure.get(ch_a, 0)+1

res = []
for i, ch in enumerate(B):
    if i in plagiarisms:
        res.append('P')
    else:
        j = not_sure.get(ch, 0)
        if j != 0:
            res.append('S')
            not_sure[ch] -= 1
        else:
            res.append('I')

print(''.join(res))
