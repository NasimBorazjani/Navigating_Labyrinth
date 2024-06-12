
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
            next_states.append((new_state, (abs(new_x - dx), abs(new_y - dy))))
    return next_states

def manhattan_distance(state):
    return sum(abs(state[i][j] - (i * 3 + j + 1)) for i in range(3) for j in range(3) if state[i][j] != '_')

def a_star(start):
    queue = [(0, 0, start)]
    visited = {tuple(row) for row in start}
    while queue:
        _, cost, state = heapq.heappop(queue)
        if state == [['89', '69', '35'], ['16', '14', '64'], ['_', '23', '32']]:
            return cost, []

        for new_state, (dx, dy) in generate_next_states(state):
            new_cost = cost + 1 + dx + dy
            if tuple(new_state) not in visited:
                visited.add(tuple(new_state))
                heapq.heappush(queue, (new_cost + manhattan_distance(new_state), new_cost, new_state))

    return None

def solve_8_puzzle(puzzle):
    cost, _ = a_star(puzzle)
    return cost

initial_state = [[89, 69, 35], [16, 14, 64], ['_', 23, 32]]
print(solve_8_puzzle(initial_state))
