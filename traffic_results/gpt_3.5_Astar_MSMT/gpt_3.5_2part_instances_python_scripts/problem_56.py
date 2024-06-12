
import heapq

def initialize():
    initial_state = ((2, 'x', 'x', 14, 'x', 19, 6, 'x', 'x', 14, 18, 'x'), ('x', 10, 1, 15, 'x', 'x', 'x', 'x', 17, 2, 9, 12), (13, 14, 'x', 2, 'x', 'x', 10, 10, 'x', 'x', 'x', 'x'), (9, 17, 3, 15, 4, 4, 'x', 9, 15, 16, 'x', 9), (10, 7, 3, 8, 'x', 7, 'x', 16, 3, 7, 'x', 'x'), (16, 20, 16, 19, 18, 3, 'x', 'x', 11, 14, 5, 'x'), (14, 13, 8, 14, 12, 19, 6, 3, 19, 10, 11, 'x'), ('x', 18, 'x', 'x', 4, 19, 6, 14, 15, 17, 7, 'x'), ('x', 2, 'x', 'x', 'x', 'x', 'x', 7, 'x', 19, 'x', 'x'), ('x', 3, 14, 1, 'x', 18, 4, 12, 'x', 3, 10, 'x'), (2, 'x', 16, 13, 'x', 17, 'x', 'x', 17, 16, 4, 10), ('x', 4, 10, 'x', 'x', 'x', 7, 'x', 19, 7, 'x', 'x'))
    num_rows = 12
    num_cols = 12
    start = (6, 9)
    end = (3, 0)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)], 3: [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11)]}
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
