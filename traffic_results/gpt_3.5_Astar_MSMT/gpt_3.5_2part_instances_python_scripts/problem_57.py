
import heapq

def initialize():
    initial_state = ((17, 9, 11, 5, 19, 4, 18, 'x', 5, 8, 'x', 'x'), (6, 13, 'x', 9, 2, 20, 11, 20, 7, 'x', 'x', 3), (4, 17, 'x', 18, 2, 10, 'x', 16, 'x', 18, 'x', 'x'), (12, 10, 9, 14, 'x', 'x', 12, 6, 1, 2, 'x', 'x'), (5, 'x', 'x', 3, 'x', 4, 9, 14, 8, 'x', 10, 12), (1, 'x', 6, 3, 18, 18, 17, 17, 10, 'x', 'x', 10), (13, 'x', 'x', 'x', 'x', 'x', 14, 'x', 1, 19, 'x', 7), (11, 'x', 'x', 5, 9, 'x', 18, 19, 13, 13, 'x', 10), ('x', 'x', 11, 'x', 17, 'x', 'x', 'x', 14, 17, 'x', 13), (19, 'x', 'x', 'x', 'x', 19, 12, 7, 3, 14, 'x', 9), ('x', 12, 7, 15, 1, 'x', 16, 11, 9, 17, 'x', 'x'), ('x', 'x', 'x', 10, 'x', 1, 7, 'x', 'x', 'x', 6, 12))
    num_rows = 12
    num_cols = 12
    start = (7, 0)
    end = (3, 8)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)], 3: [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11)]}
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
