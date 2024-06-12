
import heapq

def initialize():
    initial_state = ((19, 'x', 17, 14, 3, 'x', 10, 5, 2), ('x', 'x', 1, 'x', 'x', 'x', 19, 7, 1), (16, 12, 'x', 3, 19, 2, 14, 1, 14), ('x', 1, 16, 'x', 12, 3, 13, 'x', 3), ('x', 'x', 7, 19, 10, 'x', 5, 'x', 19), (5, 'x', 'x', 6, 14, 'x', 'x', 10, 12), ('x', 'x', 'x', 'x', 18, 'x', 'x', 15, 12), ('x', 'x', 16, 8, 'x', 3, 4, 'x', 'x'), ('x', 'x', 'x', 16, 'x', 'x', 8, 14, 7))
    num_rows = 9
    num_cols = 9
    start = (3, 1)
    end = (5, 8)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (4, 1), (4, 2), (4, 3)], 3: [(5, 0), (5, 1), (5, 2), (5, 3), (6, 0), (6, 1), (6, 2), (6, 3), (7, 0), (7, 1), (7, 2), (7, 3), (8, 0), (8, 1), (8, 2), (8, 3)]}
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
