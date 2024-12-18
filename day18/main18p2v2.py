
SIZE = 70 + 1 # 6 +1

grid = [['.'] * SIZE for _ in range(SIZE)]
drops = [list(map(int, line.split(","))) for line in open("input.txt")]

drop_count = 0
for drop_r, drop_col in drops:
    print(f"Drop {drop_count}° falling at {drop_r, drop_col}")
    grid[drop_r][drop_col] = '#'
    drop_count += 1


def print_grid(grid):
    for r in range(SIZE):
        for c in range(SIZE):
            print(grid[r][c], end='')
        print()

print_grid(grid)

class UnionFind:
    def __init__(self, grid_size: int):
        self.parents = {(r, c): (r, c) for r in range(grid_size) for c in range(grid_size)}
        self.sizes = {(r, c): 1 for r in range(grid_size) for c in range(grid_size)}

    def find(self, a):
        if self.parents[a] != a:
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def unite(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root == b_root: return;

        if self.sizes[a_root] < self.sizes[b_root]:
            self.parents[a_root] = b_root
            self.sizes[a_root] += self.sizes[b_root]
        else:
            self.parents[b_root] = a_root
            self.sizes[b_root] += self.sizes[a_root]

    def connected(self, a, b):
        return self.find(a) == self.find(b)



uf = UnionFind(SIZE)
for r in range(SIZE):
    for c in range(SIZE):
        if grid[r][c] == '#': continue
        for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
            if nr < 0 or nc < 0 or nr >= SIZE or nc >= SIZE: continue
            if grid[nr][nc] == '#': continue
            uf.unite((r, c), (nr, nc))

assert not uf.connected((0, 0), (SIZE - 1, SIZE - 1))

drop_count = len(drops)
for drop_r, drop_c in reversed(drops):
    print(f"Removing {drop_count}° from {drop_r, drop_c}")
    grid[drop_r][drop_c] = '.'

    for nr, nc in [(drop_r + 1, drop_c), (drop_r, drop_c + 1), (drop_r - 1, drop_c), (drop_r, drop_c - 1)]:
        if nr < 0 or nc < 0 or nr >= SIZE or nc >= SIZE: continue
        if grid[nr][nc] == '#': continue
        uf.unite((drop_r, drop_c), (nr, nc))

    start_end_connected = uf.connected((0, 0), (SIZE - 1, SIZE - 1))
    print(f"Are START and END connected? {start_end_connected}")
    drop_count -= 1
    if start_end_connected:
        break

print(f"Start and end are no more connected after the {drop_count}° drop falls at {drops[drop_count]}") #6,1 #28,44
