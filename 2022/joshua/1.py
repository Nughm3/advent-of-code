with open('1.in') as f:
    l = f.read().splitlines()

sums = [0 for i in range(1000)]
c = 0
for i in l:
    if i == '':
        c += 1
    else:
        sums[c] += int(i)

print('Part 1: ', max(sums))

total = 0
for i in range(3): total += (sums.pop(sums.index(max(sums))))
print('Part 2: ', total)
