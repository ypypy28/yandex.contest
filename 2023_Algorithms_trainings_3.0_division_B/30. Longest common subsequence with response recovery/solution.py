n = int(input())
seq1 = input().split()
m = int(input())
seq2 = input().split()

first = ((0, tuple()), (1, (seq1[0],)))[seq1[0] == seq2[0]]
dp = [[first for _ in range(n)] for _ in range(m)]

for i in range(1, n):
    if seq1[i] !=  seq2[0]:
        dp[0][i] = dp[0][i-1]
    else:
        cur = dp[0][i-1][0] + 1, (seq2[0],)
        dp[0][i] = cur

for j in range(1, m):
    for i in range(j, n):
        if seq1[i] != seq2[j]:
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])
        else:
            prev = dp[j-1][i-1]
            cur = prev[0] + 1, (*prev[1], seq1[i])
            dp[j][i] = cur

print(' '.join(dp[-1][-1][1]))
