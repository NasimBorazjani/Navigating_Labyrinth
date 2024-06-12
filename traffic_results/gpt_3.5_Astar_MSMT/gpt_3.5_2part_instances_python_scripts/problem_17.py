
import heapq

def initialize():
    initial_state = ((16, 2, 16, 'x', 4, 'x', 'x', 1, 16, 'x'), ('x', 'x', 19, 'x', 3, 'x', 5, 'x', 'x', 'x'), ('x', 'x', 'x', 3, 'x', 'x', 2, 'x', 10, 'x'), (11, 5, 20, 'x', 1, 3, 1, 'x', 9, 'x'), ('x', 'x', 8, 19, 'x', 16, 9, 'x', 16, 15), ('x', 3, 5, 10, 'x', 'x', 'x', 4, 1, 'x'), (9, 18, 10, 17, 5, 6, 'x', 'x', 'x', 5), ('x', 'x', 14, 5, 18, 'x', 'x', 1, 15, 1), (13, 'x', 13, 13, 14, 2, 19, 12, 'x', 1), (9, 6, 'x', 4, 12, 1, 13, 8, 2, 13))
    num_rows = 10
    num_cols = 10
    start = (7, 9)
    end = (3, 2)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)], 3: [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9)]}
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
