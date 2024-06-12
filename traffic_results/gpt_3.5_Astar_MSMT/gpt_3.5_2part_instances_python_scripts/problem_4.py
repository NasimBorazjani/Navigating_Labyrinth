
import heapq

def initialize():
    initial_state = ((18, 9, 2, 'x', 9, 14, 'x', 1, 'x'), (3, 14, 18, 7, 'x', 3, 'x', 2, 19), (6, 18, 20, 3, 13, 'x', 6, 10, 'x'), (20, 'x', 12, 4, 14, 6, 'x', 'x', 'x'), (7, 18, 8, 5, 19, 3, 'x', 'x', 7), (15, 9, 14, 16, 5, 14, 6, 'x', 'x'), ('x', 5, 13, 'x', 'x', 19, 'x', 'x', 2), ('x', 'x', 8, 'x', 'x', 'x', 'x', 17, 12), ('x', 1, 'x', 'x', 3, 19, 'x', 2, 18))
    num_rows = 9
    num_cols = 9
    start = (2, 0)
    end = (5, 6)
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
