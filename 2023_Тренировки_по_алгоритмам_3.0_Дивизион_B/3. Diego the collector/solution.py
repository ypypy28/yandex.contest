from bisect import bisect_left


n = int(input())
nums = sorted({int(val) for val in input().split()})
k = int(input())
pi = [int(val) for val in input().split()]

prefix_count = {val: i+1 for i, val in enumerate(nums)}

for p in pi:
    minimum_i = bisect_left(nums, p)
    print(0 if minimum_i == 0 else prefix_count[nums[minimum_i-1]])
