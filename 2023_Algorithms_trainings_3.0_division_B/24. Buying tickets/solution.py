n = int(input())

specs = [None]*n
dp= [None]*n

for i in range(n):
    specs[i] = tuple(int(val) for val in input().split())

dp[0] = min(specs[0][:n])
if n > 1:
    dp[1] = min(specs[0][1], specs[0][0] + min(specs[1][:n-1+1]))

if n > 2:
    dp[2] = min(specs[0][2],
                specs[0][1] + min(specs[2]),
                specs[0][0] + min(specs[1][1:n-i+1]),
                specs[0][0] + specs[1][0] + min(specs[2][:n-i]))

for i in range(3, n):
    dp[i] = min(dp[i-1] + specs[i][0],
                dp[i-2] + specs[i-1][1],
                dp[i-3] + specs[i-2][2])
print(dp[-1])
