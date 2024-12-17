import re

a, b, c, *instructions = map(int, re.findall(r"\d+", open("input.txt").read()))

pointer = 0
output = []

def combo(operand: int):
    assert 0 <= operand <= 6
    if operand == 4: return a
    if operand == 5: return b
    if operand == 6: return c
    return operand

while pointer < len(instructions):
    curr = instructions[pointer]
    operand = instructions[pointer + 1]
    if curr == 0: # adv
        a = a >> combo(operand)
    elif curr == 1: # bxl
        b = b ^ operand
    elif curr == 2: # bst
        b = combo(operand) % 8
    elif curr == 3: # jnz
        if a != 0:
            pointer = operand
            continue # skip pointer += 2
    elif curr == 4: # bxc
        b = b ^ c
    elif curr == 5: # out
        output.append(combo(operand) % 8)
    elif curr == 6: # bdv
        b = a >> combo(operand)
    elif curr == 7: # cdv
        c = a >> combo(operand)
    pointer += 2

print(*output, sep=",") # 2,1,0,4,6,2,4,2,0