
import heapq

def initialize():
    initial_state = ((11, 5, 18, 'x', 14, 7, 'x', 15, 11, 14), ('x', 'x', 'x', 'x', 13, 13, 11, 17, 8, 13, 'x'), (8, 1, 5, 17, 'x', 4, 8, 20, 7, 4), (10, 'x', 'x', 18, 1, 'x', 'x', 20, 'x', 'x'), (18, 15, 'x', 6, 'x', 4, 3, 4, 3, 13, 'x'), (5, 1, 'x', 4, 'x', 'x', 'x', 11, 'x', 14, 18), (19, 19, 'x', 'x', 'x', 'x', 15, 'x', 10, 'x', 'x'), (15, 5, 7, 'x', 14, 6, 'x', 'x', 'x', 13, 'x'), (18, 7, 'x', 19, 'x', 12, 'x', 'x', 15, 'x', 'x'), (10, 9, 'x', 1, 'x', 'x', 15, 'x', 11, 'x', 2), ('x', 'x', 8, 'x', 19, 'x', 1, 3, 'x', 'x', 8))
    num_rows = 11
    num_cols = 11
    start = (7, 0)
    end = (3, 8)
    districts = {1: [(0, 0), (1, 0)], 2: [(2, 0), (6, 0)], 3: [(7, 0), (10, 0)]}
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
