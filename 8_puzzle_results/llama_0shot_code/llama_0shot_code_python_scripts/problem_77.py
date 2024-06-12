
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
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 5:
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            next_states.append((new_state, (abs(new_x - empty_x), abs(new_y - empty_y))))
    return next_states

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(5):
            if state[i][j] != '_' and state[i][j] != 'goal':
                goal_x, goal_y = divmod(state[i][j] - 1, 5)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def a_star(start):
    queue = [(0, 0, start)]
    visited = {tuple(row) for row in start}
    while queue:
        _, _, state = heapq.heappop(queue)
        if state == 'goal':
            return []

        for new_state, (dx, dy) in generate_next_states(state):
            new_cost = manhattan_distance(new_state) + dx + dy
            if tuple(new_state) not in visited:
                visited.add(tuple(new_state))
                heapq.heappush(queue, (new_cost, len(queue), new_state))

    return None

initial_state = [
    [60, 66, 46, 8, 36],
    [81, '_', 88, 70, 24],
    [20, 17, 6, 62, 28]
]

goal_state = [
    [8, 6, 4, 2, 1],
    [7, 6, 5, 3, '_']
]

initial_state.append(goal_state[0] + [goal_state[1]])

print(a_star(initial_state))
