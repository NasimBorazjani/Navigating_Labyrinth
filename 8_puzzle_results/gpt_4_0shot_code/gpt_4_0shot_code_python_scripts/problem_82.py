
from queue import PriorityQueue

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def get_neighbors(pos):
    x, y = pos
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    result = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx >= 0 and nx < 3 and ny >= 0 and ny < 5:
            result.append((nx, ny))
    return result

def solve_puzzle(start):
    pq = PriorityQueue()
    pq.put((0, start, []))
    seen = set([start])
    while not pq.empty():
        _, current, path = pq.get()
        if is_goal(current):
            return path
        for neighbor in get_neighbors(current):
            if neighbor not in seen:
                seen.add(neighbor)
                pq.put((heuristic(neighbor, goal), neighbor, path + [current[neighbor]]))
    return None

def is_goal(state):
    goal = [[88, 72, 70, 60, 51], [87, 85, 43, 39, 30], [84, 64, 47, 27, '_']]
    return state == goal

start = [[60, 70, 88, 51, 72], [87, 43, 39, 85, 30], ['_', 64, 27, 84, 47]]
print(solve_puzzle(start))
