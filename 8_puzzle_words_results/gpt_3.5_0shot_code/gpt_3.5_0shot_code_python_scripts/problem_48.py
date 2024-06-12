
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
    frontier.put((0, initial_state))
    came_from = {initial_state: None}
    g_score = {initial_state: 0}
    
    while not frontier.empty():
        _, current_state = frontier.get()
        
        if current_state == tuple(tuple(row) for row in target_words):
            path = []
            while current_state is not None:
                path.insert(0, current_state)
                current_state = came_from[current_state]
            return path[1:]
        
        for neighbor in get_neighbors(current_state):
            new_g_score = g_score[current_state] + 1
            if neighbor not in g_score or new_g_score < g_score[neighbor]:
                g_score[neighbor] = new_g_score
                f_score = new_g_score + heuristic(neighbor, target_words)
                frontier.put((f_score, neighbor))
                came_from[neighbor] = current_state
    
    return None

initial_state = [['l', 'a', 'd', 'd', 'e', 'd'], ['a', 'h', 't', 'g', 'e', 'a'], ['_', 'n', 'd', 'i', 'r', 'n'], ['p', 'a', 't', 'i', 'o', 'n']]
target_words = [['a', 'd', 'd', 'e', 'd', '_'], ['a', 'l', 't', 'h', 'e', 'a'], ['i', 'n', 'd', 'i', 'g', 'n'], ['p', 'a', 't', 'r', 'o', 'n']]

path = a_star(tuple(tuple(row) for row in initial_state), target_words)

if path:
    for i in range(len(path) - 1):
        current_state = path[i]
        next_state = path[i + 1]
        for i in range(len(current_state)):
            for j in range(len(current_state[0])):
                if current_state[i][j] != next_state[i][j]:
                    print(f"Swap '{current_state[i][j]}' with '_' at position ({i}, {j})")
else:
    print("No solution found.")
