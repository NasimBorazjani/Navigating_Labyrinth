
import heapq

def initialize():
    initial_state = ((6, 9, 19, 'x', 5, 9, 'x', 15, 'x'), (8, 10, 16, 'x', 'x', 'x', 5, 11, 4), (5, 11, 20, 1, 14, 16, 7, 1, 5), (10, 5, 3, 5, 12, 8, 'x', 'x', 2), (16, 15, 15, 14, 'x', 13, 10, 'x', 10), (6, 4, 7, 13, 'x', 'x', 'x', 'x', 13), ('x', 1, 6, 3, 'x', 'x', 17, 9, 5), ('x', 11, 'x', 9, 'x', 5, 7, 'x', 'x'), ('x', 'x', 'x', 18, 'x', 2, 'x', 'x', 12))
    num_rows = 9
    num_cols = 9
    start = (1, 8)
    end = (4, 0)
    districts = {1: [(0, 0), (0, 1)], 2: [(2, 0), (4, 1), (6, 2)], 3: [(7, 0), (8, 1), (8, 2)]}
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
