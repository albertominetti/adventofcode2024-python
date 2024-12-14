import re

in_file = open("input.txt").read().splitlines()

ROWS, COLS = 103, 101
#ROWS, COLS = 11, 7

quadrants = [0,0,0,0]
for line in in_file:
    x, y, vx, vy = list(map(int, re.findall(r"-?\d+", line)))
    print(f"Robot {x, y, vx, vy}", end="")
    new_x = (x + 100 * vx) % COLS
    new_y = (y + 100 * vy) % ROWS
    print(f" moves in {new_x, new_y}", end="")

    HALF_COLS = (COLS-1) // 2
    HALF_ROWS = (ROWS-1) // 2
    if new_x == HALF_COLS:
        print(f" in the center row")
    if new_y == HALF_ROWS:
        print(f" in the center column")

    if 0 <= new_x < HALF_COLS and 0 <= new_y < HALF_ROWS:
        print(f" in quadrant 1: {0} < {new_x} <= {HALF_COLS} and {0} <= {new_y} < {HALF_ROWS}")
        quadrants[0] += 1
    if 0 <= new_x < HALF_COLS and HALF_ROWS + 1 <= new_y < ROWS:
        print(f" in quadrant 2: {0} < {new_x} <= {HALF_COLS} and {HALF_ROWS + 1} <= {new_y} < {ROWS}")
        quadrants[1] += 1
    if HALF_COLS + 1 <= new_x < COLS and 0 <= new_y < HALF_ROWS:
        print(f" in quadrant 3: {HALF_COLS + 1} < {new_x} <= {COLS} and {0} <= {new_y} < {HALF_ROWS}")
        quadrants[2] += 1
    if HALF_COLS + 1 <= new_x < COLS and HALF_ROWS + 1 <= new_y < ROWS:
        print(f" in quadrant 3: {HALF_COLS + 1} < {new_x} <= {COLS} and {HALF_ROWS + 1} <= {new_y} < {ROWS}")
        quadrants[3] += 1

print("Quadrants: ", quadrants)

saf_factor = 1
for idx, quadrant in enumerate(quadrants):
    print(f"Quad {idx} contains {quadrant} robots")
    saf_factor *= quadrant
print(saf_factor) #225552000