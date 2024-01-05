with open("input1") as f:
    data = f.read().splitlines()

for part in range(1, 3):
    total = 0

    for line in data:
        if part == 2:
            for a, b in [
                ("one", "one1one"),
                ("two", "two2two"),
                ("three", "three3three"),
                ("four", "four4four"),
                ("five", "five5five"),
                ("six", "six6six"),
                ("seven", "seven7seven"),
                ("eight", "eight8eight"),
                ("nine", "nine9nine"),
            ]:
                line = line.replace(a, b)

        first = len(line)
        for idx, ch in enumerate(line):
            if ch.isnumeric():
                first = min(first, idx)
        last = 0
        for idx, ch in enumerate(line[::-1]):
            if ch.isnumeric():
                last = max(last, len(line) - idx - 1)
        total += int(line[first] + line[last]) 

    print(part, total)
