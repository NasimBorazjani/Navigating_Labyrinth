
import heapq

def initialize():
    initial_state = ((5, 15, 15, 5, 6, 19, 'x', 9, 2, 'x', 16, 'x', 15), (16, 'x', 'x', 7, 5, 'x', 'x', 'x', 5, 2, 19, 'x', 3), ('x', 11, 2, 19, 17, 5, 11, 6, 3, 18, 15, 16, 'x'), (2, 'x', 12, 'x', 20, 11, 7, 19, 2, 'x', 4, 14, 'x'), (3, 'x', 19, 'x', 11, 19, 'x', 14, 'x', 12, 'x', 18, 7), (6, 'x', 5, 8, 3, 12, 12, 11, 5, 14, 'x', 6, 'x'), ('x', 'x', 13, 2, 'x', 20, 'x', 'x', 'x', 18, 18, 'x', 3), ('x', 'x', 13, 1, 10, 18, 'x', 'x', 'x', 'x', 10, 'x', 15), (10, 'x', 9, 2, 17, 19, 16, 8, 'x', 18, 10, 'x', 13), ('x', 'x', 2, 8, 2, 7, 'x', 17, 'x', 1, 'x', 9, 'x'), ('x', 13, 'x', 19, 15, 3, 15, 13, 1, 12, 4, 7, 'x'), (14, 'x', 'x', 'x', 'x', 'x', 'x', 16, 'x', 15, 'x', 'x', 'x'), (3, 15, 'x', 6, 'x', 9, 'x', 'x', 9, 1, 6, 'x', 5))
    num_rows = 13
    num_cols = 13
    start = (8, 2)
    end = (2, 9)
    districts = {1: [(0, 0), (0, 1), (0, 2)], 2: [(1, 3), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (12, 5)], 3: [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11), (8, 12)]}
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
