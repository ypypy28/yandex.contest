k = int(input())
line = input()

end = len(line)
left = right = skipped = max_seq = 0
counter = {line[0]: 1}
while right+1 < end:
    if line[left] == line[right+1]:
        right += 1
        counter[line[left]] = counter.get(line[left], 0) + 1
    else:
        if skipped < k:
            right += 1
            skipped += 1
            counter[line[right]] = counter.get(line[right], 0) + 1
        else:
            seq = right - left + 1
            if max_seq < seq:
                max_seq = seq
            old_left = left
            cur = line[left]
            while line[left] == cur:
                left += 1
            counter[line[old_left]] -= left - old_left

            if left > right:
                right = left
                skipped = 0
                counter.clear()
                counter[line[left]] = 1
            else:
                skipped = sum(counter.values()) - counter[line[left]]

last = min(right - left + 1 + k - skipped, end)
if last > max_seq:
    max_seq = last

print(max_seq)

