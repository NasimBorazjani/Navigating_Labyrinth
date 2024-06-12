
import heapq

def generate_next_states(state):
    empty_x, empty_y = state['empty']
    next_states = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = empty_x + dx, empty_y + dy
        if 0 <= x < 3 and 0 <= y < 5:
            new_state = state.copy()
            new_state['grid'][empty_y][empty_x], new_state['grid'][y][x] = new_state['grid'][y][x], new_state['grid'][empty_y][empty_x]
            new_state['empty'] = (x, y)
            next_states.append(new_state)
    return next_states

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(5):
            if state['grid'][j][i] != '_' and state['grid'][j][i] != i * 3 + j + 1:
                x, y = divmod(state['grid'][j][i] - 1, 3)
                distance += abs(i - x) + abs(j - y)
    return distance

def a_star(start):
    queue = [(manhattan_distance(start), start)]
    visited = {tuple(row) for row in start['grid']}
    while queue:
        _, state = heapq.heappop(queue)
        if state['grid'] == [['8', '5', '7', '6', '_'], ['4', '1', '6', '3', '2'], ['3', '15', '4', '13', '8']]:
            return state['path']
        for next_state in generate_next_states(state):
            if tuple(row) not in visited:
                visited.add(tuple(row) for row in next_state['grid'])
                heapq.heappush(queue, (manhattan_distance(next_state) + len(next_state['path']), next_state))
    return None

initial_state = {
    'grid': [['8', '7', '7', '8', '_'], ['5', '1', '6', '3', '7'], ['2', '15', '4', '13', '8']],
    'empty': (3, 0),
    'path': []
}

print(a_star(initial_state))
