from functools import reduce
from collections import defaultdict
import math

stones = [int(s) for s in open("input.txt").read().split(" ")]

print(stones)

def blink(s):
    if s == 0:
        return [1]
    magnitude = math.ceil(math.log10(s + 1))
    if magnitude % 2 == 0:
        firstpart = int(s // (10**(magnitude/2)))
        secondpart = int(s % (10**(magnitude/2)))
        return [firstpart, secondpart]
    return [s*2024]

curr = [(s,1) for s in stones] #[0 ,1 ,10 ,99 ,999]
#curr = [(125,1), (17, 1)]
for i in range(75):
    nex = []
    for s, count in curr:
        for x in blink(s):
            nex.append((x, count))

    el_sum = defaultdict(int)
    for el, count in nex:
        el_sum[el] += count

    nex = []
    for el in el_sum:
        nex.append((el, el_sum[el]))

    curr = nex
    print(f"loop {i} done: {curr}")

print(curr)
print(len(curr)) #55312
print(sum([count for _, count in curr]))
