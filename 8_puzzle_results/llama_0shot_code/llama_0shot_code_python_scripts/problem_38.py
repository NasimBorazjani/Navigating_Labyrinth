
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
    for i, j in [(empty_x - 1, empty_y), (empty_x + 1, empty_y), (empty_x, empty_y - 1), (empty_x, empty_y + 1)]:
        if 0 <= i < 2 and 0 <= j < 4:
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[i][j] = new_state[i][j], '_'
            next_states.append((new_state, (abs(i - empty_x) + abs(j - empty_y))))
    return next_states

def manhattan_distance(state):
    return sum(abs(row - i) + abs(col - (j + row % 2 * 2)) for i, row in enumerate(state) for j, col in enumerate(row) if col != '_' and col != 0)

def a_star(start):
    queue = [(0, 0, start, [])]
    visited = {tuple(row) for row in start}
    while queue:
        _, _, state, swaps = heapq.heappop(queue)
        if state == [['_', 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]:
            return swaps
        for next_state, cost in generate_next_states(state):
            if tuple(next_state) not in visited:
                visited.add(tuple(next_state))
                heapq.heappush(queue, (cost + manhattan_distance(next_state), manhattan_distance(next_state), next_state, swaps + [next_state[1][2]]))

initial_state = [['_', 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
print(a_star(initial_state))
