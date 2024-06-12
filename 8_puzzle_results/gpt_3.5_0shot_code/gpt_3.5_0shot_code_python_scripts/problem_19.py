
from queue import PriorityQueue

# Define the initial state of the puzzle
initial_state = [[89, 69, 35], [16, 14, 64], ['_', 23, 32]]

# Define the goal state of the puzzle
goal_state = [[89, 69, 64], [35, 32, 23], [16, 14, '_']]

# Define a function to calculate the Manhattan distance between two tiles
def manhattan_distance(tile1, tile2):
    x1, y1 = tile1
    x2, y2 = tile2
    return abs(x1 - x2) + abs(y1 - y2)

# Define a function to calculate the total Manhattan distance of a state
def total_manhattan_distance(state):
    total_distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != '_':
                x, y = divmod(state[i][j] - 1, 3)
                total_distance += manhattan_distance((i, j), (x, y))
    return total_distance

# Define a function to get the possible moves from a given state
def get_possible_moves(state):
    moves = []
    x, y = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == '_':
                x, y = i, j
    if x > 0:
        moves.append((x - 1, y))
    if x < 2:
        moves.append((x + 1, y))
    if y > 0:
        moves.append((x, y - 1))
    if y < 2:
        moves.append((x, y + 1))
    return moves

# Define the A* search algorithm to find the shortest path to the goal state
def a_star_search(initial_state, goal_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state, []))
    explored = set()

    while not frontier.empty():
        _, current_state, path = frontier.get()
        if current_state == goal_state:
            return path
        explored.add(str(current_state))

        for move in get_possible_moves(current_state):
            new_state = [row.copy() for row in current_state]
            x, y = move
            new_state[x][y], new_state[current_state.index('_') // 3][current_state.index('_') % 3] = new_state[current_state.index('_') // 3][current_state.index('_') % 3], new_state[x][y]
            if str(new_state) not in explored:
                new_path = path.copy()
                new_path.append(new_state[x][y])
                frontier.put((total_manhattan_distance(new_state), new_state, new_path))

    return None

# Find the shortest list of tiles that need to be swapped with the empty spot to achieve the goal state
solution = a_star_search(initial_state, goal_state)
print(solution)
