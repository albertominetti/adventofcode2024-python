PRUNE_MOD = 16777216
seeds = list(map(int, open("input.txt").read().splitlines()))

total = 0
for seed in seeds:
    for i in range(2000):
        seed = ((seed * 64) ^ seed) % PRUNE_MOD  # x64, mix, prune
        seed = ((seed // 32) ^ seed) % PRUNE_MOD  # //32, mix, prune
        seed = ((seed * 2048) ^ seed) % PRUNE_MOD  # x248, mix, prune
    total += seed

print(total)
