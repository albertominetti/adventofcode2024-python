from collections import defaultdict

grid = [list(l) for l in open("input.txt").read().splitlines()]

ROWS = len(grid)
COLS = len(grid[0])

for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == 'S':
            break
    else:
        continue
    break

distances = defaultdict(lambda: -1)
distances[(r, c)] = 0
dist = 0
while grid[r][c] != 'E':
    for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
        if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS: continue
        if distances[(nr, nc)] != -1: continue
        if grid[nr][nc] in ['.', 'E']:
            dist += 1
            distances[(nr, nc)] = dist
            r = nr
            c = nc

for r in range(ROWS):
    for c in range(COLS):
        print(distances[(r, c)], end='\t')
    print()

count_save_100 = 0
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == '#': continue
        for distance in range(2, 20 + 1):
            for r_dist in range(distance + 1):
                c_dist = distance - r_dist
                for nr, nc in {(r + r_dist, c + c_dist), (r + r_dist, c - c_dist), (r - r_dist, c + c_dist), (r - r_dist, c - c_dist)}:

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS: continue
                    if grid[nr][nc] in ['.', 'E']:
                        save = distances[(nr, nc)] - distances[(r, c)] - distance
                        if save >= 100:
                            count_save_100 += 1

print(count_save_100)
