
from queue import PriorityQueue

def manhattan_distance(state):
    goal_state = [[79, 90, 85, 67], [100, 61, '_', 15], [95, 41, 33, 73]]
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
    for i, j in [(empty_row-1, empty_col), (empty_row+1, empty_col), (empty_row, empty_col-1), (empty_row, empty_col+1)]:
        if 0 <= i < 3 and 0 <= j < 4:
            neighbor = [row.copy() for row in state]
            neighbor[empty_row][empty_col], neighbor[i][j] = neighbor[i][j], neighbor[empty_row][empty_col]
            neighbors.append(neighbor)
    return neighbors

def solve_puzzle(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {tuple(map(tuple, initial_state)): None}
    cost_so_far = {tuple(map(tuple, initial_state)): 0}

    while not frontier.empty():
        _, current_state = frontier.get()

        if current_state == [[79, 90, 85, 67], [100, 61, '_', 15], [95, 41, 33, 73]]:
            path = []
            while current_state != initial_state:
                path.append(current_state[1][2])
                current_state = came_from[tuple(map(tuple, current_state))]
            return path[::-1]

        for neighbor in get_neighbors(current_state):
            new_cost = cost_so_far[tuple(map(tuple, current_state))] + 1
            if tuple(map(tuple, neighbor)) not in cost_so_far or new_cost < cost_so_far[tuple(map(tuple, neighbor)]]:
                cost_so_far[tuple(map(tuple, neighbor))] = new_cost
                priority = new_cost + manhattan_distance(neighbor)
                frontier.put((priority, neighbor))
                came_from[tuple(map(tuple, neighbor))] = current_state

    return None

initial_state = [[79, 90, 85, 67], [100, 61, '_', 15], [95, 41, 33, 73]]
solution = solve_puzzle(initial_state)
print(solution)
