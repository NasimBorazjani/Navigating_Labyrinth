
from queue import PriorityQueue

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def heuristic(state, target_words):
    total_distance = 0
    for i, row in enumerate(state):
        for j, char in enumerate(row):
            if char != '_':
                target_pos = [(i, pos) for pos, word in enumerate(target_words) if char in word][0]
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

        if all(''.join(row) == word for row, word in zip(current_state, target_words)):
            path = []
            while current_state != initial_state:
                previous_state = came_from[current_state]
                i, j = get_blank_position(previous_state)
                new_i, new_j = get_blank_position(current_state)
                if new_i < i and new_j < j:
                    path.append("up-left")
                elif new_i < i and new_j > j:
                    path.append("up-right")
                elif new_i > i and new_j < j:
                    path.append("down-left")
                elif new_i > i and new_j > j:
                    path.append("down-right")
                current_state = previous_state
            return path[::-1]

        for neighbor in get_neighbors(current_state):
            new_cost = cost_so_far[current_state] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, target_words)
                frontier.put((priority, neighbor))
                came_from[neighbor] = current_state

    return None

initial_state = (('y', 'c', 'a', 'r', 'd'), ('s', 'u', 'l', 'c', 'a'), ('v', 'h', '_', 'n', 'o'), ('s', 'e', 'l', 's', 'm'), ('b', 'i', 'u', 'h', 'y'))
target_words = ['card', 'sylva', 'shune', 'solum', 'bichy']

path = a_star(initial_state, target_words)
print(path)
