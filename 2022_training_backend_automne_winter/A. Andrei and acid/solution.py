import sys


n = int(input())
if n == 1:
    print(0)
    sys.exit(0)

nums = [int(val) for val in input().split()]

for i in range(n-1):
    if nums[i] > nums[i+1]:
      print(-1)
      sys.exit(0)

print(nums[-1] - nums[0])

