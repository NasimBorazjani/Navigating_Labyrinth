
from queue import PriorityQueue

# Define the initial state of the puzzle
initial_state = [['_', 94, 43, 58, 77], [96, 100, 75, 84, 52], [50, 29, 60, 27, 74]]
goal_state = [[100, 96, 94, 84, 77], [75, 74, 60, 58, 52], [50, 43, 29, 27, '_']]

# Define a function to calculate the Manhattan distance between two points
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Define a function to find the empty spot in the puzzle
def find_empty_spot(state):
    for i in range(3):
        for j in range(5):
            if state[i][j] == '_':
                return (i, j)

# Define a function to generate the possible moves from a given state
def generate_moves(state):
    moves = []
    empty_spot = find_empty_spot(state)
    i, j = empty_spot
    if i > 0:
        moves.append((i-1, j))  # Move up
    if i < 2:
        moves.append((i+1, j))  # Move down
    if j > 0:
        moves.append((i, j-1))  # Move left
    if j < 4:
        moves.append((i, j+1))  # Move right
    return moves

# Define a function to solve the puzzle using A* search algorithm
def solve_puzzle(initial_state, goal_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {}
    cost_so_far = {str(initial_state): 0}

    while not frontier.empty():
        _, current_state = frontier.get()

        if current_state == goal_state:
            break

        for next_move in generate_moves(current_state):
            new_state = [row.copy() for row in current_state]
            i, j = find_empty_spot(new_state)
            new_state[i][j], new_state[next_move[0]][next_move[1]] = new_state[next_move[0]][next_move[1]], new_state[i][j]
            new_cost = cost_so_far[str(current_state)] + 1

            if str(new_state) not in cost_so_far or new_cost < cost_so_far[str(new_state)]:
                cost_so_far[str(new_state)] = new_cost
                priority = new_cost + manhattan_distance(next_move, find_empty_spot(new_state))
                frontier.put((priority, new_state))
                came_from[str(new_state)] = current_state

    # Reconstruct the path from the goal state to the initial state
    path = []
    current = str(goal_state)
    while current != str(initial_state):
        path.append(int(came_from[current][find_empty_spot(came_from[current])[0]][find_empty_spot(came_from[current])[1]]))
        current = str(came_from[current])

    return path[::-1]

# Solve the puzzle and print the list of tiles to be swapped
solution = solve_puzzle(initial_state, goal_state)
print(solution)
