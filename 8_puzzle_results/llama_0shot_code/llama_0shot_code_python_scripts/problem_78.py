
import heapq

def generate_next_states(state):
    empty_x, empty_y = state['empty']
    next_states = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = empty_x + dx, empty_y + dy
        if 0 <= x < 3 and 0 <= y < 5:
            new_state = state.copy()
            new_state['grid'][empty_x][empty_y], new_state['grid'][x][y] = new_state['grid'][x][y], new_state['grid'][empty_x][empty_y]
            new_state['empty'] = (x, y)
            next_states.append(new_state)
    return next_states

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(5):
            if state['grid'][i][j] != '_' and state['grid'][i][j] != 'goal':
                goal_x, goal_y = divmod(state['grid'][i][j] - 1, 5)
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
    for i in range(3):
        for j in range(5):
            if grid[i][j] == '_':
                empty = (i, j)
    start = {'grid': grid, 'empty': empty}
    goal_state = a_star(start)
    return [goal_state['grid'][empty[0]][empty[1]] for _ in range(len(grid[0]))]

grid = [[94, 92, 77, 88, '_'], [82, 43, 76, 85, 87], [24, 66, 17, 79, 75]]
print(solve_8_puzzle(grid))
