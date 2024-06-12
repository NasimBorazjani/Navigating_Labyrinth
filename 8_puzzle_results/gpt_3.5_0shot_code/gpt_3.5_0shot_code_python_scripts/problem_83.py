
import heapq

def manhattan_distance(state):
    goal_state = [[79, 82, 80, 67, 45], [51, 50, 63, 41, 5], [39, 99, 31, 16, '_']]
    distance = 0
    for i in range(3):
        for j in range(5):
            if state[i][j] != '_':
                x, y = divmod(state[i][j] - 1, 5)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_i, empty_j = None, None
    for i in range(3):
        for j in range(5):
            if state[i][j] == '_':
                empty_i, empty_j = i, j
                break
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = empty_i + di, empty_j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 5:
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
        if state == [[79, 82, 80, 67, 45], [51, 50, 63, 41, 5], [39, 99, 31, 16, '_']]:
            return cost
        if tuple(map(tuple, state)) in visited:
            continue
        visited.add(tuple(map(tuple, state))
        for neighbor in get_neighbors(state):
            heapq.heappush(heap, (manhattan_distance(neighbor) + cost + 1, cost + 1, neighbor))

initial_state = [[79, 82, 80, 67, 45], [51, '_', 63, 41, 5], [39, 99, 31, 16, 50]]
shortest_path_length = a_star_search(initial_state)
print(shortest_path_length)
