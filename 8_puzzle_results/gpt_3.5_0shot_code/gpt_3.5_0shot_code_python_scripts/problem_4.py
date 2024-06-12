
from queue import PriorityQueue

# Define the initial state of the puzzle
initial_state = [[66, 89, 70], [25, 42, 83], ['_', 24, 71]]

# Define the goal state of the puzzle
goal_state = [[89, 83, 71], [70, 66, 42], [25, 24, '_']]

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
                tile = state[i][j]
                goal_tile = [(k, l) for k in range(3) for l in range(3) if goal_state[k][l] == tile][0]
                total_distance += manhattan_distance((i, j), goal_tile)
    return total_distance

# Define a function to get the possible moves from a given state
def get_possible_moves(state):
    possible_moves = []
    empty_tile = [(i, j) for i in range(3) for j in range(3) if state[i][j] == '_'][0]
    x, y = empty_tile
    if x > 0:
        possible_moves.append((x-1, y))
    if x < 2:
        possible_moves.append((x+1, y))
    if y > 0:
        possible_moves.append((x, y-1))
    if y < 2:
        possible_moves.append((x, y+1))
    return possible_moves

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
            new_state[x][y], new_state[empty_tile[0]][empty_tile[1]] = new_state[empty_tile[0]][empty_tile[1]], new_state[x][y]
            if str(new_state) not in explored:
                new_path = path.copy()
                new_path.append(new_state[x][y])
                frontier.put((total_manhattan_distance(new_state), new_state, new_path))

    return None

# Find the shortest list of tiles to swap with the empty spot to achieve the goal state
solution = a_star_search(initial_state, goal_state)
print(solution)
