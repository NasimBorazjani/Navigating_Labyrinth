
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
            if state['grid'][i][j] != '_' and state['grid'][i][j] != 'goal':
                goal_x, goal_y = divmod(state['grid'][i][j] - 1, 4)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def a_star(start):
    start['goal'] = manhattan_distance(start)
    queue = [(start['goal'], start)]
    seen = set()
    while queue:
        _, state = heapq.heappop(queue)
        if state not in seen:
            seen.add(state)
            if state['goal'] == 0:
                return state
            next_states = generate_next_states(state)
            for next_state in next_states:
                next_state['goal'] = manhattan_distance(next_state)
                next_state['cost'] = state['cost'] + 1
                heapq.heappush(queue, (next_state['goal'] + next_state['cost'], next_state))
    return None

def solve_8_puzzle(grid):
    start = {
        'grid': grid,
        'empty': (1, 3),
        'cost': 0,
        'goal': None
    }
    solution = a_star(start)
    return [solution['grid'][state['empty'][1]][state['empty'][0]] for state in reversed(solution['path'])]

grid = [['52', '_', '99', '42'], ['56', '67', '49', '68'], ['88', '23', '33', '26']]
print(solve_8_puzzle(grid))
