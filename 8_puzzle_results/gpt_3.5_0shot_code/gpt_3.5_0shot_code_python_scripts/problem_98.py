
from queue import PriorityQueue

def manhattan_distance(state):
    goal_state = [[89, 88, 62, 57, 79, 53], [92, 48, 61, 67, 78, 14], [32, 63, 27, 19, 54, '_']]
    distance = 0
    for i in range(3):
        for j in range(6):
            if state[i][j] != '_':
                x, y = divmod(state[i][j] - 1, 6)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = [(i, j) for i in range(3) for j in range(6) if state[i][j] == '_'][0]
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 6:
            new_state = [row.copy() for row in state]
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
            neighbors.append(new_state)
    return neighbors

def solve_puzzle(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {tuple(map(tuple, initial_state)): None}
    cost_so_far = {tuple(map(tuple, initial_state)): 0}

    while not frontier.empty():
        _, current_state = frontier.get()

        if current_state == [[89, 88, 62, 57, 79, 53], [92, 48, 61, 67, 78, 14], [32, 63, 27, 19, 54, '_']]:
            break

        for neighbor in get_neighbors(current_state):
            new_cost = cost_so_far[tuple(map(tuple, current_state))] + 1
            if tuple(map(tuple, neighbor)) not in cost_so_far or new_cost < cost_so_far[tuple(map(tuple, neighbor)]]:
                cost_so_far[tuple(map(tuple, neighbor))] = new_cost
                priority = new_cost + manhattan_distance(neighbor)
                frontier.put((priority, neighbor))
                came_from[tuple(map(tuple, neighbor))] = current_state

    path = []
    while current_state != initial_state:
        previous_state = came_from[tuple(map(tuple, current_state))]
        empty_row, empty_col = [(i, j) for i in range(3) for j in range(6) if current_state[i][j] == '_'][0]
        prev_empty_row, prev_empty_col = [(i, j) for i in range(3) for j in range(6) if previous_state[i][j] == '_'][0]
        path.append(current_state[prev_empty_row][prev_empty_col])
        current_state = previous_state

    return path[::-1]

initial_state = [[89, 88, 62, 57, 79, 53], [92, 48, 61, 67, 78, 14], [32, 63, 27, '_', 19, 54]]
solution = solve_puzzle(initial_state)
print(solution)
