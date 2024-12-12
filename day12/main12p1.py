grid = [s.strip() for s in open("input_test.txt").read().splitlines()]
ROWS = len(grid)
COLS = len(grid[0])
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
print(grid, ROWS, COLS)


def dfs(p):
    if p in visited:
        return frozenset()
    visited.add(p)

    x, y = p
    r = {p}
    for d in DIRECTIONS:
        x1, y1 = x + d[0], y + d[1]
        if 0 <= x1 < ROWS and 0 <= y1 < COLS and grid[x1][y1] == grid[x][y]:
            # print(x1, y1)
            r |= dfs((x1, y1))
    return r


regions = set()
visited = set()
for x in range(ROWS):
    for y in range(COLS):
        if (x, y) not in visited:
            region = dfs((x, y))
            print(region, f" for {grid[x][y]}")
            if len(region):
                regions.add(frozenset(region))


def count_borders(region):
    perimeter = 0
    for x, y in region:
        for d in DIRECTIONS:
            x1, y1 = x + d[0], y + d[1]
            if (x1, y1) not in region:
                perimeter += 1
    return perimeter


total = 0
for region in regions:
    area = len(region)
    perimeter = count_borders(region)
    total += area * perimeter

print(total) # 140
