
from queue import PriorityQueue

def manhattan_distance(state):
    goal_state = [[94, 87, 69, 81, 4, 79], [3, 35, 86, 61, 57, 75], [41, 18, 65, 9, 53, 55]]
    distance = 0
    for i in range(3):
        for j in range(6):
            if state[i][j] != '_':
                x_goal, y_goal = divmod(goal_state[i].index(state[i][j]), 1)
                x_state, y_state = divmod(j, 1)
                distance += abs(x_goal - i) + abs(y_goal - y_state)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_x, empty_y = None, None
    for i in range(3):
        for j in range(6):
            if state[i][j] == '_':
                empty_x, empty_y = i, j
                break
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 6:
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            neighbors.append(new_state)
    return neighbors

def solve_puzzle(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {tuple(map(tuple, initial_state)): None}
    cost_so_far = {tuple(map(tuple, initial_state)): 0}

    while not frontier.empty():
        _, current_state = frontier.get()

        if current_state == [[94, 87, 69, 81, 4, 79], [3, 35, 86, 61, 57, 75], [41, 18, 65, 9, 53, 55]]:
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
            for j in range(6):
                if current_state[i][j] == '_':
                    empty_x, empty_y = i, j
                    break
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = empty_x + dx, empty_y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 6:
                new_state = [row.copy() for row in current_state]
                new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
                if tuple(map(tuple, new_state)) == tuple(map(tuple, came_from[tuple(map(tuple, current_state))]):
                    path.append(current_state[new_x][new_y])
                    current_state = new_state
                    break

    return path[::-1]

initial_state = [[94, 87, 69, 81, 4, 79], ['_', 35, 86, 61, 57, 75], [41, 18, 65, 9, 53, 55]]
solution = solve_puzzle(initial_state)
print(solution)
