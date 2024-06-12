
import heapq

def initialize():
    initial_state = ((7, 'x', 19, 11, 6, 'x', 4, 15, 9, 3), ('x', 'x', 13, 'x', 8, 17, 'x', 'x', 12, 16), ('x', 'x', 2, 'x', 15, 8, 'x', 13, 4, 'x'), (13, 11, 3, 3, 3, 'x', 'x', 'x', 'x', 'x'), (1, 16, 14, 6, 14, 17, 4, 9, 1, 'x'), ('x', 4, 9, 'x', 17, 17, 'x', 13, 2, 9), ('x', 'x', 'x', 'x', 5, 14, 17, 12, 7, 14), ('x', 15, 1, 6, 'x', 'x', 5, 'x', 'x', 1), ('x', 'x', 19, 'x', 'x', 'x', 'x', 'x', 13, 8), ('x', 6, 9, 12, 8, 8, 'x', 18, 'x', 'x'))
    num_rows = 9
    num_cols = 10
    start = (5, 9)
    end = (3, 1)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (4, 1), (4, 2), (4, 3)], 3: [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9)]}
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
