
import heapq

def initialize():
    initial_state = ((4, 1, 20, 15, 9, 'x', 8, 6, 'x', 'x', 14, 'x'), (5, 11, 9, 12, 10, 4, 15, 18, 7, 'x', 'x', 13), (15, 9, 1, 'x', 18, 3, 1, 19, 'x', 'x', 17, 17), ('x', 17, 11, 10, 'x', 19, 8, 'x', 'x', 'x', 'x', 7), (5, 'x', 1, 'x', 14, 13, 4, 8, 5, 'x', 13, 14), (16, 6, 'x', 'x', 'x', 17, 'x', 15, 4, 'x', 'x', 15), ('x', 'x', 'x', 15, 'x', 19, 10, 'x', 16, 18, 11, 1), (6, 8, 'x', 3, 'x', 5, 5, 'x', 3, 8, 9, 14), (10, 14, 'x', 'x', 'x', 'x', 'x', 'x', 6, 2, 'x', 'x'), (12, 'x', 'x', 6, 11, 4, 'x', 'x', 12, 'x', 4, 16), (4, 'x', 'x', 'x', 11, 'x', 'x', 'x', 18, 16, 'x', 10), ('x', 6, 'x', 'x', 11, 'x', 5, 13, 8, 1, 17, 9))
    num_rows = 12
    num_cols = 12
    start = (2, 0)
    end = (7, 8)
    districts = {1: [(0, 0), (1, 0)], 2: [(2, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0)], 3: [(11, 0)]}
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
