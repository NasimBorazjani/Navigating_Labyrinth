
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
    blank_pos = None
    for i, row in enumerate(state):
        for j, char in enumerate(row):
            if char == '_':
                blank_pos = (i, j)
                break
        if blank_pos:
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
    came_from = {}
    cost_so_far = {initial_state: 0}
    
    while not frontier.empty():
        _, current_state = frontier.get()
        
        if current_state == tuple(tuple(row) for row in target_words):
            break
        
        for next_state in get_neighbors(current_state):
            new_cost = cost_so_far[current_state] + 1
            if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                cost_so_far[next_state] = new_cost
                priority = new_cost + heuristic(next_state, target_words)
                frontier.put((priority, next_state))
                came_from[next_state] = current_state
    
    path = []
    while current_state != initial_state:
        prev_state = came_from[current_state]
        for i, row in enumerate(current_state):
            for j, char in enumerate(row):
                if char != prev_state[i][j]:
                    path.append((char, i, j))
        current_state = prev_state
    
    return path[::-1]

initial_state = [['s', 'n', '_', 'e', 'y', 'e'], ['a', 'e', 't', 'i', 'l', 'e'], ['o', 'e', 'c', 'i', 'v', 't'], ['m', 'l', 'w', 's', 'e', 'r']]
target_words = [['n', 'i', 'e', 'v', 'e', '_'], ['a', 's', 't', 'e', 'l', 'y'], ['o', 'e', 'c', 'i', 's', 't'], ['m', 'e', 'w', 'l', 'e', 'r']]

path = a_star(tuple(tuple(row) for row in initial_state), target_words)
print(path)
