
import heapq

def generate_next_states(state):
    empty_x, empty_y = state['empty']
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    next_states = []
    for dx, dy in directions:
        x, y = empty_x + dx, empty_y + dy
        if 0 <= x < 3 and 0 <= y < 5:
            new_state = state.copy()
            new_state['empty'] = (x, y)
            new_state['grid'][empty_x][empty_y], new_state['grid'][x][y] = new_state['grid'][x][y], new_state['grid'][empty_x][empty_y]
            next_states.append(new_state)
    return next_states

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(5):
            if state['grid'][i][j] != '_' and state['grid'][i][j] != (i * 5 + j + 1):
                distance += abs(i - (state['grid'][i][j] - 1) // 5) + abs(j - (state['grid'][i][j] - 1) % 5)
    return distance

def a_star_search(start_state):
    start_state['g'] = 0
    start_state['h'] = manhattan_distance(start_state)
    start_state['f'] = start_state['g'] + start_state['h']
    queue = [start_state]
    visited = {tuple(state['grid'])}
    while queue:
        current_state = heapq.heappop(queue)
        if current_state['grid'] == goal_state['grid']:
            return current_state
        for next_state in generate_next_states(current_state):
            next_grid = tuple(next_state['grid'])
            if next_grid not in visited:
                visited.add(next_grid)
                next_state['g'] = current_state['g'] + 1
                next_state['h'] = manhattan_distance(next_state)
                next_state['f'] = next_state['g'] + next_state['h']
                heapq.heappush(queue, next_state)

def get_shortest_path(state):
    path = []
    while state['parent'] is not None:
        path.append(state['parent']['grid'][state['empty'][0]][state['empty'][1]])
        state = state['parent']
    return path[::-1]

start_state = {'grid': [[93, 83, 50, 21, 67], [59, '_', 60, 19, 8], [14, 12, 92, 54, 9]], 'empty': (1, 1)}
goal_state = {'grid': [[9, 8, 7, 6, 5], [4, '_', 3, 2, 1], [10, 11, 12, 13, 14]], 'empty': (2, 4)}

result_state = a_star_search(start_state)
result_path = get_shortest_path(result_state)

print(result_path)
