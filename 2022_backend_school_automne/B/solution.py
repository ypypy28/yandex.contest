from collections import namedtuple


Participant = namedtuple("Participant", "name discipline score penalty")
n = int(input())
disciplines = {name: int(count)
              for name, count in [input().split(',') for _ in range(n)]}
k = int(input())
participants = [Participant(name, discipline, int(score), int(penalty))
                for name, discipline, score, penalty in (input().split(',') for _ in range(k))]

participants.sort(key=lambda x: (x.discipline, -x.score, x.penalty, x.name))
winners = []
for p in participants:
    if disciplines[p.discipline] > 0:
        disciplines[p.discipline] -= 1
        winners.append(p.name)

print(*sorted(winners), sep='\n')
