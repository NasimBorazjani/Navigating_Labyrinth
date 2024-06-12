
import heapq

def generate_next_states(state):
    empty_x, empty_y = 0, 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '_':
                empty_x, empty_y = i, j
                break
        else:
            continue
        break

    next_states = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < len(state) and 0 <= new_y < len(state[0]):
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            next_states.append((new_state, (abs(new_x - empty_x), abs(new_y - empty_y))))
    return next_states

def manhattan_distance(state):
    return sum(abs(state[i][j] - (i * len(state[0]) + j + 1)) for i in range(len(state)) for j in range(len(state[0])) if state[i][j] != '_')

def a_star(start):
    queue = [(0, 0, start, [])]
    visited = {tuple(row) for row in start}
    while queue:
        _, _, state, swaps = heapq.heappop(queue)
        if state == [['_', 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]:
            return swaps

        for new_state, (dx, dy) in generate_next_states(state):
            if tuple(new_state) not in visited:
                visited.add(tuple(new_state))
                heapq.heappush(queue, (len(swaps) + dx + dy + manhattan_distance(new_state), manhattan_distance(new_state), new_state, swaps + [new_state[1][1]]))

initial_state = [['_', 92, 75, 100, 61, 43, 87], [64, 34, 55, 90, 20, 86], [36, 32, 5, 42, 83]]
print(a_star(initial_state))
