grid = [list(map(int, l)) for l in open("input.txt").read().splitlines()]
print(grid)
print(type(grid))
print(type(grid[0]))
print(type(grid[0][0]))

ROWS = len(grid)
COLS = len(grid[0])

starts = [(x, y) for x in range(ROWS) for y in range(COLS) if grid[x][y] == 0]
print(starts)


def find_trails_to_end(p, path):
    x, y = p
    if grid[x][y] == 9:
        return [path]

    paths = []
    for d in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        next_x = x + d[0]
        next_y = y + d[1]
        if not (0 <= next_x < ROWS and 0 <= next_y < COLS):
            continue
        if grid[x][y] + 1 == grid[next_x][next_y]:
            next_p = (next_x, next_y)
            paths += find_trails_to_end(next_p, path + [next_p])
    return paths


trails = []
for (x, y) in starts:
    trails += find_trails_to_end((x, y), [(x, y)])

print(trails)

dict = {}
for t in trails:
    if t[0] not in dict:
        dict[t[0]] = []
    dict[t[0]].append(t[1:])
print(dict)

dict_count = {k: len(v) for k, v in dict.items()}
print(dict_count)

dict_start_end = set()
for s, trails in dict.items():
    for t in trails:
        e = t[-1]
        print(f"Start {s} end {e}")
        dict_start_end.add( (s, e) )
print(dict_start_end)
print(len(dict_start_end))  # test 36