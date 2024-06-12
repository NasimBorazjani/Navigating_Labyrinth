
import heapq

def manhattan_distance(state):
    goal_state = [[92, 75, 100, 61, 43, 87], [64, 34, 55, 90, 20, 86], [36, 32, 5, 42, 83, '_']]
    distance = 0
    for i in range(3):
        for j in range(6):
            if state[i][j] != '_':
                x, y = divmod(state[i][j] - 1, 6)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_i, empty_j = None, None
    for i in range(3):
        for j in range(6):
            if state[i][j] == '_':
                empty_i, empty_j = i, j
                break
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = empty_i + di, empty_j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 6:
            new_state = [row.copy() for row in state]
            new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
            neighbors.append(new_state)
    return neighbors

def a_star_search(initial_state):
    heap = [(manhattan_distance(initial_state), 0, initial_state)]
    heapq.heapify(heap)
    visited = set()
    while heap:
        _, cost, state = heapq.heappop(heap)
        if state == [[92, 75, 100, 61, 43, 87], [64, 34, 55, 90, 20, 86], [36, 32, 5, 42, 83, '_']]:
            return cost
        if tuple(map(tuple, state)) in visited:
            continue
        visited.add(tuple(map(tuple, state)))
        for neighbor in get_neighbors(state):
            heapq.heappush(heap, (manhattan_distance(neighbor) + cost + 1, cost + 1, neighbor))

initial_state = [[92, 75, 100, 61, 43, 87], [64, 34, 55, 90, 20, 86], [36, '_', 32, 5, 42, 83]]
steps = a_star_search(initial_state)
print(steps)
