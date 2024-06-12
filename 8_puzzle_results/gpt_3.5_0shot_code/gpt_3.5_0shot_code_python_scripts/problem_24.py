
from queue import PriorityQueue

# Define the initial state of the puzzle
initial_state = [[35, 92, '_'], [32, 44, 94], [97, 75, 58]]

# Define the goal state of the puzzle
goal_state = [[94, 92, 97], [75, 58, 44], [35, 32, '_']]

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
                goal_position = {(tile-1)//3, (tile-1)%3}
                total_distance += manhattan_distance((i, j), goal_position)
    return total_distance

# Define a function to get the possible moves from a given state
def get_possible_moves(state):
    possible_moves = []
    empty_position = None
    for i in range(3):
        for j in range(3):
            if state[i][j] == '_':
                empty_position = (i, j)
                break
    if empty_position[0] > 0:
        possible_moves.append((empty_position, (empty_position[0]-1, empty_position[1])))
    if empty_position[0] < 2:
        possible_moves.append((empty_position, (empty_position[0]+1, empty_position[1])))
    if empty_position[1] > 0:
        possible_moves.append((empty_position, (empty_position[0], empty_position[1]-1)))
    if empty_position[1] < 2:
        possible_moves.append((empty_position, (empty_position[0], empty_position[1]+1)))
    return possible_moves

# Define the A* search algorithm to find the shortest path to the goal state
def a_star_search(initial_state, goal_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state, []))
    explored = set()
    
    while not frontier.empty():
        current_cost, current_state, current_path = frontier.get()
        
        if current_state == goal_state:
            return current_path
        
        if str(current_state) in explored:
            continue
        
        explored.add(str(current_state))
        
        for move in get_possible_moves(current_state):
            new_state = [row.copy() for row in current_state]
            new_state[move[0][0]][move[0][1]], new_state[move[1][0]][move[1][1]] = new_state[move[1][0]][move[1][1]], new_state[move[0][0]][move[0][1]]
            new_cost = total_manhattan_distance(new_state)
            new_path = current_path + [new_state[move[1][0]][move[1][1]]]
            frontier.put((new_cost, new_state, new_path))
    
    return None

# Find the shortest list of tiles that need to be swapped with the empty spot to achieve the goal state
solution = a_star_search(initial_state, goal_state)
print(solution)
