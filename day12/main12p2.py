grid = [s.strip() for s in open("input.txt").read().splitlines()]
ROWS = len(grid)
COLS = len(grid[0])
DIRECTIONS = [(0, 1, 'E'), (0, -1, 'W'), (1, 0, 'N'), (-1, 0, 'S')]
print(grid, ROWS, COLS)


def dfs(p):
    if p in visited:
        return []
    visited.add(p)

    x, y = p
    r = [p]
    for d in DIRECTIONS:
        x1, y1 = x + d[0], y + d[1]
        if 0 <= x1 < ROWS and 0 <= y1 < COLS and grid[x1][y1] == grid[x][y]:
            # print(x1, y1)
            r += dfs((x1, y1))
    return r


regions = []
visited = set()
for x in range(ROWS):
    for y in range(COLS):
        if (x, y) not in visited:
            region = dfs((x, y))
            print(region, f" for {grid[x][y]}")
            if len(region):
                regions.append(region)


def retrieve_edges(region):
    edges = []
    for x, y in region:
        for d in DIRECTIONS:
            x1, y1 = x + d[0], y + d[1]
            if (x1, y1) not in region:
                edges += [(x1, y1, d[2])]
    return edges


total_fences = 0
for r in regions:
    (x, y) = r[0]
    print(f"Region {grid[x][y]}")
    edges = retrieve_edges(r)
    print(edges)
    side_count = 0
    visited = set()
    for e in edges:
        if e in visited: continue
        visited.add(e)
        print(f"Edge {e}")
        side_count += 1
        x, y, d = e
        if d in {'N', 'S'}:
            for y_step in [1, -1]:
                next_edge = (x, y + y_step, d)
                while next_edge in edges:
                    print(f"Checking {next_edge}")
                    visited.add(next_edge)
                    next_edge = (x, next_edge[1] + y_step, d)
        if d in {'E', 'W'}:
            for x_step in [1, -1]:
                next_edge = (x + x_step, y, d)
                while next_edge in edges:
                    print(f"Checking {next_edge}")
                    visited.add(next_edge)
                    next_edge = (next_edge[0] + x_step, y, d)

    print(f"sides: {side_count} area: {len(r)}")
    total_fences += side_count * len(r)
print(total_fences)
