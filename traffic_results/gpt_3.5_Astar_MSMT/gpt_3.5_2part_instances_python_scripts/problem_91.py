
import heapq

def initialize():
    initial_state = ((x, x, 12, x, 18, 3, 2, 15, 6, 11, 13, x, 7, 17, x), (13, x, 20, 13, 5, 2, x, x, 10, 12, 19, 19, 16, x, 17), (12, 12, 7, x, x, x, 9, x, x, 10, 10, 18, 4, x, x), (x, 14, 3, 13, 9, 2, 19, 19, x, x, x, 4, x, 2, 15), (x, 14, 2, x, 3, x, 10, 11, x, 4, x, 12, 4, x, x), (x, 9, 7, 16, x, x, 19, 17, 17, 14, 14, 12, 14, 19, 12), (2, x, x, 7, 15, x, x, 13, x, 8, 1, 1, x, 14, 19), (16, x, 14, x, x, 6, x, x, 16, x, x, 9, 10, 18, 4), (3, x, x, 3, x, x, x, x, 9, 8, x, 9, 14, x, 14), (x, x, x, 4, 19, x, 4, 15, x, x, x, 17, x, x, x), (16, 17, x, x, 13, x, 18, 5, x, 14, x, x, x, x, x), (2, x, 17, x, x, x, x, x, x, 12, 3, 8, x, 2, 9), (x, x, 14, 7, 11, x, x, 10, 9, 3, 7, 16, x, 7, 1), (x, 12, 14, 1, x, x, 3, 12, x, 7, x, x, 8, x, x), (x, 2, x, 15, 2, x, 14, 16, 13, 19, 16, 1, 11, x, x))
    num_rows = 15
    num_cols = 15
    row_sums = [None, 187, 149, None, None, None, None, None, None, None, None, None, None, None, None]
    col_sums = [None, 148, 196, None, None, None, None, None, None, None, None, None, None, None, None]
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
