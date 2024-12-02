def load_lists():
    a, b = [], []
    with open('day1.input', 'r') as f:
        for line in f.readlines():
            a.append(int(line.split()[0]))
            b.append(int(line.split()[1]))
    return a, b
def aoc_day1(list_a, list_b):
    list_a, list_b = sorted(list_a), sorted(list_b)
    return sum([abs(a-b) for a, b in zip(list_a, list_b)])

def aoc_day1_2(list_a, list_b):
    list_a = sorted(list_a)
    return sum([a*len(list(filter(lambda x: x == a, list_b))) for a in list_a])

a, b = load_lists()
print(aoc_day1_2(a, b))