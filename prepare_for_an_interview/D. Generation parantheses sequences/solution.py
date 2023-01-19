n = int(input())


def generate(seq, opened, closed, size):
  if len(seq) == size:
    yield ''.join(seq)
  else:
    if opened < (size >>1):
  	  yield from generate((*seq, '('), opened+1, closed, size)
    if opened-closed > 0:
      yield from generate((*seq, ')'), opened, closed+1, size)

print(*generate(('(',), 1, 0, 2*n), sep='\n')
