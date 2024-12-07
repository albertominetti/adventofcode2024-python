lists = [list(map(int, l.split())) for l in open("input.txt").read().splitlines()]

print(lists)

def is_valid(l):
    print(l)
    differences = [a - b for a,b in zip(l,l[1:])]
    return all(0 < d <= 3 for d in differences) or all(-3 <= d < 0 for d in differences)

count = 0
for l in lists:
    valid = any(is_valid(l[:idx]+l[idx+1:]) for idx, _ in enumerate(lists) if idx < len(l))
    if valid:
        count = count + 1
print(count) #692
