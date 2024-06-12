
import heapq

def initialize():
    initial_state = ((10, 'x', 'x', 1, 1, 'x', 'x', 'x', 'x', 'x', 'x', 'x'), (11, 9, 17, 'x', 14, 3, 'x', 13, 'x', 'x', 6, 'x'), ('x', 5, 'x', 'x', 10, 13, 13, 19, 10, 'x', 1, 12), (6, 'x', 'x', 17, 5, 6, 17, 4, 5, 'x', 1, 'x'), (4, 11, 1, 'x', 'x', 'x', 14, 7, 19, 4, 'x', 6), ('x', 'x', 6, 18, 'x', 'x', 'x', 5, 8, 2, 1, 'x'), (19, 19, 10, 9, 19, 19, 'x', 6, 'x', 1, 14, 11), ('x', 'x', 'x', 18, 11, 'x', 7, 5, 15, 13, 1, 11), ('x', 4, 'x', 8, 'x', 11, 'x', 'x', 9, 'x', 'x', 15), (10, 8, 10, 2, 'x', 'x', 'x', 'x', 'x', 12, 'x', 17), (19, 'x', 3, 11, 'x', 'x', 9, 3, 15, 'x', 5, 17), (18, 'x', 'x', 'x', 11, 14, 'x', 14, 13, 'x', 'x', 8))
    num_rows = 12
    num_cols = 12
    start = (3, 3)
    end = (8, 11)
    districts = {1: [(0, 0), (0, 1), (0, 2)], 2: [(3, 0), (7, 1), (11, 2)], 3: [(8, 0), (11, 1), (11, 2)]}
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
