
import heapq

def initialize():
    initial_state = ((6, 16, 'x', 'x', 15, 'x', 14, 11, 'x'), (5, 2, 1, 'x', 3, 'x', 4, 13, 'x'), ('x', 7, 'x', 'x', 13, 'x', 10, 14, 5), (6, 16, 'x', 13, 6, 'x', 16, 'x', 'x'), ('x', 1, 17, 'x', 6, 3, 'x', 'x', 3), (11, 10, 7, 19, 15, 8, 12, 6, 'x'), (18, 'x', 'x', 9, 8, 9, 'x', 'x', 13), (4, 'x', 'x', 'x', 18, 20, 'x', 'x', 'x'), ('x', 'x', 8, 'x', 18, 2, 6, 13, 'x'))
    num_rows = 9
    num_cols = 9
    start = (5, 5)
    end = (1, 0)
    districts = {1: [(0, 0), (1, 0)], 2: [(2, 0), (4, 0), (3, 3)], 3: [(5, 0), (8, 0)]}
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
