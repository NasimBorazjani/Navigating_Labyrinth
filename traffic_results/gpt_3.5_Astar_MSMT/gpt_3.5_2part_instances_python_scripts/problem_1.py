
import heapq

def initialize():
    initial_state = ((13, 'x', 'x', 3, 10, 20, 3, 'x', 5), ('x', 'x', 'x', 'x', 20, 16, 'x', 'x', 17), (3, 14, 18, 8, 1, 20, 14, 'x', 7), (13, 3, 6, 10, 7, 4, 6, 6, 1), (10, 12, 2, 'x', 11, 'x', 10, 8, 11), ('x', 'x', 'x', 11, 6, 18, 13, 20, 17), ('x', 'x', 16, 'x', 4, 17, 7, 10, 15), ('x', 'x', 16, 6, 19, 4, 7, 'x', 'x'), ('x', 11, 18, 'x', 'x', 'x', 3, 8, 'x'))
    num_rows = 9
    num_cols = 9
    start = (5, 7)
    end = (2, 1)
    districts = {1: [(0, 0), (0, 1), (0, 2)], 2: [(3, 0), (4, 1)], 3: [(5, 0), (8, 1)]}
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
