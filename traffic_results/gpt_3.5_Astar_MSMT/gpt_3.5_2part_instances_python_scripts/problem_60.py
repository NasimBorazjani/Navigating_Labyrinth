
import heapq

def initialize():
    initial_state = ((16, 'x', 5, 6, 'x', 14, 12, 'x', 'x', 'x', 6, 'x'), (17, 'x', 'x', 'x', 5, 'x', 5, 7, 'x', 'x', 8, 'x'), (3, 19, 'x', 'x', 'x', 'x', 18, 'x', 13, 7, 'x', 'x'), (13, 'x', 4, 'x', 'x', 8, 7, 4, 'x', 15, 'x', 'x'), (5, 17, 18, 12, 3, 'x', 14, 2, 4, 18, 'x', 1), (4, 10, 1, 19, 10, 'x', 'x', 17, 'x', 17, 16, 4), (7, 'x', 16, 'x', 'x', 1, 3, 'x', 13, 13, 'x', 'x'), ('x', 'x', 9, 1, 7, 18, 16, 3, 'x', 4, 'x', 'x'), (2, 'x', 13, 10, 'x', 4, 'x', 'x', 'x', 'x', 12, 'x'), ('x', 'x', 'x', 18, 8, 4, 'x', 11, 'x', 14, 18, 'x'), ('x', 19, 2, 'x', 2, 6, 5, 18, 'x', 5, 'x', 'x'), ('x', 2, 'x', 7, 'x', 'x', 8, 7, 'x', 11, 16, 'x'))
    num_rows = 12
    num_cols = 12
    start = (3, 0)
    end = (9, 7)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (8, 1), (11, 2)], 3: [(9, 0), (10, 1), (11, 3)]}
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
