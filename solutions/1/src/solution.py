from functools import reduce


def collect_entries(lines):
    l = [
        list(filter(None, s.split("\n")))
        for s in reduce(lambda a, b: a + b, lines).split("\n\n")
    ]
    return [list(map(lambda a: int(a), ll)) for ll in l]


def get_max_calories(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
        entries = collect_entries(lines)
        return max([sum(entry) for entry in entries])


def get_max_calories_for_top_n(file_name, n):
    with open(file_name, "r") as f:
        lines = f.readlines()
        entries = collect_entries(lines)
        return sum(sorted([sum(entry) for entry in entries], reverse=True)[:n])


calories = get_max_calories("../input.txt")
print(calories)

calories = get_max_calories_for_top_n("../input.txt", 3)
print(calories)
