
import heapq

def initialize():
    initial_state = ((98, 74, 70, 26, 65), (91, 55, 12, '_', 68), (27, 18, 67, 40, 54))
    num_rows = 3
    num_cols = 5
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = []
    heapq.heappush(queue, (0, 0, [], initial_state))
    return (initial_state, num_rows, num_cols, visited_costs, queue)

def a_star():
    (initial_state, num_rows, num_cols, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        empty_spot = [(i, j) for (i, row) in enumerate(state) for (j, element) in enumerate(row) if (element == '_')][0]
        if (empty_spot == ((num_rows - 1), (num_cols - 1))):
            return actions
        for (d_row, d_col) in [(0, (- 1)), (0, 1), ((- 1), 0), (1, 0)]:
            (new_row, new_col) = ((empty_spot[0] + d_row), (empty_spot[1] + d_col))
            if ((0 <= new_row < num_rows) and (0 <= new_col < num_cols)):
                new_state = [list(row[:]) for row in state]
                (new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col]) = (new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]])
                new_state = tuple((tuple(row) for row in new_state))
                new_cost = (g + new_state[empty_spot[0]][empty_spot[1]])
                if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, ((g + 1), new_cost, (actions + [new_state[empty_spot[0]][empty_spot[1]]]), new_state))
    return None
print(a_star())
