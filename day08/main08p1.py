lines = open("input.txt").read().splitlines()

print(lines)

print("---")

# find antennas
dict_freq = {}
for x in range(len(lines)):
    for y in range(len(lines[x])):
        print(lines[x][y], end="")
        if lines[x][y] != ".":
            f = lines[x][y]
            if f not in dict_freq:
                dict_freq[f] = list()
            dict_freq[f].append((x, y))
    print()

print(dict_freq)

antinodes = set()
for f in dict_freq:
    for idx, a in enumerate(dict_freq[f]):
        for b in dict_freq[f][idx + 1:]:
            diff1 = b[0] - a[0]
            diff2 = b[1] - a[1]
            print(f"a {a} b {b} diffs: ({diff1}, {diff2})")
            p1x = a[0] + diff1
            print(p1x)
            p1 = (a[0] + 2*diff1, a[1] + 2*diff2)
            p2 = (b[0] - 2*diff1, b[1] - 2*diff2)
            print(f"p1 {p1} p2 {p2}")
            antinodes.add(p1)
            antinodes.add(p2)

print(antinodes)

def in_map(point):
    return 0 <= point[0] < len(lines) and 0 <= point[1] < len(lines[0])

total = sum(1 for x in antinodes if in_map(x) and x not in [p for p in dict_freq.values()])
antinodes2 = []
for x in antinodes:
    if not in_map(x):
        print(f"Point {x} is outside")
        continue
    if x in [p for p in dict_freq.values()]:
        print(f"Point {x} overlaps with an antenna")
        continue
    print(f"Point {x} is an antinode")
    antinodes2.append(x)

print(total)


for x in range(len(lines)):
    for y in range(len(lines[x])):
        if (x, y) in antinodes2:
            print("#", end="")
        else:
            print(lines[x][y], end="")
    print()