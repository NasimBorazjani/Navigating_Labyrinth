
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
    visited = {tuple(start['grid'])}
    while queue:
        _, state = heapq.heappop(queue)
        if state['grid'] == [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12']]:
            return state['path']
        for next_state in generate_next_states(state):
            if tuple(next_state['grid']) not in visited:
                visited.add(tuple(next_state['grid']))
                next_state['path'] = state['path'] + [next_state['grid'][state['empty'][1]][state['empty'][0]]]
                heapq.heappush(queue, (manhattan_distance(next_state) + len(next_state['path']), next_state))

initial_state = {
    'grid': [[25, 94, 12, '_'], [70, 43, 47, 85], [86, 64, 52, 92]],
    'empty': (3, 0),
    'path': []
}

print(a_star(initial_state))
