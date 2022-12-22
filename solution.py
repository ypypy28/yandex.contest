from collections import namedtuple, deque


LeftSeats = namedtuple("LeftSeats", "A B C")
RightSeats = namedtuple("RightSeats", "F E D")


def free_from(position: str, seats: LeftSeats | RightSeats) -> int:
    if position == "window":
        i = count = 0
        while i < 3 and seats[i] == '.':
            count += 1
            i += 1
        return count

    i = 2
    count = 0
    while i > -1 and seats[i] == '.':
        count += 1
        i -= 1
    return count


def print_seats(seats):
    buf = [f"{''.join(l)}_{''.join(r[::-1])}"
           for l, r in zip(seats["left"], seats["right"])]
    print('\n'.join(buf))


n = int(input())
left, right = [], []
seats = {
    "left": [],
    "right": [],
}
free_count = {
    'left': {
        "window": {i: deque() for i in range(4)},
        "aisle": {i: deque() for i in range(4)}
    },
    'right': {
        "window": {i: deque() for i in range(4)},
        "aisle": {i: deque() for i in range(4)}
    }
}
for i, _ in enumerate(range(n)):
    row = input().split('_')
    seats["left"].append(LeftSeats(*row[0]))
    seats["right"].append(RightSeats(*row[1][::-1]))
    free_count["left"]["window"][free_from("window", seats["left"][i])].append(i)
    free_count["left"]["aisle"][free_from("aisle", seats["left"][i])].append(i)
    free_count["right"]["window"][free_from("window", seats["right"][i])].append(i)
    free_count["right"]["aisle"][free_from("aisle", seats["right"][i])].append(i)

m = int(input())
passengers = []
for _ in range(m):
    num, side, position = input().split()
    num = int(num)
    sideSeats = LeftSeats if side == "left" else RightSeats
    i = None
    for j in range(num, 4):
        try:
            i = free_count[side][position][j].popleft()
            while free_from(position, seats[side][i]) < num:
                i = free_count[side][position][j].popleft()
            break
        except IndexError:
            continue
    if free_from(position, seats[side][i]) < num:
        print("Cannot fulfill passengers requirements")
        continue

    if position == "window":
        seats[side][i] = sideSeats(*('X' for _ in range(num)), *seats[side][i][num:])
        positions = ' '.join(sorted([f"{i+1}{field}" for _, field in zip(range(num), seats[side][i]._fields)]))
        free_count["left"]["window"][free_from("window", seats["left"][i])].appendleft(i)
        free_count["left"]["aisle"][free_from("aisle", seats["left"][i])].appendleft(i)
        free_count["right"]["window"][free_from("window", seats["right"][i])].appendleft(i)
        free_count["right"]["aisle"][free_from("aisle", seats["right"][i])].appendleft(i)
    else:
        seats[side][i] = sideSeats(*seats[side][i][:3-num], *('X' for _ in range(num)))
        positions = ' '.join(sorted([f"{i+1}{field}" for _, field in zip(range(num), seats[side][i]._fields[::-1])]))
        free_count["left"]["window"][free_from("window", seats["left"][i])].appendleft(i)
        free_count["left"]["aisle"][free_from("aisle", seats["left"][i])].appendleft(i)
        free_count["right"]["window"][free_from("window", seats["right"][i])].appendleft(i)
        free_count["right"]["aisle"][free_from("aisle", seats["right"][i])].appendleft(i)

    print(f"Passengers can take seats: {positions}")

    print_seats(seats)

    seats[side][i] = sideSeats(*((ch, '#')[ch == 'X'] for ch in seats[side][i]))
