
import heapq

def initialize():
    initial_state = ((13, 13, 16, 8, 'x', 19, 1, 18, 13, 8, 'x', 7, 'x'), ('x', 13, 'x', 15, 'x', 12, 20, 1, 13, 19, 4, 17, 'x'), ('x', 12, 9, 11, 13, 12, 2, 12, 19, 5, 19, 16, 8), ('x', 12, 18, 19, 'x', 7, 'x', 12, 3, 2, 'x', 16, 11), ('x', 7, 'x', 'x', 8, 13, 15, 3, 1, 'x', 15, 15, 'x'), (11, 9, 'x', 16, 2, 10, 1, 2, 16, 1, 'x', 10, 12), ('x', 'x', 9, 9, 7, 'x', 6, 'x', 'x', 10, 7, 2, 'x'), ('x', 13, 10, 8, 1, 11, 'x', 'x', 'x', 'x', 'x', 'x', 'x'), (11, 14, 'x', 'x', 'x', 'x', 4, 8, 'x', 'x', 18, 'x', 'x'), (13, 14, 'x', 10, 'x', 'x', 16, 'x', 'x', 'x', 'x', 'x', 'x'), ('x', 'x', 16, 'x', 10, 'x', 17, 'x', 12, 'x', 10, 'x', 5), (9, 'x', 10, 'x', 19, 16, 'x', 14, 16, 12, 15, 7, 'x'), (1, 'x', 8, 10, 14, 'x', 6, 9, 'x', 'x', 8, 11, 11))
    num_rows = 13
    num_cols = 13
    start = (3, 12)
    end = (6, 2)
    districts = {1: [(0, 0), (1, 1)], 2: [(2, 0), (5, 5)], 3: [(6, 0), (12, 12)]}
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
