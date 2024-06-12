
import heapq
import numpy as np

def heuristic(a, b):
    return np.sum(np.abs(a - b))

def solve_puzzle(start, goal):
    stack = [(0, start, [])]
    seen = set()
    while stack:
        (cost, point, path) = heapq.heappop(stack)
        if np.array_equal(point, goal):
            return path
        for (next_point, action) in neighbors(point):
            if str(next_point) not in seen:
                seen.add(str(next_point))
                heapq.heappush(stack, (cost + heuristic(next_point, goal), next_point, path + [action]))

def neighbors(point):
    list = []
    x = np.where(point == '_')[0][0]
    y = np.where(point == '_')[1][0]
    if x > 0:
        new_point = np.copy(point)
        new_point[x][y], new_point[x - 1][y] = new_point[x - 1][y], new_point[x][y]
        list.append((new_point, new_point[x][y]))
    if x < 2:
        new_point = np.copy(point)
        new_point[x][y], new_point[x + 1][y] = new_point[x + 1][y], new_point[x][y]
        list.append((new_point, new_point[x][y]))
    if y > 0:
        new_point = np.copy(point)
        new_point[x][y], new_point[x][y - 1] = new_point[x][y - 1], new_point[x][y]
        list.append((new_point, new_point[x][y]))
    if y < 2:
        new_point = np.copy(point)
        new_point[x][y], new_point[x][y + 1] = new_point[x][y + 1], new_point[x][y]
        list.append((new_point, new_point[x][y]))
    return list

start = np.array([[87, 50, 82], [68, '_', 74], [23, 61, 11]])
goal = np.array([[87, 82, 74], [68, 61, 50], [23, 11, '_']])
print(solve_puzzle(start, goal))
