inputs = [l.splitlines() for l in open("input.txt").read().split("\n\n")]

locks = []
keys = []
for i in inputs:
    if i[0] == '#####': #locks
        lock = [l.count("#") for l in list(zip(*i[1:]))]
        locks.append(lock)
    else: #keys
        key = [l.count("#") for l in list(zip(*i[:-1]))]
        keys.append(key)


total_fits = 0
# loop_count = 0
for l in locks:
    for k in keys:
        # loop_count += 1
        # print(f" [{loop_count}] Checking lock: {l} and key: {k}")
        # fits = True
        # for i in range(len(l)):
        #     # print(f"pos {i}; sum; {l[i] + k[i]}")
        #     if l[i] + k[i] > 5:
        #         print(f"Lock: {l} Key: {k} does not fit")
        #         fits = False
        #         break
        # if not fits: continue
        # print(f"Lock: {l} Key: {k} fits!")
        if all(l[i] + k[i] <= 5 for i in range(len(l))):
            total_fits +=1

print(total_fits)