from collections import deque


ops = (lambda x: None if x % 3 != 0 else x // 3,
       lambda x: None if x % 2 != 0 else x >> 1,
       lambda x: x-1)
n = int(input())

nums = [None]*(n+1)

i = num = n
q = deque()
while num != 1:
     for op in ops:
         num = op(i)
         if num is not None and nums[num] is None:
             q.appendleft(num)
             nums[num] = i
             if num == 1:
                 break
     else:
         i = q.pop()
         continue
     break

res = ["1"]
i = 1
while i != n:
    i = nums[i]
    res.append(str(i))

print(len(res)-1,
      ' '.join(res),
      sep='\n')
