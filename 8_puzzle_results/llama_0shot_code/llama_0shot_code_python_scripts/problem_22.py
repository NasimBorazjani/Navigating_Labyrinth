
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
    visited = {tuple(map(tuple, start['grid'])): 0}
    while heap:
        _, state = heapq.heappop(heap)
        if state['grid'] == [['8', '5', '_'], ['1', '6', '4'], ['7', '3', '2']]:
            return visited[tuple(map(tuple, state['grid']))]
        for next_state in generate_next_states(state):
            key = tuple(map(tuple, next_state['grid']))
            if key not in visited or visited[key] > visited[tuple(map(tuple, state['grid']))] + 1:
                visited[key] = visited[tuple(map(tuple, state['grid']))] + 1
                heapq.heappush(heap, (visited[key] + manhattan_distance(next_state), next_state))

start = {'grid': [[81, 25, '_'], [19, 56, 14], [61, 41, 39]], 'empty': (2, 0)}
print(a_star(start))
