
from queue import PriorityQueue

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def heuristic(state, target_words):
    total_distance = 0
    for i, row in enumerate(state):
        for j, char in enumerate(row):
            if char != '_':
                target_pos = [(i, pos) for pos, val in enumerate(target_words[i]) if val == char][0]
                total_distance += manhattan_distance((i, j), target_pos)
    return total_distance

def get_neighbors(state):
    neighbors = []
    blank_pos = [(i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == '_'][0]
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
            while current_state != initial_state:
                prev_state = came_from[current_state]
                blank_pos = [(i, j) for i, row in enumerate(current_state) for j, val in enumerate(row) if val == '_'][0]
                prev_blank_pos = [(i, j) for i, row in enumerate(prev_state) for j, val in enumerate(row) if val == '_'][0]
                path.append((prev_blank_pos[0] - blank_pos[0], prev_blank_pos[1] - blank_pos[1]))
                current_state = prev_state
            return path[::-1]
        
        for neighbor in get_neighbors(current_state):
            tentative_g_score = g_score[current_state] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, target_words)
                frontier.put((f_score, neighbor))
                came_from[neighbor] = current_state
    
    return None

initial_state = [['n', 'j', '_', 'b', 'e', 'y'], ['e', 'i', 't', 'u', 'n', 'o'], ['x', 'e', 'n', 'i', 'b', 'm'], ['e', 'n', 'w', 'o', 'm', 'b']]
target_words = [['j', 'i', 'b', 'b', 'y', '_'], ['e', 'n', 't', 'o', 'n', 'e'], ['x', 'e', 'n', 'i', 'u', 'm'], ['e', 'n', 'w', 'o', 'm', 'b']]

path = a_star(tuple(tuple(row) for row in initial_state), target_words)
print(path)
