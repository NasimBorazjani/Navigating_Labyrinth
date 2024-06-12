
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
                x, y = divmod(state['grid'][i][j]-1, 3)
                distance += abs(i - x) + abs(j - y)
    return distance

def a_star(start):
    heap = [(manhattan_distance(start), start)]
    visited = set()
    while heap:
        _, state = heapq.heappop(heap)
        if state not in visited:
            visited.add(state)
            if state['grid'] == goal_state['grid']:
                return state
            for next_state in generate_next_states(state):
                heapq.heappush(heap, (manhattan_distance(next_state), next_state))
    return None

start_state = {'grid': [[30, 12, 67], [21, '_', 28], [80, 16, 37]], 'empty': (1, 1)}
goal_state = {'grid': [[80, 30, 67], [21, 12, 28], [16, '_', 37]], 'empty': (2, 2)}

state = a_star(start_state)
result = []
while state['parent'] is not None:
    result.append(state['grid'][state['empty'][0]][state['empty'][1]])
    state = state['parent']
result.reverse()
print(result)
