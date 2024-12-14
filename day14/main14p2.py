import re
from functools import reduce
from operator import mul

in_file = open("input.txt").read().splitlines()

ROWS, COLS = 103, 101
#ROWS, COLS = 11, 7
HALF_COLS = COLS // 2
HALF_ROWS = ROWS // 2

starting_positions = []
speeds = []
for line in in_file:
    x, y, vx, vy = list(map(int, re.findall(r"-?\d+", line)))
    starting_positions.append((x, y))
    speeds.append((vx, vy))

curr_positions = starting_positions


def print_robots(positions):
    for x in range(COLS):
        consecutives = 0
        for y in range(ROWS):
            if (x, y) in positions:
                consecutives += 1
                print("#", end="")
            else:
                consecutives = 0
                print(".", end="")
        print()

def evaluate_consecutives(positions):
    for x in range(COLS):
        consecutives = 0
        for y in range(ROWS):
            if (x, y) in positions:
                consecutives += 1
            else:
                consecutives = 0
        if consecutives > 5:
            return True
    return False


min_saf = float("+inf")
# low safety factor with the same number of robots
# => the product of the quads is low
# => many robots in the same quad, probably making the easter egg
move_with_min_saf = 0
positions_for_move_with_min_saf = []
for move in range(1, ROWS*COLS):
    new_positions = []
    print(f"Move: {move}")
    for rid, _ in enumerate(curr_positions):
        x, y = curr_positions[rid]
        vx, vy = speeds[rid]
        #print(f"Robot {x, y, vx, vy}", end="")
        new_x = (x + vx) % COLS
        new_y = (y + vy) % ROWS
        new_positions.append((new_x, new_y))
        #print(f" moves in {new_x, new_y}", end="")

    quadrants = [0, 0, 0, 0]
    for p in new_positions:
        x, y = p
        if x == HALF_COLS or y == HALF_ROWS: continue

        if 0 <= x < HALF_COLS and 0 <= y < HALF_ROWS:
            quadrants[0] += 1
        if 0 <= x < HALF_COLS and HALF_ROWS + 1 <= y < ROWS:
            quadrants[1] += 1
        if HALF_COLS + 1 <= x < COLS and 0 <= y < HALF_ROWS:
            quadrants[2] += 1
        if HALF_COLS + 1 <= x < COLS and HALF_ROWS + 1 <= y < ROWS:
            quadrants[3] += 1

    saf_factor = reduce(mul, quadrants, 1)
    if saf_factor < min_saf:
        min_saf = saf_factor
        move_with_min_saf = move
        positions_for_move_with_min_saf = new_positions

    curr_positions = new_positions

print(f"MINIMUMS move {move_with_min_saf} and safety factory {min_saf}")  # 7371
print_robots(positions_for_move_with_min_saf)
