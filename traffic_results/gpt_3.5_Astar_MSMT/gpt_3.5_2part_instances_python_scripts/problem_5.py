
import heapq

def initialize():
    initial_state = ((8, 'x', 4, 7, 10, 'x', 12, 5, 'x'), ('x', 'x', 4, 11, 16, 4, 12, 15, 'x'), (3, 'x', 16, 16, 4, 'x', 'x', 'x', 'x'), (11, 6, 3, 12, 8, 2, 19, 14, 'x'), (20, 18, 19, 'x', 4, 18, 'x', 15, 13), (8, 15, 'x', 16, 11, 'x', 10, 14, 1), ('x', 'x', 'x', 19, 'x', 'x', 'x', 'x', 'x'), (7, 'x', 'x', 'x', 'x', 'x', 1, 7, 8), (15, 3, 'x', 'x', 'x', 'x', 'x', 'x', 'x'))
    num_rows = 9
    num_cols = 9
    start = (5, 0)
    end = (3, 7)
    districts = {1: [(0, 0), (0, 2), (1, 2), (2, 0), (2, 2), (3, 0), (3, 1)], 2: [(4, 0), (4, 2), (5, 2), (6, 0), (6, 1)], 3: [(5, 1), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]}
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
