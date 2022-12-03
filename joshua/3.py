with open('3.ex') as f:
    l = f.read().splitlines()

matching = []

def calc_pri(x):
    return ord(x) - 38 if x.isupper() else ord(x) - 96


for i in l:
    p1, p2 = i[:int(len(i) / 2)], i[int(len(i) / 2):]
    for j in range(len(p1)):
        for k in range(len(p2)):
            if p1[j] == p2[k]:
                matching.append(p1[j])
                break
        else:
            continue
        break

print(sum(map(calc_pri, matching)))

matching2 = []

for i in range(0, len(l) - 2, 3):
    p1, p2, p3 = l[i], l[i + 1], l[i + 2]
    for j in range(len(p1)):
        for k in range(len(p2)):
            for m in range(len(p3)):
                if p1[j] == p2[k] and p2[k] == p3[m]:
                    matching2.append(p1[j])
                    break
            else:
                continue
            break
        else:
            continue
        break

print(sum(map(calc_pri, matching2)))
