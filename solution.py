from collections import namedtuple, deque


LeftSeats = namedtuple("LeftSeats", "A B C")
RightSeats = namedtuple("RightSeats", "F E D")


def free_from(position: str, seats: LeftSeats | RightSeats) -> int:
    n = len(seats)
    if position == "window":
        i = count = 0
        while i < n and seats[i] == '.':
            count += 1
            i += 1
        return count

    i = n-1
    count = 0
    while i > -1 and seats[i] == '.':
        count += 1
        i -= 1
    return count


def print_seats(seats):
    buf = [f"{''.join(l)}_{''.join(r[::-1])}"
           for l, r in zip(seats["left"], seats["right"])]
    print('\n'.join(buf))


class SeatsIterator:
    def __init__(self, n_seats, position, seats):
        self._n_seats = n_seats
        self._position = position
        self._seats = seats
        self.row = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.row >= len(self._seats):
            raise StopIteration
        seats_ = self._seats[self.row]
        while self._n_seats > free_from(self._position, seats_):
            self.row += 1
            if self.row >= len(self._seats):
                break
            seats_ = self._seats[self.row]
        if self._n_seats > free_from(self._position, seats_):
            raise StopIteration

        return self.row


if __name__ == "__main__":
    n = int(input())
    left, right = [], []
    seats = {
        "left": [],
        "right": [],
    }
    for i, _ in enumerate(range(n)):
        row = input().split('_')
        seats["left"].append(LeftSeats(*row[0]))
        seats["right"].append(RightSeats(*row[1][::-1]))

    iterators = {
        "left": {
            "window": {i: iter(SeatsIterator(i, "window", seats['left'])) for i in range(1, 4)},
            "aisle": {i: iter(SeatsIterator(i, "aisle", seats['left'])) for i in range(1, 4)},
        },
        "right": {
            "window": {i: iter(SeatsIterator(i, "window", seats['right'])) for i in range(1, 4)},
            "aisle": {i: iter(SeatsIterator(i, "aisle", seats['right'])) for i in range(1, 4)},
        }
    }

    m = int(input())
    passengers = []
    for _ in range(m):
        num, side, position = input().split()
        num = int(num)
        sideSeats = LeftSeats if side == "left" else RightSeats
        i = None
        try:
            i = next(iterators[side][position][num])
        except StopIteration:
            print("Cannot fulfill passengers requirements")
            continue

        if position == "window":
            seats[side][i] = sideSeats(*('X' for _ in range(num)), *seats[side][i][num:])
            positions = ' '.join(sorted([f"{i+1}{field}" for _, field in zip(range(num), seats[side][i]._fields)]))
        else:
            seats[side][i] = sideSeats(*seats[side][i][:-num], *('X' for _ in range(num)))
            positions = ' '.join(sorted([f"{i+1}{field}" for _, field in zip(range(num), seats[side][i]._fields[::-1])]))

        print(f"Passengers can take seats: {positions}")

        print_seats(seats)
        seats[side][i] = sideSeats(*((ch, '#')[ch == 'X'] for ch in seats[side][i]))
