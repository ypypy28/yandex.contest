from collections import Counter

(n, k), a = ([int(x) for x in input().split()] for _ in range(2))

c = Counter(a)
res, sub = [], []
for i in range(n):
    sub.clear()
    sub.extend((a[i] for _ in range(c[a[i]]-1)))
    j = 1
    while len(sub) < k:
        for _ in range(c[a[i]+j]):
            sub.append(a[i]+j)
        for _ in range(c[a[i]-j]):
            sub.append(a[i]-j)
        j += 1

    if len(sub) > k:
        sub = sub[:k]

    res.append(str(sum(abs(a[i] - b) for b in sub)))


print(' '.join(res))
