a, b = list(map(list, zip(*[list(map(int, l.split())) for l in open("input.txt").read().splitlines()])))

aCount = {x:a.count(x) for x in a}
bCount = {x:b.count(x) for x in b}

print(aCount, bCount)

sum([k * aCount[k] * bCount.get(k, 0) for k in aCount])