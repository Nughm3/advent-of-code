with open('input2') as f:
    data = f.read().splitlines()

sum = 0

for line in data:
    id = int(line.split(' ')[1][:-1])
    turns = line.split(': ')[1].split('; ')

    red = green = blue = 0
    for turn in turns:
        colors = turn.split(', ')

        for color in colors:
            n = int(color.split(' ')[0])
            if color.endswith("red"):
                red = max(red, n)
            elif color.endswith("green"):
                green = max(green, n)
            elif color.endswith("blue"):
                blue = max(blue, n)
            else:
                raise Exception("invalid color")

    sum += red * green * blue

print(sum)
