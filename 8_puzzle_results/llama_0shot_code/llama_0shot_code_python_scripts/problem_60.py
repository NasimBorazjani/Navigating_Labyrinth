
import heapq

def generate_next_states(state):
    empty_row, empty_col = find_empty(state)
    next_states = []
    for row, col in [(empty_row-1, empty_col), (empty_row+1, empty_col), (empty_row, empty_col-1), (empty_row, empty_col+1)]:
        if 0 <= row < len(state) and 0 <= col < len(state[0]):
            new_state = swap(state, empty_row, empty_col, row, col)
            next_states.append((new_state, state[row][col]))
    return next_states

def find_empty(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '_':
                return i, j

def swap(state, row1, col1, row2, col2):
    new_state = [list(row) for row in state]
    new_state[row1][col1], new_state[row2][col2] = new_state[row2][col2], new_state[row1][col1]
    return new_state

def manhattan_distance(state):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != '_':
                goal_i, goal_j = divmod(int(state[i][j])-1, len(state[0]))
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def a_star(start):
    queue = [(manhattan_distance(start), start, [])]
    visited = set()
    while queue:
        _, state, swaps = heapq.heappop(queue)
        if state not in visited:
            visited.add(state)
            if is_goal(state):
                return swaps
            for next_state, tile in generate_next_states(state):
                heapq.heappush(queue, (manhattan_distance(next_state) + len(swaps) + 1, next_state, swaps + [tile]))

def is_goal(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != '_' and state[i][j] != str(i*len(state[0]) + j + 1):
                return False
    return True

initial_state = [[31, 92, 67, 69], [87, 35, 42, 72], [53, '_', 28, 19]]
print(a_star(initial_state))
