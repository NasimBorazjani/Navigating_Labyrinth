
import heapq

def initialize():
    initial_state = ((x, 12, x, x, x, 5, 9, 14, 6, x, 3, 14, x), (x, x, 3, x, 11, x, 13, x, x, x, x, 9, 8), (x, 18, x, x, x, 13, 4, 5, x, x, x, 13, x), (10, 4, x, x, x, x, x, 18, x, 15, x, x, x), (x, 1, 7, x, 7, 6, x, 3, x, 2, x, x, 5), (x, 15, 5, x, x, 10, x, 19, x, x, x, 10, 6), (x, 18, 1, 2, x, 7, 16, 19, x, x, 10, 8, 8), (8, x, x, 6, 2, x, x, x, 7, 11, 5, 11, 2), (x, 4, 1, 1, 5, 12, 3, 6, 2, 1, x, 3, 8), (x, x, 5, 5, 14, 15, 7, x, x, 11, x, 7, 9), (x, 6, 12, 16, 17, x, x, 4, x, 19, 9, 5, x), (12, x, 4, x, 8, 4, x, 5, x, x, x, 5, x), (x, 5, x, x, x, x, x, 7, x, x, 11, x, x))
    num_rows = 13
    num_cols = 13
    start = (6, 12)
    end = (4, 1)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)], 2: [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4)], 3: [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12)]}
    visited_costs = {}
    visited_costs[start] = 0
    queue = [(0, 0, [], start)]
    return (initial_state, num_rows, num_cols, start, end, districts, visited_costs, queue)

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
