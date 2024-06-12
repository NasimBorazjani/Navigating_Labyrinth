
import heapq

def initialize():
    initial_state = ((9, 4, 16, 7, 'x', 2, 'x', 'x', 14, 'x', 'x', 'x'), ('x', 15, 10, 5, 12, 16, 'x', 'x', 'x', 3, 12, 18), (12, 'x', 'x', 'x', 9, 16, 3, 9, 'x', 'x', 'x', 7), (10, 6, 3, 10, 'x', 'x', 1, 17, 'x', 12, 12, 'x'), (11, 8, 15, 'x', 8, 16, 'x', 'x', 5, 15, 12, 7), ('x', 'x', 'x', 'x', 6, 'x', 11, 19, 17, 17, 10, 20), ('x', 3, 17, 17, 'x', 'x', 18, 4, 'x', 'x', 9, 4), ('x', 1, 5, 17, 8, 15, 4, 17, 5, 6, 9, 11), ('x', 'x', 4, 5, 17, 18, 3, 'x', 9, 1, 11, 2), ('x', 'x', 5, 3, 4, 14, 14, 1, 17, 3, 12, 12), ('x', 15, 9, 7, 3, 'x', 'x', 'x', 'x', 'x', 17, 'x'), ('x', 'x', 13, 16, 6, 'x', 6, 'x', 'x', 'x', 'x', 'x'))
    num_rows = 12
    num_cols = 12
    start = (3, 9)
    end = (7, 1)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (8, 1), (9, 2), (10, 3), (11, 4)], 3: [(9, 0), (10, 1), (11, 2)]}
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
