
import heapq

def generate_next_states(state):
    empty_x, empty_y = 0, 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == '_':
                empty_x, empty_y = i, j
                break
        else:
            continue
        break

    next_states = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            next_states.append((new_state, (abs(new_x - empty_x), abs(new_y - empty_y))))
    return next_states

def manhattan_distance(state):
    return sum(abs(state[i][j] - str(i * 3 + j + 1)) for i in range(3) for j in range(3) if state[i][j] != '_')

def a_star(start):
    queue = [(0, 0, start)]
    visited = {tuple(row) for row in start}
    while queue:
        _, _, state = heapq.heappop(queue)
        if state == [['8', '7', '6'], ['5', '4', '3'], ['2', '1', '_']]:
            return []
        for new_state, (dx, dy) in generate_next_states(state):
            if tuple(new_state) not in visited:
                visited.add(tuple(new_state))
                heapq.heappush(queue, (manhattan_distance(new_state) + dx + dy, dx + dy, new_state))
    return None

initial_state = [['25', '71', '58'], ['61', '94', '53'], ['50', '18', '_']]
print(a_star(initial_state))
