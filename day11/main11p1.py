from functools import reduce

stones = [int(s) for s in open("input.txt").read().split(" ")]

print(stones)

def blink(s):
    if s == 0:
        return [1]
    if len(str(s)) % 2 == 0:
        s_string =str(s)
        firstpart, secondpart = s_string[:len(s_string) // 2], s_string[len(s_string) // 2:]
        return [int(firstpart), int(secondpart) if secondpart else 0]
    return [s*2024]


cache = {}
i=0
curr = stones #[0 ,1 ,10 ,99 ,999]
for i in range(25):
    nex = []
    for s in curr:
        if s not in cache:
            cache[s] = blink(s)
        l = cache[s]
        nex += l
    curr = nex
    print(f"loop {i} done")

print(curr)
print(len(curr)) #55312
