
import heapq

def initialize():
    initial_state = ((x, x, 7, 18, 11, 4, 9, x, 15, x, x, x, 1, x, x), (x, x, 14, x, 10, x, x, x, 8, x, x, 16, 1, x, x), (17, 17, x, x, x, x, x, 7, 6, 12, x, x, x, 7, x), (x, x, x, x, 10, x, x, 18, 1, 11, 4, x, 13, 10, 16), (x, x, x, 12, 1, x, x, x, 2, 7, 1, x, 2, x, 5), (x, x, 8, x, 12, x, x, 5, 17, x, 2, x, 4, 10, 18), (x, x, 4, 19, 1, x, 18, 7, x, 10, 3, x, 19, 16, 19), (6, 12, 15, 16, 5, 9, 16, 18, 10, 15, 5, x, 5, 14, x), (x, 16, 8, 17, 12, 11, 16, 8, 9, 9, 7, 4, 5, 20, 3), (19, 17, 15, x, x, 17, x, 3, 2, 2, 11, 7, 8, 16, 1), (13, 4, 17, x, x, x, x, 5, x, 18, 16, 15, 19, 4, x), (11, x, x, x, x, 12, x, x, x, x, x, x, 19, x, x), (18, x, x, x, 9, 19, x, 16, 6, x, 9, 3, 16, 15, x), (x, x, x, 10, x, x, 4, 3, x, 3, x, 16, 18, x, 12), (x, 13, x, x, x, x, x, 10, 5, x, 17, x, x, 7, x))
    num_rows = 15
    num_cols = 15
    start = (7, 2)
    end = (4, 14)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)], 2: [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4)], 3: [(9, 0), (9, 1), (9, 2), (9, 3), (9, 4)]}
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
