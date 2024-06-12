
import heapq

def generate_next_states(state):
    empty_spot = state.index('_')
    next_states = []
    if empty_spot % 4 != 0:  # not at the left edge
        next_state = list(state)
        next_state[empty_spot], next_state[empty_spot - 1] = next_state[empty_spot - 1], next_state[empty_spot]
        next_states.append(tuple(next_state))
    if empty_spot % 4 != 3:  # not at the right edge
        next_state = list(state)
        next_state[empty_spot], next_state[empty_spot + 1] = next_state[empty_spot + 1], next_state[empty_spot]
        next_states.append(tuple(next_state))
    if empty_spot > 3:  # not at the top row
        next_state = list(state)
        next_state[empty_spot], next_state[empty_spot - 4] = next_state[empty_spot - 4], next_state[empty_spot]
        next_states.append(tuple(next_state))
    if empty_spot < 12:  # not at the bottom row
        next_state = list(state)
        next_state[empty_spot], next_state[empty_spot + 4] = next_state[empty_spot + 4], next_state[empty_spot]
        next_states.append(tuple(next_state))
    return next_states

def manhattan_distance(state):
    return sum(abs(state.index('_') // 4 - i // 4) + abs(state.index('_') % 4 - i % 4) for i, v in enumerate(state) if v != '_')

def a_star(start):
    queue = [(manhattan_distance(start), start, [])]
    visited = set()
    while queue:
        _, state, swaps = heapq.heappop(queue)
        if tuple(state) not in visited:
            visited.add(tuple(state))
            if state == ['_', 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 21, 22, 23, 27, 54, 58, 81, 85, 100]:
                return swaps
            for next_state in generate_next_states(state):
                heapq.heappush(queue, (manhattan_distance(next_state) + len(swaps) + 1, next_state, swaps + [next_state[state.index('_')]]))

initial_state = [81, '_', 58, 10], [85, 22, 23, 54], [100, 21, 27, 12]
flattened_initial_state = [item for sublist in initial_state for item in sublist]
print(a_star(flattened_initial_state))
