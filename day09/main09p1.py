chars = open("input.txt").read().rstrip()

print(chars)

blocks = []
is_file = True
id = 0
space = -1
for c in chars:
    size = int(c)
    if is_file:
        blocks.append( (id, size) )
        id += 1
    else:
        blocks.append( (space, size) )
        space -= 1
    is_file = not is_file

print(blocks)
print(len(blocks))

left = 1
right = len(blocks) - 1

while left < right:
    if blocks[left][0] >= 0:
        print(f"Error: left should be always a space, position {left}")
        exit(1)
    if blocks[right][0] < 0:
        print(f"Error: right should be always a file, position {right}")
        exit(1)
    filePart = min(blocks[right][1], blocks[left][1])
    blocks[left] = (blocks[left][0], blocks[left][1] - filePart)
    blocks[right] = (blocks[right][0], blocks[right][1] - filePart)
    if filePart > 0:
        blocks.insert(left, (blocks[right][0], filePart))
        left += 1
        right += 1
    if blocks[left][1] == 0:
        left += 2
        continue
    if blocks[right][1] == 0:
        right -= 2
        continue

print(f"left {left}, right {right}")
print(blocks)
print(blocks[left-10:right+10])
print(len(blocks))

expansion = [] #it can be huge
for b in blocks:
    if b[0] >= 0:
        for _ in range(b[1]):
            expansion.append(b[0])
print(expansion)

total = 0
for id, e in enumerate(expansion):
    if int(e) < 0:
        break
    total += int(e) * id
print(total) # 6283170117911