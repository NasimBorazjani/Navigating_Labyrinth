
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

def get_blank_position(state):
    for i, row in enumerate(state):
        for j, char in enumerate(row):
            if char == '_':
                return (i, j)

def get_neighbors(state):
    i, j = get_blank_position(state)
    neighbors = []
    if i > 0 and j > 0:
        new_state = [list(row) for row in state]
        new_state[i][j], new_state[i-1][j-1] = new_state[i-1][j-1], new_state[i][j]
        neighbors.append(tuple(tuple(row) for row in new_state))
    if i > 0 and j < len(state[0]) - 1:
        new_state = [list(row) for row in state]
        new_state[i][j], new_state[i-1][j+1] = new_state[i-1][j+1], new_state[i][j]
        neighbors.append(tuple(tuple(row) for row in new_state))
    if i < len(state) - 1 and j > 0:
        new_state = [list(row) for row in state]
        new_state[i][j], new_state[i+1][j-1] = new_state[i+1][j-1], new_state[i][j]
        neighbors.append(tuple(tuple(row) for row in new_state))
    if i < len(state) - 1 and j < len(state[0]) - 1:
        new_state = [list(row) for row in state]
        new_state[i][j], new_state[i+1][j+1] = new_state[i+1][j+1], new_state[i][j]
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
        previous_state = came_from[current_state]
        i, j = get_blank_position(current_state)
        pi, pj = get_blank_position(previous_state)
        if i < pi and j < pj:
            path.append("down-right")
        elif i < pi and j > pj:
            path.append("down-left")
        elif i > pi and j < pj:
            path.append("up-right")
        elif i > pi and j > pj:
            path.append("up-left")
        current_state = previous_state

    return path[::-1]

initial_state = [['a', 'm', '_', 'p'], ['p', 'e', 'h', 'a'], ['l', 'e', 'y', 'l'], ['v', 'i', 'a', 'i'], ['w', 'u', 's', 'p']]
target_words = [['m', 'a', 'p', '_'], ['p', 'a', 'h', 'i'], ['y', 'e', 'e', 'l'], ['v', 'i', 'a', 'l'], ['w', 'u', 's', 'p']]

path = a_star(tuple(tuple(row) for row in initial_state), target_words)
print(path)