
import heapq

def initialize():
    initial_state = ((10, 'x', 19, 11, 'x', 'x', 6, 12, 'x', 'x', 'x'), (2, 9, 10, 'x', 'x', 10, 17, 'x', 'x', 11, 5), ('x', 15, 8, 9, 'x', 7, 17, 20, 'x', 'x', 13), (1, 9, 15, 14, 9, 9, 13, 7, 12, 'x', 10), (9, 'x', 17, 'x', 'x', 7, 'x', 'x', 1, 'x', 14), (16, 18, 11, 'x', 14, 18, 9, 13, 'x', 'x', 'x'), (9, 3, 5, 8, 17, 15, 19, 'x', 3, 'x', 14), (2, 13, 'x', 'x', 17, 13, 14, 18, 9, 'x', 6), (3, 'x', 18, 6, 'x', 14, 'x', 'x', 'x', 8, 19), (2, 4, 'x', 'x', 'x', 'x', 3, 4, 'x', 19, 'x'), ('x', 'x', 'x', 'x', 11, 'x', 'x', 'x', 'x', 5, 5))
    num_rows = 11
    num_cols = 11
    start = (3, 7)
    end = (7, 0)
    districts = {1: [(0, 0), (0, 1), (0, 2)], 2: [(3, 0), (6, 1), (10, 2)], 3: [(7, 0), (10, 1), (10, 10)]}
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
