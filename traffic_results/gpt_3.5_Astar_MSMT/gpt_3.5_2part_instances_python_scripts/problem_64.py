
import heapq

def initialize():
    initial_state = ((8, 'x', 12, 'x', 16, 'x', 'x', 'x', 'x', 'x', 'x', 7, 'x', 'x'), ('x', 'x', 'x', 'x', 16, 'x', 7, 8, 'x', 17, 'x', 19, 'x', 'x'), (7, 'x', 13, 'x', 19, 'x', 6, 'x', 14, 'x', 18, 'x', 19, 'x'), (9, 20, 2, 'x', 10, 6, 'x', 18, 'x', 'x', 'x', 18, 'x', 'x'), ('x', 'x', 8, 12, 7, 14, 13, 9, 8, 6, 14, 11, 7, 'x'), ('x', 14, 'x', 'x', 'x', 19, 13, 15, 3, 12, 16, 16, 3, 'x'), ('x', 'x', 'x', 13, 'x', 9, 13, 10, 'x', 14, 'x', 4, 18, 'x'), (6, 12, 10, 'x', 'x', 18, 7, 20, 18, 'x', 13, 1, 'x', 'x'), ('x', 5, 'x', 18, 12, 'x', 'x', 3, 12, 14, 19, 16, 'x', 'x'), (10, 'x', 19, 'x', 'x', 'x', 'x', 11, 14, 16, 12, 'x', 8, 'x'), (8, 'x', 'x', 'x', 'x', 'x', 'x', 9, 16, 15, 'x', 'x', 8, 'x'), ('x', 'x', 2, 'x', 1, 'x', 'x', 16, 'x', 'x', 3, 'x', 'x', 'x'), (9, 'x', 5, 'x', 'x', 15, 'x', 'x', 'x', 7, 15, 9, 'x', 'x'))
    num_rows = 14
    num_cols = 14
    start = (3, 0)
    end = (6, 12)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (5, 0)], 3: [(6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0)]}
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
