n = int(input())
base = [0, 2, 4, 7]  # 13 24

if n < 4:
    print(base[n])
else:
    dp =[-1]*(n+1)
    dp[0:4] = base

    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])
