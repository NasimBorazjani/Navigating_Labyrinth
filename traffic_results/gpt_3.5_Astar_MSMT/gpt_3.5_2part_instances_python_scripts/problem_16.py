
import heapq

def initialize():
    initial_state = ((16, 'x', 'x', 1, 13, 17, 7, 14, 'x'), (10, 'x', 12, 'x', 13, 'x', 8, 19, 4), (9, 13, 'x', 'x', 15, 'x', 'x', 16, 'x'), (3, 8, 'x', 16, 12, 'x', 'x', 13, 'x'), (13, 'x', 1, 15, 18, 8, 10, 'x', 'x'), (8, 1, 2, 14, 'x', 8, 4, 'x', 11), (14, 13, 15, 'x', 16, 13, 2, 'x', 19), ('x', 4, 10, 'x', 16, 'x', 11, 'x', 'x'), ('x', 14, 'x', 'x', 'x', 18, 6, 18, 'x'), ('x', 3, 2, 6, 7, 'x', 9, 8, 5))
    num_rows = 10
    num_cols = 9
    start = (5, 1)
    end = (3, 9)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (4, 1)], 3: [(6, 0), (9, 1)]}
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
