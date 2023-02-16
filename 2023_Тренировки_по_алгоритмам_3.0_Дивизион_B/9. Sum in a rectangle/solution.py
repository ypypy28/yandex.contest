n, m, k = [int(val) for val in input().split()]
prefix_sum = [[0 for _ in range(m+1)] for _ in range(n+1)]

for x in range(n):
    vals = [int(val) for val in input().split()]
    for y in range(m):
        prefix_sum[x+1][y+1] = vals[y] + prefix_sum[x][y+1] + prefix_sum[x+1][y] - prefix_sum[x][y]


for _ in range(k):
    x1, y1, x2, y2 = [int(val) for val in input().split()]
    print(prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1])
