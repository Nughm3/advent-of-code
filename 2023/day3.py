import re

with open("input3") as f:
    data = f.read().splitlines()

def issymbol(c):
    # return c != '.' and not c.isnumeric()
    return c == '*'

# data = """
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# """.strip().splitlines()

total = 0

for y, line in enumerate(data):
    for x, ch in enumerate(line):
        if issymbol(ch):
            parts = []
            for dy in range(y - 1, y + 2):
                if dy < 0 or dy >= len(data):
                    continue
                for match in re.finditer(r"\d+", data[dy]):
                    if abs(match.start() - x) <= 1 or abs(match.end() - 1 - x) <= 1:
                        parts.append(int(match.group()))
            if len(parts) == 2:
                total += parts[0] * parts[1]

print(total)
