
import heapq
import numpy as np

def heuristic(a, b):
    return np.sum(np.abs(a - b))

def solve_puzzle(initial_state, goal_state):
    heap = []
    heapq.heappush(heap, (0, 0, initial_state, []))
    visited = set()

    while heap:
        (h, g, current_state, path) = heapq.heappop(heap)
        if np.array_equal(current_state, goal_state):
            return path
        if str(current_state.tolist()) in visited:
            continue
        visited.add(str(current_state.tolist()))
        empty_spot = tuple(map(int, np.where(current_state == '_')))
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_spot = (empty_spot[0] + direction[0], empty_spot[1] + direction[1])
            if 0 <= new_spot[0] < current_state.shape[0] and 0 <= new_spot[1] < current_state.shape[1]:
                new_state = current_state.copy()
                new_state[empty_spot], new_state[new_spot] = new_state[new_spot], new_state[empty_spot]
                new_path = path + [new_state[new_spot]]
                new_g = g + 1
                new_h = new_g + heuristic(new_state, goal_state)
                heapq.heappush(heap, (new_h, new_g, new_state, new_path))

initial_state = np.array([[28, 11, 50, 15], [94, 93, '_', 26], [34, 7, 3, 82]])
goal_state = np.array([[94, 93, 82, 50], [28, 26, 15, 11], [34, 7, 3, '_']])
print(solve_puzzle(initial_state, goal_state))
