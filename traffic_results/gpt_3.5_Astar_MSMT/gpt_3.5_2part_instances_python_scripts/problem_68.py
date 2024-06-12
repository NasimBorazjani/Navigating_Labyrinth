
import heapq

def initialize():
    initial_state = ((18, 'x', 'x', 'x', 19, 'x', 'x', 8, 6, 3, 'x', 'x', 'x'), ('x', 'x', 8, 1, 11, 'x', 'x', 'x', 'x', 'x', 4, 6, 4), (1, 4, 15, 13, 17, 11, 'x', 15, 'x', 13, 1, 'x', 'x'), (3, 'x', 6, 1, 15, 2, 'x', 13, 13, 'x', 10, 'x', 'x'), (17, 12, 13, 11, 6, 1, 3, 'x', 'x', 19, 6, 6, 'x'), ('x', 17, 7, 12, 1, 15, 17, 20, 3, 'x', 'x', 18, 10), (16, 14, 15, 'x', 'x', 11, 'x', 17, 20, 15, 7, 10, 'x'), (5, 11, 'x', 7, 19, 'x', 6, 18, 15, 'x', 8, 'x', 1), (10, 'x', 1, 'x', 'x', 6, 'x', 11, 'x', 13, 'x', 'x', 'x'), ('x', 'x', 'x', 'x', 4, 'x', 8, 'x', 12, 'x', 12, 13, 'x'), ('x', 'x', 18, 14, 'x', 'x', 5, 'x', 'x', 13, 1, 'x', 'x'), ('x', 'x', 1, 17, 8, 18, 'x', 7, 'x', 'x', 16, 8, 'x'), ('x', 'x', 'x', 16, 1, 'x', 19, 'x', 'x', 'x', 'x', 14, 'x'))
    num_rows = 13
    num_cols = 13
    start = (5, 12)
    end = (1, 2)
    districts = {1: [(0, 0), (0, 1)], 2: [(2, 0), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1)], 3: [(3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0)]}
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
