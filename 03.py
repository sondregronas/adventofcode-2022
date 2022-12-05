clue = open('inputs/03.txt', 'r').read()

# 1
# priorities: a-Z have values 1-52
priorities = {letter: i+1 for i, letter in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')}
# rucksacks: contains objects represented by a-Z
rucksacks = [x for x in clue.split('\n')]
# compartments: split all rucksacks into two equal compartments
compartments = [(rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]) for rucksack in rucksacks]

# find the shared item in each compartment, and add its priority to the total
total_1 = 0
for a, b in compartments:
    for letter in a:
        if letter in b:
            total_1 += priorities[letter]
            break

print('(1): Sum of priorities:', total_1)

# 2
# groups: add 3 rucksacks together into groups
groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]

# find the shared item in each group, and add the priority of that item to the total
total_2 = 0
for group in groups:
    for letter in group[0]:
        if letter in group[1] and letter in group[2]:
            total_2 += priorities[letter]
            break

print('(2): Sum of priorities, groups of 3:', total_2)
