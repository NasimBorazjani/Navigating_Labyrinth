
import heapq

def initialize():
    initial_state = ((19, 14, 16, 4, 15, 16, 15, 'x', 9, 'x', 'x', 'x'), ('x', 7, 12, 6, 'x', 12, 'x', 3, 'x', 14, 5, 9), (1, 12, 'x', 'x', 12, 'x', 'x', 'x', 'x', 'x', 10, 1), ('x', 1, 15, 14, 'x', 2, 13, 'x', 'x', 'x', 10, 9), (7, 'x', 13, 'x', 14, 1, 14, 8, 'x', 'x', 8, 5), (18, 'x', 8, 13, 12, 13, 'x', 12, 3, 'x', 14, 'x'), ('x', 15, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 17, 10), ('x', 5, 'x', 4, 'x', 'x', 'x', 3, 5, 6, 6, 11), ('x', 15, 6, 'x', 4, 18, 'x', 'x', 14, 10, 2, 8), (13, 10, 13, 7, 3, 6, 'x', 'x', 10, 17, 10, 15), (4, 'x', 'x', 7, 19, 4, 13, 13, 12, 'x', 'x', 13), (5, 'x', 'x', 9, 19, 18, 'x', 'x', 16, 'x', 2, 'x'))
    num_rows = 12
    num_cols = 12
    start = (4, 11)
    end = (9, 2)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (8, 1), (11, 2)], 3: [(9, 0), (11, 1), (11, 3)]}
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
