
import heapq

def generate_next_states(state):
    empty_x, empty_y = 0, 0
    for i in range(3):
        for j in range(4):
            if state[i][j] == '_':
                empty_x, empty_y = i, j
                break
        else:
            continue
        break

    next_states = []
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 4:
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            next_states.append((new_state, (abs(new_x - empty_x), abs(new_y - empty_y))))
    return next_states

def estimate_cost(state):
    cost = 0
    for i in range(3):
        for j in range(4):
            if state[i][j] != '_' and state[i][j] != str(i * 3 + j + 1):
                cost += abs(i * 3 + j - int(state[i][j]))
    return cost

def solve_8_puzzle(initial_state):
    queue = [(estimate_cost(initial_state), initial_state, [])]
    visited = set()

    while queue:
        _, state, swaps = heapq.heappop(queue)
        if tuple(tuple(row) for row in state) not in visited:
            visited.add(tuple(tuple(row) for row in state))
            if state == [['1', '2', '3', '4'], ['5', '6', '_', '8'], ['9', '10', '11', '12']]:
                return swaps

            for next_state, (dx, dy) in generate_next_states(state):
                new_swaps = swaps + [state[dx][dy]]
                heapq.heappush(queue, (estimate_cost(next_state) + len(new_swaps), next_state, new_swaps))

    return None

initial_state = [['7', '1', '2', '2'], ['7', '9', '_', '6'], ['8', '5', '8', '1']]
print(solve_8_puzzle(initial_state))
