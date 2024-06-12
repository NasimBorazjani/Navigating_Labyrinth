
from queue import PriorityQueue

def manhattan_distance(state):
    goal_state = [[61, 62, 63, 64], [65, 66, 67, 68], [69, 70, 71, 72]]
    distance = 0
    for i in range(3):
        for j in range(4):
            if state[i][j] != '_':
                num = state[i][j]
                goal_i, goal_j = divmod(num - 61, 4)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_i, empty_j = None, None
    for i in range(3):
        for j in range(4):
            if state[i][j] == '_':
                empty_i, empty_j = i, j
                break
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = empty_i + di, empty_j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 4:
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

        if manhattan_distance(current_state) == 0:
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
        for i in range(3):
            for j in range(4):
                if current_state[i][j] == '_':
                    empty_i, empty_j = i, j
                    break
        prev_state = came_from[tuple(map(tuple, current_state))]
        for i in range(3):
            for j in range(4):
                if prev_state[i][j] == '_':
                    prev_empty_i, prev_empty_j = i, j
                    break
        if empty_i - prev_empty_i == 1:
            path.append(current_state[empty_i - 1][empty_j])
        elif empty_i - prev_empty_i == -1:
            path.append(current_state[empty_i + 1][empty_j])
        elif empty_j - prev_empty_j == 1:
            path.append(current_state[empty_i][empty_j - 1])
        elif empty_j - prev_empty_j == -1:
            path.append(current_state[empty_i][empty_j + 1])
        current_state = prev_state

    return path[::-1]

initial_state = [[61, '_', 99, 70], [42, 81, 90, 16], [41, 54, 28, 45]]
solution = solve_puzzle(initial_state)
print(solution)
