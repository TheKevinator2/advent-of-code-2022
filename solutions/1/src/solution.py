from functools import reduce


def sum_entries(lines):
    l = [
        list(filter(None, s.split("\n")))
        for s in reduce(lambda a, b: a + b, lines).split("\n\n")
    ]
    return [sum(map(lambda a: int(a), ll)) for ll in l]


def get_max_calories(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
        summed = sum_entries(lines)
        return max(summed)


def get_max_calories_for_top_n(file_name, n):
    with open(file_name, "r") as f:
        lines = f.readlines()
        summed = sum_entries(lines)
        return sum(sorted(summed, reverse=True)[:n])


calories = get_max_calories("../input.txt")
print(calories)

calories = get_max_calories_for_top_n("../input.txt", 3)
print(calories)
