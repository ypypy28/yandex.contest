m, n = [int(input()) for _ in range(2)]

hd = set()
for os in range(n):
    a, b = [int(val) for val in input().split()]
    corrupted = []
    for prev_os in hd:
        if a in prev_os or b in prev_os:
            corrupted.append(prev_os)
    for c in corrupted:
        hd.remove(c)

    hd.add(range(a, b+1))

print(len(hd))
