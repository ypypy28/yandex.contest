m, n = [int(input()) for _ in range(2)]

hd = [None]*(m+1)
oses = set()
for os in range(n):
    oses.add(os)
    a, b = [int(val) for val in input().split()]
    for i in range(a, b+1):
        cur_os = hd[i]
        if cur_os in oses:
            oses.remove(cur_os)
        hd[i] = os
print(len(oses))
