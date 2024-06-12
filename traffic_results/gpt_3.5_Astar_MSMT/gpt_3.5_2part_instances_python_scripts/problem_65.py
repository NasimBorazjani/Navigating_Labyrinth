
import heapq

def initialize():
    initial_state = ((11, 'x', 'x', 'x', 15, 5, 18, 4, 1, 17, 14, 'x', 9), ('x', 10, 10, 7, 12, 12, 6, 'x', 'x', 8, 4, 19, 11), (17, 'x', 'x', 12, 8, 'x', 'x', 'x', 14, 19, 'x', 18, 16), (17, 'x', 16, 'x', 'x', 17, 4, 'x', 15, 'x', 'x', 'x', 17), (17, 'x', 'x', 6, 'x', 'x', 12, 6, 10, 3, 11, 'x', 19), (10, 'x', 9, 15, 17, 4, 'x', 'x', 'x', 'x', 14, 17, 18), (4, 'x', 'x', 'x', 'x', 13, 18, 13, 'x', 17, 12, 'x', 19), ('x', 2, 11, 7, 6, 14, 9, 'x', 12, 17, 9, 13, 14), ('x', 18, 16, 'x', 'x', 'x', 11, 6, 12, 'x', 'x', 10, 'x'), (5, 3, 'x', 'x', 'x', 5, 'x', 14, 'x', 'x', 'x', 'x', 'x'), (18, 'x', 'x', 'x', 'x', 14, 'x', 'x', 13, 1, 3, 'x', 'x'), (1, 16, 10, 'x', 'x', 14, 13, 'x', 10, 'x', 1, 'x', 18), (8, 'x', 'x', 10, 2, 10, 'x', 'x', 'x', 'x', 'x', 13, 5))
    num_rows = 13
    num_cols = 13
    start = (8, 11)
    end = (2, 3)
    districts = {1: [(0, 0), (0, 1), (0, 2)], 2: [(3, 0), (7, 1), (12, 2)], 3: [(8, 0), (12, 1)]}
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
