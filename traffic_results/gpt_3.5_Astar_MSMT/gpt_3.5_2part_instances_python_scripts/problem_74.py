
import heapq

def initialize():
    initial_state = ((10, 'x', 'x', 'x', 16, 9, 'x', 13, 12, 8, 'x', 16, 17), (9, 2, 'x', 'x', 5, 'x', 'x', 'x', 12, 'x', 3, 'x', 'x'), ('x', 'x', 7, 3, 12, 'x', 11, 18, 10, 'x', 'x', 13, 'x'), ('x', 6, 'x', 19, 2, 'x', 'x', 11, 13, 13, 1, 'x', 7), ('x', 'x', 11, 'x', 16, 16, 4, 12, 5, 20, 2, 4, 15), (19, 'x', 18, 5, 11, 'x', 'x', 3, 17, 18, 3, 8, 18), (12, 'x', 9, 'x', 'x', 'x', 'x', 9, 4, 15, 16, 'x', 9), ('x', 15, 'x', 6, 10, 'x', 1, 1, 'x', 9, 4, 7, 1), ('x', 19, 15, 'x', 1, 10, 5, 17, 'x', 8, 'x', 1, 'x'), ('x', 'x', 'x', 'x', 5, 'x', 1, 'x', 'x', 7, 4, 'x', 'x'), (9, 'x', 4, 'x', 5, 13, 'x', 15, 'x', 'x', 18, 9, 15), (17, 2, 'x', 'x', 'x', 18, 8, 'x', 8, 'x', 'x', 8, 7), ('x', 'x', 5, 'x', 'x', 8, 'x', 8, 'x', 15, 19, 'x', 'x'))
    num_rows = 13
    num_cols = 13
    start = (3, 12)
    end = (7, 3)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)], 3: [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12)]}
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
