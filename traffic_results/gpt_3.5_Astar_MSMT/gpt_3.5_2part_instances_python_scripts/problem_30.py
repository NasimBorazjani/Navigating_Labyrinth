
import heapq

def initialize():
    initial_state = ((8, 'x', 'x', 9, 15, 13, 11, 2, 'x', 'x'), (13, 'x', 'x', 'x', 5, 'x', 'x', 7, 'x', 'x'), (12, 3, 'x', 'x', 'x', 'x', 'x', 10, 'x', 'x'), (12, 'x', 'x', 9, 15, 9, 11, 5, 17, 'x'), (3, 5, 12, 'x', 11, 5, 'x', 15, 1, 18), (14, 3, 'x', 'x', 18, 14, 19, 19, 12, 15), ('x', 20, 17, 15, 11, 'x', 'x', 'x', 'x', 'x'), (12, 13, 18, 'x', 'x', 5, 'x', 2, 'x', 13), ('x', 'x', 13, 19, 4, 'x', 12, 'x', 'x', 8), ('x', 'x', 10, 'x', 'x', 'x', 15, 'x', 4, 16))
    num_rows = 10
    num_cols = 10
    start = (4, 9)
    end = (6, 1)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (5, 0)], 3: [(6, 0), (7, 0), (8, 0), (9, 0)]}
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
