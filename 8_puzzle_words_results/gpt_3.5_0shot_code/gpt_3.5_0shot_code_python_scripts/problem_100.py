
from queue import PriorityQueue

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def heuristic(state, target_words):
    total_distance = 0
    for i, row in enumerate(state):
        for j, char in enumerate(row):
            if char != '_':
                target_pos = [(i, k) for k, c in enumerate(target_words[i]) if c == char][0]
                total_distance += manhattan_distance((i, j), target_pos)
    return total_distance

def get_neighbors(state):
    neighbors = []
    blank_pos = None
    for i, row in enumerate(state):
        if '_' in row:
            blank_pos = (i, row.index('_'))
            break
    for di, dj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        new_i, new_j = blank_pos[0] + di, blank_pos[1] + dj
        if 0 <= new_i < len(state) and 0 <= new_j < len(state[0]):
            new_state = [list(row) for row in state]
            new_state[blank_pos[0]][blank_pos[1]], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_pos[0]][blank_pos[1]]
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

def a_star(initial_state, target_words):
    frontier = PriorityQueue()
    frontier.put((heuristic(initial_state, target_words), 0, initial_state, []))
    visited = set()

    while not frontier.empty():
        _, cost, current_state, path = frontier.get()

        if current_state in visited:
            continue

        visited.add(current_state)

        if ["".join(row) for row in current_state] == target_words:
            return path

        for neighbor in get_neighbors(current_state):
            new_cost = cost + 1
            new_path = path + [neighbor]
            frontier.put((new_cost + heuristic(neighbor, target_words), new_cost, neighbor, new_path))

    return None

initial_state = [('o', 'k', 's', 't', 'a', 'r'), ('b', 'y', 'n', 'i', 'a', 'a'), ('s', 'a', '_', 'b', 'a', 'r'), ('m', 'o', 'p', 'e', 'n', 'u'), ('v', 'o', 'm', 'e', 'a', 'r')]
target_words = ['katar', 'bonsai', 'sambar', 'mopane', 'voyeur']

result = a_star(tuple(tuple(row) for row in initial_state), target_words)

for i in range(len(result) - 1):
    print(result[i])
