
import heapq

def initialize():
    initial_state = ((x, x, 17, 7, x, x, 11, 4, 5, 15, 17, 6, 6, 2), (17, x, x, 6, x, x, x, x, 1, 8, x, x, x, 7), (x, x, x, 17, 4, 10, 6, 4, x, 8, 16, 11, x, x), (x, 4, x, x, 10, x, 8, 10, x, 11, x, x, 1, x), (x, x, 11, 9, 4, x, 8, 8, x, x, x, 16, 13, 8), (x, 12, 3, 15, 13, 13, x, 15, 19, x, 2, 2, 6, x), (15, 1, x, x, x, x, 5, 4, x, 5, 12, 2, 5, x), (20, 13, 7, 18, 8, 18, 5, 2, 17, 7, 11, x, 15, 13), (4, 11, x, x, 10, 9, x, 18, 14, x, 19, x, x, x), (19, x, 2, x, 18, 17, 10, x, x, x, 13, 15, x, 10), (16, 5, 2, 3, 13, x, x, x, x, x, x, x, x, 3), (x, x, x, x, 17, 9, x, x, x, x, x, 6, x, x), (11, x, x, 9, 14, x, x, 16, x, 15, 13, 13, 15, 1), (9, x, x, 10, 14, x, x, x, x, x, x, x, 1, 19))
    num_rows = 14
    num_cols = 14
    start = (4, 12)
    end = (7, 0)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)], 2: [(5, 0), (6, 0)], 3: [(7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0)]}
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
