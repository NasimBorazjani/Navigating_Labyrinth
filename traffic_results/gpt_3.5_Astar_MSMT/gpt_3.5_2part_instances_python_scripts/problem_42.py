
import heapq

def initialize():
    initial_state = ((14, 'x', 11, 'x', 8, 15, 17, 18, 'x', 11), (13, 9, 2, 7, 9, 12, 7, 'x', 'x', 12), ('x', 2, 8, 13, 5, 'x', 'x', 7, 18, 'x'), (19, 6, 1, 6, 19, 13, 14, 'x', 'x', 17), ('x', 9, 6, 'x', 'x', 14, 10, 'x', 'x', 5), (12, 'x', 'x', 'x', 7, 17, 11, 'x', 'x', 1), ('x', 16, 'x', 2, 11, 15, 6, 'x', 14, 14, 4), ('x', 15, 14, 11, 'x', 17, 20, 18, 4, 16, 8), ('x', 3, 6, 4, 1, 5, 'x', 'x', 3, 7, 9), (18, 14, 3, 4, 'x', 'x', 'x', 12, 15, 10, 'x'), ('x', 8, 'x', 1, 18, 'x', 'x', 'x', 'x', 'x', 'x'))
    num_rows = 11
    num_cols = 11
    start = (6, 10)
    end = (3, 2)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (5, 0)], 3: [(6, 0), (7, 0), (8, 0), (9, 0), (10, 0)]}
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
