import re

in_file = open("input.txt").read().splitlines()

ROWS, COLS = 101, 103
#ROWS, COLS = 11, 7

quadrants = [0,0,0,0]
for line in in_file:
    x, y, vx, vy = list(map(int, re.findall(r"-?\d+", line)))
    print(f"Robot {x, y, vx, vy}", end="")
    new_x = (x + 100 * vx) % COLS
    new_y = (y + 100 * vy) % ROWS
    print(f" moves in {new_x, new_y}", end="")

    if 0 <= new_x < COLS // 2 and 0 <= new_y < ROWS // 2:
        print(f" in quadrant 1: {0} < {new_x} <= {COLS // 2} and {0} <= {new_y} < {ROWS // 2}")
        quadrants[0] += 1
    if 0 <= new_x < COLS // 2 and ROWS // 2 + 1 <= new_y < ROWS:
        print(f" in quadrant 2: {0} < {new_x} <= {COLS // 2} and {ROWS // 2 + 1} <= {new_y} < {ROWS}")
        quadrants[1] += 1
    if COLS // 2 + 1 <= new_x < COLS and 0 <= new_y < ROWS // 2:
        print(f" in quadrant 3: {COLS // 2 + 1} < {new_x} <= {COLS} and {0} <= {new_y} < {ROWS // 2}")
        quadrants[2] += 1
    if COLS // 2 + 1 <= new_x < COLS and ROWS // 2 + 1 <= new_y < ROWS:
        print(f" in quadrant 3: {COLS // 2 + 1} < {new_x} <= {COLS} and {ROWS // 2 + 1} <= {new_y} < {ROWS}")
        quadrants[3] += 1

    if new_x == COLS // 2:
        print(f" in the center row")
    if new_y == ROWS // 2:
        print(f" in the center column")

saf_factor = 1
for idx, quadrant in enumerate(quadrants):
    print(f"Quad {idx} contains {quadrant} robots")
    saf_factor *= quadrant
print(saf_factor) #225552000