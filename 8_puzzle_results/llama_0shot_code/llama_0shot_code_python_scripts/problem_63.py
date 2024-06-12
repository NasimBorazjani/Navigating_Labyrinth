
import heapq

def generate_next_states(state):
    empty_x, empty_y = 0, 0
    for i in range(3):
        for j in range(5):
            if state[i][j] == '_':
                empty_x, empty_y = i, j
                break
        else:
            continue
        break

    next_states = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 5:
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            next_states.append((new_state, (abs(new_x - empty_x), abs(new_y - empty_y))))
    return next_states

def manhattan_distance(state):
    return sum(abs(row - (i // 5)) + abs(col - (i % 5)) for i, row, col in ((v, x, y) for x in range(3) for y in range(5) for v in state[x] if v != '_'))

def a_star(start):
    queue = [(0, 0, start)]
    visited = {tuple(row) for row in start}
    while queue:
        _, cost, state = heapq.heappop(queue)
        if state == goal_state:
            return cost
        for new_state, (dx, dy) in generate_next_states(state):
            new_cost = cost + 1 + dx + dy
            if tuple(new_state) not in visited:
                visited.add(tuple(new_state))
                heapq.heappush(queue, (new_cost + manhattan_distance(new_state), new_cost, new_state))

initial_state = [[98, 80, 41, 91, 88], [75, 93, 24, '_', 12], [38, 37, 49, 65, 43]]
goal_state = [[98, 88, 91, 80, 41], [75, 93, 65, 49, 43], [24, 12, 38, 37, '_']]

print(a_star(initial_state))
