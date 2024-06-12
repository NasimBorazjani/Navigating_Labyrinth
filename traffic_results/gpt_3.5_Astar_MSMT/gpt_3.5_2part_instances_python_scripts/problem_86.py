
import heapq

def initialize():
    initial_state = ((x, x, 11, 16, x, x, x, x, 4, x, 14, 5, x, x), (3, 1, 13, x, x, 14, 11, x, x, 15, 12, 15, x, x), (17, 15, 17, 10, 11, x, 7, 1, 1, 14, x, 9, x, x), (8, x, x, 13, 2, 12, x, 8, x, x, 9, 13, 19, 5), (4, x, 2, 3, 8, x, x, 17, x, x, 16, 10, x, x), (x, x, x, x, 3, 13, 14, 16, 18, 11, 4, 19, 20, x), (x, 11, x, x, 3, 10, 8, 9, 18, 7, 1, 14, x, 6), (11, x, 12, 11, x, 11, 10, 3, 10, 12, 15, x, 11, x), (x, x, 4, 18, x, x, 13, x, 14, 10, x, 8, x, 17), (x, x, x, x, x, x, x, 7, 7, x, x, 18, 19, 18), (19, 4, x, 2, 14, 2, x, 9, x, 10, 7, 17, 4, 12), (13, 2, x, x, 18, 5, x, 11, x, x, x, 18, x, x), (x, x, 13, 1, 13, x, 2, x, x, x, x, x, 14, x), (x, 12, x, x, x, x, x, x, x, 19, x, x, 9, 1))
    num_rows = 14
    num_cols = 14
    start = (3, 0)
    end = (5, 12)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)], 3: [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (7, 13)]}
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
