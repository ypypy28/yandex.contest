n = int(input())
seq1 = input().split()
m = int(input())
seq2 = input().split()

first = int(seq1[0] == seq2[0])
dp = [[first for _ in range(n)] for _ in range(m)]

for i in range(1, n):
    if seq1[i] == seq2[0]:
        dp[0][i] = 1
    else:
        dp[0][i] = dp[0][i-1]

for j in range(1, m):
    if seq1[0] == seq2[j]:
        dp[j][0] = 1
    else:
        dp[j][0] = dp[j-1][0]

for j in range(1, m):
    for i in range(1, n):
        if seq1[i] == seq2[j]:
            dp[j][i] = dp[j-1][i-1] + 1
        else:
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])

j, i = m-1, n-1
k = dp[j][i]
res = [None]*k
k -= 1
while k >= 0:
    cur = dp[j][i]
    while dp[j-1][i] == cur and j > 0:
        j -= 1
    while dp[j][i-1] == cur and i > 0:
        i -= 1
    res[k] = seq1[i]
    j, i = j-1, i-1
    if j < 0:
        j = 0
    if i < 0:
        i = 0
    k -=1

print(' '.join(res))
