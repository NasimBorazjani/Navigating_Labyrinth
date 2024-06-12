
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
    blank_pos = [(i, row.index('_')) for i, row in enumerate(state) if '_' in row][0]
    for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        new_x, new_y = blank_pos[0] + dx, blank_pos[1] + dy
        if 0 <= new_x < len(state) and 0 <= new_y < len(state[0]):
            new_state = [list(row) for row in state]
            new_state[blank_pos[0]][blank_pos[1]], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[blank_pos[0]][blank_pos[1]]
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

        for neighbor in get_neighbors(current_state):
            new_cost = cost_so_far[current_state] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, target_words)
                frontier.put((priority, neighbor))
                came_from[neighbor] = current_state

    path = []
    while current_state != initial_state:
        previous_state = came_from[current_state]
        blank_pos = [(i, row.index('_')) for i, row in enumerate(current_state) if '_' in row][0]
        prev_blank_pos = [(i, row.index('_')) for i, row in enumerate(previous_state) if '_' in row][0]
        dx, dy = blank_pos[0] - prev_blank_pos[0], blank_pos[1] - prev_blank_pos[1]
        if dx == 1 and dy == 1:
            path.append("down-right")
        elif dx == 1 and dy == -1:
            path.append("down-left")
        elif dx == -1 and dy == 1:
            path.append("up-right")
        elif dx == -1 and dy == -1:
            path.append("up-left")
        current_state = previous_state

    return path[::-1]

initial_state = [['o', 'a', '_', 'i', 't', 's'], ['d', 'r', 'o', 'o', 'o', 'a'], ['c', 'e', 'm', 'i', 'l', 'e'], ['c', 'c', 'm', 't', 'i', 'e']]
target_words = [['a', 'l', 'i', 'a', 's'], ['d', 'o', 'o', 'c', 'o', 't'], ['c', 'e', 'r', 'i', 't', 'e'], ['c', 'o', 'm', 'm', 'i', 'e']]

path = a_star(tuple(tuple(row) for row in initial_state), target_words)
print(path)
