
from queue import PriorityQueue

# Define the initial state of the puzzle
initial_state = [[88, 52, 85], [98, 96, 83], [50, 80, '_']]
goal_state = [[98, 96, 88], [85, 83, 80], [52, 50, '_']]

# Define a function to calculate the Manhattan distance between two points
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Define a function to find the empty spot in the puzzle
def find_empty_spot(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == '_':
                return (i, j)

# Define a function to generate possible moves from a given state
def generate_moves(state):
    moves = []
    empty_spot = find_empty_spot(state)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for d in directions:
        new_spot = (empty_spot[0] + d[0], empty_spot[1] + d[1])
        if 0 <= new_spot[0] < 3 and 0 <= new_spot[1] < 3:
            new_state = [row.copy() for row in state]
            new_state[empty_spot[0]][empty_spot[1]] = new_state[new_spot[0]][new_spot[1]]
            new_state[new_spot[0]][new_spot[1]] = '_'
            moves.append((new_state, state[empty_spot[0]][empty_spot[1]]))
    
    return moves

# Define a function to solve the puzzle using A* search algorithm
def solve_puzzle(initial_state, goal_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state, []))
    visited = set()
    
    while not frontier.empty():
        cost, current_state, path = frontier.get()
        
        if current_state == goal_state:
            return path
        
        visited.add(str(current_state))
        
        for next_state, move in generate_moves(current_state):
            if str(next_state) not in visited:
                new_cost = cost + 1 + manhattan_distance(find_empty_spot(next_state), (2, 2))
                frontier.put((new_cost, next_state, path + [move]))
    
    return None

# Solve the puzzle
solution = solve_puzzle(initial_state, goal_state)
print(solution)
