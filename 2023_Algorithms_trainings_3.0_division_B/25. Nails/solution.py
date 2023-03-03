n = int(input())

nails = sorted([int(x) for x in input().split()])

dp = [0]*n
dists = [0]*(n-1)
for i in range(n-1):
    dists[i] = nails[i+1] - nails[i]
dp[1] = dists[0]
if n > 2:
    dp[2] = dp[1] + dists[1]

if n > 3:
    dp[3] = dp[2] + dists[2] - dists[1]

if n > 4:
    dp[4] = dp[3] + dists[3] - dists[2] + min(dists[2], dists[1])

for i in range(5, n):
    dp[i] = min(dp[i-4] + dists[i-1] + min(dists[i-2] + dists[i-4], dists[i-3]),
                dp[i-3] + dists[i-1] + min(dists[i-2], dists[i-3]))
print(dp[-1])
