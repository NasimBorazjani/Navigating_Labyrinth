
from queue import PriorityQueue

# Define the initial state of the puzzle
initial_state = [[99, 69, 19], [53, '_', 30], [100, 63, 40]]

# Define the goal state of the puzzle
goal_state = [[100, 99, 69], [63, 53, 40], [30, 19, '_']]

# Define a function to calculate the Manhattan distance between two tiles
def manhattan_distance(tile1, tile2):
    x1, y1 = tile1
    x2, y2 = tile2
    return abs(x1 - x2) + abs(y1 - y2)

# Define a function to calculate the total Manhattan distance of the puzzle state
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
    empty_tile = None
    for i in range(3):
        for j in range(3):
            if state[i][j] == '_':
                empty_tile = (i, j)
                break
    if empty_tile[0] > 0:
        moves.append((empty_tile, (empty_tile[0] - 1, empty_tile[1])))
    if empty_tile[0] < 2:
        moves.append((empty_tile, (empty_tile[0] + 1, empty_tile[1])))
    if empty_tile[1] > 0:
        moves.append((empty_tile, (empty_tile[0], empty_tile[1] - 1)))
    if empty_tile[1] < 2:
        moves.append((empty_tile, (empty_tile[0], empty_tile[1] + 1)))
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
            (x1, y1), (x2, y2) = move
            new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
            
            if str(new_state) not in explored:
                new_path = path.copy()
                new_path.append(new_state[x2][y2])
                frontier.put((total_manhattan_distance(new_state), new_state, new_path))

# Find the shortest path to the goal state
shortest_path = a_star_search(initial_state, goal_state)
print(shortest_path)
