from collections import defaultdict
import heapq

map = [list(l) for l in open("input.txt").read().splitlines()]
print(map)

DIRECTIONS = {'v': (1, 0), '<': (0, -1), '>': (0, 1), '^': (-1, 0)}

end = start = ()
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "S":
            start = (i, j)
        if map[i][j] == "E":
            end = (i, j)

print(f"start: {start}; end: {end}")

pos_and_dir = (*start, ">")
print(pos_and_dir)

def calc_distances(p_d):
    r, c, d = p_d

    distances = defaultdict(lambda: float("inf"))
    distances[(r, c, d)] = 0
    prev_nodes = dict()

    heap = [(0, (r, c, d))]

    while heap:
        dist, pos = heapq.heappop(heap)
        r, c, d = pos
        for dd in DIRECTIONS:
            additional_score = 0
            if DIRECTIONS[dd][0] == DIRECTIONS[d][0] and DIRECTIONS[dd][1] == DIRECTIONS[d][1]:
                additional_score = 0  # 0°
            elif DIRECTIONS[dd][0] == DIRECTIONS[d][0] or DIRECTIONS[dd][1] == DIRECTIONS[d][1]:
                continue  # additional_score = 2000 # 180°
            else:
                additional_score = 1000  # 90° or -90°

            next_r, next_c = r + DIRECTIONS[dd][0], c + DIRECTIONS[dd][1]
            next_pos = (next_r, next_c, dd)

            if map[next_r][next_c] == '#': continue

            if distances[next_pos] > dist + additional_score + 1:
                distances[next_pos] = dist + additional_score + 1
                prev_nodes[next_pos] = pos
                heapq.heappush(heap, (distances[next_pos], next_pos))

    return distances, prev_nodes


distances, prev_nodes = calc_distances(pos_and_dir)
print(distances)
print(prev_nodes)

min_dist = float("inf")
for d in DIRECTIONS:
    if (end[0], end[1], d) in distances:
        print(f"end: {end} in direction {d} is {distances[(end[0], end[1], d)]}")
        min_dist = min(min_dist, distances[(end[0], end[1], d)])

print(min_dist) # 11048
