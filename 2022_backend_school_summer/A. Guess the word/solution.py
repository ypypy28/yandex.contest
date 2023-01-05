S, Q = (input() for _ in range(2))
s_tokens = dict()
correct = set()
for i, ch in enumerate(S):
    if Q[i] == ch:
        correct.add(i)
    else:
        s_tokens[ch] = s_tokens.get(ch, 0)+1

for i, ch in enumerate(Q):
    if i in correct:
        print("correct")
    else:
        j = s_tokens.get(ch, 0)
        if j != 0:
            print("present")
            s_tokens[ch] -= 1
        else:
            print("absent")
