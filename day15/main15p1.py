import re

map, moves = open("input.txt").read().split("\n\n")
map = [list(l) for l in map.splitlines()]
moves = re.sub(r'\n+', '', moves)

initial_map = map

start = (0, 0)
for r, _ in enumerate(map):
    for c, e in enumerate(map[r]):
        if e == '@':
            start = (r, c)
            break

print(f"start: {start} and value is {map[start[0]][start[1]]}")


def print_map(m):
    for line in m:
        for e in line:
            print(e, end='')
        print()


DIRECTIONS = {'v': (1, 0), '<': (0, -1), '>': (0, 1), '^': (-1, 0)}

map = initial_map
print_map(map)
robot = start
for move_id, m in enumerate(moves):
    print(f"Move {move_id+1} in {m}", end=" ")
    r, c = robot
    direction = DIRECTIONS[m]
    next_r, next_c = r + direction[0], c + direction[1]

    if map[next_r][next_c] == '#':
        print(f"can't go {m} because of a wall")
        continue

    if map[next_r][next_c] == 'O':
        stone_r, stone_c = next_r, next_c
        stones = []
        while map[stone_r][stone_c] == 'O':
            print(f"Stone! {stone_r}, {stone_c}")
            stones.append((stone_r, stone_c))
            stone_r, stone_c = stone_r + direction[0], stone_c + direction[1]

        print(f"robot found {len(stones)} stones to move, next at {stone_r, stone_c} is {map[stone_r][stone_c]}", end=" ")
        if map[stone_r][stone_c] == '#':
            print(f", but he cannot move because there is a wall behind", end=" ")
        elif map[stone_r][stone_c] == '.':
            for s in reversed(stones):
                map[s[0] + direction[0]][s[1] + direction[1]] = 'O'
                map[s[0]][s[1]] = '.'
            print(f", and he moved all of them by 1 space", end=" ")

    if map[next_r][next_c] == '.':
        map[robot[0]][robot[1]] = '.'
        robot = (next_r, next_c)
        print(f"Robot moves to {robot} because there was space", end="")
        map[next_r][next_c] = '@'
    print()
    #print_map(map)
    print()

print_map(map)

total = 0
for r, line in enumerate(map):
    for c, e in enumerate(line):
        if map[r][c] == 'O':
            print(f"")
            total += r * 100 + c
print(total) # larger example 10092; simpler example 1028
