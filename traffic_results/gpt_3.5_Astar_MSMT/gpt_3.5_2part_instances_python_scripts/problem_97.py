
import heapq

def initialize():
    initial_state = ((17, 8, 'x', 3, 'x', 13, 'x', 'x', 14, 11, 'x', 'x', 'x', 'x', 'x'), ('x', 'x', 'x', 7, 'x', 'x', 13, 'x', 'x', 'x', 'x', 'x', 16, 'x', 13), ('x', 'x', 2, 'x', 'x', 12, 10, 'x', 'x', 'x', 2, 'x', 'x', 5, 17), (4, 3, 'x', 14, 'x', 'x', 16, 'x', 'x', 'x', 1, 'x', 'x', 'x', 'x'), (9, 'x', 18, 11, 19, 5, 'x', 'x', 'x', 'x', 'x', 'x', 3, 'x', 'x'), ('x', 14, 'x', 4, 14, 12, 1, 'x', 13, 7, 10, 8, 8, 6, 9), (7, 10, 'x', 18, 15, 8, 13, 14, 15, 'x', 'x', 'x', 13, 'x', 17), (17, 7, 19, 15, 20, 19, 'x', 15, 13, 'x', 9, 'x', 11, 'x', 1), ('x', 9, 6, 17, 14, 'x', 16, 'x', 19, 11, 'x', 14, 11, 'x', 'x'), ('x', 18, 8, 2, 14, 2, 4, 'x', 4, 4, 4, 'x', 'x', 8, 19), ('x', 'x', 5, 'x', 'x', 'x', 1, 5, 'x', 11, 'x', 'x', 1, 14, 'x'), ('x', 'x', 'x', 'x', 5, 'x', 10, 'x', 'x', 'x', 'x', 10, 18, 'x', 19), ('x', 'x', 2, 'x', 1, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 6, 16, 'x'), ('x', 12, 1, 12, 'x', 'x', 15, 7, 18, 15, 13, 19, 'x', 2, 'x'), ('x', 13, 8, 19, 5, 1, 'x', 13, 'x', 'x', 'x', 17, 'x', 3, 'x'))
    num_rows = 15
    num_cols = 15
    start = (9, 1)
    end = (7, 14)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)], 2: [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8)], 3: [(9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14)]}
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
