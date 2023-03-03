from math import inf


n, m = [int(val) for val in input().split()]

field = [None]*n
for i in range(n):
    field[i] = [int(x) for x in input().split()]

dp = [[(None, inf)[i==0 or j == 0] for i in range(m+1)] for j in range(n+1)]
dp[1][1] = field[0][0]
for j in range(n):
    for i in range(m):
        prev = min(dp[j+1][i], dp[j][i+1])
        if prev == inf:
            dp[j+1][i+1] = field[j][i]
        else:
            dp[j+1][i+1] = field[j][i] + prev

print(dp[n][m])
