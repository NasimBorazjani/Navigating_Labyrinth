
import heapq

def initialize():
    initial_state = ((6, 9, 'x', 'x', 10, 14, 7, 3, 12), (11, 3, 14, 16, 17, 1, 4, 14, 8, 16), (3, 'x', 6, 1, 18, 16, 'x', 6, 3, 11), (11, 4, 8, 'x', 1, 3, 9, 8, 7), (3, 'x', 'x', 8, 14, 18, 'x', 'x', 18), (1, 'x', 14, 'x', 'x', 'x', 3, 4, 20), ('x', 14, 19, 15, 'x', 'x', 3, 16, 15), (6, 18, 'x', 'x', 16, 1, 3, 'x', 11), (3, 15, 19, 10, 'x', 'x', 'x', 'x', 'x'), (9, 'x', 'x', 17, 17, 'x', 16, 'x', 13), (8, 'x', 1, 'x', 'x', 'x', 19, 19, 1), (9, 'x', 10, 11, 8, 'x', 'x', 'x', 'x'))
    num_rows = 12
    num_cols = 11
    start = (1, 3)
    end = (6, 10)
    districts = {1: [(0, 0), (1, 0)], 2: [(2, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0)], 3: [(3, 0), (4, 0)]}
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
