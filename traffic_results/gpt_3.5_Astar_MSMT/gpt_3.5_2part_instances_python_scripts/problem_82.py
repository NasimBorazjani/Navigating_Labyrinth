
import heapq

def initialize():
    initial_state = ((15, 19, 13, 4, 'x', 'x', 13, 7, 16, 6, 'x', 'x', 17, 'x'), (2, 2, 'x', 7, 'x', 12, 12, 'x', 19, 'x', 10, 4, 14, 2), (11, 'x', 'x', 3, 7, 'x', 7, 'x', 'x', 6, 'x', 19, 'x', 1), ('x', 'x', 11, 'x', 3, 'x', 17, 'x', 1, 20, 17, 8, 15, 1), ('x', 'x', 13, 'x', 12, 17, 5, 4, 'x', 16, 9, 'x', 19, 14), ('x', 16, 'x', 'x', 13, 17, 14, 6, 2, 17, 19, 6, 13, 6), ('x', 1, 'x', 'x', 3, 10, 2, 18, 7, 8, 'x', 8, 'x', 'x'), (12, 2, 1, 6, 11, 7, 10, 'x', 'x', 'x', 4, 2, 8, 'x'), ('x', 'x', 'x', 13, 16, 2, 'x', 6, 9, 2, 11, 7, 14, 6), ('x', 'x', 'x', 'x', 'x', 11, 'x', 16, 'x', 'x', 'x', 'x', 'x', 3), ('x', 'x', 'x', 'x', 10, 'x', 3, 'x', 18, 9, 'x', 'x', 'x', 15), ('x', 'x', 'x', 'x', 10, 'x', 3, 'x', 18, 9, 'x', 'x', 'x', 15), ('x', 'x', 11, 9, 3, 'x', 'x', 16, 'x', 5, 'x', 4, 10, 'x'), (18, 1, 13, 'x', 7, 'x', 7, 5, 'x', 11, 10, 2, 'x', 2), ('x', 'x', 'x', 'x', 'x', 'x', 'x', 11, 'x', 10, 'x', 'x', 14, 6))
    num_rows = 14
    num_cols = 14
    start = (1, 13)
    end = (7, 4)
    districts = {1: [(0, 0), (1, 0)], 2: [(2, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0)], 3: [(3, 0), (4, 0), (5, 0)]}
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
