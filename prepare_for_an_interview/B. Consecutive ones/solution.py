seq_ones = max_seq_ones = 0
for _ in range(int(input())):
    ch = input()
    if ch == "1":
        seq_ones += 1
    else:
        if seq_ones > max_seq_ones:
            max_seq_ones = seq_ones
        seq_ones = 0
print(max(seq_ones, max_seq_ones))
