n, k = [int(val) for val in input().split()]

dp = [0]*n
end_base = min(k+1, n)
dp[0] = 1
for i in range(1, end_base):
    dp[i] = sum(dp[:i])
for i in range(end_base, n):
    first_variant = max(i-k, 0)
    dp[i] = sum(dp[first_variant:i])

print(dp[-1])
