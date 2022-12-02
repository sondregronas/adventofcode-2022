clue = open('d01.txt', 'r').read()

o = {}
for i, x in enumerate(clue.split('\n\n')):
    o[i] = sum(int(n) for n in x.split('\n'))

# sort keys by largest value
o = sorted(o.items(), key=lambda x: x[1], reverse=True)

# list of all values, sorted by largest
l = [x[1] for x in o]

print(f'Largest value: {l[0]}')
print(f'Top 3 values combined: {sum(l[:3])}')