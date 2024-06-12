
import heapq

def initialize():
    initial_state = ((19, 'x', 7, 'x', 12, 'x', 15, 5, 19, 14), (17, 'x', 3, 5, 7, 'x', 'x', 'x', 17, 20), ('x', 11, 15, 8, 'x', 16, 4, 'x', 1, 1), ('x', 8, 19, 4, 3, 3, 3, 17, 8, 15), (13, 10, 17, 17, 6, 1, 'x', 8, 13, 20), (20, 'x', 'x', 'x', 'x', 4, 18, 4, 17, 'x'), (5, 'x', 'x', 10, 'x', 'x', 14, 2, 5, 'x'), (7, 'x', 4, 'x', 'x', 'x', 15, 'x', 'x', 'x'), (18, 'x', 18, 'x', 4, 'x', 'x', 'x', 17, 'x'), ('x', 'x', 'x', 'x', 'x', 'x', 'x', 13, 'x', 'x'))
    num_rows = 10
    num_cols = 10
    start = (6, 0)
    end = (4, 9)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (5, 0)], 3: [(6, 0), (7, 0), (8, 0), (9, 0)]}
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
