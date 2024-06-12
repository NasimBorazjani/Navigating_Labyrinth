
import heapq

def initialize():
    initial_state = ((x, 13, 9, x, x, 16, 6, 18, 7), (x, 3, 11, x, x, 5, 7, x, 19), (8, x, 2, 5, 6, 12, 9, 10, 7), (12, 1, 6, 20, 19, 18, 12, x, 14), (16, 5, 10, 3, x, x, x, 1, 9), (x, 3, x, x, x, x, x, x, 4), (7, 10, x, 1, x, x, 17, x, 8), (x, 5, x, x, x, 17, x, 9, x), (13, 16, 8, 15, x, 2, x, 1, 2))
    num_rows = 9
    num_cols = 9
    row_sums = [None, 187, 149, None]
    col_sums = [None, 148, 196, None]
    diagonal_sum = 166
    numbers = set(range(29, 54))
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, num_rows, num_cols, row_sums, col_sums, diagonal_sum, numbers, visited_costs, queue)

def a_star():
    (initial_state, num_rows, num_cols, start, end, districts, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        if (state == end):
            return actions
        for (d_row, d_col) in [(0, 1), (0, (- 1)), (1, 0), ((- 1), 0)]:
            (new_row, new_col) = ((state[0] + d_row), (state[1] + d_col))
            if ((0 <= new_row < num_rows) and (0 <= new_col < num_cols) and (initial_state[new_row][new_col] != 'x')):
                new_state = (new_row, new_col)
                new_cost = (g + initial_state[new_row][new_col])
                for (district, workshops) in districts.items():
                    if ((state in workshops) and (new_state not in workshops)):
                        new_cost += 100
                if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (((g + abs((new_row - end[0]))) + abs((new_col - end[1]))), new_cost, (actions + [new_state]), new_state))
    return None
print(a_star())
