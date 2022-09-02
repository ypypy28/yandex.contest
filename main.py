from typing import Literal, Generator, Iterable


CHUNK_SIZE = 10
brackets: dict[str, list[int]] = {"{": [], "}": []}


def merged_brackets(open_brs: list[int], close_brs: list[int], ignore: int | None=None
                    ) -> Generator[Literal["{"] | Literal["}"], None, None]:
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


def extract_br_positions(line: str, pos: int) -> None:
    for i, ch in enumerate(tmp):
        for br in brackets:
            if ch == br:
                brackets[br].append(pos + i)


def is_valid_sequence(seq: Iterable) -> bool:
    opening_stack: list[int] = []
    for br in seq:
        if not opening_stack:
            if br == "}":
                return False
            else:
                opening_stack.append(br)
        else:
            if br == "{":
                opening_stack.append(br)
            else:
                opening_stack.pop()

    return True if not opening_stack else False


with open("input.txt") as f:
    pos = 1
    while True:
        tmp = f.read(CHUNK_SIZE)
        if not tmp:
            break
        extract_br_positions(tmp, pos)
        pos += CHUNK_SIZE

res_idx = -1
candidate_idx = max(brackets.values(), key=len)
print(f"{brackets=}", ''.join(merged_brackets(brackets["{"], brackets["}"])))
print(f"{candidate_idx=}")
for i in candidate_idx:
    seq = ''.join(merged_brackets(brackets["{"], brackets["}"], ignore=i))
    print(f"ignore={i}, {seq=}")
    if is_valid_sequence(seq):
        res_idx = i
        break

print(res_idx)

# for br, i in merged_brackets(brackets["{"], brackets["}"]):
#     if not opening_stack:
#         if br == "}":
#             if res_idx == -1:
#                 res_idx = i
#             else:
#                 break
#         else:
#             opening_stack.append(i)
#     else:
#         if br == "{":
#             opening_stack.append(i)
#         else:
#             opening_stack.pop()

# if not opening_stack:
#     print(res_idx)
# elif len(opening_stack) == 1:
#     print(opening_stack[0])
# else:
#     print(-1)
# print(f"{res_idx=} {opening_stack=}")
# # print(-1 if len(opening_stack) != 1 else max(res_idx, opening_stack[0]))

# print(''.join(br for br, _ in merged_brackets(brackets["{"], brackets["}"])))
