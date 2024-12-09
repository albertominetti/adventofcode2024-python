chars = open("input.txt").read().rstrip()

print(chars)

blocks = []
parsing_file = True
id = 0
space = -1
for c in chars:
    size = int(c)
    if parsing_file:
        blocks.append( (id, size) )
        id += 1
    else:
        blocks.append( (space, size) )
        space -= 1
    parsing_file = not parsing_file

print(blocks)
print(len(blocks))





def is_file(i):
    return blocks[i][0] >= 0

def is_space(i):
    return blocks[i][0] < 0

right = len(blocks) - 1
while right > 0:
    print(f"Checking position {right}: {blocks[right]}")
    if is_space(right):
        #print(" It is a space, ignoring ", right)
        right -= 1
        continue
    fileId, fileSize = blocks[right]

    left = 1 #always start from the beginning
    while left < right:
       # print(f"  Checking is there is space in {left}: {blocks[left]}")
        if not is_space(left):
            #print("  It is not a space, ignoring ", left)
            left += 1
            continue
        if not blocks[left][1] >= fileSize: #find next space
            #print("  It is not big enough, ignoring ", left)
            left += 1
            continue
        break

    if left >= right:
        #print("Crossed the right bound, ignoring the move of it.")
        right -= 1
        continue

    spaceId, spaceSize = blocks[left]
    if spaceSize >= fileSize:
        print(f" File {blocks[right]} in positon {right} can be move inside {blocks[left]} at position {left}.")
        del blocks[right] #and remove from the right side
        blocks.insert(right, (spaceId, fileSize)) #insert the free space at the file pos
        blocks[left] = (spaceId, spaceSize - fileSize) #decrease the free space
        blocks.insert(left, (fileId, fileSize)) #insert the full file
    right -= 1


print(blocks)
print(len(blocks))

expansion = [] #it can be huge
for id, b in enumerate(blocks):
    for _ in range(b[1]):
        expansion.append(b[0] if is_file(id) else '.')
print(expansion)

total = 0
for id, e in enumerate(expansion):
    if e == '.':
        continue
    total += int(e) * id
print(total) # 6307653242596