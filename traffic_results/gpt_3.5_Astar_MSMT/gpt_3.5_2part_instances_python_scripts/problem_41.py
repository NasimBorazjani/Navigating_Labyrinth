
import heapq

def initialize():
    initial_state = ((19, 7, 11, 'x', 3, 18, 8, 'x', 'x', 'x', 'x'), (12, 18, 6, 1, 13, 12, 14, 11, 13, 5, 19), (11, 10, 10, 18, 15, 'x', 12, 'x', 4, 17, 10), (4, 3, 3, 7, 'x', 19, 'x', 'x', 'x', 12, 9), ('x', 'x', 6, 19, 'x', 4, 14, 'x', 9, 4, 15), (4, 7, 6, 5, 8, 'x', 15, 3, 'x', 16, 3), (13, 'x', 'x', 1, 9, 1, 9, 'x', 'x', 'x', 'x'), (2, 13, 5, 9, 5, 'x', 6, 'x', 18, 'x', 3), (19, 'x', 2, 9, 4, 13, 'x', 'x', 'x', 16, 6), ('x', 'x', 'x', 12, 'x', 7, 9, 3, 9, 8, 1), ('x', 10, 'x', 12, 3, 6, 'x', 4, 12, 4, 'x'))
    num_rows = 11
    num_cols = 11
    start = (5, 10)
    end = (3, 0)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0)], 3: [(5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0)]}
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
