
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
            if state['grid'][i][j] != '_' and state['grid'][i][j] != (i * 3 + j + 1):
                distance += abs(i - (state['grid'][i][j] - 1) // 3) + abs(j - (state['grid'][i][j] - 1) % 3)
    return distance

def a_star(start):
    queue = [(manhattan_distance(start), start)]
    visited = {tuple(row) for row in start['grid']}
    while queue:
        _, state = heapq.heappop(queue)
        if state['grid'] == [['8', '7', '6'], ['5', '4', '3'], ['2', '1', '_']]:
            return [state['grid'][1][1]]
        for next_state in generate_next_states(state):
            if tuple(next_state['grid'][i]) not in visited:
                visited.add(tuple(next_state['grid'][i]))
                heapq.heappush(queue, (manhattan_distance(next_state) + len(next_state['sequence']), next_state))

initial_state = {
    'grid': [['78', '98', '89'], ['38', '_', '7'], ['58', '95', '70']],
    'empty': (1, 1)
}

print(a_star(initial_state))
