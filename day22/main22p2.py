from collections import Counter

PRUNE_MOD = 16777216
seeds = list(map(int, open("input.txt").read().splitlines()))

all_prices = []
all_deltas = []
for seed in seeds:
    prices = [seed % 10]
    deltas = []
    for i in range(2000):
        seed = ((seed * 64) ^ seed) % PRUNE_MOD  # x64, mix, prune
        seed = ((seed // 32) ^ seed) % PRUNE_MOD  # //32, mix, prune
        seed = ((seed * 2048) ^ seed) % PRUNE_MOD  # x248, mix, prune
        prices += [seed % 10]
    deltas = [b - a for a, b in list(zip(prices, prices[1:]))]
    all_prices += [prices]
    all_deltas += [deltas]

# trovare tutti i possibili grouppi di delta da 4: (-9 a 9) 19^4
# rimuovere i duplicati

all_sequences = Counter()
for deltas in all_deltas:
    delta_seqs = [ deltas[i:i+4] for i in range(len(deltas) - 3)]
    assert not [len(delta_seqs) for delta_seqs in delta_seqs if len(delta_seqs) != 4]
    all_sequences.update( set(map(tuple, delta_seqs)))
len(set(map(tuple, all_sequences.keys())))

all_sequences.most_common(10)

# brute foooorceee!
max_total_bananas = 0
for seq, counts in all_sequences.most_common(50):
    total_bananas = 0
    for i in range(len(all_prices)):
        # print("\t".join(list(map(str, all_prices[0]))))
        # print("\t".join(list(map(str, all_deltas[0]))))

        prices_and_deltas = list(zip(all_prices[i], [None] + all_deltas[i]))
        #print(prices_and_deltas)

        for idx in range(len(prices_and_deltas) - 3):

            cur_seq= prices_and_deltas[idx:idx + len(seq)]
            if seq == tuple([x[1] for x in cur_seq]):
                bananas = cur_seq[len(seq) - 1][0]
                #print(f"found {cur_seq}! Price is {bananas}")
                total_bananas += bananas
                break
    print(f"With seq {seq} we got {total_bananas} bananas.")
    max_total_bananas = max(max_total_bananas, total_bananas)

