from collections import deque
from math import inf


n, m = [int(input()) for _ in range(2)]

stations = [[set(), set(), inf] for _ in range(n+1)]
lines = [None for _ in range(m+1)]

for i in range(1, m+1):
    p, *line = [int(x) for x in input().split()]
    lines[i] = line
    stations[line[0]][0].add(line[1])
    stations[line[0]][1].add(i)
    stations[line[-1]][0].add(line[-2])
    stations[line[-1]][1].add(i)
    for j in range(1, p-1):
        stations[line[j]][0].add(line[j-1])
        stations[line[j]][1].add(i)
        stations[line[j]][0].add(line[j+1])
        stations[line[j]][1].add(i)

a, b = [int(x) for x in input().split()]

stations[a][2] = 0
q = deque()
for line in stations[a][1]:
    q.append((a, line, 0))

while q:
    st, cur_line, transfer = q.popleft()

    for s in lines[cur_line]:
        if stations[s][2] > transfer:
            stations[s][2] = transfer
            q.append((s, cur_line, transfer))

    transfer += 1

    for line in stations[st][1]:
        if line != cur_line:
            for s in lines[line]:
                if stations[s][2] > transfer:
                    stations[s][2] = transfer
                    q.append((s, cur_line, transfer))

print(-1 if stations[b][2] == inf else stations[b][2])
