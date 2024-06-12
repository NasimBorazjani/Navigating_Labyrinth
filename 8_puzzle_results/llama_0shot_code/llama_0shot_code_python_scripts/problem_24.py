
import heapq

def generate_next_states(state):
    empty_x, empty_y = find_empty(state)
    next_states = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = empty_x + dx, empty_y + dy
        if 0 <= x < 3 and 0 <= y < 3:
            new_state = swap(state, empty_x, empty_y, x, y)
            next_states.append((new_state, (abs(dx), abs(dy))))
    return next_states

def find_empty(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == '_':
                return i, j

def swap(state, x1, y1, x2, y2):
    new_state = [row.copy() for row in state]
    new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
    return new_state

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != '_':
                goal_x, goal_y = divmod(state[i][j]-1, 3)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def a_star(start):
    queue = [(manhattan_distance(start), start, [])]
    visited = set()
    while queue:
        _, state, swaps = heapq.heappop(queue)
        if tuple(tuple(row) for row in state) not in visited:
            visited.add(tuple(tuple(row) for row in state))
            if state == goal_state:
                return swaps
            for new_state, (dx, dy) in generate_next_states(state):
                heapq.heappush(queue, (manhattan_distance(new_state) + len(swaps) + dx + dy, new_state, swaps + [state[1][2]]))

start_state = [[35, 92, '_'], [32, 44, 94], [97, 75, 58]]
goal_state = [[8, 7, 6], [5, 4, 3], [2, 1, '_']]

print(a_star(start_state))
