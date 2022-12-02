clue = open('d02.txt', 'r').read()

l = [tuple(x.split(' ')) for x in clue.split('\n')]

rock = 1
paper = 2
scissors = 3
win = 6
draw = 3
loss = 0

map = {
    'A': rock,
    'B': paper,
    'C': scissors,
    'Y': paper,
    'X': rock,
    'Z': scissors
}

winners = {
    rock: paper,
    paper: scissors,
    scissors: rock
}

losers = {
    rock: scissors,
    paper: rock,
    scissors: paper
}

# version 1
sum_v1 = 0
# for each game, calculate the score
for a, b in l:
    if map[a] == map[b]:  # draw
        sum_v1 += map[b] + draw
    elif map[a] == losers[map[b]]:  # b wins
        sum_v1 += map[b] + win
    else:
        sum_v1 += map[b] + loss  # everything else is a loss


# version 2
sum_v2 = 0

for a, b in l:
    if b == 'Y':  # draw
        sum_v2 += draw + map[a]
    elif b == 'X':  # loss
        sum_v2 += loss + losers[map[a]]
    elif b == 'Z':  # win
        sum_v2 += win + winners[map[a]]

print(f'Incorrect strategy guide: {sum_v1}')
print(f'Correct strategy guide: {sum_v2}')