
import heapq

def initialize():
    initial_state = ((18, 19, 9, 'x', 'x', 'x', 3, 'x', 8, 'x'), (13, 2, 3, 15, 3, 'x', 8, 9, 'x', 'x'), ('x', 6, 18, 1, 20, 7, 16, 8, 1, 19), ('x', 'x', 'x', 20, 14, 'x', 19, 11, 9, 6), (2, 'x', 'x', 6, 5, 6, 7, 1, 'x', 8), (17, 9, 5, 3, 3, 'x', 16, 18, 'x', 8), (10, 'x', 14, 16, 'x', 8, 'x', 9, 6, 'x'), ('x', 17, 8, 11, 12, 'x', 4, 8, 'x', 13), ('x', 'x', 6, 'x', 'x', 'x', 'x', 13, 'x', 7), (9, 'x', 'x', 'x', 3, 10, 'x', 3, 10, 1))
    num_rows = 10
    num_cols = 10
    start = (5, 1)
    end = (3, 9)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (4, 1), (4, 2), (4, 3)], 3: [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9)]}
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
