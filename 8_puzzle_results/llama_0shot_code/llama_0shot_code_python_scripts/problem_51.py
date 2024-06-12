
import heapq

def generate_next_states(state):
    empty_x, empty_y = find_empty(state)
    next_states = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = empty_x + dx, empty_y + dy
        if 0 <= x < 3 and 0 <= y < 4:
            new_state = swap(state, empty_x, empty_y, x, y)
            next_states.append((new_state, (abs(9 - new_state[0][0]) + abs(9 - new_state[1][0]) + abs(9 - new_state[1][1]) + abs(9 - new_state[1][2]) + abs(9 - new_state[1][3]) + abs(9 - new_state[2][0]) + abs(9 - new_state[2][1]) + abs(9 - new_state[2][2]) + abs(9 - new_state[2][3]))))
    return next_states

def find_empty(state):
    for i in range(3):
        for j in range(4):
            if state[i][j] == '_':
                return i, j

def swap(state, x1, y1, x2, y2):
    state[x1][y1], state[x2][y2] = state[x2][y2], state[x1][y1]
    return state

def a_star(start):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        _, state, path = heapq.heappop(queue)
        if state not in visited:
            visited.add(state)
            if is_goal(state):
                return path
            for next_state, cost in generate_next_states(state):
                heapq.heappush(queue, (cost, next_state, path + [next_state[1][1]]))

def is_goal(state):
    return state == [
        [9, 8, 7, 6],
        [5, 4, 3, 2],
        [1, 10, 11, 12]
    ]

initial_state = [
    [96, 53, 19, 15],
    [37, 32, '_', 87],
    [78, 100, 17, 13]
]

print(a_star(initial_state))
