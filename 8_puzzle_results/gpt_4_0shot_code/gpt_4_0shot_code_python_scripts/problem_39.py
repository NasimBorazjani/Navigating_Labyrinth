
import heapq
import copy

# Define the initial state and the goal state
initial_state = [[30, 39, 59, 78], [100, 57, 55, 48], [82, '_', 15, 88]]
goal_state = [[100, 88, 82, 78], [59, 57, 55, 48], [39, 30, 15, '_']]

# Define the moves: up, down, left, right
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

# A* search algorithm
def a_star_search(initial_state, goal_state):
    heap = [(0, initial_state, [])]
    while heap:
        (cost, current_state, path) = heapq.heappop(heap)
        if current_state == goal_state:
            return path
        for move in moves:
            if valid_move(current_state, move):
                new_state = apply_move(current_state, move)
                new_cost = cost + 1 + sum(abs(b - a) for a, b in zip(find_empty(new_state), find_empty(goal_state)))
                new_path = path + [new_state[find_empty(new_state)[0]][find_empty(new_state)[1]]]
                heapq.heappush(heap, (new_cost, new_state, new_path))

# Print the solution
print(a_star_search(initial_state, goal_state))
