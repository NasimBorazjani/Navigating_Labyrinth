
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
    return sum(abs(state.index(i) // 5 - i // 10) + abs(state.index(i) % 5 - i % 10) for i in '12345678_')

def a_star(start):
    queue = [(0, start, [])]
    visited = {str(start): 0}
    while queue:
        _, state, swaps = heapq.heappop(queue)
        if state == [['_', '8', '7', '6', '5'], ['4', '3', '2', '1', '16'], ['15', '14', '13', '12', '11']]:
            return swaps

        for new_state, tile in generate_next_states(state):
            new_state_str = str(new_state)
            if new_state_str not in visited or visited[new_state_str] > len(swaps) + 1 + manhattan_distance(new_state):
                heapq.heappush(queue, (len(swaps) + 1 + manhattan_distance(new_state), new_state, swaps + [tile]))
                visited[new_state_str] = len(swaps) + 1 + manhattan_distance(new_state)

initial_state = [['79', '82', '80', '67', '45'], ['51', '_', '63', '41', '5'], ['39', '99', '31', '16', '50']]
print(a_star(initial_state))
