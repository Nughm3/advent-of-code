from itertools import repeat

with open("input8") as f:
    data = f.read().splitlines()

data = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)   
""".strip().splitlines()

maps = {}
ins = data[0]
names = []

for line in data[2:]:
    line = line.split(" = ")
    name = line[0]
    pos = line[1].lstrip("(").rstrip(")").split(", ")
    maps[name] = (pos[0], pos[1])
    names.append(name)

step = 0
pos = list(filter(lambda node: node[-1] == "A", names))

cycle_lengths = []
for p in pos:
    step = 0
    offset = None
    c = p
    for cmd in repeat(ins):
        c = maps[c][0] if cmd == "L" else maps[c][1]
        step += 1

        if c[-1] == "Z" and offset is None:
            offset = step
        elif c == p:
            break
    cycle_lengths.append((step, offset))

print(cycle_lengths)
