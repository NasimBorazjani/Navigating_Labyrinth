
import heapq

def initialize():
    initial_state = ((x, 2, 16, x, 9, x, 14, x, 8, x, 16, x, x, 4, 8), (9, x, 4, x, x, 7, 11, x, x, 13, x, x, 6, 11, x), (x, x, 10, 14, x, x, 18, x, x, x, x, x, 6, 16, x), (x, 14, x, 1, x, 7, 5, 16, x, 19, x, x, 10, 7, x), (1, 3, x, 19, 7, 2, 17, x, x, 6, x, x, x, 10, 14), (14, x, x, x, 12, x, 16, 5, 8, 12, 17, 2, 19, x, 5), (9, 9, 8, 15, 18, x, 16, x, 10, x, x, 14, x, x, x), (18, 20, x, x, 11, 2, 17, 6, x, 18, 8, x, 6, 16, x), (12, x, x, x, x, 7, 14, 4, 8, 12, 3, x, 15, 13, 2), (16, x, x, x, 12, x, 8, 1, 7, 7, 12, 17, 2, 2, 7), (x, 13, 3, 3, 1, x, 6, 14, 20, 8, x, 4, 10, 17, x), (1, 8, x, 16, x, x, x, 9, x, x, 10, x, x, 5, 8), (x, x, 1, x, x, 6, x, x, x, 7, 16, x, x, x, x), (14, x, x, 10, 18, x, 6, 13, x, x, x, x, 15, x, x), (x, 8, 2, x, 17, x, 12, 16, 11, 4, 4, x, x, 17, x))
    num_rows = 15
    num_cols = 15
    start = (4, 0)
    end = (9, 11)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)], 2: [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4)], 3: [(10, 0), (10, 1), (10, 2), (10, 3), (10, 4)]}
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
