from collections import deque


MOVEMENTS = (
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2),
)


def bfs(
    start: tuple[int, int],
    n: int,
    m: int,
    board: [list[list[int]]]
) -> None:

    cur = start
    board[cur[0]][cur[1]] = 0
    q = deque((cur,))

    while q:
        cur = q.popleft()
        new_length = board[cur[0]][cur[1]] + 1

        for next_cell in [(j, i)
                          for dy, dx in MOVEMENTS if (
                              0 < (j:=cur[0]+dy) <= n
                              and 0 < (i:=cur[1]+dx) <= m
                          )]:
            if board[next_cell[0]][next_cell[1]] == -1:
                board[next_cell[0]][next_cell[1]] = new_length
                if next_cell == end:
                    q.clear()
                    break
                q.append(next_cell)
    return


n, m, s, t, q = [int(x) for x in input().split()]
end = s, t

board = [[-1 for _ in range(m+1)] for _ in range(n+1)]
bfs((s, t), n, m, board)

total = 0
for k in range(q):
    j, i = tuple(int(x) for x in input().split())
    length = board[j][i]
    if length == -1:
        total = -1
        break
    total += length

print(total)
