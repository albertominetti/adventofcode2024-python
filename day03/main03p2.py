import re

line = open("input.txt").read()
print(line)

res = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", line)

enable = True


total = 0
for exp in res:
    if exp.group(0) == "do()":
        enable = True

    if exp.group(0) == "don't()":
        enable = False

    if exp.group(0).startswith("mul(") and enable:
        total += int(exp.group(1)) * int(exp.group(2))

print(total)