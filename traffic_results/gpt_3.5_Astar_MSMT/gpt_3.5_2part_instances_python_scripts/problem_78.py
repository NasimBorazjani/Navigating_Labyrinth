
import heapq

def initialize():
    initial_state = ((x, x, x, 16, 11, 12, x, x, 17, 3, x, x, 4, 6), (4, 17, x, x, 3, x, x, 1, 9, 11, 12, 4, x, x), (5, x, x, 7, 14, 4, 5, 7, 13, 4, 7, x, x, x), (6, 6, 19, 3, 15, x, x, x, x, 4, 10, 19, 2, 4), (3, 16, 8, x, 5, x, 12, 17, 16, x, 9, 5, 6, x), (17, 2, x, x, 16, x, 5, x, x, 5, 17, 7, 2, 5), (19, x, x, x, x, 2, 15, 15, x, 3, 11, x, 4, x), (x, x, 11, x, x, 17, 5, x, 5, x, x, 19, 6, x), (16, 17, 16, x, 12, x, 2, 18, 9, 7, x, 13, x, x), (18, 11, x, x, 19, 5, x, x, 18, 4, x, x, x, x), (x, x, x, x, 2, 5, 4, 12, 3, x, 4, 14, 7, 19), (18, x, x, x, 7, 17, x, x, 3, 15, x, 16, x, 10), (x, 11, 15, x, x, x, x, x, 2, 13, x, x, x, 3), (4, 8, x, x, x, x, 12, 13, x, x, 19, x, 6, x))
    num_rows = 14
    num_cols = 14
    start = (7, 12)
    end = (2, 0)
    districts = {1: [(0, 0), (0, 1), (0, 2)], 2: [(3, 0), (6, 0), (9, 0)], 3: [(10, 0), (13, 0)]}
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
