
import heapq

def initialize():
    initial_state = ((x, x, 6, x, 7, x, 9, 4, 11), (x, 3, x, 6, 5, 3, 15, x, 3), (x, x, x, 4, x, 9, 1, 8, x), (15, 18, 1, 6, 5, 10, 6, 14, 8), (18, 10, 7, 18, 2, x, x, x, 7), (11, 9, 16, x, 11, x, 11, x, 17), (7, x, 18, x, 8, 10, 20, 6, x), (15, 4, 17, x, 16, 2, 12, 16, x), (9, 10, 18, 17, 9, 6, 7, x, 15))
    num_rows = 9
    num_cols = 9
    start = (3, 0)
    end = (6, 6)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 8)], 3: [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8)]}
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
