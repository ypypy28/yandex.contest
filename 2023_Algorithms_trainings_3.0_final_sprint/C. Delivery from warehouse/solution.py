import heapq


n = int(input())

c1 = []
c2 = []
orders = [None]*n
finished = 0

for i in range(n):
    a, b = [int(x) for x in input().split()]

    heapq.heappush(c1, (a, b, i))
    heapq.heappush(c2, (b, a, i))

while finished != n:
    while c1 and orders[c1[0][2]] is not None:
        heapq.heappop(c1)

    if c1:
        a, b, i = heapq.heappop(c1)
        orders[i] = "1"
        finished += 1

    while c2 and orders[c2[0][2]] is not None:
        heapq.heappop(c2)

    if c2:
        a, b, i = heapq.heappop(c2)
        orders[i] = "2"
        finished += 1

print(' '.join(orders))
