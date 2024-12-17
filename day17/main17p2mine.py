import re

init_a, init_b, init_c, *instructions = (
    map(int, re.findall(r"\d+", open("input.txt").read())))

program = ",".join(map(str, instructions))
print(program)

def find_sol_with_backtrack(instr: [], partial_a):
    if len(instr) == 0: return partial_a
    expected = instr[-1]
    print(f"Expected {expected}")
    found = False
    for i in range(8):
        x = partial_a * 8 + i
        value = (4 ^ ((7 ^ (x % 8)) ^ (x // (2 ** (7 ^ (x % 8))))) % 8) # formula for my input
        # possible to use the execution part of part 1 without the loop to run any input
        print(f" with {i}: using {x} calculate {value}")
        found = expected == value
        if found:
            sub_a = find_sol_with_backtrack(instr[:-1], x)
            if sub_a:
                return sub_a
            else:
                found = False

find_sol_with_backtrack(instructions, 0)
