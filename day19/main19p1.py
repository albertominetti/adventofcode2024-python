from functools import cache

lines = open("input.txt").read().splitlines()

towels = lines[0].split(", ")
print(towels)

patterns = lines[2:]
print(patterns)

@cache
def count_how(pattern):
    if pattern == "":
        return 1
    count = 0
    for t in towels:
        if pattern.startswith(t):
            count += count_how(pattern[len(t):])
    return count

print(sum([1 for p in patterns if count_how(p) > 0]))