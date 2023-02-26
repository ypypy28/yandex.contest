ops = (lambda x: x+1, lambda x: x*2, lambda x: x*3)
n = int(input())

nums = [(1, (0,))]

i = 0
num, prev = nums[i]
while num != n:
    for op in ops:
        nums.append((op(num), (*prev, len(nums))))
    i += 1
    num, prev = nums[i]

print(len(nums[i][1])-1)
print(*[nums[j][0] for j in nums[i][1]])
