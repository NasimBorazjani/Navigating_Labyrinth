
import heapq

def initialize():
    initial_state = ((17, 'x', 'x', 'x', 5, 'x', 'x', 12, 16, 'x', 'x', 5, 16), ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 12, 4, 6), (9, 'x', 'x', 'x', 'x', 'x', 19, 'x', 'x', 13, 6, 11, 19), (1, 'x', 'x', 'x', 13, 'x', 'x', 'x', 3, 2, 7, 4, 3), ('x', 'x', 'x', 14, 19, 20, 10, 13, 14, 2, 'x', 9, 3), (15, 'x', 11, 7, 'x', 11, 6, 16, 'x', 'x', 'x', 8, 19), (19, 16, 4, 8, 5, 5, 5, 11, 10, 17, 9, 'x', 5), ('x', 3, 17, 'x', 'x', 6, 17, 19, 'x', 'x', 14, 'x', 'x'), ('x', 'x', 'x', 'x', 'x', 14, 'x', 10, 14, 13, 'x', 13, 'x'), (15, 5, 4, 'x', 'x', 'x', 'x', 2, 12, 6, 'x', 16, 14), (10, 'x', 'x', 'x', 9, 'x', 'x', 'x', 'x', 'x', 13, 2, 'x'), ('x', 'x', 17, 'x', 'x', 'x', 'x', 7, 'x', 'x', 16, 'x', 'x'), (12, 10, 'x', 15, 16, 'x', 'x', 7, 11, 7, 'x', 17, 'x'))
    num_rows = 13
    num_cols = 13
    start = (1, 12)
    end = (6, 3)
    districts = {1: [(0, 0), (0, 1)], 2: [(2, 0), (5, 5)], 3: [(6, 0), (12, 12)]}
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
