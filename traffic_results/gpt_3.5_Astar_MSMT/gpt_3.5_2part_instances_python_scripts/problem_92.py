
import heapq

def initialize():
    initial_state = ((15, 1, 'x', 3, 'x', 9, 15, 8, 17, 'x', 'x', 6, 'x', 12, 3), ('x', 'x', 'x', 14, 'x', 7, 18, 6, 14, 2, 19, 15, 'x', 'x', 'x'), (4, 3, 'x', 10, 8, 4, 16, 13, 6, 'x', 18, 10, 14, 'x', 'x'), ('x', 'x', 'x', 10, 'x', 14, 10, 7, 'x', 'x', 'x', 4, 2, 19, 3), (5, 'x', 10, 'x', 18, 12, 20, 15, 'x', 'x', 11, 11, 1, 10, 19), (8, 'x', 13, 'x', 'x', 'x', 16, 7, 3, 'x', 'x', 2, 18, 11, 'x'), (12, 'x', 15, 'x', 'x', 6, 'x', 'x', 'x', 'x', 18, 3, 14, 3, 6), ('x', 6, 13, 19, 19, 'x', 7, 12, 18, 5, 'x', 1, 4, 18, 11), (5, 'x', 18, 'x', 12, 4, 3, 7, 'x', 16, 1, 'x', 16, 2, 'x'), ('x', 'x', 'x', 'x', 18, 'x', 'x', 14, 15, 1, 'x', 'x', 9, 'x', 'x'), ('x', 13, 'x', 7, 7, 'x', 'x', 16, 10, 'x', 'x', 'x', 'x', 8, 'x'), ('x', 'x', 19, 18, 8, 18, 'x', 'x', 12, 'x', 13, 'x', 17, 12, 7), ('x', 'x', 'x', 'x', 7, 7, 13, 17, 'x', 'x', 'x', 'x', 'x', 9, 5), (9, 'x', 14, 'x', 9, 'x', 8, 'x', 'x', 'x', 17, 4, 12, 12, 12), (8, 1, 11, 'x', 'x', 'x', 'x', 'x', 15, 'x', 'x', 2, 16, 'x', 15))
    num_rows = 15
    num_cols = 15
    start = (7, 14)
    end = (2, 4)
    districts = {1: [(0, 0), (0, 1), (0, 2)], 2: [(1, 3), (1, 4), (1, 5)], 3: [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (7, 13), (7, 14)]}
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
