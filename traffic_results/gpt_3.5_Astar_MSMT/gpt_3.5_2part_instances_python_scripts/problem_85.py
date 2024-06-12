
import heapq

def initialize():
    initial_state = ((5, 10, 'x', 'x', 'x', 16, 'x', 'x', 16, 'x', 10, 8, 'x'), (1, 'x', 13, 'x', 7, 'x', 'x', 'x', 10, 3, 3, 13, 18, 11), (14, 'x', 'x', 'x', 9, 16, 16, 15, 'x', 'x', 15, 'x', 4, 4), (15, 'x', 3, 'x', 'x', 17, 'x', 16, 10, 9, 'x', 6, 16, 17), (12, 8, 'x', 10, 'x', 'x', 13, 10, 'x', 'x', 6, 3, 'x', 1), ('x', 'x', 'x', 5, 8, 9, 6, 14, 1, 'x', 'x', 2, 12, 'x'), (13, 'x', 'x', 'x', 16, 6, 'x', 17, 12, 18, 'x', 17, 8, 'x'), (10, 'x', 14, 15, 'x', 'x', 'x', 20, 'x', 17, 18, 8, 'x', 4), ('x', 11, 3, 'x', 'x', 'x', 'x', 7, 'x', 4, 'x', 'x', 11, 2), (7, 'x', 'x', 10, 'x', 19, 'x', 7, 17, 'x', 'x', 14, 'x', 15), (12, 11, 'x', 'x', 9, 7, 'x', 15, 1, 5, 5, 11, 15, 'x'), ('x', 9, 9, 'x', 'x', 'x', 'x', 8, 'x', 8, 19, 11, 12, 12), ('x', 17, 5, 'x', 'x', 17, 'x', 'x', 12, 'x', 15, 12, 10, 'x'), (18, 'x', 'x', 'x', 3, 'x', 7, 'x', 8, 5, 12, 8, 10, 'x'))
    num_rows = 14
    num_cols = 14
    start = (10, 12)
    end = (4, 3)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)], 2: [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4)], 3: [(10, 0), (10, 1), (10, 2), (10, 3)]}
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
