# vacances = tuple(map(
#     lambda v: (v[0], int(v[1])),
#     [tuple(input().split(','))
#      for _ in range(int(input()))]
# ))


vacances = {s: int(m) for s, m in [input().split(',')
                                   for _ in range(int(input()))]}

candidates = [(c, q, int(r), int(p))
              for c,q,r,p in [input().split(',')
                              for _ in range(int(input()))]]
candidates.sort(key=lambda x: (x[1],-x[2],x[3],x[0]))

res = []
for candidat, vacancy, r, q in candidates:
    if vacances[vacancy] > 0:
        vacances[vacancy] -= 1
        res.append(candidat)

# print(vacances)
# print(candidates)
print(*sorted(res), sep='\n')

