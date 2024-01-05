with open("input12") as f:
    data = f.read().splitlines()

data = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".strip().splitlines()

total = 0

for line in data:
    line = line.split(" ")
    springs = line[0]
    clusters = [c.strip(".") for c in springs.split(".") if len(c) > 0]
    groups = [int(i) for i in line[1].split(",")][::-1]

    print(clusters, groups)
    ways = 0

    for g in groups:
        for cluster in clusters[::-1]:
            l = len(cluster)
            for c in cluster:
                if c == "#":
                    g -= 1
                    l -= 1
            if l > g:
                ways += l - g + 1
            elif l != 0 or g != 0:
                raise Exception("no match between cluster and group size")

    print(ways)
    total += ways
    # break

print(total)
