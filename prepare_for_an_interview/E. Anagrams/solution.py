a, b = (input() for _ in range(2))


if len(a) != len(b):
  print(0)
else:
  counter = dict()
  for i in range(len(a)):
    counter[a[i]] = counter.get(a[i], 0) + 1
    counter[b[i]] = counter.get(b[i], 0) - 1
  print(int(all(val == 0 for val in counter.values())))
