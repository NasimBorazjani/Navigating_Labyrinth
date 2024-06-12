
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
            next_states.append((new_state, new_state[new_x][new_y]))
    return next_states

def manhattan_distance(state):
    return sum(abs(row - i//len(state[0])) + abs(col - j%len(state[0]))
               for i, row in enumerate(state)
               for j, col in enumerate(row)
               if col != '_' and (row, col) != (i//len(state[0]), j%len(state[0])))

def a_star(start):
    queue = [(0, 0, start, [])]
    visited = {tuple(row) for row in start}
    while queue:
        _, cost, state, swaps = heapq.heappop(queue)
        if state == [['_', '8', '67', '69'], ['15', '24', '30', '44'], ['47', '56', '63', '73']]:
            return swaps[::-1]
        for next_state, tile in generate_next_states(state):
            if tuple(next_state) not in visited:
                visited.add(tuple(next_state))
                heapq.heappush(queue, (cost + 1 + manhattan_distance(next_state), manhattan_distance(next_state), next_state, swaps + [tile]))

initial_state = [['69', '56', '8', '67'], ['15', '47', '44', '30'], ['73', '_', '24', '63']]
print(a_star(initial_state))
