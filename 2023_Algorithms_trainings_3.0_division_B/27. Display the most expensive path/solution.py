n, m = [int(val) for val in input().split()]

field = [None]*n
for i in range(n):
    field[i] = [int(x) for x in input().split()]

dp = [[(None, (-1, tuple()))[i == 0 or j == 0] for i in range(m+1)] for j in range(n+1)]
dp[1][1] = field[0][0], tuple()

for i in range(1, m):
    dp[1][i+1] = dp[1][i][0] + field[0][i], (*dp[1][i][1], 'R')
for j in range(1, n):
    for i in range(m):
        prev, dir_  = ((dp[j+1][i], 'R'), (dp[j][i+1], 'D'))[dp[j][i+1][0] > dp[j+1][i][0]]
        dp[j+1][i+1] = field[j][i] + prev[0], (*prev[1], dir_)

max_sum, path = dp[n][m]
print(max_sum, ' '.join(path), sep='\n')
