
import heapq

def initialize():
    initial_state = ((9, 'x', 'x', 20, 3, 9), (17, 11, 17, 'x', 9, 2, 7, 'x', 15), ('x', 4, 2, 19, 12, 6, 'x', 4, 17), (15, 'x', 'x', 15, 11, 19, 'x', 9, 5), (3, 9, 19, 15, 2, 'x', 'x', 18, 'x'), (19, 5, 9, 11, 9, 'x', 'x', 3, 'x'), ('x', 'x', 2, 8, 8, 'x', 'x', 'x', 19), ('x', 'x', 14, 'x', 'x', 'x', 18, 'x', 18), ('x', 14, 18, 7, 8, 'x', 10, 15, 'x'))
    num_rows = 9
    num_cols = 9
    start = (3, 7)
    end = (5, 0)
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
