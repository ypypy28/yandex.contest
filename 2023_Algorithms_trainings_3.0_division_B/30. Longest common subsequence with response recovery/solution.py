n = int(input())
seq1 = input().split()
m = int(input())
seq2 = input().split()

empty = (0, tuple())
dp = [[empty for _ in range(n)] for _ in range(m)]

dp[0][0] = (int(seq1[0] == seq2[0]), tuple())
max_subseq = empty
for i in range(1, n):
    if seq1[i] !=  seq2[0]:
        dp[0][i] = empty
    else:
        cur = dp[0][i-1][0] + 1, (seq2[0],)
        if cur[0] > max_subseq[0]:
            max_subseq = cur
        dp[0][i] = cur

for j in range(1, m):
    for i in range(j, n):
        if seq1[i] != seq2[j]:
            dp[j][i] = empty
        else:
            # prev = max(dp[j][i-1], dp[j-1][i])
            prev = dp[j-1][i-1]
            cur = prev[0] + 1, (*prev[1], seq1[i])
            # print(f"{cur=}")
            if cur[0] > max_subseq[0]:
                max_subseq = cur
            dp[j][i] = cur

# print(*dp, sep='\n')
# print(max_subseq)
print(' '.join(max_subseq[1]))
