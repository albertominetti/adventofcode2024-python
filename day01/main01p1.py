lists = list(map(list, zip(*[list(map(int, l.split())) for l in open("input.txt").read().splitlines()])))
lists[0].sort()
lists[1].sort()

print(sum(abs(a - b) for a, b in zip(*lists)))
