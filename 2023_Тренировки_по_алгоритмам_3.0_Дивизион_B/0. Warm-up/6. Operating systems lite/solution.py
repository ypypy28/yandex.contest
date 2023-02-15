m, n = [int(input()) for _ in range(2)]

hd = set()
for os in range(n):
    a, b = [int(val) for val in input().split()]
    new_os = range(a, b+1)
    corrupted = []
    for prev_os in hd:
        if prev_os.start in new_os or (prev_os.stop-1) in new_os:
            corrupted.append(prev_os)
    for c in corrupted:
        hd.remove(c)

    hd.add(new_os)

print(len(hd))
