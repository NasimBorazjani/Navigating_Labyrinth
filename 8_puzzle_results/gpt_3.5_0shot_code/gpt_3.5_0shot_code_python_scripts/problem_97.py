
from queue import PriorityQueue

def manhattan_distance(state):
    goal_state = [[100, 96, 93, 82, 6, 19], [68, 53, 50, 9, '_', 24], [16, 15, 48, 10, 76, 74]]
    distance = 0
    for i in range(3):
        for j in range(6):
            if state[i][j] != '_':
                x, y = divmod(state[i][j] - 1, 6)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_i, empty_j = None, None
    for i in range(3):
        for j in range(6):
            if state[i][j] == '_':
                empty_i, empty_j = i, j
                break
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = empty_i + di, empty_j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 6:
            new_state = [row.copy() for row in state]
            new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
            neighbors.append(new_state)
    return neighbors

def solve_puzzle(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {tuple(map(tuple, initial_state)): None}
    cost_so_far = {tuple(map(tuple, initial_state)): 0}

    while not frontier.empty():
        _, current_state = frontier.get()

        if current_state == [[100, 96, 93, 82, 6, 19], [68, 53, 50, 9, '_', 24], [16, 15, 48, 10, 76, 74]]:
            break

        for neighbor in get_neighbors(current_state):
            new_cost = cost_so_far[tuple(map(tuple, current_state))] + 1
            if tuple(map(tuple, neighbor)) not in cost_so_far or new_cost < cost_so_far[tuple(map(tuple, neighbor))]:
                cost_so_far[tuple(map(tuple, neighbor))] = new_cost
                priority = new_cost + manhattan_distance(neighbor)
                frontier.put((priority, neighbor))
                came_from[tuple(map(tuple, neighbor))] = current_state

    path = []
    while current_state != initial_state:
        previous_state = came_from[tuple(map(tuple, current_state))]
        for i in range(3):
            for j in range(6):
                if current_state[i][j] == '_':
                    empty_i, empty_j = i, j
                    break
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = empty_i + di, empty_j + dj
            if 0 <= new_i < 3 and 0 <= new_j < 6 and previous_state[new_i][new_j] == '_':
                path.append(current_state[new_i][new_j])
                break
        current_state = previous_state

    return path[::-1]

initial_state = [[100, 96, 93, 82, 6, 19], [68, 53, 50, 9, '_', 24], [16, 15, 48, 10, 76, 74]]
solution = solve_puzzle(initial_state)
print(solution)
