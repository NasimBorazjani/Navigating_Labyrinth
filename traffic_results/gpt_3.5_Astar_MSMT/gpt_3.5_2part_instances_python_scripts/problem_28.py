
import heapq

def initialize():
    initial_state = ((15, 'x', 8, 'x', 6, 9, 'x', 'x', 'x'), (14, 'x', 8, 'x', 14, 'x', 5, 11, 'x', 9), ('x', 17, 8, 'x', 17, 15, 12, 'x', 'x', 13), ('x', 13, 'x', 'x', 2, 'x', 17, 17, 1, 'x'), (6, 'x', 1, 5, 17, 'x', 2, 18, 11, 7), (12, 8, 17, 10, 'x', 'x', 'x', 15, 'x', 16), (12, 12, 'x', 4, 'x', 13, 'x', 10, 'x', 16), ('x', 'x', 10, 'x', 6, 'x', 'x', 'x', 8, 5), ('x', 2, 11, 18, 15, 'x', 11, 'x', 'x', 12), ('x', 'x', 14, 'x', 'x', 7, 14, 15, 18, 9))
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
