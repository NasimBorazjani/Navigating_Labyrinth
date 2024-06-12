
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

def manhattan_distance(state):
    return sum(abs(row - (i // len(state[0]))) + abs(col - (i % len(state[0]))) for i, row, col in ((i, x, y) for row in state for i, x in enumerate(row) for y in range(len(state[0])) if x != '_'))

def a_star(start):
    queue = [(0, 0, start, [])]
    visited = {tuple(row) for row in start}
    while queue:
        _, cost, state, swaps = heapq.heappop(queue)
        if state == [['_', 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]:
            return swaps
        for next_state, tile in generate_next_states(state):
            if tuple(next_state) not in visited:
                visited.add(tuple(next_state))
                heapq.heappush(queue, (cost + 1 + manhattan_distance(next_state), cost + 1 + manhattan_distance(next_state), next_state, swaps + [tile]))

initial_state = [['_', 98, 74, 70, 26], [65, 91, 55, 12, 68], [27, 18, 67, 40, 54]]
print(a_star(initial_state))
