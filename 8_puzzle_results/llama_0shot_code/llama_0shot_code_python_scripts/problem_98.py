
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
        new_empty_x, new_empty_y = empty_x + dx, empty_y + dy
        if 0 <= new_empty_x < len(state) and 0 <= new_empty_y < len(state[0]):
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[new_empty_x][new_empty_y] = new_state[new_empty_x][new_empty_y], new_state[empty_x][empty_y]
            next_states.append((new_state, new_state[new_empty_x][new_empty_y]))
    return next_states

def heuristic(state):
    return sum(abs(row - i//3 + col - j//3) for i, row in enumerate(state) for j, col in enumerate(row) if col != '_' and (row, col) != (8, 8))

def a_star(start):
    queue = [(0, 0, start, [])]
    visited = {tuple(row) for row in start}
    while queue:
        _, _, state, swaps = heapq.heappop(queue)
        if state == [[8, 7, 6, 5, 4, 3], [9, 2, 1, '_', 10, 11], [12, 13, 14, 15, 16, 17]]:
            return swaps
        for next_state, tile in generate_next_states(state):
            if tuple(next_state) not in visited:
                visited.add(tuple(next_state))
                heapq.heappush(queue, (len(swaps) + heuristic(next_state), heuristic(next_state), next_state, swaps + [tile]))

initial_state = [[8, 7, 6, 5, 4, 3], [9, 2, 1, '_', 10, 11], [12, 13, 14, 15, 16, 17]]
print(a_star(initial_state))
