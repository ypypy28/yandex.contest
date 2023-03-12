from collections import deque


def calc_shortest_path(start: int, end: int, all_vertices: list[list[int]]) -> int:
    if start == end:
        return 0

    all_vertices[start][1] = 0
    q = deque((start,))
    while q:
        cur = q.popleft()
        new_length = all_vertices[cur][1] + 1

        for v in all_vertices[cur][0]:
            if all_vertices[v][1] == -1:
                all_vertices[v][1] = new_length
                if v == end:
                    q.clear()
                    break
                q.append(v)

    return all_vertices[end][1]


def get_shortest_path(start: int, end: int, all_vertices: list[list[int]]) -> list[int]:
    cur = end
    path = [cur]
    while cur != start:
        next_length = all_vertices[cur][1] - 1

        for v in all_vertices[cur][0]:
            if all_vertices[v][1] == next_length:
                path.append(v)
                cur = v
                break

    return path[::-1]


n = int(input())

vertices = [[[], -1] for _ in range(n+1)]

for j in range(1, n+1):
    bs = [int(x) for x in input().split()]

    for i, b in enumerate(bs, start=1):
        if b == 1:
            vertices[j][0].append(i)

start, end = [int(x) for x in input().split()]


res = calc_shortest_path(start, end, vertices)
print(res)
if res not in (-1, 0):
    path = get_shortest_path(start, end, vertices)
    print(' '.join(str(v) for v in path))
