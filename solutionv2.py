n, k = [int(x) for x in input().split()]
a = [(int(x), i) for i, x in enumerate(input().split())]
a_sorted = sorted(a)
# print([x[0] for x in a_sorted])

start, end = 0, k+1
dist = [0]*n
# dist[0] = sum(x[0] - a_sorted[0][0] for x in a_sorted[1: k+1])
for i in range(n):
    while end < n and ((a_sorted[end-1][0] - a_sorted[i][0]) < (a_sorted[i][0] - a_sorted[start][0])):
        # print(f"{a_sorted[end-1][0] - a_sorted[i][0]=} {(a_sorted[i][0] - a_sorted[start][0])=}")
        if end-1 == i and a_sorted[end][0] - a_sorted[i][0] > a_sorted[i][0] - a_sorted[start+1][0]:
            break
        start += 1
        end += 1
    # while start > -1 and ((a_sorted[end-1][0] - a_sorted[i][0]) < (a_sorted[i][0] - a_sorted[start][0])):
    #     start -= 1
    #     end -=1
    # print(f"{(start,end)=} {k=}", end=' ')
    # if (end - start) != k+1:
    #     print(f"{start=}")
    #     start -= k + 1 - end + start
    #     print(f"{start=}")
    dist[i] = sum(abs(a_sorted[i][0] - x[0]) for x in a_sorted[start:end])
    # print(f"{a_sorted[i][0]=}: {dist[i]=} args {' '.join((str(x[0]) for x in a_sorted[start:end]))}")
# print(f"{dist=}")
res = [str(dist[j]) for _, j in a_sorted]
print(' '.join(res))


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

# left, right, s = 0, k, dist[0]
# d = [0]*n
# d[0] = s
# for i in range(n-1):
#     s += (a_sorted[i][0] - a_sorted[i+1][0]) * ((right - i) - (i - left + 1))
#     print("S", s, f"{((right - i) - (i - left + 1))=}")
#     while right < n-1:
#         delta = (a_sorted[right+1][0] - a_sorted[i+1][0]) - (a_sorted[i+1][0] - a_sorted[left][0])
#         if delta < 0:
#             left += 1
#             right += 1
#             s += delta
#         else:
#             break
#     d[i+1] = s
# print(dist)
# print(d)
