
import heapq

def initialize():
    initial_state = ((2, 2, 3, 'x', 2, 10, 'x', 8, 6, 'x'), (6, 11, 'x', 'x', 'x', 'x', 'x', 16, 'x', 7), (17, 17, 7, 12, 13, 15, 5, 6, 10, 13), (1, 15, 13, 3, 'x', 'x', 'x', 14, 'x', 9), (14, 'x', 'x', 6, 15, 2, 12, 18, 'x', 18), (11, 19, 1, 19, 10, 8, 'x', 14, 'x', 'x'), (11, 'x', 'x', 'x', 3, 'x', 'x', 7, 'x', 2), (16, 12, 'x', 'x', 'x', 5, 'x', 'x', 10, 'x'), ('x', 11, 'x', 2, 12, 'x', 8, 'x', 8, 'x'), ('x', 'x', 16, 'x', 'x', 'x', 16, 'x', 16, 12))
    num_rows = 10
    num_cols = 10
    start = (1, 0)
    end = (5, 7)
    districts = {1: [(0, 0), (0, 1)], 2: [(2, 0), (4, 1), (4, 2), (4, 3), (4, 4)], 3: [(5, 0), (9, 1)]}
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
