import sys


k = int(input())
line = input()

if not line:
    print(0)
    sys.exit(0)

end = len(line)
cur = line[0]
i = max_count = count = 1
skipped = 0
while i < end:
    # print(f"{i=} ", end='')
    if line[i] == cur:
        count += 1
    else:
        if skipped < k:
            skipped += 1
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 1
            skipped = 0
            i = i - k + 1
            cur = line[i-1]


    i += 1
    # print(f"{i=} {skip= }", end='')
    if i == end and skipped != 0 and max_count < skipped:
        i = i - skipped + 1
        skipped = 0
        cur = line[i-1]
        count = 1
    # print(f"{i=}")

if max_count < count:
    max_count = count
print(max_count)
