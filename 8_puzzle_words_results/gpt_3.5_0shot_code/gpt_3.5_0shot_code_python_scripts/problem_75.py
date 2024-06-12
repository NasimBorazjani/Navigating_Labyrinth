
from queue import PriorityQueue

def heuristic(state, target_words):
    # Calculate the number of characters that are not in the correct position
    count = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != '_' and state[i][j] != target_words[i][j]:
                count += 1
    return count

def get_neighbors(state):
    neighbors = []
    blank_pos = None
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '_':
                blank_pos = (i, j)
                break
    if blank_pos[0] > 0:
        neighbors.append((blank_pos[0]-1, blank_pos[1], 'up'))
    if blank_pos[0] < len(state)-1:
        neighbors.append((blank_pos[0]+1, blank_pos[1], 'down'))
    if blank_pos[1] > 0:
        neighbors.append((blank_pos[0], blank_pos[1]-1, 'left'))
    if blank_pos[1] < len(state[0])-1:
        neighbors.append((blank_pos[0], blank_pos[1]+1, 'right'))
    return neighbors

def a_star(initial_state, target_words):
    frontier = PriorityQueue()
    frontier.put((0, initial_state, []))
    visited = set()

    while not frontier.empty():
        cost, state, path = frontier.get()

        if state == target_words:
            return path

        if tuple(map(tuple, state)) in visited:
            continue

        visited.add(tuple(map(tuple, state))

        for neighbor in get_neighbors(state):
            new_state = [list(row) for row in state]
            new_state[neighbor[0]][neighbor[1]], new_state[blank_pos[0]][blank_pos[1]] = new_state[blank_pos[0]][blank_pos[1]], new_state[neighbor[0]][neighbor[1]]
            new_cost = cost + 1 + heuristic(new_state, target_words)
            new_path = path + [neighbor[2]]
            frontier.put((new_cost, new_state, new_path))

    return None

initial_state = [['_', 's', 's', 'h', 'o'], ['r', 'i', 'l', 'o', 'y'], ['j', 'o', 'l', 'i', 'p'], ['d', 'r', 'a', 'i', 'n'], ['n', 'i', 'v', 'a', 'l']]
target_words = [['s', 'o', 'h', 'o', '_'], ['r', 'i', 'l', 'l', 'y'], ['j', 'o', 's', 'i', 'p'], ['d', 'r', 'a', 'i', 'n'], ['n', 'i', 'v', 'a', 'l']]

result = a_star(initial_state, target_words)
print(result)
