
import heapq

def initialize():
    initial_state = ((x, 6, 19, 13, x, 16, 11, 6, 14, 15, 7, x, x, x), (x, 6, 16, 15, x, 19, 16, 18, x, 8, 10, x, x, x), (x, 5, 10, 14, 2, x, x, x, 11, x, 11, x, x, x), (6, 13, 15, 10, x, x, x, x, 19, x, x, x, 2, x), (x, 15, 10, 6, 6, 8, 10, 9, 11, x, x, x, 16, x), (x, x, x, 8, 15, 12, 10, 19, 1, 18, 19, 4, x, 10), (1, 17, x, x, 6, 8, 4, x, 15, 8, 10, 6, 4, x), (x, x, x, x, 13, x, 5, x, 9, 10, x, x, x, x), (12, x, 11, x, 13, x, 11, 7, 5, 13, x, x, 6, 15), (x, 18, 19, x, x, x, 3, x, 16, 11, x, 15, x, x), (x, x, x, x, x, x, 2, 15, x, x, 8, x, x, x), (11, x, 6, 13, 12, x, 12, x, x, 9, x, 17, x, x), (x, 1, x, 18, 18, 3, x, 11, 13, 1, 13, x, x, x), (x, x, x, x, x, 6, x, x, 8, x, x, x, 4, 11))
    num_rows = 14
    num_cols = 14
    start = (3, 0)
    end = (6, 12)
    districts = {1: [(0, 0), (0, 1), (0, 2)], 2: [(3, 0), (5, 1), (4, 2)], 3: [(6, 0), (13, 1), (12, 2), (11, 3), (10, 4), (9, 5), (8, 6), (7, 7)]}
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
