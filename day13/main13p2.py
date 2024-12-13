import re

input = open("input.txt").read()

total = 0
for block in input.split("\n\n"):
    ax, ay, bx, by, tx, ty = map(int, re.findall(r"(\d+)", block))
    if (by * ax - bx * ay) == 0:
        print("error: division by Zero")
    tx += 10000000000000
    ty += 10000000000000
    ac = (tx * by - ty * bx) / (by * ax - bx * ay)
    bc = (ty * ax - tx * ay) / (ax * by - bx * ay)
    if int(ac) == ac and int(bc) == bc:
        print(f"For {ax, ay, bx, by, tx, ty} a solution is with Bx{bc} and Ax{ac}")
        total += bc * 1 + ac * 3

print(total)
