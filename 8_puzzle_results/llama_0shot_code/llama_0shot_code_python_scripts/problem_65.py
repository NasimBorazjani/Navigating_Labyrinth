
from collections import deque

# Define the initial state and the goal state
initial_state = [[94, 93, 84, 27, 6], [55, 18, 91, 82, 8], [19, 32, 37, 30, '_']]
goal_state = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, '_']]

# Function to check if the puzzle is in the goal state
def is_goal_state(puzzle):
    return puzzle == goal_state

# Function to find the empty spot
def find_empty_spot(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == '_':
                return (i, j)

# Function to create a new state
def create_new_state(puzzle, empty_spot, direction):
    new_puzzle = [row.copy() for row in puzzle]
    if direction == 'up':
        new_puzzle[empty_spot[0]][empty_spot[1]], new_puzzle[empty_spot[0] - 1][empty_spot[1]] = new_puzzle[empty_spot[0] - 1][empty_spot[1]], new_puzzle[empty_spot[0]][empty_spot[1]]
        return (new_puzzle, (empty_spot[0] - 1, empty_spot[1]))
    elif direction == 'down':
        new_puzzle[empty_spot[0]][empty_spot[1]], new_puzzle[empty_spot[0] + 1][empty_spot[1]] = new_puzzle[empty_spot[0] + 1][empty_spot[1]], new_puzzle[empty_spot[0]][empty_spot[1]]
        return (new_puzzle, (empty_spot[0] + 1, empty_spot[1]))
    elif direction == 'left':
        new_puzzle[empty_spot[0]][empty_spot[1]], new_puzzle[empty_spot[0]][empty_spot[1] - 1] = new_puzzle[empty_spot[0]][empty_spot[1] - 1], new_puzzle[empty_spot[0]][empty_spot[1]]
        return (new_puzzle, (empty_spot[0], empty_spot[1] - 1))
    elif direction == 'right':
        new_puzzle[empty_spot[0]][empty_spot[1]], new_puzzle[empty_spot[0]][empty_spot[1] + 1] = new_puzzle[empty_spot[0]][empty_spot[1] + 1], new_puzzle[empty_spot[0]][empty_spot[1]]
        return (new_puzzle, (empty_spot[0], empty_spot[1] + 1))

# Function to solve the puzzle
def solve_puzzle(puzzle):
    visited = set()
    queue = deque([(puzzle, None)])
    while queue:
        current_puzzle, parent = queue.popleft()
        if current_puzzle not in visited:
            visited.add(current_puzzle)
            empty_spot = find_empty_spot(current_puzzle)
            if is_goal_state(current_puzzle):
                return parent
            for direction in ['up', 'down', 'left', 'right']:
                new_puzzle, new_empty_spot = create_new_state(current_puzzle, empty_spot, direction)
                if new_puzzle not in visited:
                    queue.append((new_puzzle, current_puzzle))
    return None

# Function to create the list of numbers
def create_number_list(parent):
    number_list = []
    while parent is not None:
        number_list.append(parent[1][1][1])
        parent = solve_puzzle(parent[0])
    return number_list[::-1]

# Print the list of numbers
print(create_number_list(solve_puzzle(initial_state)))
