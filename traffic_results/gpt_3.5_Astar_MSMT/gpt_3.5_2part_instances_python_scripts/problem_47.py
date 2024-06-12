
import heapq

def initialize():
    initial_state = ((5, 'x', 'x', 4, 'x', 12, 7, 11, 8, 3, 19, 'x'), ('x', 'x', 6, 15, 16, 'x', 'x', 4, 'x', 7, 8, 19), (18, 'x', 'x', 15, 'x', 'x', 'x', 8, 4, 16, 7, 9), ('x', 19, 'x', 'x', 'x', 16, 'x', 'x', 17, 15, 'x', 9), (15, 8, 19, 'x', 4, 4, 'x', 'x', 'x', 3, 3, 10), (18, 6, 14, 5, 'x', 18, 19, 15, 18, 19, 12, 5), (12, 'x', 2, 2, 6, 3, 3, 8, 3, 1, 'x', 15), (10, 4, 'x', 9, 15, 3, 'x', 7, 'x', 17, 'x', 'x'), (5, 18, 'x', 17, 'x', 17, 'x', 'x', 15, 'x', 18, 'x'), (4, 'x', 16, 11, 10, 3, 12, 'x', 11, 14, 3, 'x'), ('x', 9, 9, 14, 19, 15, 'x', 1, 10, 19, 6, 'x'), ('x', 'x', 17, 4, 'x', 2, 'x', 7, 'x', 4, 4, 18))
    num_rows = 12
    num_cols = 12
    start = (4, 11)
    end = (6, 0)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)], 2: [(5, 0), (5, 1)], 3: [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11)]}
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
