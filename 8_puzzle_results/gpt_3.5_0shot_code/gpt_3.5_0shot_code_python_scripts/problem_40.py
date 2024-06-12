
from queue import PriorityQueue

def manhattan_distance(state):
    goal_state = [[28, 11, 50, 15], [94, 93, '_', 26], [34, 7, 3, 82]]
    distance = 0
    for i in range(3):
        for j in range(4):
            if state[i][j] != '_':
                x, y = divmod(goal_state.index(state[i][j]), 4)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = [(i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == '_'][0]
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 4:
            new_state = [row.copy() for row in state]
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
            neighbors.append(new_state)
    return neighbors

def solve_puzzle(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state, []))
    visited = set()

    while not frontier.empty():
        _, state, path = frontier.get()
        if state == [[28, 11, 50, 15], [94, 93, '_', 26], [34, 7, 3, 82]]:
            return path
        visited.add(str(state))
        for neighbor in get_neighbors(state):
            if str(neighbor) not in visited:
                priority = len(path) + 1 + manhattan_distance(neighbor)
                frontier.put((priority, neighbor, path + [neighbor[empty_row][empty_col]]))

initial_state = [[28, 11, 50, 15], [94, 93, '_', 26], [34, 7, 3, 82]]
solution = solve_puzzle(initial_state)
print(solution)
