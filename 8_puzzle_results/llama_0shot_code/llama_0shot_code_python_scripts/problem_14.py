
import heapq

def generate_next_states(state):
    empty_x, empty_y = state['empty']
    next_states = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = empty_x + dx, empty_y + dy
        if 0 <= x < 3 and 0 <= y < 3:
            new_state = state.copy()
            new_state['grid'][empty_y][empty_x], new_state['grid'][y][x] = new_state['grid'][y][x], new_state['grid'][empty_y][empty_x]
            new_state['empty'] = (x, y)
            next_states.append(new_state)
    return next_states

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state['grid'][i][j] != '_':
                x, y = divmod(state['grid'][i][j] - 1, 3)
                distance += abs(i - x) + abs(j - y)
    return distance

def a_star(start):
    heap = [(manhattan_distance(start), start)]
    visited = {tuple(row) for row in start['grid']}
    while heap:
        _, state = heapq.heappop(heap)
        if state['grid'] == [['8', '7', '6'], ['5', '4', '3'], ['2', '1', '_']]:
            return [state['grid'][1][1]]
        for next_state in generate_next_states(state):
            if tuple(next_state['grid']) not in visited:
                visited.add(tuple(row) for row in next_state['grid'])
                heapq.heappush(heap, (manhattan_distance(next_state) + len(next_state['sequence']), next_state))
    return []

initial_state = {
    'grid': [[28, 51, 19], [89, '_', 21], [43, 39, 45]],
    'empty': (1, 1),
    'sequence': [89]
}

print(a_star(initial_state))
