n, k = [int(x) for x in input().split()]
a = [[int(x), None] for x in input().split()]
a_sorted = sorted(a, key=lambda x: x[0])

start, end = 0, k+1
a_sorted[0][1] = sum(x[0] - a_sorted[0][0] for x in a_sorted[1: k+1])
for i in range(1, n):
    a_sorted[i][1] = (
        a_sorted[i-1][1] +
        (a_sorted[i-1][0] - a_sorted[i][0])*((end - i) - (i - start))
    )
    while end < n:
        delta = ((a_sorted[end][0] - a_sorted[i][0]) - (a_sorted[i][0] - a_sorted[start][0]))
        if delta >= 0:
            break
        start += 1
        end += 1
        a_sorted[i][1] += delta

print(' '.join(f"{x[1]}" for x in a))
