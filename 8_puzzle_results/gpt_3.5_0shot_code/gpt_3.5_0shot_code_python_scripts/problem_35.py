
from queue import PriorityQueue

def manhattan_distance(state):
    goal_state = [[95, 94, 80, 69], [67, 66, 53, 35], [27, 26, 18, '_']]
    distance = 0
    for i in range(3):
        for j in range(4):
            if state[i][j] != '_':
                num = state[i][j]
                goal_i, goal_j = divmod(goal_state.index(num), 4)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_i, empty_j = [(i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == '_'][0]
    for i, j in [(empty_i-1, empty_j), (empty_i+1, empty_j), (empty_i, empty_j-1), (empty_i, empty_j+1)]:
        if 0 <= i < 3 and 0 <= j < 4:
            new_state = [row.copy() for row in state]
            new_state[empty_i][empty_j], new_state[i][j] = new_state[i][j], new_state[empty_i][empty_j]
            neighbors.append(new_state)
    return neighbors

def solve_puzzle(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {tuple(map(tuple, initial_state)): None}
    cost_so_far = {tuple(map(tuple, initial_state)): 0}

    while not frontier.empty():
        _, current_state = frontier.get()

        if current_state == [[95, 94, 80, 69], [67, 66, 53, 35], [27, 26, 18, '_']]:
            path = []
            while current_state != initial_state:
                path.append(current_state[empty_i][empty_j])
                current_state = came_from[tuple(map(tuple, current_state))]
            return path[::-1]

        for neighbor in get_neighbors(current_state):
            new_cost = cost_so_far[tuple(map(tuple, current_state))] + 1
            if tuple(map(tuple, neighbor)) not in cost_so_far or new_cost < cost_so_far[tuple(map(tuple, neighbor)]:
                cost_so_far[tuple(map(tuple, neighbor))] = new_cost
                priority = new_cost + manhattan_distance(neighbor)
                frontier.put((priority, neighbor))
                came_from[tuple(map(tuple, neighbor))] = current_state

    return None

initial_state = [[95, '_', 80, 18], [67, 66, 35, 94], [27, 26, 69, 53]]
solution = solve_puzzle(initial_state)
print(solution)
