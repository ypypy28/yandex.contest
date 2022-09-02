CHUNK_SIZE = 1024
brackets = {"{": [], "}": []}


def merged_brackets(open_brs, close_brs, ignore=None):
    i = j = 0
    end_i, end_j = (len(brs) for brs in (open_brs, close_brs))
    while i < end_i and j < end_j:
        if open_brs[i] == ignore:
            i += 1
            continue
        elif close_brs[j] == ignore:
            j += 1
            continue

        if open_brs[i] < close_brs[j]:
            yield "{"
            i += 1
        else:
            yield "}"
            j += 1

    while i < end_i:
        if open_brs[i] == ignore:
            i += 1
            continue
        yield "{"
        i += 1
    while j < end_j:
        if close_brs[j] == ignore:
            j += 1
            continue
        yield "}"
        j += 1


def extract_br_positions(line, pos):
    for i, ch in enumerate(tmp):
        for br in brackets:
            if ch == br:
                brackets[br].append(pos + i)


def is_valid_sequence(seq):
    opening_stack = 0
    for br in seq:
        if not opening_stack:
            if br == "}":
                return False
            else:
                opening_stack += 1
        else:
            if br == "{":
                opening_stack += 1
            else:
                opening_stack -= 1

    return True if not opening_stack else False


with open("input.txt") as f:
    pos = 1
    while True:
        tmp = f.read(CHUNK_SIZE)
        if not tmp:
            break
        extract_br_positions(tmp, pos)
        pos += CHUNK_SIZE
        del tmp

res_idx = -1
# candidate_idx = max((brackets["{"], brackets["}"]), key=len)
candidate_idx = None
opens, closes = len(brackets["{"]), len(brackets["}"])
if opens - closes not in (-1, 1):
    pass
elif opens > closes:
    candidate_idx = brackets["{"]
else:
    candidate_idx = brackets["}"]

if candidate_idx:
    for i in candidate_idx:
        seq = ''.join(merged_brackets(brackets["{"], brackets["}"], ignore=i))
        if is_valid_sequence(seq):
            res_idx = i
            break
        del seq

print(res_idx)
