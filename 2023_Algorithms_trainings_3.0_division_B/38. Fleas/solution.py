from collections import deque
from copy import deepcopy


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


def calc_shortes_path(
    start: tuple[int, int],
    end: tuple[int, int],
    n: int,
    m: int,
    board: [list[list[int]]]
) -> int:
    if start == end:
        return 0

    brd = deepcopy(board)
    cur = start
    brd[cur[0]][cur[1]] = 0
    q = deque((cur,))

    while q:
        cur = q.popleft()
        # print(f"{start=} {cur=} {end=}", *brd, sep='\n', end='\n\n')
        new_length = brd[cur[0]][cur[1]] + 1

        for next_cell in [(j, i)
                          for dy, dx in MOVEMENTS if (
                              0 < (j:=cur[0]+dy) <= n
                              and 0 < (i:=cur[1]+dx) <= m
                          )]:
            if brd[next_cell[0]][next_cell[1]] == -1:
                brd[next_cell[0]][next_cell[1]] = new_length
                if next_cell == end:
                    q.clear()
                    break
                q.append(next_cell)
        # print(f"{q=}", end='\n\n')

    return brd[end[0]][end[1]]


n, m, s, t, q = [int(x) for x in input().split()]
end = s, t

board = [[-1 for _ in range(m+1)] for _ in range(n+1)]

# fleas = [None]*q

total = 0
for k in range(q):
    flea = tuple(int(x) for x in input().split())
    # flea = (j, i, [])
    # fleas[k] = flea
    # board[j][i] = flea
    length = calc_shortes_path(flea, end, n, m, board)
    # print(k, length)
    if length == -1:
        total = -1
        break
    total += length

print(total)
