
import heapq

def generate_next_states(state):
    empty_spot = state.index('_')
    next_states = []
    row, col = empty_spot // len(state), empty_spot % len(state)
    
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < len(state) and 0 <= nc < len(state):
            new_state = list(state)
            new_state[empty_spot], new_state[nr * len(state) + nc] = new_state[nr * len(state) + nc], new_state[empty_spot]
            next_states.append((new_state, (nr, nc)))
    
    return next_states

def manhattan_distance(state):
    return sum(abs(row - tile // len(state)) + abs(col - tile % len(state)) for tile, (row, col) in enumerate(state) if tile != '_')

def a_star(start):
    queue = [(0, start, [])]
    visited = set()
    
    while queue:
        _, state, swaps = heapq.heappop(queue)
        if state not in visited:
            visited.add(state)
            if state == goal_state:
                return swaps
            
            for new_state, (row, col) in generate_next_states(state):
                new_swaps = swaps + [state[row * len(state) + col]]
                heapq.heappush(queue, (len(new_swaps) + manhattan_distance(new_state), new_state, new_swaps))

    return None

initial_state = [[95, '_', 80, 18], [67, 66, 35, 94], [27, 26, 69, 53]]
goal_state = ['_', 1, 2, 3, 4, 5, 6, 7, 8]

print(a_star(initial_state))
