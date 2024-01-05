with open("input11") as f:
    data = f.read().splitlines()

# data = """
# ...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....
# """.strip().splitlines()

galaxy = [list(row) for row in data]
# total = 0

# new = []
# for idx in range(len(galaxy)):
#     row = galaxy[idx]
#     new.append(row)
#     if "#" not in row:
#         # new.append(row)
#         xrows.append(idx)
# galaxy = [list(row) for row in list(zip(*new))]
# new = []
# for idx in range(len(galaxy)):
#     row = galaxy[idx]
#     new.append(row)
#     if "#" not in row:
#         # new.append(row)
#         xcols.append(idx)
# galaxy = [list(row) for row in list(zip(*new))]

count = 0
coord = []
for y, row in enumerate(galaxy):
    for x, col in enumerate(row):
        if col == "#":
            count += 1
            # galaxy[y][x] = count
            coord.append((x, y))
        else:
            galaxy[y][x] = 0

# for a in coord:
#     for b in coord:
#         if a != b:
#             x1, y1 = a
#             x2, y2 = b
#             total += abs(x1 - x2) + abs(y1 - y2)

# print(total / 2)

total = 0
trans = [list(i) for i in list(zip(*galaxy))]

for a in coord:
    for b in coord:
        if a != b:
            x1, y1 = a
            x2, y2 = b

            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1

            for i in range(x1, x2):
                if "#" not in trans[i]:
                    total += 1_000_000
                else:
                    total += 1
            for i in range(y1, y2):
                if "#" not in galaxy[i]:
                    total += 1_000_000
                else:
                    total += 1
print(total / 2)
