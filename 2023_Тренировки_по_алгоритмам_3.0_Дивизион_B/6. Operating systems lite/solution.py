m, n = [int(input()) for _ in range(2)]

hd = set()
for os in range(n):
    a, b = [int(val) for val in input().split()]
    corrupted = []
    for prev_os in hd:
        if (prev_os[0] <= a <= prev_os[1]
            or prev_os[0] <= b <= prev_os[1]
            or (a <= prev_os[0] and b >= prev_os[1])):
            corrupted.append(prev_os)
    for c in corrupted:
        hd.remove(c)

    hd.add((a, b))

print(len(hd))
