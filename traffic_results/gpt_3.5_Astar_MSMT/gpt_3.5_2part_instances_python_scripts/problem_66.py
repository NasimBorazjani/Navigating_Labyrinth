
import heapq

def initialize():
    initial_state = ((x, 17, 14, 18, x, x, 8, 18, 10, 5, 5, x, x), (x, x, x, x, 17, 18, 17, 17, 6, 12, x, 7, 16), (17, x, 17, 6, 18, x, 10, 13, 10, 19, 15, 4, 13), (15, 5, 15, 3, 17, 3, x, x, 18, 15, 19, 3, 2), (x, x, x, x, 2, 10, x, x, x, 18, 14, 5, 12), (x, 16, x, 12, 4, 7, x, x, 9, x, x, x, x), (x, 7, x, x, 16, 2, 9, 1, 3, x, x, 4, x), (15, 16, x, 10, 1, 16, x, x, 2, 18, 1, x, x), (x, x, 8, 3, x, 19, x, x, x, 5, 9, x, x), (x, 8, 12, 14, x, x, x, 16, x, 8, x, 3, 2), (8, 1, x, x, x, x, 13, x, x, x, 9, x, 12), (x, x, 3, 3, 11, x, x, 16, x, x, 5, x, x), (x, 11, 17, x, x, x, x, 9, x, x, 2, 15, x))
    num_rows = 13
    num_cols = 13
    start = (3, 10)
    end = (9, 2)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (8, 1), (8, 2), (8, 3), (8, 4)], 3: [(9, 0), (10, 1), (11, 2), (12, 3)]}
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
