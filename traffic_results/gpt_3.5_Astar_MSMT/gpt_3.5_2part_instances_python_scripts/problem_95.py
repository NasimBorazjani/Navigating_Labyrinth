
import heapq

def initialize():
    initial_state = ((x, x, x, x, 9, x, 14, 17, x, 13, 3, x, 13, 10, 18), (1, x, 11, 12, 14, 13, 8, x, 5, 7, x, x, x, x, x), (3, x, x, 18, 11, 16, x, x, x, x, 1, x, 15, 12, 10), (x, 10, x, 3, 2, 15, 14, x, x, x, 17, x, 6, 1, x), (8, 10, x, x, x, x, 1, 19, 6, x, 17, 2, x, x, x), (x, 6, 15, 2, 17, 2, 11, 5, 9, x, 12, 15, x, x, 16), (x, x, 8, x, 14, x, 13, 20, 17, 12, 19, 9, x, x, x), (13, 10, 1, 4, 11, 3, 15, x, x, 3, 14, 20, x, 6, x), (x, 11, 16, 9, 19, 18, 12, 2, x, x, 1, 10, x, x, x), (x, 13, 18, 18, 7, x, x, x, x, 18, 5, 6, x, 7, 3), (x, x, x, 18, 6, 16, 10, 18, 9, 19, x, 3, 5, 3, 4), (14, 18, 4, 1, 17, x, 7, x, 3, 16, 11, x, 17, 11, 1), (x, x, 12, 16, x, 14, 9, x, x, x, 13, 1, x, x, 19), (19, x, 3, x, 8, x, x, x, 3, x, x, x, 17, 9, 8), (15, x, 2, 8, 9, 13, x, 14, x, 6, x, 19, x, x, 5))
    num_rows = 15
    num_cols = 15
    start = (5, 2)
    end = (9, 13)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)], 2: [(5, 0), (6, 0), (7, 0), (8, 0), (9, 0)], 3: [(10, 0), (11, 0), (12, 0), (13, 0), (14, 0)]}
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
