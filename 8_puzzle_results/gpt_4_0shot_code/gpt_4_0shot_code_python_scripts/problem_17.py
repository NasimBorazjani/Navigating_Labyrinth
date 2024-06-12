
import heapq
import numpy as np

def heuristic(a, b):
    return np.sum(np.abs(a - b))

def solve_puzzle(start, goal):
    queue = [(0, start)]
    seen = {np.array2string(start): True}
    while queue:
        (priority, current) = heapq.heappop(queue)
        if np.array_equal(current, goal):
            return priority
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            for i in range(3):
                for j in range(3):
                    if current[i][j] == '_':
                        ni, nj = i + direction[0], j + direction[1]
                        if 0 <= ni < 3 and 0 <= nj < 3:
                            next_state = np.copy(current)
                            next_state[i][j], next_state[ni][nj] = next_state[ni][nj], next_state[i][j]
                            if np.array2string(next_state) not in seen:
                                seen[np.array2string(next_state)] = True
                                heapq.heappush(queue, (priority + 1 + heuristic(next_state, goal), next_state))
    return -1

start = np.array([[27, 18, 79], [22, 99, 9], [49, 53, '_']])
goal = np.array([[99, 79, 53], [49, 27, 22], [18, 9, '_']])
print(solve_puzzle(start, goal))
