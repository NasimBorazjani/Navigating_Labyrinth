
import heapq

def generate_next_states(state):
    empty_x, empty_y = state['empty']
    next_states = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = empty_x + dx, empty_y + dy
        if 0 <= x < 3 and 0 <= y < 4:
            new_state = state.copy()
            new_state['grid'][empty_y][empty_x], new_state['grid'][y][x] = new_state['grid'][y][x], new_state['grid'][empty_y][empty_x]
            new_state['empty'] = (x, y)
            next_states.append(new_state)
    return next_states

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(4):
            if state['grid'][j][i] != '_' and state['grid'][j][i] != (i + 1) * (j + 1):
                goal_x, goal_y = divmod((i + 1) * (j + 1), 4)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

def a_star(start):
    queue = [(manhattan_distance(start), start)]
    visited = {tuple(state['grid']): state for state in generate_next_states(start)}
    while queue:
        _, state = heapq.heappop(queue)
        if state['grid'] == [['_', 8, 10, 54], [89, 77, 33, 29], [26, 44, 61, 18]]:
            return state['path']
        for next_state in generate_next_states(state):
            grid = tuple(next_state['grid'])
            if grid not in visited or visited[grid]['cost'] > next_state['cost']:
                heapq.heappush(queue, (next_state['cost'], next_state))
                visited[grid] = next_state
    return None

initial_state = {
    'grid': [[81, 10, 54, '_'], [89, 77, 33, 29], [26, 44, 61, 18]],
    'empty': (3, 0),
    'path': [],
    'cost': manhattan_distance({
        'grid': [[81, 10, 54, '_'], [89, 77, 33, 29], [26, 44, 61, 18]],
        'empty': (3, 0)
    })
}

print(a_star(initial_state))
