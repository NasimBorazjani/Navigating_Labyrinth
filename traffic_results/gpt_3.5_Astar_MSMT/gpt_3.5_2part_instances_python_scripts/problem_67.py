
import heapq

def initialize():
    initial_state = ((x, x, 10, x, x, x, 3, x, x, x, x, x, x), (6, 19, x, x, x, 12, x, x, 3, x, x, x, x), (5, 3, 7, 7, x, 7, 9, x, 18, x, x, x, x), (1, 4, 19, 19, 16, 6, x, 2, 10, x, 1, 7, x), (14, 10, x, x, 2, 3, 5, 3, 13, 7, x, 8, x), (x, 8, 11, 14, 18, x, x, 16, 15, 8, x, 10, x), (x, 17, x, x, 15, x, x, 1, 17, 9, 7, x, 10), (18, 6, 14, 4, 12, 12, x, 12, 5, x, x, 5, 18), (x, x, x, x, x, x, x, 7, 17, 4, 16, x, x), (x, 6, 17, x, x, x, x, x, 15, x, x, 12, x), (14, x, x, 12, 3, 11, x, x, x, x, x, x, 17), (x, 16, x, x, x, 3, 5, 19, x, 16, 14, x, 19), (13, x, 11, x, 3, 16, x, 1, x, x, 1, x, x))
    num_rows = 13
    num_cols = 13
    start = (2, 3)
    end = (8, 10)
    districts = {1: [(0, 0), (0, 1), (0, 2)], 2: [(3, 0), (7, 1), (8, 2)], 3: [(9, 0), (12, 1)]}
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