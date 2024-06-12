
import heapq

def initialize():
    initial_state = ((18, 'x', 'x', 14, 5, 'x', 'x', 5, 18, 'x', 3, 'x'), ('x', 'x', 'x', 9, 2, 2, 'x', 15, 14, 12, 'x', 18), ('x', 'x', 3, 16, 3, 9, 'x', 16, 'x', 14, 'x', 17), ('x', 'x', 'x', 19, 7, 20, 'x', 'x', 11, 4, 'x', 4), (7, 'x', 8, 11, 'x', 1, 15, 5, 'x', 'x', 11, 'x'), ('x', 'x', 'x', 'x', 'x', 'x', 6, 11, 'x', 'x', 'x', 8), ('x', 15, 2, 'x', 'x', 18, 'x', 1, 16, 15, 6, 5), ('x', 4, 18, 8, 9, 'x', 'x', 17, 20, 13, 'x', 10), ('x', 16, 'x', 'x', 19, 'x', 17, 'x', 13, 11, 14, 2), (12, 'x', 11, 'x', 3, 'x', 5, 3, 'x', 13, 17, 6), (14, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 11, 'x', 16), (12, 'x', 'x', 'x', 12, 'x', 10, 'x', 18, 14, 8, 'x'))
    num_rows = 12
    num_cols = 12
    row_sums = [None, 187, 149, None, 7, None, 15, 4, 16, None, 11, None]
    col_sums = [None, 148, 196, None, 5, 6, 2, 11, 20, 13, 17, 8]
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
