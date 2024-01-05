with open("input5") as f:
    data = f.read()

# data = """
# seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4""".strip()

seeds = [int(n) for n in data.splitlines()[0].split(": ")[1].split(' ')]

tmp = []
for i in range(0, len(seeds), 2):
    start = seeds[i]
    length = seeds[i + 1]
    for i in range(start, start + length):
        tmp.append(i)
seeds = tmp

arrays = []
names = []
for chunk in data.split("\n\n")[1:]:
    chunk = chunk.splitlines()
    current = []
    names.append(chunk[0])
    for line in chunk[1:]:
        current.append([int(n) for n in line.split(' ')])
    arrays.append(current)
print(arrays)

for name, array in zip(names, arrays):
    mapped = []
    for subarray in array:
        dst, src, size = subarray[0], subarray[1], subarray[2]

        for idx in range(len(seeds)):
            seed = seeds[idx]
            if seed >= src and seed < src + size and seed not in mapped:
                seed += dst - src
                mapped.append(seed)

                if idx == 1:
                    print(f"{name} [{seeds[idx]}->{seed} ({dst-src})]")

                seeds[idx] = seed
            elif idx == 1:
                print(f"{name} {seed} (no change)")

print(seeds)
print(min(seeds))
