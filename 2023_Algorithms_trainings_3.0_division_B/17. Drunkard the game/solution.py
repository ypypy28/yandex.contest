import sys
from collections import deque


first, second = [deque(input().split()) for _ in range(2)]
round_i = 0
end = 10**6

while first and second:
    round_i += 1
    if round_i > end:
        break
    cards = first.popleft(), second.popleft()
    match cards:
        case "0", "9":
            first.extend(cards)
        case "9", "0":
            second.extend(cards)

        case i, j:
            if i > j:
                first.extend(cards)
            elif i < j:
                second.extend(cards)
if first and second:
    print("botva")
elif first:
    print("first", round_i)
else:
    print("second", round_i)
