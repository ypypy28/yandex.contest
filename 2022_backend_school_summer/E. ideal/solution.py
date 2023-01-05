def make_seq(br: dict[str, list[int]], ignore: int) -> list[str]:
    seq = []
    i = j = 0
    while i < len(br['(']) and j < len(br[')']):
        if ignore == br['('][i]:
            i += 1
            continue
        elif ignore == br[')'][j]:
            j += 1
            continue
        elif br['('][i] < br[')'][j]:
            seq.append('(')
            i += 1
        else:
            seq.append(')')
            j += 1

    while i < len(br['(']):
        if ignore != br['('][i]:
            seq.append('(')
        i += 1

    while j < len(br[')']):
        if ignore != br[')'][j]:
            seq.append(')')
        j += 1

    return seq


def is_valid(br, ignore):
    stack = []
    for i, ch in enumerate(make_seq(br, ignore)):
        if ch == '(':
            stack.append(')')
        elif not stack:
            return False
        else:
            stack.pop()

    return True if not stack else False


with open('input3.txt', 'r') as f:
    expr = f.read().strip()

# print(expr)
brackets = {'(': [], ')': []}
for i, ch in enumerate(expr):
    if ch in '()':
        brackets[ch].append(i)

del expr

if (not brackets['(']
    or not brackets[')']
    or abs(len(brackets['(']) - len(brackets[')'])) != 1
    ):
    print(-1)
else:
    candidates = brackets[max(brackets, key=lambda br: len(brackets[br]))]

    # print(brackets)
    # print(candidates)

    res = -1
    for candidate in candidates:
        if is_valid(brackets, candidate):
            res = candidate + 1  # task starts indexes from 1
            break

    print(res)
