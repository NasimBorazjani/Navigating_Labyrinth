
import heapq

def initialize():
    initial_state = ((9, 1, 14, 11, 15, 12), (18, 14, 11, 3, 18, 2), (3, 8, 6, 10, 9, 7), (1, 5, 6, 1, 2, 15), (12, 3, 2, 15, 8, 19), (2, 13, 7, 3, 12, 16), (9, 5, 7, 10, 11, 17), (3, 11, 4, 19, 5, 9), (13, 4, 7, 13, 10, 13), (9, 8, 8, 14, 19, 19), (1, 11, 11, 9, 16, 12), (9, 16, 12, 6, 5, 16), (19, 14, 5, 13, 9, 16))
    num_rows = 13
    num_cols = 6
    start = (6, 12)
    end = (5, 0)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (4, 1)], 3: [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12)]}
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
