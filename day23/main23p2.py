import time

lines = open("input.txt").read().splitlines()

connections = {}
for a, b in [l.split("-") for l in lines]:
    connections.setdefault(a, []).append(b)
    connections.setdefault(b, []).append(a)
print(connections)

con_len = { k: len(val) for k, val in connections.items()}

computers_groups = set([tuple(sorted(l.split("-"))) for l in lines])

while computers_groups:
    start_time = time.time()
    e = next(iter(computers_groups))
    print(f"There are {len(computers_groups)} of size {len(e)}")
    computers_groups_with_one_more = set()
    for group in computers_groups:
        for other in connections.keys():
            if other in group: continue
            if all([g in connections[other] for g in group]):
                computers_groups_with_one_more.add(tuple(sorted(group + (other,))))
    print("--- %s seconds ---" % (time.time() - start_time))
    if len(computers_groups_with_one_more) == 0:
        break
    computers_groups = computers_groups_with_one_more

print(computers_groups)
print(",".join(next(iter(computers_groups)))) # av,fr,gj,hk,ii,je,jo,lq,ny,qd,uq,wq,xc
#print(",".join(group))