import heapq
from math import inf


n = int(input())

c1 = []
c2 = []
orders = [None]*n
finished = 0

for i in range(n):
    a, b = [int(x) for x in input().split()]

    heapq.heappush(c1, (-a, b, i))
    heapq.heappush(c2, (-b, a, i))

elapsed1 = elapsed2 = 0

while finished != n:
    while c1 and orders[c1[0][2]] is not None:
        heapq.heappop(c1)

    while c2 and orders[c2[0][2]] is not None:
        heapq.heappop(c2)

    # print(f"{c1=} {c2=} {orders=}")

    if c1 and not c2:
        a, b, i = heapq.heappop(c1)
        a = -a
        orders[i] = "1"
        finished += 1
        elapsed1 += a
    elif c2 and not c1:
        b, a, i = heapq.heappop(c2)
        b = -b
        orders[i] = "2"
        finished += 1
        elapsed2 += b
    else:
        a1, b1, i1 = heapq.heappop(c1)
        a1 = -a1
        b2, a2, i2 = heapq.heappop(c2)
        b2 = -b2
        finished += 1

        if a1 + elapsed1 > b2 + elapsed2:
            if b1 < b2:
                orders[i1] = "2"
                elapsed2 += b1
                if i1 != i2:
                    heapq.heappush(c2, (-b2, a2, i2))
            else:
                orders[i2] = "2"
                elapsed2 += b2
                if i1 != i2:
                    heapq.heappush(c2, (-b1, a1, i1))
        else:
            if a1 < a2:
                orders[i2] = "1"
                elapsed1 += a2
                if i1 != i2:
                    heapq.heappush(c1, (-a1, b1, i1))
            else:
                orders[i1] = "1"
                elapsed1 += a1
                if i1 != i2:
                    heapq.heappush(c1, (-a2, b2, i2))


# print(f"{elapsed1=} {elapsed2=}")
print(' '.join(orders))
