
import heapq

def initialize():
    initial_state = ((x, x, 13, x, x, 7, x, 13, 3, x, 13), (10, 4, x, 4, 12, 2, x, 3, 4, x, 15), (x, 3, x, x, 15, 9, x, x, 18, 17, 14), (5, x, x, x, 3, x, 11, x, 17, 9, 17), (8, 3, 13, x, 5, 7, 8, 17, 7, x, x), (x, x, 13, 2, 2, 11, 6, 8, x, x, x), (x, 1, 9, 6, 5, 13, 16, 1, 7, 5, x), (4, x, 13, x, 10, 18, 3, x, x, 19, 19), (x, x, x, 2, 5, 9, 13, x, 7, 1, x), (x, x, 7, x, x, 5, 19, x, x, x, 1))
    num_rows = 9
    num_cols = 11
    start = (5, 2)
    end = (2, 10)
    districts = {1: [(0, 0), (0, 1), (0, 2)], 2: [(3, 0), (3, 1)], 3: [(5, 0), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10)]}
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