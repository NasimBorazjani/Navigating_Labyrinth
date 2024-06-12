
import heapq

def initialize():
    initial_state = ((x, 14, 15, 10, x, 14, x, x, 18, 6, x, x, 4), (6, x, x, x, 1, x, 15, x, x, 2, x, 17, x), (x, 4, x, 17, 3, 14, 4, 2, x, 3, x, 11, x), (6, 6, x, 19, x, 13, x, 11, 13, 6, 3, x, x), (3, 10, 11, x, x, 4, 4, 1, 19, x, x, x, 17), (8, x, x, 8, 11, 18, 17, 19, 18, x, 1, 1, x), (14, 14, 1, 19, 6, x, 19, 19, 18, 9, x, 12, 18), (17, 6, 8, x, 1, 14, 19, 13, x, x, 9, x, 3), (16, 4, x, x, x, 9, 5, x, x, x, 18, x, x), (x, x, 10, x, 18, x, 1, x, x, 12, 9, 8, 3), (x, 13, 17, x, x, x, 5, 8, 1, x, 1, 10, x), (10, 11, x, 12, x, 6, 11, x, 9, 9, 15, x, 10), (5, 15, 1, x, 8, 5, x, 6, x, 9, 18, x, x))
    num_rows = 13
    num_cols = 13
    start = (3, 8)
    end = (8, 0)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (4, 1), (4, 2), (4, 3)], 3: [(8, 0), (8, 1), (8, 2), (8, 3)]}
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
