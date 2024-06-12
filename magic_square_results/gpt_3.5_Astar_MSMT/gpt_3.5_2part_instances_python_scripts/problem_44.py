
import heapq

def initialize():
    initial_state = [['x', 'x', '39', 'x'], ['x', 'x', 'x', '43'], ['x', 'x', 'x', '47'], ['46', '49', 'x', '53']]
    goal_sums = [None, 177, 160, None]
    unique_integers = set(range(35, 62))
    visited_costs = {}
    visited_costs[str(initial_state)] = 0
    queue = []
    heapq.heappush(queue, (0, 0, [], initial_state))
    return (initial_state, goal_sums, unique_integers, visited_costs, queue)

def a_star():
    (initial_state, goal_sums, unique_integers, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        state_str = str(state)
        if ('x' in [cell for row in state for cell in row]):
            for (row_idx, row) in enumerate(state):
                for (col_idx, cell) in enumerate(row):
                    if (cell == 'x'):
                        for num in unique_integers:
                            new_state = [list(row) for row in state]
                            new_state[row_idx][col_idx] = str(num)
                            new_state_str = str(new_state)
                            new_cost = (g + 1)
                            if ((new_state_str not in visited_costs) or (new_cost < visited_costs[new_state_str])):
                                visited_costs[new_state_str] = new_cost
                                heapq.heappush(queue, ((new_cost + heuristic(new_state, goal_sums, unique_integers)), new_cost, (actions + [(row_idx, col_idx, num)]), new_state))
        else:
            return actions
    return None

def heuristic(state, goal_sums, unique_integers):
    state = [[(int(cell) if (cell != 'x') else 0) for cell in row] for row in state]
    row_sums = [sum(row) for row in state]
    col_sums = [sum(col) for col in zip(*state)]
    diag_sum1 = sum((state[i][i] for i in range(3)))
    diag_sum2 = sum((state[i][(2 - i)] for i in range(3)))
    row_diff = sum((abs((row_sum - goal_sum)) for (row_sum, goal_sum) in zip(row_sums, goal_sums)))
    col_diff = sum((abs((col_sum - goal_sum)) for (col_sum, goal_sum) in zip(col_sums, goal_sums)))
    diag_diff1 = abs((diag_sum1 - goal_sums[2]))
    diag_diff2 = abs((diag_sum2 - goal_sums[2]))
    h = (((row_diff + col_diff) + diag_diff1) + diag_diff2)
    return h
print(a_star())
