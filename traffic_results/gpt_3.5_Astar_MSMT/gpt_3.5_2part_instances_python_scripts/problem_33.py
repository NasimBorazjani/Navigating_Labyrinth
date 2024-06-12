
import heapq

def initialize():
    initial_state = ((16, 10, 'x', 16, 1, 12, 6, 12, 3, 7, 'x'), ('x', 16, 10, 9, 12, 19, 7, 10, 12, 13, 7), (5, 'x', 9, 'x', 5, 16, 16, 8, 'x', 16, 8), ('x', 4, 14, 'x', 'x', 'x', 'x', 'x', 'x', 7, 18), (13, 12, 16, 14, 'x', 2, 4, 2, 'x', 6, 3), ('x', 11, 20, 'x', 'x', 'x', 1, 'x', 'x', 9, 'x'), ('x', 'x', 8, 10, 'x', 'x', 3, 1, 'x', 'x', 6), ('x', 2, 9, 'x', 8, 13, 'x', 'x', 'x', 12, 11), (12, 'x', 2, 'x', 'x', 1, 6, 'x', 15, 'x', 1), (3, 'x', 'x', 'x', 17, 'x', 18, 4, 1, 'x', 'x'), ('x', 'x', 6, 'x', 'x', 12, 'x', 'x', 'x', 15, 12))
    num_rows = 11
    num_cols = 11
    start = (2, 10)
    end = (5, 2)
    districts = {1: [(0, 0), (1, 1)], 2: [(2, 0), (4, 1), (3, 2), (5, 3), (6, 4)], 3: [(7, 0), (10, 1), (8, 2), (9, 3)]}
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
