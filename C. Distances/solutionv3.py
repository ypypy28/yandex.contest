n, k = [int(x) for x in input().split()]
a = [(int(x), i) for i, x in enumerate(input().split())]
a_sorted = sorted(a)
# print([x[0] for x in a_sorted])

start, end = 0, k+1
dist = [0]*n
dist[0] = sum(x[0] - a_sorted[0][0] for x in a_sorted[1: k+1])
# print(dist)
for i in range(1, n):
    # cur_dist = dist[i-1] + a_sorted[i-1][0]*k - a_sorted[i][0]*k
    # print(i, cur_dist)
    while end < n and ((a_sorted[end][0] - a_sorted[i][0]) < (a_sorted[i][0] - a_sorted[start][0])):
        # print(f"{a_sorted[end-1][0] - a_sorted[i][0]=} {(a_sorted[i][0] - a_sorted[start][0])=}")
        # if end-1 == i and a_sorted[end][0] - a_sorted[i][0] > a_sorted[i][0] - a_sorted[start+1][0]:
            # break
        start += 1
        end += 1
    # dist[i] = cur_dist
    # while start > -1 and ((a_sorted[end-1][0] - a_sorted[i][0]) < (a_sorted[i][0] - a_sorted[start][0])):
    #     start -= 1
    #     end -=1
    # print(f"{(start,end)=} {k=}", end=' ')
    # if (end - start) != k+1:
    #     print(f"{start=}")
    #     start -= k + 1 - end + start
    #     print(f"{start=}")
    # dist[i] = sum(abs(a_sorted[i][0] - x[0]) for x in a_sorted[start:end])
    dist[i] = sum(abs(a_sorted[i][0] - x[0]) for x in a_sorted[start:end])
    # print(f"{a_sorted[i][0]=}: {dist[i]=} args {' '.join((str(x[0]) for x in a_sorted[start:end]))}")
# print(f"{dist=}")
# print(a_sorted, dist, sep='\n')
# res = [str(dist[j]) for i, (_, j) in enumerate(a_sorted)]
pos = iter((x[1] for x in a_sorted))
dist.sort(key=lambda x: next(pos))
print(*dist, sep=' ')


# for i in range(1, n):
#     s = dist[i-1] + (a_sorted[i-1][0] - a_sorted[i][0]) * ((end - i + 1) - (i - start))
#     print("S", s, f"{((end - i - 1) - (i - start))=}")
#     while end < n:
#         delta = ((a_sorted[end][0] - a_sorted[i][0])
#                  - (a_sorted[i][0] - a_sorted[start][0]))
#         if delta >= 0:
#             break
#         start += 1
#         end += 1
#         s += delta
#     dist[i] = s
#     print(i, start, end, s)

# start, end, s = 0, k, dist[0]
# d = [0]*n
# d[0] = s
# for i in range(n-1):
#     s += (a_sorted[i][0] - a_sorted[i+1][0]) * ((end - i) - (i - start + 1))
#     print("S", s, f"{((end - i) - (i - start + 1))=}")
#     while end < n-1:
#         delta = (a_sorted[end+1][0] - a_sorted[i+1][0]) - (a_sorted[i+1][0] - a_sorted[start][0])
#         if delta > 0:
#             break
#         start += 1
#         end += 1
#         print(f"{s=} {delta=}")
#         s += delta
#     d[i+1] = s
# print(dist)
# print(d)
