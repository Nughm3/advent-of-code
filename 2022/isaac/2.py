import aoc

input = [x.split(" ") for x in aoc.input(2, 2022).splitlines()]

win = {"A": "Y", "B": "Z", "C": "X"}
lose = {"A": "Z", "B": "X", "C": "Y"}

scoring = {}
scoring["A"] = scoring["X"] = 1
scoring["B"] = scoring["Y"] = 2
scoring["C"] = scoring["Z"] = 3


@aoc.bench
def part1():
    score = 0

    for them, me in input:
        if win[them] == me:
            score += scoring[me] + 6
        elif lose[them] == me:
            score += scoring[me]
        else:
            score += scoring[me] + 3

    print(score)


@aoc.bench
def part2():
    score = 0

    for them, outcome in input:
        if outcome == "X":
            score += scoring[lose[them]]
        elif outcome == "Z":
            score += scoring[win[them]] + 6
        else:
            score += scoring[them] + 3

    print(score)


part1()
part2()
