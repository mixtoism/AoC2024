from functools import cache
def load_levels():
    with open('day2.input', 'r') as f:
        return [list(map(int, line.split())) for line in f.readlines()]

def aoc_day2(levels):
    return sum([compute(level) for level in levels])

def compute(level):
    diff = [level[x] - level[x - 1] for x in range(1, len(level))]
    return list(filter(lambda x: x not in range(-3, 4), diff)) == [] and ((min(diff) < 0 and max(diff) < 0) or (min(diff) > 0 and max(diff) > 0))

def second_chance(level):
    for avoided in range(len(level)):
        if compute(level[0:avoided] + level[avoided+1:]):
            return True
    return False

def aoc_day2_2(levels):
    computed = [compute(level) for level in levels]
    n_first = len(list(filter(lambda x: x, computed)))
    n_else = sum(map(lambda x: second_chance(x), filter(lambda x:  not compute(x), levels)))
    return n_first + n_else
    
levels = load_levels()
print(aoc_day2_2(levels))