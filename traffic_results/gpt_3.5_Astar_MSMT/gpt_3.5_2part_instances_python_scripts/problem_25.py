
import heapq

def initialize():
    initial_state = ((x, x, 6, x, x, x, x, 15, x, x), (x, 17, 13, 13, x, 12, x, 3, 10, 2), (x, 5, 13, 15, 4, x, x, 20, 6, 2), (x, 9, x, 6, 2, 16, 18, 9, 13, x), (x, x, 15, 17, x, 10, 11, x, x, x), (3, x, 3, 17, 8, x, 1, x, 16, x), (x, x, 13, 15, x, x, 11, x, x, 4), (x, x, 12, 1, x, x, x, 14, 11, x), (x, 14, x, x, 19, 13, 4, x, x, x), (1, x, x, 14, 11, 19, 2, 17, 2, 5))
    num_rows = 10
    num_cols = 10
    row_sums = [None, 187, 149, None]
    col_sums = [None, 148, 196, None]
    diagonal_sum = 166
    numbers = set(range(29, 55))
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
