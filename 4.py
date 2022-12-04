with open('4.in') as f:
    l = f.read().splitlines()

subsets = 0
intersections = 0

for i in l:
    r = [[int(k) for k in j.split('-')] for j in i.split(',')]
    r1 = set(range(r[0][0], r[0][1] + 1))
    r2 = set(range(r[1][0], r[1][1] + 1))
    subsets += r1.issubset(r2) or r2.issubset(r1)
    intersections += 1 if r1.intersection(r2) else 0

print(f'Part 1: {subsets}\nPart 2: {intersections}')
