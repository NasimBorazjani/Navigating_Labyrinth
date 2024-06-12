
import heapq

def initialize():
    initial_state = ((16, 'x', 5, 13, 'x', 'x', 2, 'x', 6, 'x', 'x'), ('x', 'x', 17, 'x', 15, 'x', 10, 'x', 5, 17, 'x'), ('x', 'x', 'x', 'x', 15, 3, 10, 2, 4, 13, 14), ('x', 'x', 'x', 'x', 17, 2, 4, 'x', 1, 4, 5), (2, 'x', 'x', 2, 6, 17, 'x', 'x', 'x', 4, 19), (19, 5, 'x', 'x', 'x', 'x', 10, 12, 1, 18, 10), ('x', 3, 'x', 12, 'x', 10, 15, 11, 'x', 4, 15), (2, 'x', 11, 9, 'x', 12, 11, 'x', 15, 10, 6), (19, 'x', 16, 5, 'x', 'x', 'x', 11, 'x', 11, 8), (12, 2, 'x', 3, 'x', 4, 'x', 'x', 15, 'x', 'x'), ('x', 'x', 18, 16, 'x', 'x', 4, 'x', 12, 13, 'x'))
    num_rows = 11
    num_cols = 11
    start = (8, 10)
    end = (3, 4)
    districts = {1: [(0, 0), (0, 1), (0, 2)], 2: [(3, 0), (7, 1), (10, 2)], 3: [(8, 0), (10, 1), (10, 3)]}
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
