n = int(input())
nums = input().split()

i = 0
cur = prev = nums[0]
diffs = []
while i < n:
    if nums[i] != prev:
        diff = int(nums[i]) - int(prev)
        if diff < 0:
            diffs = [-1]
            break
        diffs.append(diff)
        prev = nums[i]
    i += 1
print(sum(diffs))
# if i != n:
#     cur = nums[i]

#     while i < n and nums[i] == cur:
#         i += 1
#     if i != n:
#         print(-1)
#     else:
#         diff = int(cur) - int(prev)
#         if diff < 0:
#             print(-1)
#         else:
#             print(diff)
# else:
#     print(0)
