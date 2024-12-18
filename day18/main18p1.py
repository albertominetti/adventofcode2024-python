from collections import deque

SIZE = 71 #6
TIME = 1024

grid = [['.'] * SIZE for _ in range(SIZE)]
drops = [list(map(int, line.split(","))) for line in open("input.txt")]

for c, r in drops[:TIME]:
    grid[r][c] = '#'

q = deque([(0, 0, 0)])
seen = {(0, 0)}

while q:
    r, c, d = q.popleft()
    for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
        if nr < 0 or nc < 0 or nr >= SIZE or nc >= SIZE: continue
        if grid[nr][nc] == '#': continue
        if (nr, nc) in seen: continue
        if nr == nc == (SIZE - 1):
            print(d + 1)
            exit(0)
        seen.add((nr, nc))
        q.append((nr, nc, d + 1))
