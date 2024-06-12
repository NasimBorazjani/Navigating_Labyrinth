
import heapq

def initialize():
    initial_state = ((8, 15, 3, 10, 6, 15, 'x', 4, 'x', 'x', 'x', 'x', 'x', 4), (3, 'x', 14, 8, 16, 19, 'x', 18, 4, 'x', 2, 'x', 6, 'x'), (18, 18, 'x', 4, 'x', 17, 11, 10, 17, 9, 'x', 4, 1, 5), ('x', 2, 'x', 12, 1, 'x', 13, 17, 14, 15, 17, 'x', 15, 'x'), ('x', 'x', 'x', 15, 'x', 2, 2, 11, 7, 'x', 5, 7, 4, 18), (16, 'x', 5, 'x', 19, 12, 5, 9, 13, 16, 9, 'x', 3, 'x'), ('x', 'x', 'x', 'x', 14, 18, 'x', 16, 13, 'x', 1, 5, 10, 'x'), (3, 11, 'x', 1, 8, 'x', 'x', 'x', 18, 8, 11, 'x', 'x', 6), (19, 2, 'x', 19, 5, 'x', 'x', 'x', 9, 'x', 6, 'x', 'x', 4), ('x', 2, 'x', 10, 9, 15, 'x', 'x', 'x', 16, 'x', 8, 'x', 'x'), (18, 8, 10, 'x', 3, 'x', 11, 'x', 17, 'x', 17, 'x', 'x', 'x'), (14, 12, 'x', 2, 'x', 19, 2, 19, 14, 'x', 'x', 'x', 3, 'x'), (7, 'x', 'x', 'x', 'x', 'x', 'x', 9, 8, 7, 'x', 15, 2, 'x'), ('x', 'x', 15, 'x', 'x', 15, 16, 'x', 'x', 'x', 19, 'x', 13, 1))
    num_rows = 14
    num_cols = 14
    start = (2, 0)
    end = (6, 11)
    districts = {1: [(0, 0), (0, 1), (0, 2)], 2: [(3, 0), (3, 1), (3, 2)], 3: [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11)]}
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