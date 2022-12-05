o = sorted([sum(int(n) for n in x.split('\n')) for x in open('inputs/01.txt', 'r').read().split('\n\n')], reverse=True)
print(f'Largest: {o[0]} calories \n'
      f'Top 3: {sum(o[:3])} calories')
