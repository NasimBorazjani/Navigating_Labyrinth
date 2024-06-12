
import heapq

def generate_next_states(state):
    empty_row, empty_col = find_empty(state)
    next_states = []
    for row_offset, col_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = empty_row + row_offset, empty_col + col_offset
        if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
            new_state = swap(state, empty_row, empty_col, new_row, new_col)
            next_states.append((new_state, (new_state, (empty_row, empty_col), (new_row, new_col))))
    return next_states

def find_empty(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '_':
                return i, j

def swap(state, row1, col1, row2, col2):
    state[row1][col1], state[row2][col2] = state[row2][col2], state[row1][col1]
    return state

def manhattan_distance(state):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != '_':
                num, goal_row, goal_col = state[i][j], i, j
                distance += abs(goal_row - (num - 1) // len(state)) + abs(goal_col - (num - 1) % len(state[0]))
    return distance

def a_star(start):
    queue = [(manhattan_distance(start), 0, start, [])]
    visited = set()
    while queue:
        _, cost, state, swapped = heapq.heappop(queue)
        if state not in visited:
            visited.add(state)
            if is_goal(state):
                return swapped
            for next_state, (_, _, _, swap) in generate_next_states(state):
                heapq.heappush(queue, (manhattan_distance(next_state) + cost + 1, cost + 1, next_state, swapped + swap))

def is_goal(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != '_' and state[i][j] != i * len(state) + j + 1:
                return False
    return True

initial_state = [[28, 11, 50, 15], [94, 93, '_', 26], [34, 7, 3, 82]]
print(a_star(initial_state))
