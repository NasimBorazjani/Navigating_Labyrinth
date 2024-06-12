
import heapq

def initialize():
    initial_state = ((13, 'x', 10, 17, 'x', 4, 8, 'x', 7, 'x', 12, 19, 4), (17, 'x', 8, 11, 7, 'x', 'x', 19, 'x', 11, 'x', 13, 18), (15, 6, 2, 12, 16, 7, 'x', 14, 'x', 2, 'x', 14, 4), ('x', 18, 4, 'x', 'x', 'x', 13, 14, 2, 4, 20, 10, 7), (7, 2, 19, 16, 'x', 'x', 'x', 18, 'x', 'x', 'x', 2, 2), (10, 17, 14, 7, 17, 3, 3, 19, 'x', 19, 'x', 'x', 9), (9, 'x', 'x', 'x', 5, 18, 13, 6, 'x', 'x', 'x', 19, 10), ('x', 'x', 'x', 'x', 'x', 2, 7, 4, 'x', 'x', 'x', 'x', 'x'), ('x', 'x', 6, 3, 'x', 1, 'x', 'x', 14, 'x', 18, 'x', 1), (14, 'x', 4, 18, 14, 12, 'x', 'x', 'x', 'x', 2, 'x', 13), (12, 'x', 3, 1, 12, 9, 'x', 6, 'x', 'x', 16, 'x', 18), (13, 'x', 11, 5, 3, 4, 'x', 'x', 'x', 'x', 'x', 'x', 18), (15, 9, 9, 1, 'x', 6, 'x', 'x', 14, 'x', 'x', 1, 14))
    num_rows = 13
    num_cols = 13
    start = (5, 1)
    end = (2, 11)
    districts = {1: [(0, 0), (1, 0)], 2: [(2, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0)], 3: [(12, 0)]}
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
