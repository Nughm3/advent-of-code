import aoc

input = aoc.today().splitlines()

@aoc.bench
def both():

    count_a = 0
    count_b = 0
    for line in input:
        line = line.split(",")
    
        a = line[0].split("-")
        a = set(range(int(a[0]), int(a[1])+1))

        b = line[1].split("-")
        b = set(range(int(b[0]), int(b[1])+1))
    
        if a.issubset(b) or b.issubset(a):
            count_a += 1
        if a.intersection(b):
            count_b += 1

    print(count_a)
    print(count_b)
    
both()
