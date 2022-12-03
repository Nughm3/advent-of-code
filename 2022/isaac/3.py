import aoc

ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

input = aoc.input(3).splitlines()


@aoc.bench
def part_1():
    total = 0
    for bag in input:
        mid = len(bag) >> 1

        left = bag[:mid]
        right = bag[mid:]

        common = list(set(left).intersection(right))[0]
        priority = ALPHA.index(common) + 1
        total += priority

    print(total)


@aoc.bench
def part_2():
    total = 0
    for i in range(0, len(input), 3):
        a, b, c = input[i], input[i + 1], input[i + 2]
        common = list(set(a).intersection(b, c))[0]
        priority = ALPHA.index(common) + 1
        total += priority

    print(total)


part_1()
part_2()
