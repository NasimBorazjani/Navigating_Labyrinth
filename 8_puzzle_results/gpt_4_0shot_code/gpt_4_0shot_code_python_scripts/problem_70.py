
import heapq
import copy

# Define the initial state and goal state
initial_state = [[86, 100, 92, 37, 95], [88, '_', 97, 10, 67], [32, 82, 19, 53, 4]]
goal_state = [[100, 97, 95, 92, 86], [88, 82, 67, 53, 37], [32, 19, 10, 4, '_']]

# Define the possible moves
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Function to find the position of the empty spot
def find_empty(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '_':
                return (i, j)

# Function to generate the successors of a state
def generate_successors(state):
    successors = []
    i, j = find_empty(state)
    for move in moves:
        ni, nj = i + move[0], j + move[1]
        if 0 <= ni < len(state) and 0 <= nj < len(state[i]):
            successor = copy.deepcopy(state)
            successor[i][j], successor[ni][nj] = successor[ni][nj], successor[i][j]
            successors.append((successor, successor[ni][nj]))
    return successors

# Function to calculate the heuristic of a state
def heuristic(state):
    return sum(abs(i - j) for row_s, row_g in zip(state, goal_state) for i, j in zip(row_s, row_g) if i != '_')

# A* search algorithm
def astar():
    heap = [(heuristic(initial_state), initial_state, [])]
    while heap:
        h, state, path = heapq.heappop(heap)
        if state == goal_state:
            return path
        for successor, tile in generate_successors(state):
            if tile not in path:
                heapq.heappush(heap, (heuristic(successor) + len(path), successor, path + [tile]))

# Print the solution
print(astar())
