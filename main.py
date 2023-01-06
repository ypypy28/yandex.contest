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
    opening_count = 0
    for br in seq:
        if br == "{":
            opening_count += 1
        else:
            if not opening_count:
                return False
            else:
                opening_count -= 1

    return True if not opening_count else False


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
# print(f"{brackets=}", ''.join(merged_brackets(brackets["{"], brackets["}"])))
# print(f"{candidate_idx=}")
for i in candidate_idx:
    seq = ''.join(merged_brackets(brackets["{"], brackets["}"], ignore=i))
    # print(f"ignore={i}, {seq=}")
    if is_valid_sequence(seq):
        res_idx = i
        break

print(res_idx)
