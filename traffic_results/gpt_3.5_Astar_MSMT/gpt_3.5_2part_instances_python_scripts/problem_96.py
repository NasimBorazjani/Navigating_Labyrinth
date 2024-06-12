
import heapq

def initialize():
    initial_state = ((9, 'x', 10, 'x', 11, 13, 5, 4, 'x', 'x', 19, 13, 'x', 'x'), (6, 3, 8, 18, 8, 1, 5, 2, 'x', 'x', 17, 'x', 'x', 'x'), ('x', 11, 5, 11, 13, 20, 7, 'x', 'x', 'x', 'x', 15, 4), (3, 14, 4, 20, 4, 15, 12, 12, 4, 'x', 8, 4, 'x', 'x'), (1, 'x', 9, 17, 'x', 17, 'x', 11, 16, 6, 12, 'x', 18, 'x'), (5, 17, 'x', 1, 'x', 'x', 19, 14, 2, 1, 'x', 'x', 'x', 'x'), (11, 'x', 14, 'x', 'x', 'x', 'x', 'x', 2, 12, 4, 16, 'x', 'x'), ('x', 2, 'x', 6, 6, 8, 'x', 11, 18, 11, 10, 'x', 'x', 'x'), ('x', 'x', 16, 7, 'x', 'x', 'x', 7, 11, 18, 9, 17, 'x', 'x'), (13, 19, 13, 'x', 18, 'x', 14, 'x', 14, 14, 'x', 'x', 20, 15, 15), ('x', 'x', 'x', 17, 'x', 8, 'x', 'x', 'x', 'x', 'x', 6, 11, 'x'), ('x', 7, 'x', 15, 'x', 'x', 19, 1, 'x', 'x', 10, 'x', 'x', 18), (11, 19, 'x', 18, 5, 'x', 19, 16, 'x', 'x', 13, 'x', 'x', 5), (8, 16, 6, 13, 1, 'x', 14, 4, 'x', 'x', 1, 'x', 'x', 5), ('x', 19, 5, 'x', 'x', 'x', 12, 5, 9, 16, 11, 9, 14, 'x', 'x'))
    num_rows = 15
    num_cols = 15
    start = (8, 13)
    end = (3, 3)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3)], 2: [(4, 0), (4, 1), (4, 2), (4, 3)], 3: [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14)]}
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
