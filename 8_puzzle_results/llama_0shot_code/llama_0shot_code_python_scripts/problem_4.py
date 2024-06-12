
import heapq

def generate_next_states(state):
    empty_x, empty_y = 0, 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == '_':
                empty_x, empty_y = i, j
                break
        else:
            continue
        break

    next_states = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            next_states.append((new_state, (abs(new_x - dx) + abs(new_y - dy))))
    return next_states

def a_star(start):
    heap = [(0, 0, start)]
    visited = set()
    while heap:
        _, _, state = heapq.heappop(heap)
        if state in visited:
            continue
        visited.add(state)
        if state == goal_state:
            return []
        for new_state, cost in generate_next_states(state):
            priority = cost + manhattan_distance(new_state)
            heapq.heappush(heap, (priority, cost, new_state))
    return None

def manhattan_distance(state):
    return sum(abs(state[i][j] - goal_state[i][j]) for i in range(3) for j in range(3) if state[i][j] != '_')

initial_state = [[66, 89, 70], [25, 42, 83], ['_', 24, 71]]
goal_state = [[8, 7, 6], [5, 4, 3], [2, 1, '_']]

print(a_star(initial_state))
