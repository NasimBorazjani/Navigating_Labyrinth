
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
        for j, char in enumerate(row):
            if char == '_':
                blank_pos = (i, j)
                break
    if blank_pos[0] > 0:
        new_state = [list(row) for row in state]
        new_state[blank_pos[0]][blank_pos[1]] = new_state[blank_pos[0]-1][blank_pos[1]]
        new_state[blank_pos[0]-1][blank_pos[1]] = '_'
        neighbors.append((tuple(tuple(row) for row in new_state), 'up-left'))
    if blank_pos[0] < len(state) - 1:
        new_state = [list(row) for row in state]
        new_state[blank_pos[0]][blank_pos[1]] = new_state[blank_pos[0]+1][blank_pos[1]]
        new_state[blank_pos[0]+1][blank_pos[1]] = '_'
        neighbors.append((tuple(tuple(row) for row in new_state), 'down-left'))
    if blank_pos[1] > 0:
        new_state = [list(row) for row in state]
        new_state[blank_pos[0]][blank_pos[1]] = new_state[blank_pos[0]][blank_pos[1]-1]
        new_state[blank_pos[0]][blank_pos[1]-1] = '_'
        neighbors.append((tuple(tuple(row) for row in new_state), 'up-right'))
    if blank_pos[1] < len(state[0]) - 1:
        new_state = [list(row) for row in state]
        new_state[blank_pos[0]][blank_pos[1]] = new_state[blank_pos[0]][blank_pos[1]+1]
        new_state[blank_pos[0]][blank_pos[1]+1] = '_'
        neighbors.append((tuple(tuple(row) for row in new_state), 'down-right'))
    return neighbors

def a_star(initial_state, target_words):
    frontier = PriorityQueue()
    frontier.put((0, initial_state, []))
    visited = set()
    
    while not frontier.empty():
        cost, state, path = frontier.get()
        
        if state in visited:
            continue
        
        visited.add(state)
        
        if state == tuple(tuple(list(word) for word in target_words)):
            return path
        
        for neighbor, direction in get_neighbors(state):
            new_cost = len(path) + 1 + heuristic(neighbor, target_words)
            frontier.put((new_cost, neighbor, path + [direction]))
    
    return None

initial_state = [['y', 'h', 'r', 'm', '_', 's'], ['b', 'o', 'w', 'k', 'r', 'u'], ['r', 'e', 'l', 'e', 'u', 's'], ['c', 'c', 'a', 'u', 't', 'y']]
target_words = ['humus', 'bywork', 'cereus', 'clarty']

result = a_star(tuple(tuple(row) for row in initial_state), target_words)
print(result)
