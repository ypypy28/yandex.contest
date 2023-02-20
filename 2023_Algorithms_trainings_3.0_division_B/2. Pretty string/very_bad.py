from collections import Counter


k = int(input())
line = input()

end = len(line)
# print(k, line)
left = 0
right = left + 1 + k
skipped = k
max_seq = right - left
cur = line[0]
while right < end:
    c = Counter(line[left:right])
    cur = max(c, key=lambda x: c[x])
    while right < end and line[right] == cur:
        right += 1
    skipped = sum(c.values()) - c[cur]

    if skipped > k:
        # print(f"SKIPPED > K {cur=} {left=} {right=} {skipped=} {line[left:right]=}")
        left = right
        right = left + 1 + k
        continue

    while right < end and skipped != k:
        old_right = right
        right = right + k - skipped
        new_counter = Counter(line[old_right:right])
        c += new_counter
        cur = max(c, key=lambda x: c[x])
        # skipped = right - 1 - left - c[cur]
        skipped = sum(c.values()) - c[cur]
        # print(f"{cur=} {left=} {right=} {skipped=} {line[left:right]=}")

    while right < end and line[right] == cur:
        right += 1

    seq = right - left
    if max_seq < seq:
        max_seq = seq

    # print(f"{cur=} {left=} {right=} {skipped=} {line[left:right]=}")
    new_left = left + 1
    if right < end:
        for i in range(right-k, left, -1):
            if line[i] != cur:
                new_left = i
                break

    # left = max(left + 1, right - k - 25)
    # left = max(left + 1, new_left)
    left = new_left

    right = left + 1 + k


# last = min(right - left + 1 + k - skipped, end)
# # print(f"{last=}")
# if last > max_seq:
#     max_seq = last

print(max_seq)

