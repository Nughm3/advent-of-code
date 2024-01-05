with open("input10") as f:
    data = f.read().splitlines()

# data = """
# FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L
# """.strip().splitlines()

start = None
for y, line in enumerate(data):
    for x, c in enumerate(line):
        if c == "S":
            start = (x, y)

delta = [(-1, 0, ["L", "F", "-"]), (0, -1, ["7", "F", "|"]), (1, 0, ["J", "7", "-"]), (0, 1, ["L", "J", "|"])]

pos = []
for dx, dy, types in delta:
    x, y = start; x += dx; y += dy
    if x >= 0 and x < len(data[0]) and y >= 0 and y < len(data) and data[y][x] in types:
        d = dx if dx != 0 else dy
        horiz = dy == 0
        pos.append((x, y, d, horiz))

p = pos[0]
step = area = 0
oldp = None
mask = [[" " for _ in range(len(data[0]))] for _ in range(len(data))]
enclosed = []
traversed = [[False for _ in range(len(data[0]))] for _ in range(len(data))]
while p != start and oldp != p:
    x, y, d, horiz = p
    # print(p)
    oldp = p
    c = data[y][x]
    traversed[y][x] = True

    if c == "-":
        x += d
        mask[y][x] = "R" if d == 1 else "L"
    elif c == '|':
        y += d
        mask[y][x] = "D" if d == 1 else "U"
    elif c == "L":
        enclosed.append((x + 1, y - 1))
        if horiz:
            y -= 1
            d = -1
            mask[y][x] = "U"
        else:
            x += 1
            d = 1
            mask[y][x] = "R"
        horiz = not horiz
    elif c == "F":
        enclosed.append((x + 1, y + 1))
        if horiz:
            y += 1
            mask[y][x] = "D"
        else:
            x += 1
            mask[y][x] = "R"
        d = 1
        horiz = not horiz
    elif c == "7":
        enclosed.append((x - 1, y + 1))
        if horiz:
            y += 1
            d = 1
            mask[y][x] = "D"
        else:
            x -= 1
            d = -1
            mask[y][x] = "L"
        horiz = not horiz
    elif c == "J":
        enclosed.append((x - 1, y - 1))
        if horiz:
            y -= 1
            mask[y][x] = "U"
        else:
            x -= 1
            mask[y][x] = "L"
        d = -1
        horiz = not horiz
        
    step += 1
    p = (x, y, d, horiz)
# print(step / 2)

# print('---')
for y in range(len(data)):
    for x in range(len(data[0])):
        if not traversed[y][x]:
            l = list(data[y])
            l[x] = "."
            data[y] = "".join(l)
expand = [[" " for _ in range(len(data[0]) * 3)] for _ in range(len(data) * 3)]
dots = 0
for y, row in enumerate(data):
    for x, col in enumerate(row):
        dy = 3 * y + 1; dx = 3 * x + 1
        expand[dy][dx] = col if mask[y][x] != " " else " "
        expand[dy][dx] = col
        ch = data[y][x]
        if ch == ".":
            dots += 1
        elif ch == "L":
            expand[dy-1][dx] = "|"
            expand[dy][dx+1] = "-"
        elif ch == "F":
            expand[dy+1][dx] = "|"
            expand[dy][dx+1] = "-"
        elif ch == "J":
            expand[dy-1][dx] = "|"
            expand[dy][dx-1] = "-"
        elif ch == "7":
            expand[dy+1][dx] = "|"
            expand[dy][dx-1] = "-"
        elif ch == "|":
            expand[dy-1][dx] = expand[dy+1][dx] = "|"
        elif ch == "-":
            expand[dy][dx-1] = expand[dy][dx+1] = "-"
        elif ch == "S":
            expand[dy][dx-1] = expand[dy][dx+1] = "-"
            expand[dy-1][dx] = expand[dy+1][dx] = "|"
            
# for row in expand:
#     for col in row:
#         print(col, end="")
#     print()
x, y = pos[0][0], pos[0][1]
q = [(9, 0)]
v = []
while len(q) > 0:
    p = q.pop(0)
    if p in v:
        continue
    v.append(p)

    expand[p[1]][p[0]] = "O"
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            x = p[0] + dx; y = p[1] + dy
            if x < 0 or x >= len(expand[0]) or y < 0 or y >= len(expand):
                continue
            if expand[y][x] == "." or expand[y][x] == " ":
                q.append((x, y))
            

print("---")
for row in expand:
    for col in row:
        print(col, end="")
    print()

dots2=0
for y in expand:
    for c in y:
        if c == ".":
            dots2 += 1

print(dots2)
