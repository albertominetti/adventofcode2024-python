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

def in_map(point):
    return 0 <= point[0] < len(lines) and 0 <= point[1] < len(lines[0])

antinodes = set()
for f in dict_freq:
    for idx, a in enumerate(dict_freq[f]):
        for b in dict_freq[f][idx + 1:]:
            diff1 = b[0] - a[0]
            diff2 = b[1] - a[1]

            p=b
            while True:
                p = (p[0] + diff1, p[1] + diff2)
                if not in_map(p):
                    break
                antinodes.add(p)

            p=a
            while True:
                p = (p[0] - diff1, p[1] - diff2)
                if not in_map(p):
                    break
                antinodes.add(p)

print(antinodes)
print(f"Antinodes are {len(antinodes)}")
print(f"Antinodes are {sum( len(v) for v in dict_freq.values())}")

node_and_antinodes= set()
for f in dict_freq.values():
    for f1 in f:
        node_and_antinodes.add(f1)
for f1 in antinodes:
    node_and_antinodes.add(f1)
print(len(node_and_antinodes))


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


for x in range(len(lines)):
    for y in range(len(lines[x])):
        if (x, y) in antinodes2:
            print("#", end="")
        else:
            print(lines[x][y], end="")
    print()