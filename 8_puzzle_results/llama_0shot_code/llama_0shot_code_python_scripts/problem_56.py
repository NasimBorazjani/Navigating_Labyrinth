
import heapq

def generate_next_states(state):
    empty_x, empty_y = 0, 0
    for i in range(3):
        for j in range(4):
            if state[i][j] == '_':
                empty_x, empty_y = i, j
                break
        else:
            continue
        break

    next_states = []
    for i, j in [(empty_x-1, empty_y), (empty_x+1, empty_y), (empty_x, empty_y-1), (empty_x, empty_y+1)]:
        if 0 <= i < 3 and 0 <= j < 4:
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[i][j] = new_state[i][j], '_'
            next_states.append((new_state, (abs(i - empty_x) + abs(j - empty_y))))
    return next_states

def a_star(start):
    queue = [(0, 0, start)]
    visited = set()
    while queue:
        _, _, state = heapq.heappop(queue)
        if state not in visited:
            visited.add(state)
            if state == goal_state:
                return []
            for new_state, cost in generate_next_states(state):
                heapq.heappush(queue, (cost + manhattan_distance(new_state), manhattan_distance(new_state), new_state))
    return None

def manhattan_distance(state):
    return sum(abs(state[i][j] - goal_state[i][j]) for i in range(3) for j in range(4))

initial_state = [[66, 96, 24, 10], [79, 33, 84, 100], [22, 80, 15, '_']]
goal_state = [[100, 96, 84, 10], [79, 66, 33, 22], [80, 15, '_', '_']]

print(a_star(initial_state))
