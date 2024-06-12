
import heapq

def generate_next_states(state):
    empty_row, empty_col = find_empty(state)
    next_states = []
    for row, col in [(empty_row-1, empty_col), (empty_row+1, empty_col), (empty_row, empty_col-1), (empty_row, empty_col+1)]:
        if 0 <= row < len(state) and 0 <= col < len(state[0]):
            new_state = swap(state, empty_row, empty_col, row, col)
            next_states.append((new_state, (row, col)))
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
    queue = [(0, start, [])]
    visited = set()
    while queue:
        _, state, swaps = heapq.heappop(queue)
        if tuple(state) not in visited:
            visited.add(tuple(state))
            if state == goal_state:
                return swaps
            for new_state, (empty_row, empty_col) in generate_next_states(state):
                heapq.heappush(queue, (manhattan_distance(new_state) + len(swaps) + 1, new_state, swaps + [state[empty_row][empty_col]]))

initial_state = [[94, 87, 69, 81, 4, 79], ['_', 35, 86, 61, 57, 75], [41, 18, 65, 9, 53, 55]]
goal_state = [[95, 84, 73, 62, 50, 38], [36, 25, 17, 8, 1, 56], [42, 19, 66, 10, 51, 54]]

print(a_star(initial_state))
