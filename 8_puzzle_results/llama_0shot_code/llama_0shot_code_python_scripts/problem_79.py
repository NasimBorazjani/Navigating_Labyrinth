
import heapq

def generate_next_states(state):
    empty_x, empty_y = 0, 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '_':
                empty_x, empty_y = i, j
                break
        else:
            continue
        break

    next_states = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < len(state) and 0 <= new_y < len(state[0]):
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            next_states.append((new_state, (abs(new_x - empty_x), abs(new_y - empty_y))))
    return next_states

def estimate_cost(state):
    cost = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != '_' and state[i][j] != '0':
                x, y = divmod(state[i][j] - 1, len(state[0]))
                cost += abs(i - x) + abs(j - y)
    return cost

def solve_8_puzzle(initial_state):
    start = (initial_state, ())
    goal = ((('0',) + '_' * 8)[:9],) + (('1',) + '2345678')[:8]
    queue = [(0, estimate_cost(initial_state), start)]
    visited = set()

    while queue:
        _, _, (state, swaps)) = heapq.heappop(queue)
        if state == goal:
            return [i for i, _ in swaps[::-1]]

        if state not in visited:
            visited.add(state)
            for next_state, (dx, dy) in generate_next_states(state):
                new_swaps = swaps + ((state[dx][dy], dx, dy),)
                heapq.heappush(queue, (len(new_swaps) + estimate_cost(next_state), estimate_cost(next_state), (next_state, new_swaps)))

    return None

initial_state = [[42, 89, 21, 58, 67], [54, 32, 99, 69, 38], [77, 33, '_', 39, 16]]
print(solve_8_puzzle(initial_state))
