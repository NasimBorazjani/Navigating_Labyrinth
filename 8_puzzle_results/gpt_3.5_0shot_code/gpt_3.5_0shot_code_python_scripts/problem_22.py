
from queue import PriorityQueue

# Define the initial state of the puzzle
initial_state = [[81, 25, '_'], [19, 56, 14], [61, 41, 39]]

# Define the goal state of the puzzle
goal_state = [[81, 56, 39], [61, 41, 25], [19, 14, '_']]

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
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == '_':
                if i > 0:
                    new_state = [row[:] for row in state]
                    new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
                    possible_moves.append((new_state, state[i-1][j]))
                if i < 2:
                    new_state = [row[:] for row in state]
                    new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
                    possible_moves.append((new_state, state[i+1][j]))
                if j > 0:
                    new_state = [row[:] for row in state]
                    new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
                    possible_moves.append((new_state, state[i][j-1]))
                if j < 2:
                    new_state = [row[:] for row in state]
                    new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
                    possible_moves.append((new_state, state[i][j+1]))
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
        explored.add(tuple(map(tuple, current_state)))

        for next_state, move in get_possible_moves(current_state):
            if tuple(map(tuple, next_state)) not in explored:
                new_path = path + [move]
                priority = len(new_path) + total_manhattan_distance(next_state)
                frontier.put((priority, next_state, new_path))

    return None

# Find the shortest list of tiles that need to be swapped with the empty spot
solution = a_star_search(initial_state, goal_state)
print(solution)