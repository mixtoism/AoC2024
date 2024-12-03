import re
def mul(o, u, flag, modifd={"do": 1, "don't": 0, "current": 1}, _int=lambda x: int(x) if x else 0):
        return (modifd.update({"current": modifd.get(flag, modifd["current"])}), modifd["current"] * _int(o) * _int(u))[1]
print(sum([mul(*m) for m in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do(?:n't)?)", "".join(open("day_3.input", "r").readlines()))]))