
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
    return sum(abs(row - (i // len(state[0]))) + abs(col - (i % len(state[0]))) for i, (row, col) in enumerate(positions))

def a_star(start):
    queue = [(0, 0, start, [])]
    visited = {tuple(row) for row in start}
    while queue:
        _, cost, state, swaps = heapq.heappop(queue)
        if state == goal:
            return swaps
        for new_state, (dx, dy) in generate_next_states(state):
            new_cost = cost + 1 + heuristic(new_state)
            if tuple(new_state) not in visited:
                visited.add(tuple(new_state))
                heapq.heappush(queue, (new_cost, cost + 1 + dx + dy, new_state, swaps + [new_state[-1][-1]]))

positions = [(i // len(start[0]), i % len(start[0])) for i, _ in enumerate(start)]
goal = [[str(9 - i) if str(9 - i) != '_' else '_' for i in range(9)] for _ in range(3)]
start = [[str(i) if str(i) != '9' else '_' for i in row] for row in [[91, 86, 16, 48, 81], [13, 89, 5, '_', 58], [54, 22, 36, 37, 31]]]

print(a_star(start))
