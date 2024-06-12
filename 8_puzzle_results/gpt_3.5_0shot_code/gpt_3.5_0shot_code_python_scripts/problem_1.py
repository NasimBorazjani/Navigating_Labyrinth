
from queue import PriorityQueue

# Define the initial state of the puzzle
initial_state = [[12, 55, '_'], [35, 97, 43], [17, 25, 9]]

# Define the goal state of the puzzle
goal_state = [[97, 55, 43], [35, 25, 17], [12, 9, '_']]

# Define a function to calculate the Manhattan distance between two tiles
def manhattan_distance(tile1, tile2):
    x1, y1 = tile1
    x2, y2 = tile2
    return abs(x1 - x2) + abs(y1 - y2)

# Define a function to find the empty spot in the puzzle
def find_empty_spot(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == '_':
                return (i, j)

# Define a function to generate the possible moves from a given state
def generate_moves(state):
    moves = []
    empty_spot = find_empty_spot(state)
    x, y = empty_spot
    if x > 0:
        moves.append((x-1, y))
    if x < 2:
        moves.append((x+1, y))
    if y > 0:
        moves.append((x, y-1))
    if y < 2:
        moves.append((x, y+1))
    return moves

# Define a function to solve the puzzle using A* search algorithm
def solve_puzzle(initial_state, goal_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {}
    cost_so_far = {}
    came_from[str(initial_state)] = None
    cost_so_far[str(initial_state)] = 0

    while not frontier.empty():
        current_cost, current_state = frontier.get()

        if current_state == goal_state:
            break

        for next_move in generate_moves(current_state):
            new_state = [row[:] for row in current_state]
            x1, y1 = find_empty_spot(new_state)
            x2, y2 = next_move
            new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
            new_cost = current_cost + 1

            if str(new_state) not in cost_so_far or new_cost < cost_so_far[str(new_state)]:
                cost_so_far[str(new_state)] = new_cost
                priority = new_cost + manhattan_distance(find_empty_spot(new_state), (2, 2))
                frontier.put((priority, new_state))
                came_from[str(new_state)] = current_state

    # Reconstruct the path from the goal state to the initial state
    path = []
    current_state = goal_state
    while current_state != initial_state:
        path.append(current_state)
        current_state = came_from[str(current_state)]
    path.append(initial_state)
    path.reverse()

    # Extract the list of tiles that need to be swapped with the empty spot
    moves = []
    for i in range(1, len(path)):
        x1, y1 = find_empty_spot(path[i-1])
        x2, y2 = find_empty_spot(path[i])
        moves.append(path[i][x2][y2])

    return moves

# Solve the puzzle and print the list of tiles to be swapped
solution = solve_puzzle(initial_state, goal_state)
print(solution)
