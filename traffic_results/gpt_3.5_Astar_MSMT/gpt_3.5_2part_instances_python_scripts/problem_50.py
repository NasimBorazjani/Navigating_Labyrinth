
import heapq

def initialize():
    initial_state = ((12, 17, 10, 'x', 'x', 'x', 'x', 9, 15, 5, 'x', 'x'), ('x', 'x', 'x', 'x', 'x', 12, 20, 9, 19, 8, 12, 11), (9, 'x', 'x', 2, 'x', 2, 1, 9, 8, 14, 16, 'x'), (19, 'x', 1, 20, 7, 9, 18, 'x', 18, 7, 'x', 'x'), (5, 2, 11, 9, 'x', 5, 4, 16, 'x', 1, 'x', 10), (10, 8, 8, 4, 11, 11, 'x', 'x', 5, 'x', 'x', 'x'), (15, 15, 'x', 'x', 13, 5, 19, 'x', 'x', 15, 'x', 'x'), (15, 16, 9, 18, 'x', 'x', 16, 'x', 'x', 'x', 5, 12), ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'), ('x', 'x', 14, 14, 'x', 'x', 15, 6, 6, 'x', 'x', 'x'), ('x', 'x', 'x', 'x', 'x', 8, 14, 'x', 5, 'x', 'x', 15), ('x', 6, 15, 'x', 'x', 'x', 'x', 'x', 'x', 8, 'x', 'x'))
    num_rows = 12
    num_cols = 12
    start = (3, 9)
    end = (7, 1)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 5), (4, 6), (4, 7)], 3: [(7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11), (11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5)]}
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
