def collect_entries(lines):
    l = []
    ll = []
    for line in lines:
        if line == "\n":
            l.append(ll)
            ll = []
            continue
        ll.append(int(line.rstrip()))
    return l


def get_max_calories(file_name, n):
    with open(file_name, "r") as f:
        lines = f.readlines()
        p = collect_entries(lines)
        summed = [sum(elf) for elf in p]
        return sum(sorted(summed, reverse=True)[:n])


calories = get_max_calories("input.txt", 3)
print(calories)
