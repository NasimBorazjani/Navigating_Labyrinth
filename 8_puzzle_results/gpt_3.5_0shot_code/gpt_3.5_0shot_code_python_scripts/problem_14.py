
from queue import PriorityQueue

# Define the initial state of the puzzle
initial_state = [[28, 51, 19], [89, '_', 21], [43, 39, 45]]
goal_state = [[89, 51, 45], [43, 39, 28], [21, 19, '_']]

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
        moves.append((x-1, y))  # Move up
    if x < 2:
        moves.append((x+1, y))  # Move down
    if y > 0:
        moves.append((x, y-1))  # Move left
    if y < 2:
        moves.append((x, y+1))  # Move right
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
            x, y = find_empty_spot(new_state)
            new_state[x][y], new_state[next_move[0]][next_move[1]] = new_state[next_move[0]][next_move[1]], '_'
            new_cost = current_cost + 1

            if str(new_state) not in cost_so_far or new_cost < cost_so_far[str(new_state)]:
                cost_so_far[str(new_state)] = new_cost
                priority = new_cost + manhattan_distance(next_move, find_empty_spot(goal_state))
                frontier.put((priority, new_state))
                came_from[str(new_state)] = current_state

    # Reconstruct the path from the goal state to the initial state
    current_state = goal_state
    path = []
    while current_state != initial_state:
        previous_state = came_from[str(current_state)]
        x, y = find_empty_spot(current_state)
        prev_x, prev_y = find_empty_spot(previous_state)
        path.append(current_state[prev_x][prev_y])
        current_state[prev_x][prev_y], current_state[x][y] = current_state[x][y], '_'
        current_state = previous_state

    return path[::-1]

# Solve the puzzle and print the list of tiles to be swapped
solution = solve_puzzle(initial_state, goal_state)
print(solution)
