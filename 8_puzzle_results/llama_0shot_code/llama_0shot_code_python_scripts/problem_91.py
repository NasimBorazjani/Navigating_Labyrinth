
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
            if state[i][j] != '_' and state[i][j] != 0:
                goal_x, goal_y = divmod(state[i][j] - 1, len(state[0]))
                cost += abs(i - goal_x) + abs(j - goal_y)
    return cost

def solve_8_puzzle(initial_state):
    queue = [(estimate_cost(initial_state), initial_state, [])]
    visited = set()

    while queue:
        _, state, swaps = heapq.heappop(queue)
        if state not in visited:
            visited.add(state)
            if state == [[9, 8, 7, 6, 5, 4], [3, 2, 1, 15, 14, 13], [12, 11, 10, 16, 17, 18]]:
                return swaps

            for next_state, (dx, dy) in generate_next_states(state):
                if next_state not in visited:
                    heapq.heappush(queue, (estimate_cost(next_state) + dx + dy, next_state, swaps + [next_state[1][3]]))

    return None

initial_state = [[9, 3, 8, 1, 5, 6], [5, 5, 8, 9, 4, 10], [2, '_', 1, 4, 5, 18]]
print(solve_8_puzzle(initial_state))
