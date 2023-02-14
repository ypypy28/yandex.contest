import sys


k = int(input())
line = input()

end = len(line)
left = right = skipped = max_seq = 0
# print(k, line)
while right+1 < end:
    if line[left] == line[right+1]:
        right += 1
    else:
        if skipped < k:
            right += 1
            skipped += 1
        else:
            seq = right - left + 1
            if max_seq < seq:
                max_seq = seq
            left += 1 # max(left+1, right-k-1)
            right = left
            skipped = 0
    # print(f"{left=} {right=} {skipped=} {line[left:right+1]=} {right-left+1=}")

last = min(right - left + 1 + k - skipped, end)
if last > max_seq:
    max_seq = last

print(max_seq)

