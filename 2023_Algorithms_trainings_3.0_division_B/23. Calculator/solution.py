ops = (lambda x: None if x % 2 != 0 else x >> 1,
       lambda x: None if x % 3 != 0 else x // 3,
       lambda x: x-1)
n = int(input())

nums = [n]
prevs = [None]

i = 0
num, prev = nums[i], prevs[i]
while num != 1:
    for op in ops:
        num = op(nums[i])
        if num is not None:
            nums.append(num)
            prevs.append(i)
            if num == 1:
                prev = len(nums)-1
                break
    else:
        i += 1
        continue
    break

res = []
while prev is not None:
    res.append(str(nums[prev]))
    prev = prevs[prev]

print(len(res)-1 if res else 0,
      ' '.join(res) or 1,
      sep='\n')
