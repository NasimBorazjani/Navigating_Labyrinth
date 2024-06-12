
from queue import PriorityQueue

# Define the initial state of the puzzle
initial_state = [[82, '_', 39, 54], [55, 62, 53, 35], [69, 16, 11, 71]]
goal_state = [[82, 71, 62, 55], [54, 53, 39, 35], [16, 11, '_', 0]]

# Define a function to calculate the Manhattan distance between two tiles
def manhattan_distance(tile1, tile2):
    x1, y1 = tile1
    x2, y2 = tile2
    return abs(x1 - x2) + abs(y1 - y2)

# Define a function to find the empty spot in the puzzle
def find_empty_spot(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '_':
                return (i, j)

# Define a function to generate the possible moves from a given state
def generate_moves(state):
    moves = []
    empty_spot = find_empty_spot(state)
    x, y = empty_spot
    if x > 0:
        moves.append((x-1, y))
    if x < len(state) - 1:
        moves.append((x+1, y))
    if y > 0:
        moves.append((x, y-1))
    if y < len(state[0]) - 1:
        moves.append((x, y+1))
    return moves

# Define a function to calculate the heuristic value of a state
def heuristic(state):
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != '_':
                tile = state[i][j]
                goal_tile = goal_state[i][j]
                h += manhattan_distance((i, j), (goal_tile // len(state), goal_tile % len(state)))
    return h

# Define the A* search algorithm
def a_star_search(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {}
    cost_so_far = {}
    came_from[str(initial_state)] = None
    cost_so_far[str(initial_state)] = 0

    while not frontier.empty():
        _, current_state = frontier.get()

        if current_state == goal_state:
            break

        for next_move in generate_moves(current_state):
            new_state = [row[:] for row in current_state]
            x, y = find_empty_spot(new_state)
            new_state[x][y], new_state[next_move[0]][next_move[1]] = new_state[next_move[0]][next_move[1]], new_state[x][y]
            new_cost = cost_so_far[str(current_state)] + 1

            if str(new_state) not in cost_so_far or new_cost < cost_so_far[str(new_state)]:
                cost_so_far[str(new_state)] = new_cost
                priority = new_cost + heuristic(new_state)
                frontier.put((priority, new_state))
                came_from[str(new_state)] = current_state

    # Reconstruct the path from the goal state to the initial state
    path = []
    current = goal_state
    while current != initial_state:
        path.append(current)
        current = came_from[str(current)]
    path.append(initial_state)
    path.reverse()

    # Extract the list of tiles that need to be swapped with the empty spot
    moves = []
    for i in range(1, len(path)):
        x1, y1 = find_empty_spot(path[i-1])
        x2, y2 = find_empty_spot(path[i])
        moves.append(path[i][x1][y1])

    return moves

# Solve the 8-puzzle problem
solution = a_star_search(initial_state)
print(solution)
