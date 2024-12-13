import re

line = open("input.txt").read()
print(line)

res = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", line)

sum([int(exp.group(1))*int(exp.group(2)) for exp in res])