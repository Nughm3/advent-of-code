with open("input9") as f:
    data = f.read().splitlines()

# data = """
# 0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45
# """.strip().splitlines()

def diff(seq):
    a = []
    for i in range(len(seq) - 1):
        a.append(seq[i + 1] - seq[i])
    return a

def next(seq):
    d = diff(seq)
    layers = [seq]
    while len(list(filter(lambda x: x != 0, d))) != 0:
        layers.append(d)
        d = diff(d)
    layers.append(d)

    layers[-1].append(0)
    for i in range(len(layers) - 2, 0, -1):
        layers[i].append(layers[i + 1][-1] + layers[i][-1])
    layers[0][-1] += layers[1][-1]
        
    return layers[0][-1]

total = 0
for line in data:
    seq = [int(n) for n in line.split(' ')]
    total += next(seq[::-1])
print(total)
