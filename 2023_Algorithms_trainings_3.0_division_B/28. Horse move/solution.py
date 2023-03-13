n, m = [int(val) for val in input().split()]

field = [[0 for _ in range(m+2)] for _ in range(n+2)]

field[2][2] = 1

for i in range(3, m+2):
    field[2][i] = field[0][i-1] + field[1][i-2]

for j in range(3, n+2):
    for i in range(2, m+2):

        field[j][i] = field[j-2][i-1] + field[j-1][i-2]

print(field[-1][-1])

