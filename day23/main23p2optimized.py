import time

lines = open("input.txt").read().splitlines()

connections = {}
for a, b in [l.split("-") for l in lines]:
    connections.setdefault(a, []).append(b)
    connections.setdefault(b, []).append(a)
print(connections)

computers_groups = set()
def search(comp, group):
    new_group = tuple(sorted({*group, comp}))
    if new_group in computers_groups: return

    if all([g in connections[comp] for g in group]):
        computers_groups.add(new_group)
        for g in connections[comp]:
            if g in group: continue
            search(g, new_group)

for c in connections.keys():
    search(c, set())

print(",".join(max(computers_groups, key=lambda x: len(x))))