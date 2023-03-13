import heapq
from math import inf


n = int(input())

c1 = []
c2 = []
orders = [None]*n
finished = 0

for i in range(n):
    a, b = [int(x) for x in input().split()]

    heapq.heappush(c1, (a, b, i))
    heapq.heappush(c2, (b, a, i))

elapsed1 = elapsed2 = 0

while finished != n:
    while c1 and orders[c1[0][2]] is not None:
        heapq.heappop(c1)

    while c2 and orders[c2[0][2]] is not None:
        heapq.heappop(c2)

    if c1 and not c2:
        a, b, i = heapq.heappop(c1)
        orders[i] = "1"
        finished += 1
        elapsed1 += a
    elif c2 and not c1:
        b, a, i = heapq.heappop(c2)
        orders[i] = "2"
        finished += 1
        elapsed2 += b
    else:
        a1, b1, i1 = heapq.heappop(c1)
        b2, a2, i2 = heapq.heappop(c2)


        while c1 and orders[c1[0][2]] is not None:
            heapq.heappop(c1)
        while c2 and orders[c2[0][2]] is not None:
            heapq.heappop(c2)
        next1 = c1[0] if c1 else (inf, inf, inf)
        next2 = c2[0] if c2 else (inf, inf, inf)
        # print(f"{a1, b1, i1=} {elapsed1=} {next1=}")
        # print(f"{a2, b2, i2=} {elapsed2=} {next2=}")

        if next1[0] + a1 + elapsed1 < next2[0] + b2 + elapsed2:
            orders[i1] = "1"
            finished += 1
            elapsed1 += a1
            if i1 != i2:
                heapq.heappush(c2, (b2, a2, i2))
        elif next1[2] == next2[2]:
            if a1+elapsed1 < b2+elapsed2:
                orders[i1] = "1"
                finished += 1
                elapsed1 += a1
                if i1 != i2:
                    heapq.heappush(c2, (b2, a2, i2))
            else:
                orders[i2] = "2"
                finished += 1
                elapsed2 += b2
                if i1 != i2:
                    heapq.heappush(c1, (a1, b1, i1))
        else:
            orders[i2] = "2"
            finished += 1
            elapsed2 += b2
            if i1 != i2:
                heapq.heappush(c1, (a1, b1, i1))
        # print(orders)

# print(f"{elapsed1=} {elapsed2=}")
print(' '.join(orders))
