
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
            next_states.append((new_state, (abs(new_empty_x - dx), abs(new_empty_y - dy))))
    return next_states

def heuristic(state):
    return sum(abs(row - (i // len(state[0]))) + abs(col - (i % len(state[0]))) for i, (row, col) in enumerate(pos for sublist in state for pos in sublist if pos != '_'))

def a_star(start):
    queue = [(0, 0, start, [])]
    visited = {tuple(row) for row in start}
    while queue:
        _, cost, state, swaps = heapq.heappop(queue)
        if state == [['_', 8, 7, 6, 5], [4, 3, 2, 1, 10], [11, 12, 13, 14, 15]]:
            return swaps
        for new_state, (dx, dy) in generate_next_states(state):
            if tuple(new_state) not in visited:
                visited.add(tuple(new_state))
                heapq.heappush(queue, (cost + 1 + heuristic(new_state), cost + 1 + heuristic(new_state), new_state, swaps + [new_state[dx][dy]]))

initial_state = [['_', 67, 21, 97, 69], [61, 68, 55, 16, 73], [42, 41, 31, 83, 53]]
print(a_star(initial_state))
