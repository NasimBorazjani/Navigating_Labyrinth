
import heapq

def heuristic(state):
    goal = [[97, 55, 43], [35, 25, 17], [12, 9, '_']]
    return sum(s != g for row_s, row_g in zip(state, goal) for s, g in zip(row_s, row_g))

def get_neighbors(state):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i, row in enumerate(state):
        for j, tile in enumerate(row):
            if tile == '_':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < 3 and 0 <= nj < 3:
                        neighbor = [row.copy() for row in state]
                        neighbor[i][j], neighbor[ni][nj] = neighbor[ni][nj], neighbor[i][j]
                        yield neighbor
                return

def solve(initial):
    queue = [(heuristic(initial), 0, initial, [])]
    visited = set(str(initial))
    while queue:
        _, cost, state, path = heapq.heappop(queue)
        if heuristic(state) == 0:
            return path
        for neighbor in get_neighbors(state):
            if str(neighbor) not in visited:
                visited.add(str(neighbor))
                for i, row in enumerate(neighbor):
                    for j, tile in enumerate(row):
                        if tile == '_':
                            if len(path) == 0 or path[-1] != state[i][j]:
                                heapq.heappush(queue, (cost + 1 + heuristic(neighbor), cost + 1, neighbor, path + [state[i][j]]))

initial = [[12, 55, '_'], [35, 97, 43], [17, 25, 9]]
print(solve(initial))
