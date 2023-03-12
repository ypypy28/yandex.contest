from collections import deque


def calc_shortest_path(start: int, end: int, all_vertices: list[list[int]]) -> int:
    if start == end:
        return 0

    res = -1
    q = deque(((start, 0), ))
    while q:
        cur, length = q.popleft()

        for v in vertices[cur]:
            new_length = length + 1
            if v == end:
                res = new_length
                q.clear()
                break
            q.append((v, new_length))

    return res


n = int(input())

vertices = [[] for _ in range(n+1)]

for i, _ in enumerate(range(n), start=1):
    bs = [int(x) for x in input().split()]

    for j, b in enumerate(bs, start=1):
        if b == 1:
            vertices[i].append(j)

start, end = [int(x) for x in input().split()]
print(calc_shortest_path(start, end, vertices))
