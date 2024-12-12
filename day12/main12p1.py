grid = [s.strip() for s in open("input.txt").read().splitlines()]
ROWS = len(grid)
COLS = len(grid[0])
print(grid, ROWS, COLS)


def dfs(p):
    if p in visited:
        return frozenset()
    visited.add(p)

    x, y = p
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
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


def count_borders(p):
    x, y = p
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    num = 0
    for d in DIRECTIONS:
        x1, y1 = x + d[0], y + d[1]
        if 0 <= x1 < ROWS and 0 <= y1 < COLS and grid[x1][y1] != grid[x][y]:
            num += 1
        if not 0 <= x1 < ROWS or not 0 <= y1 < COLS:
            num += 1
    return num


total = 0
for region in regions:
    area = len(region)
    perimeter = 0
    for p in region:
        perimeter += count_borders(p)
    total += area * perimeter

print(total) # 140
