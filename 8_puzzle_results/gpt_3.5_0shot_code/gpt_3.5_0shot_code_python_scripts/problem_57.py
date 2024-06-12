
from queue import PriorityQueue

def manhattan_distance(state):
    goal_state = [[71, 42, 22, 90], [79, 78, '_', 68], [25, 58, 28, 12]]
    distance = 0
    for i in range(3):
        for j in range(4):
            if state[i][j] != '_':
                x, y = divmod(state[i][j] - 1, 4)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = None, None
    for i in range(3):
        for j in range(4):
            if state[i][j] == '_':
                empty_row, empty_col = i, j
                break
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 4:
            new_state = [row[:] for row in state]
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], '_'
            neighbors.append(new_state)
    return neighbors

def solve_puzzle(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {tuple(map(tuple, initial_state)): None}
    cost_so_far = {tuple(map(tuple, initial_state)): 0}

    while not frontier.empty():
        _, current_state = frontier.get()

        if current_state == [[71, 42, 22, 90], [79, 78, '_', 68], [25, 58, 28, 12]]:
            break

        for next_state in get_neighbors(current_state):
            new_cost = cost_so_far[tuple(map(tuple, current_state))] + 1
            if tuple(map(tuple, next_state)) not in cost_so_far or new_cost < cost_so_far[tuple(map(tuple, next_state))]:
                cost_so_far[tuple(map(tuple, next_state))] = new_cost
                priority = new_cost + manhattan_distance(next_state)
                frontier.put((priority, next_state))
                came_from[tuple(map(tuple, next_state))] = current_state

    path = []
    while current_state != initial_state:
        for i in range(3):
            for j in range(4):
                if current_state[i][j] == '_':
                    empty_row, empty_col = i, j
                    break
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = empty_row + dr, empty_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 4:
                if current_state[new_row][new_col] != came_from[tuple(map(tuple, current_state))][new_row][new_col]:
                    path.append(current_state[new_row][new_col])
                    current_state[empty_row][empty_col], current_state[new_row][new_col] = current_state[new_row][new_col], '_'
                    break

    return path

initial_state = [[71, 42, 22, 90], [79, 78, '_', 68], [25, 58, 28, 12]]
solution = solve_puzzle(initial_state)
print(solution)
