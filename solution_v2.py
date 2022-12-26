import sys


n = int(input())
nums = tuple(int(x) for x in input().split())
nums_set = set(nums)
if len(nums_set) == 1:
    print(0)
    sys.exit(0)
elif len(nums_set) > 2:
    print(-1)
    sys.exit(0)

if nums[-1] < nums[0]:
    print(-1)
    sys.exit(0)

diff = 0
for i in range(n-1):
    if nums[i] != nums[i+1]:
        if diff != 0:
            print(-1)
            sys.exit(0)
        diff = nums[i+1] - nums[i]
        if diff < 0:
            print(-1)
            sys.exit(0)
print(diff)
