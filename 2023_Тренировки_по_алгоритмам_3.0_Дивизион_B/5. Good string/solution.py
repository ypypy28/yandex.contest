n = int(input())
letters = [0]*n

for i in range(n):
    letters[i] = int(input())

goodness = 0
# print(letters)
for i in range(n-1, 0, -1):
    diff = letters[i-1] - letters[i]
    if diff >= 0:
        goodness += letters[i]
    else:
        goodness += letters[i-1]
print(goodness)
