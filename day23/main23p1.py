from itertools import *

lines = open("input.txt").read().splitlines()

connections = {}
for a, b in [l.split("-") for l in lines]:
    connections.setdefault(a, []).append(b)
    connections.setdefault(b, []).append(a)
print(connections)

three_computers = set()
for a, vals in connections.items():
    for idx, b in enumerate(vals):
        for c in vals[idx + 1:]:
            print(f"checking {a, b, c}", end=" ")
            if b in connections[c]:
                print("found")
                three_computers.add(tuple(sorted((a, b, c))))
            else: print("not found")

print(three_computers)

# total = 0
# for computers in three_computers:
#     print(computers, end=" ")
#     if any([c.startswith("t") for c in computers]):
#         print("found")
#         total += 1
#     else: print("not found")
# print(total)


total = sum([any(c.startswith("t") for c in computers) for computers in three_computers])
print(total)