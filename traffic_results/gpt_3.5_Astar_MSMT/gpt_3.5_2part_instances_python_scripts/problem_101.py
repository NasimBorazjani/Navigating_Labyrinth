
import heapq

def initialize():
    initial_state = ((x, 3, 1, 19, 8, 1, 4, 18, 15, 17, 4, 3, x, 3, x), (x, 11, x, x, x, 12, x, 19, 15, 4, x, x, x, x, x), (4, 1, x, 8, x, 12, 17, x, 14, 4, 9, 11, 13, 6, 19), (2, x, 6, 14, 15, x, 18, 9, x, 10, 10, x, x, 1, x), (x, 11, x, 8, x, 5, x, 8, 7, 6, x, x, 13, 6, x), (x, x, x, 17, x, 13, x, x, x, x, 18, 19, 5, x, x), (x, 12, 18, x, x, x, 19, x, 12, x, 11, 7, 19, 12, x), (6, 6, x, 6, 4, x, 18, x, x, 15, 18, x, 6, 8, x), (10, 10, x, x, 6, 4, 11, 19, x, 9, x, 2, x, 3, 14), (x, 18, 14, 10, x, 1, x, 6, x, 15, x, 6, x, 14, x), (x, x, 7, 10, x, 2, x, 7, 14, 4, 11, x, x, x, x), (12, x, 6, x, 8, 5, 6, 6, 8, x, x, x, 4, 7, x), (x, x, 1, 8, 10, 4, 10, 17, 19, 11, 2, x, x, x, 16), (x, x, x, 17, 8, 19, x, 14, x, 17, 17, 5, 7, 6, 7), (1, x, 14, x, 3, x, 18, 6, 18, 8, x, 13, 10, x, x))
    num_rows = 15
    num_cols = 15
    start = (7, 0)
    end = (4, 13)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)], 2: [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4)], 3: [(9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (13, 0), (13, 1), (13, 2), (13, 3), (13, 4), (14, 0), (14, 1), (14, 2), (14, 3), (14, 4)]}
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
