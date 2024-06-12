
import heapq

def initialize():
    initial_state = ((15, 8, 18, 3, 19, 'x', 17, 'x', 'x', 'x', 'x'), (19, 16, 'x', 18, 20, 2, 5, 7, 11, 12, 3), (18, 'x', 18, 1, 2, 'x', 'x', 'x', 12, 16, 4), (9, 20, 4, 19, 5, 15, 'x', 'x', 'x', 6, 4), ('x', 18, 8, 1, 'x', 7, 1, 7, 10, 1, 4), ('x', 18, 'x', 18, 19, 9, 18, 5, 15, 1, 7), (3, 'x', 12, 14, 'x', 'x', 'x', 'x', 1, 'x', 'x'), ('x', 12, 6, 'x', 6, 'x', 1, 'x', 1, 7, 'x'), ('x', 5, 10, 14, 2, 'x', 'x', 7, 11, 3, 'x'), (6, 9, 13, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 3), (19, 12, 'x', 15, 'x', 14, 'x', 9, 'x', 'x', 19))
    num_rows = 11
    num_cols = 11
    start = (3, 1)
    end = (5, 10)
    districts = {1: [(0, 0), (0, 1), (0, 2)], 2: [(3, 0), (4, 1)], 3: [(5, 0), (10, 1)]}
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
