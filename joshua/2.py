with open('2.in') as f:
    l = f.read().splitlines()

win = {
        'X': 'C',
        'Y': 'A',
        'Z': 'B'
        }
towin = {
        'C': 'X',
        'A': 'Y',
        'B': 'Z'
        }

tolose = {
        'C': 'Y',
        'A': 'Z',
        'B': 'X'
        }
total = 0

for i in l:
    p1, p2 = i.split()    
    if ord(p1) - ord('A') == ord(p2) - ord('X'):
        total += 3
    elif win[p2] == p1:
        total += 6
    total += ord(p2) - ord('X') + 1


print('Part 1: ', total)

total2 = 0

for i in l:
    p1, p2 = i.split()    
    if p2 == 'X':
        total2 += ord(tolose[p1]) - ord('X')  + 1
    elif p2 == 'Y':
        total2 += 3
        total2 += ord(p1) - ord('A') + 1
    elif p2 == 'Z':
        total2 += 6
        total2 += (ord(towin[p1]) - ord('X')) + 1


print('Part 2: ', total2)
