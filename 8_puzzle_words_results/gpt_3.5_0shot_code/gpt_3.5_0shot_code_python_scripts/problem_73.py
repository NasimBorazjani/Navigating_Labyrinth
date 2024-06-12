
from queue import PriorityQueue

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def heuristic(state, goal):
    total_distance = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != '_':
                goal_pos = goal[state[i][j]]
                total_distance += manhattan_distance((i, j), goal_pos)
    return total_distance

def get_blank_position(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '_':
                return (i, j)

def get_neighbors(state):
    neighbors = []
    i, j = get_blank_position(state)
    if i > 0 and j > 0:
        new_state = [list(row) for row in state]
        new_state[i][j], new_state[i-1][j-1] = new_state[i-1][j-1], new_state[i][j]
        neighbors.append((tuple(map(tuple, new_state)), 'up-left'))
    if i > 0 and j < len(state[0]) - 1:
        new_state = [list(row) for row in state]
        new_state[i][j], new_state[i-1][j+1] = new_state[i-1][j+1], new_state[i][j]
        neighbors.append((tuple(map(tuple, new_state)), 'up-right'))
    if i < len(state) - 1 and j > 0:
        new_state = [list(row) for row in state]
        new_state[i][j], new_state[i+1][j-1] = new_state[i+1][j-1], new_state[i][j]
        neighbors.append((tuple(map(tuple, new_state)), 'down-left'))
    if i < len(state) - 1 and j < len(state[0]) - 1:
        new_state = [list(row) for row in state]
        new_state[i][j], new_state[i+1][j+1] = new_state[i+1][j+1], new_state[i][j]
        neighbors.append((tuple(map(tuple, new_state)), 'down-right'))
    return neighbors

def a_star(initial_state, goal_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {}
    cost_so_far = {}
    came_from[initial_state] = None
    cost_so_far[initial_state] = 0

    while not frontier.empty():
        _, current_state = frontier.get()

        if current_state == goal_state:
            break

        for next_state, action in get_neighbors(current_state):
            new_cost = cost_so_far[current_state] + 1
            if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                cost_so_far[next_state] = new_cost
                priority = new_cost + heuristic(next_state, goal_state)
                frontier.put((priority, next_state))
                came_from[next_state] = (current_state, action)

    actions = []
    while current_state != initial_state:
        current_state, action = came_from[current_state]
        actions.append(action)

    return actions[::-1]

initial_board = [['o', 't', 'f', 'a', 'g'], ['h', 'r', 'p', 'r', 'd'], ['s', 'h', '_', 'l', 't'], ['n', 'e', 'a', 'e', 'h'], ['f', 'a', 'e', 's', 'e']]
goal_board = {'t': (0, 1), 'r': (1, 1), 'a': (3, 2), 'g': (0, 4), 'h': (3, 4), 'o': (0, 0), 'p': (1, 2), 's': (2, 0), 'f': (4, 0), 'e': (3, 3), 'd': (1, 4), 'l': (2, 3), '_': (2, 2)}

initial_state = tuple(map(tuple, initial_board))
goal_state = tuple(map(tuple, [['t', 'r', 'a', 'g', '_'], ['o', 'p', 's', 'h', 'f'], ['f', 'h', 'l', 'e', 'e'], ['n', 'e', 'a', 'r', 'd'], ['a', 't', 'e', 's', 'h']]))

actions = a_star(initial_state, goal_state)
print(actions)
