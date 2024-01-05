from collections import Counter
from functools import cmp_to_key

with open("input7") as f:
    data = f.read().splitlines()

data = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip().splitlines()

card_points = { "A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1 }

def most_common(counter: Counter, n: int):
    return [x[1] for x in counter.most_common(n)]
    
def five_of_a_kind(deck: Counter):
    return len(deck) == 1

def four_of_a_kind(deck: Counter):
    return len(deck) == 2 and most_common(deck, 1)[0] == 4

def full_house(deck: Counter):
    return len(deck) == 2 and most_common(deck, 2) == [3, 2]

# if not full house
def three_of_a_kind(deck: Counter):
    return most_common(deck, 1)[0] == 3

def two_pair(deck: Counter):
    return len(deck) == 3 and most_common(deck, 2) == [2, 2]

def one_pair(deck: Counter):
    return len(deck) == 4 and most_common(deck, 1)[0] == 2

def base_score(deck):
    score = 0
    cnt = Counter(deck)
    for idx, fn in enumerate([one_pair, two_pair, three_of_a_kind, full_house, four_of_a_kind, five_of_a_kind]):
        if fn(cnt):
            score += (idx + 1) * 1000000
            break
    for n in deck:
        score += 100 * (n/10)
    return score

def left_is_stronger(left, right):
    l, r = base_score(left), base_score(right)
    # if l == r:
    #     for a, b in zip(left, right):
    #         if a > b:
    #             return True
    #     return False
    return l > r

decks = []
for idx, line in enumerate(data):
    line = line.split(" ")
    cards = [card_points[card] for card in line[0]]
    decks.append((cards, int(line[1])))

# for i in range(len(decks)):
#     swapped = False

#     for j in range(0, len(decks) - i - 1):
#         if left_is_stronger(decks[j][0], decks[j + 1][0]):
#             print(f"{decks[j]} is stronger than {decks[j + 1]}")
#             decks[j], decks[j + 1] = decks[j + 1], decks[j]
#             swapped = True

#     if not swapped:
#         break

def compare(a, b):
    if left_is_stronger(a[0], b[0]):
        return 1
    else:
        return -1

from functools import cmp_to_key
decks.sort(key=cmp_to_key(compare))

for d in decks: print(d)

total = 0
for idx, (_, bid) in enumerate(decks):
    rank = idx + 1
    total += rank * bid
print(total)
