from collections import deque


n = int(input())
wagons_1 = deque([int(val) for val in input().split()])
wagons_2 = set()

cur = 1
deadend = []

while wagons_1:
    if deadend and deadend[-1] == cur:
        wagons_2.add(deadend.pop())
        cur += 1
    else:
        wagon = wagons_1.popleft()
        if wagon == cur:
            wagons_2.add(cur)
            cur += 1
        else:
            deadend.append(wagon)

while deadend:
    if deadend[-1] == cur:
        wagons_2.add(deadend.pop())
        cur += 1
    else:
        break

print("YES" if not deadend else "NO")
# print(f"{cur=} {deadend=} {wagons_2=}")
