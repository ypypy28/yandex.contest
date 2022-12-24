n, k = [int(x) for x in input().split()]
a = [[int(x), None] for x in input().split()]
a_sorted = sorted(a)

start, end = 0, k+1
a_sorted[0][1] = sum(x[0] - a_sorted[0][0] for x in a_sorted[1: k+1])
for i in range(1, n):
    while end < n and ((a_sorted[end][0] - a_sorted[i][0]) < (a_sorted[i][0] - a_sorted[start][0])):
        start += 1
        end += 1
    a_sorted[i][1] = sum(a_sorted[i][0] - x[0] for x in a_sorted[start:i]) + sum(x[0] - a_sorted[i][0] for x in a_sorted[i+1:end])

print(' '.join(f"{x[1]}" for x in a))
