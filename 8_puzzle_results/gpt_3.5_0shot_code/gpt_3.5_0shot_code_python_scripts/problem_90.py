
from queue import PriorityQueue

def manhattan_distance(state):
    goal_state = [[88, 59, 84, 71, 80], [72, 79, 74, 96, 51], [48, 28, 25, 24, 19]]
    distance = 0
    for i in range(3):
        for j in range(5):
            if state[i][j] != '_':
                x_goal, y_goal = divmod(goal_state[i][j] - 1, 5)
                x_state, y_state = divmod(state[i][j] - 1, 5)
                distance += abs(x_goal - x_state) + abs(y_goal - y_state)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_x, empty_y = None, None
    for i in range(3):
        for j in range(5):
            if state[i][j] == '_':
                empty_x, empty_y = i, j
                break
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 5:
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            neighbors.append((new_state, (new_x, new_y)))
    return neighbors

def solve_puzzle(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state, []))
    visited = set()

    while not frontier.empty():
        _, current_state, path = frontier.get()
        if current_state == [[88, 59, 84, 71, 80], [72, 79, 74, 96, 51], [48, 28, 25, 24, 19]]:
            return path
        visited.add(str(current_state))
        for neighbor_state, move in get_neighbors(current_state):
            if str(neighbor_state) not in visited:
                new_path = path.copy()
                new_path.append(neighbor_state[move[0]][move[1]])
                frontier.put((len(new_path) + manhattan_distance(neighbor_state), neighbor_state, new_path))

initial_state = [[88, 59, 84, 71, 80], [72, 79, 74, 96, 51], ['_', 28, 25, 24, 19]]
solution = solve_puzzle(initial_state)
print(solution)
