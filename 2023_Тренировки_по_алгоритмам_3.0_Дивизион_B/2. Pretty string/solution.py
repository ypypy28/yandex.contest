import sys


k = int(input())
line = input()

if not line:
    print(0)
    sys.exit(0)

end = len(line)
cur = line[0]
i = max_count = count = 1
skip = []
while i < end:
    # print(f"{i=} ", end='')
    if line[i] == cur:
        count += 1
    else:
        if len(skip) < k:
            skip.append(line[i])
            count += 1
        else:
            count = 1
            cur, *skip = skip
            i = i - k + 1
    if max_count < count:
        max_count = count

    i += 1
    # print(f"{i=} {skip= }", end='')
    if i == end and skip:
        i = i - len(skip) + 1
        cur, *skip = skip
        count = 1
    # print(f"{i=}")

print(max_count)
