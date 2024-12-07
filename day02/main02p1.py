lists = [list(map(int, l.split())) for l in open("input.txt").read().splitlines()]

print(lists)

count = 0
for l in lists:
    differences = [a - b for a,b in zip(l,l[1:])]
    valid = all(0 < d <= 3 for d in differences) or all(-3 <= d < 0 for d in differences)
    if valid:
        count = count + 1
print(count) #663
