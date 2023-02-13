n = int(input())
letters = [0]*n

for i in range(n):
    letters[i] = int(input())

goodness = 0
i = i_prev = 0
letters[i] -= 1
while not all(l == 0 for l in letters):
    i = (i + 1) % n
    while letters[i] == 0:
        i = (i + 1) % n
    letters[i] -= 1
    if i - i_prev == 1:
        goodness += 1
    i_prev = i
print(goodness)
