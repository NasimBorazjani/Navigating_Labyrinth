
from queue import PriorityQueue

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def heuristic(state, target_words):
    total_distance = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            char = state[i][j]
            if char != '_':
                target_pos = [(k, l) for k, word in enumerate(target_words) for l, c in enumerate(word) if c == char][0]
                total_distance += manhattan_distance((i, j), target_pos)
    return total_distance

def get_neighbors(state):
    neighbors = []
    blank_pos = [(i, j) for i, row in enumerate(state) for j, char in enumerate(row) if char == '_'][0]
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for d in directions:
        new_pos = (blank_pos[0] + d[0], blank_pos[1] + d[1])
        if 0 <= new_pos[0] < len(state) and 0 <= new_pos[1] < len(state[0]):
            new_state = [list(row) for row in state]
            new_state[blank_pos[0]][blank_pos[1]], new_state[new_pos[0]][new_pos[1]] = new_state[new_pos[0]][new_pos[1]], new_state[blank_pos[0]][blank_pos[1]]
            neighbors.append((tuple(row) for row in new_state))
    return neighbors

def a_star(initial_state, target_words):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {initial_state: None}
    g_score = {initial_state: 0}
    
    while not frontier.empty():
        _, current_state = frontier.get()
        
        if all(''.join(row) == word for row, word in zip(current_state, target_words)):
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

initial_state = [('_', 'p', 'h', 'm', 'p'), ('s', 'a', 'd', 'r', 'e'), ('i', 'u', 'n', 'i', 'r'), ('u', 'a', 'z', 'e', 'n')]
target_words = ['pimp', 'sadhe', 'aurir', 'unzen']

result = a_star(tuple(tuple(row) for row in initial_state), target_words)
for i in range(len(result) - 1):
    current_state = result[i]
    next_state = result[i + 1]
    blank_pos = [(i, j) for i, row in enumerate(current_state) for j, char in enumerate(row) if char == '_'][0]
    next_blank_pos = [(i, j) for i, row in enumerate(next_state) for j, char in enumerate(row) if char == '_'][0]
    direction = (next_blank_pos[0] - blank_pos[0], next_blank_pos[1] - blank_pos[1])
    if direction == (1, 1):
        print("Move blank space down-right")
    elif direction == (1, -1):
        print("Move blank space down-left")
    elif direction == (-1, 1):
        print("Move blank space up-right")
    elif direction == (-1, -1):
        print("Move blank space up-left")
