
import heapq

def generate_next_states(state):
    empty_spot_row, empty_spot_col = find_empty_spot(state)
    next_states = []
    for row_diff, col_diff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = empty_spot_row + row_diff, empty_spot_col + col_diff
        if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
            new_state = swap_tiles(state, empty_spot_row, empty_spot_col, new_row, new_col)
            next_states.append((new_state, (abs(new_row - empty_spot_row) + abs(new_col - empty_spot_col))))
    return next_states

def find_empty_spot(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '_':
                return i, j

def swap_tiles(state, row1, col1, row2, col2):
    state[row1][col1], state[row2][col2] = state[row2][col2], state[row1][col1]
    return state

def a_star_search(start):
    visited = set()
    queue = [(0, 0, start)]
    while queue:
        _, _, state = heapq.heappop(queue)
        if state not in visited:
            visited.add(state)
            if is_goal_state(state):
                return get_solution(state)
            for next_state, cost in generate_next_states(state):
                priority = cost + manhattan_distance(next_state)
                heapq.heappush(queue, (priority, len(visited), next_state))

def manhattan_distance(state):
    empty_spot_row, empty_spot_col = find_empty_spot(state)
    return sum(abs(empty_spot_row - i) + abs(empty_spot_col - j) for i, row in enumerate(state) for j, tile in enumerate(row) if tile != '_' and tile != i * len(state) + j)

def is_goal_state(state):
    return all(state[i][j] == (i * len(state) + j - len(state) * (len(state) - 1) // 2) if i * len(state) + j != len(state) * len(state[0]) - 1 else state[i][j] == '_' for i in range(len(state)) for j in range(len(state[0])))

def get_solution(state):
    solution = []
    while state != [[86, 78, 77, 39, 76], [54, 45, 25, 59, 21], [38, 46, 43, 27, '_']]:
        empty_spot_row, empty_spot_col = find_empty_spot(state)
        for row_diff, col_diff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = empty_spot_row + row_diff, empty_spot_col + col_diff
            if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
                state = swap_tiles(state, empty_spot_row, empty_spot_col, new_row, new_col)
                solution.append(state[new_row][new_col])
                break
    return solution[::-1]

initial_state = [[86, 78, 77, 39, 76], [54, 45, 25, 59, 21], [38, 46, 43, 27, '_']]
print(a_star_search(initial_state))
