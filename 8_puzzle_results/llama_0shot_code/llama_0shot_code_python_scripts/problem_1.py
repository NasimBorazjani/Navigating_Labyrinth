
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
                goal_x, goal_y = divmod(state['grid'][i][j] - 1, 3)
                distance += abs(i - goal_y) + abs(j - goal_x)
    return distance

def a_star(start):
    start['cost'] = 0
    start['estimate'] = manhattan_distance(start)
    queue = [(start['cost'] + start['estimate'], start)]
    while queue:
        _, state = heapq.heappop(queue)
        if state['grid'] == goal_state['grid']:
            return state['path']
        for next_state in generate_next_states(state):
            next_state['cost'] = state['cost'] + 1
            next_state['estimate'] = manhattan_distance(next_state)
            next_state['path'] = state['path'] + [next_state['grid'][state['empty'][1]][state['empty'][0]]]
            heapq.heappush(queue, (next_state['cost'] + next_state['estimate'], next_state))

initial_state = {
    'grid': [[12, 55, '_'], [35, 97, 43], [17, 25, 9]],
    'empty': (2, 1),
}

goal_state = {
    'grid': [[8, 7, 6], [5, 4, 3], [2, 1, '_']],
    'empty': (2, 2),
}

print(a_star(initial_state))
