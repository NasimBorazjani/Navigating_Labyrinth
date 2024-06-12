
import heapq

def astar(start, goal):
    queue = [(heuristic(start, goal), start)]
    seen = {str(start): 0}
    path = {str(start): []}
    while queue:
        (cost, current) = heapq.heappop(queue)
        if current == goal:
            return path[str(current)]
        for next in successors(current):
            next_cost = seen[str(current)] + 1
            if str(next) not in seen or next_cost < seen[str(next)]:
                seen[str(next)] = next_cost
                heapq.heappush(queue, (next_cost + heuristic(next, goal), next))
                path[str(next)] = path[str(current)] + [tile_to_move(current, next)]
    return []

def heuristic(state, goal):
    return sum(tile != goal[i][j] for i, row in enumerate(state) for j, tile in enumerate(row))

def successors(state):
    i, j = next((i, j) for i, row in enumerate(state) for j, tile in enumerate(row) if tile == '_')
    directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    return [swap(state, (i, j), d) for d in directions if valid(state, d)]

def valid(state, (i, j)):
    return 0 <= i < len(state) and 0 <= j < len(state[0])

def swap(state, (i, j), (x, y)):
    new_state = [list(row) for row in state]
    new_state[i][j], new_state[x][y] = new_state[x][y], new_state[i][j]
    return new_state

def tile_to_move(state, next):
    return next(i for i, row in enumerate(state) for j, tile in enumerate(row) if tile != next[i][j])

start = [[77, 49, '_'], [56, 72, 74], [96, 33, 59]]
goal = [[96, 77, 74], [72, 56, 49], [33, 59, '_']]
print(astar(start, goal))
