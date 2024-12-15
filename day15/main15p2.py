import re
from collections import deque

map, moves = open("input.txt").read().split("\n\n")
map = map.replace("#", "##")
map = map.replace("O", "[]")
map = map.replace(".", "..")
map = map.replace("@", "@.")
map = [list(l) for l in map.splitlines()]
moves = re.sub(r'\n+', '', moves)

initial_map = map


def print_map(m):
    for line in m:
        for e in line:
            print(e, end='')
        print()


print_map(initial_map)

start = (0, 0)
for r, _ in enumerate(map):
    for c, e in enumerate(map[r]):
        if e == '@':
            start = (r, c)
            break

print(f"start: {start} and value is {map[start[0]][start[1]]}")

DIRECTIONS = {'v': (1, 0), '<': (0, -1), '>': (0, 1), '^': (-1, 0)}

map = initial_map
print_map(map)
robot = start
for move_id, m in enumerate(moves):
    print(f"Move {move_id + 1} in {m}", end=" ")
    r, c = robot
    direction = DIRECTIONS[m]
    next_r, next_c = r + direction[0], c + direction[1]

    if map[next_r][next_c] == '#':
        print(f"can't go {m} because of a wall")
        continue

    if map[next_r][next_c] in ['[', ']']:
        stone_r, stone_c = next_r, next_c
        if map[stone_r][stone_c] == ']':
            stone_c -= 1  # always refer to a stone by the west side
        stones = [(stone_r, stone_c)]

        stones_to_visit = deque(stones)
        while stones_to_visit:
            stone_r, stone_c = stones_to_visit.popleft()
            print(f"Stone in {stone_r, stone_c}")

            if m in ['<', '>']:  # push to west or east
                assert direction[0] == 0

                if m == '<' and map[stone_r][stone_c - 1] == '#':
                    print(f"There is a wall at left, can't move anything")
                    stones = []
                    break
                elif m == '>' and map[stone_r][stone_c + 2] == '#':
                    print(f"There is a wall at right, can't move anything")
                    stones = []
                    break

                stone_r, stone_c = stone_r + direction[0], stone_c + 2 * direction[1]
                if map[stone_r][stone_c] == '[':
                    assert map[stone_r][stone_c + 1] == ']'
                    stones.append((stone_r, stone_c))
                    stones_to_visit.append((stone_r, stone_c))

            else:
                assert direction[1] == 0
                stone_r, stone_c = stone_r + direction[0], stone_c

                print(f"Checking if {stone_r, stone_c} is a stone or wall or space")
                if map[stone_r][stone_c] == '#' or map[stone_r][stone_c + 1] == '#':
                    print(f"There is a wall, can't move anything")
                    stones = []
                    break

                if map[stone_r][stone_c] == '[':
                    assert map[stone_r][stone_c + 1] == ']'
                    stones.append((stone_r, stone_c))
                    stones_to_visit.append((stone_r, stone_c))
                elif map[stone_r][stone_c] == ']':
                    assert map[stone_r][stone_c - 1] == '['
                    stones.append((stone_r, stone_c - 1))
                    stones_to_visit.append((stone_r, stone_c - 1))
                if map[stone_r][stone_c + 1] == '[':
                    assert map[stone_r][stone_c + 2] == ']'
                    stones.append((stone_r, stone_c + 1))
                    stones_to_visit.append((stone_r, stone_c + 1))
        print(f"robot found {len(stones)} movable stones: {stones}", end=" ")
        if stones:
            for s in reversed(stones):
                print(f"moving stone: {s} in {s[0] + direction[0], s[1] + direction[1]}")
                if m in ['<', '>']:
                    map[s[0]][s[1] + direction[1]] = '['
                    map[s[0]][s[1] + direction[1] + 1] = ']'
                    if m == '<':
                        map[s[0]][s[1] + 1] = '.'
                    else:
                        map[s[0]][s[1]] = '.'
                else:
                    map[s[0] + direction[0]][s[1]] = '['
                    map[s[0] + direction[0]][s[1] + 1] = ']'
                    map[s[0]][s[1]] = '.'
                    map[s[0]][s[1] + 1] = '.'
            print(f", and he moved all of them by 1 space", end=" ")

    if map[next_r][next_c] == '.':
        map[robot[0]][robot[1]] = '.'
        robot = (next_r, next_c)
        print(f"Robot moves to {robot} because there was space", end="")
        map[next_r][next_c] = '@'
    print()
    print_map(map)
    print()

print_map(map)

total = 0
for r, line in enumerate(map):
    for c, e in enumerate(line):
        if map[r][c] == '[':
            print(f"")
            total += r * 100 + c
print(total)  # larger example 9021
