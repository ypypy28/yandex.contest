j,s = (input() for _ in range(2))
j = set(j)
print(sum(rock in j for rock in s))
