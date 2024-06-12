
import heapq
import copy

# Define the initial state and the goal state
initial_state = [[42, 89, 21, 58, 67], [54, 32, 99, 69, 38], [77, 33, '_', 39, 16]]
goal_state = [[99, 89, 77, 67, 58], [54, 42, 39, 38, 33], [32, 21, 16, '_', '_']]

# Define the possible moves
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Find the position of the empty spot
def find_empty(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '_':
                return (i, j)

# Check if a move is valid
def valid_move(state, move):
    empty = find_empty(state)
    new_pos = (empty[0] + move[0], empty[1] + move[1])
    return 0 <= new_pos[0] < len(state) and 0 <= new_pos[1] < len(state[0])

# Apply a move
def apply_move(state, move):
    empty = find_empty(state)
    new_pos = (empty[0] + move[0], empty[1] + move[1])
    new_state = copy.deepcopy(state)
    new_state[empty[0]][empty[1]], new_state[new_pos[0]][new_pos[1]] = new_state[new_pos[0]][new_pos[1]], new_state[empty[0]][empty[1]]
    return new_state

# Calculate the Manhattan distance
def manhattan_distance(state):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != '_':
                goal_pos = [(index, row.index(state[i][j])) for index, row in enumerate(goal_state) if state[i][j] in row][0]
                distance += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return distance

# A* search algorithm
def a_star_search():
    heap = [(manhattan_distance(initial_state), initial_state)]
    while heap:
        (cost, state) = heapq.heappop(heap)
        if state == goal_state:
            return state
        for move in moves:
            if valid_move(state, move):
                new_state = apply_move(state, move)
                new_cost = cost - manhattan_distance(state) + manhattan_distance(new_state)
                heapq.heappush(heap, (new_cost, new_state))

# Print the solution
print(a_star_search())
