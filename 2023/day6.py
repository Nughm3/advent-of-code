import re

with open("input6") as f:
    data = f.read().splitlines()

times = [int(n) for n in re.findall(r"\d+", data[0].split(": ")[1].replace(" ", ""))]
distances = [int(n) for n in re.findall(r"\d+", data[1].split(": ")[1].replace(" ", ""))]
# times = [int(n) for n in re.findall(r"\d+", data[0].split(": ")[1])]
# distances = [int(n) for n in re.findall(r"\d+", data[1].split(": ")[1])]

ans = 1

for race in range(len(times)):
    t = times[race]
    d = distances[race]

    count = 0
    for hold in range(t):
        remaining = t - hold
        distance = remaining * hold
        if distance > d:
            count += 1

    ans *= count if count > 0 else 1

print(ans)
