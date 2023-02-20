from collections import deque


n = int(input())
wagons_1 = deque([int(val) for val in input().split()])

cur = 1
deadend = []

while wagons_1:
    if deadend and deadend[-1] == cur:
        deadend.pop()
        cur += 1
    else:
        wagon = wagons_1.popleft()
        if wagon == cur:
            cur += 1
        else:
            deadend.append(wagon)

while deadend:
    if deadend[-1] == cur:
        deadend.pop()
        cur += 1
    else:
        break

print("YES" if not deadend else "NO")
