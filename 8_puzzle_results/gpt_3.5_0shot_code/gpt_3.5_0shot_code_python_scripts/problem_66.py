
from queue import PriorityQueue

def manhattan_distance(state):
    goal_state = [[94, 91, 33, 29, 78], [97, 20, 14, 54, 25], [38, 22, 32, 17, 0]]
    distance = 0
    for i in range(3):
        for j in range(5):
            if state[i][j] != goal_state[i][j]:
                distance += 1
    return distance

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = None, None
    for i in range(3):
        for j in range(5):
            if state[i][j] == 0:
                empty_row, empty_col = i, j
                break
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 5:
            new_state = [row.copy() for row in state]
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
            neighbors.append(new_state)
    return neighbors

def a_star_search(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {}
    cost_so_far = {str(initial_state): 0}

    while not frontier.empty():
        _, current_state = frontier.get()

        if manhattan_distance(current_state) == 0:
            path = []
            while str(current_state) in came_from:
                path.append(current_state)
                current_state = came_from[str(current_state)]
            path.reverse()
            return [state[2][4] for state in path]

        for neighbor in get_neighbors(current_state):
            new_cost = cost_so_far[str(current_state)] + 1
            if str(neighbor) not in cost_so_far or new_cost < cost_so_far[str(neighbor)]:
                cost_so_far[str(neighbor)] = new_cost
                priority = new_cost + manhattan_distance(neighbor)
                frontier.put((priority, neighbor))
                came_from[str(neighbor)] = current_state

    return None

initial_state = [[94, 91, 33, 29, 78], [97, 20, 14, 54, 25], [38, 22, 32, 17, 0]]
solution = a_star_search(initial_state)
print(solution)
