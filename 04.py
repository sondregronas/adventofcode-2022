clue = open('inputs/04.txt', 'r').read()

assignment_pairs = [x for x in clue.split('\n')]
assignments = [x.split(',') for x in assignment_pairs]
assignments_ranges = [[range(int(x.split('-')[0]), int(x.split('-')[1])+1) for x in y] for y in assignments]

# Part 1:
# Find the number of ranges that are contained within the pairs
total_1 = sum(all(x in b for x in a) or
              all(x in a for x in b)
              for a, b in assignments_ranges)
print('(1): Amount of duplicate work:', total_1)

# Part 2:
# Find the number of ranges that overlap at all
total_2 = sum(any(x in b for x in a)
              for a, b in assignments_ranges)
print('(2): Amount of overlapping work:', total_2)
