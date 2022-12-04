import aoc

input = aoc.input(1, 2022).splitlines()

total = []


@aoc.bench
def calc():
    sum = 0
    for line in input:
        if line == "":
            total.append(sum)
            sum = 0
        else:
            sum += int(line)


calc()
total.sort()

print(total[-1])
print(sum([total[-1], total[-2], total[-3]]))
