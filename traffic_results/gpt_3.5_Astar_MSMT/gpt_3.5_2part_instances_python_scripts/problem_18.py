
import heapq

def initialize():
    initial_state = ((13, 'x', 'x', 'x', 'x', 'x', 8, 'x', 6), ('x', 'x', 'x', 8, 10, 'x', 17, 'x', 15, 14), ('x', 6, 'x', 'x', 'x', 16, 12, 7, 8, 11), ('x', 15, 'x', 1, 11, 19, 9, 17, 'x', 'x'), (18, 20, 16, 19, 12, 1, 'x', 'x', 'x', 5), (11, 'x', 18, 14, 'x', 2, 'x', 9, 8, 1), ('x', 2, 5, 16, 3, 9, 2, 18, 'x', 'x'), ('x', 8, 15, 17, 16, 6, 'x', 3, 'x', 10), (3, 'x', 'x', 'x', 8, 9, 10, 'x', 6, 'x'), (6, 'x', 9, 16, 1, 3, 16, 18, 'x', 'x'))
    num_rows = 10
    num_cols = 10
    start = (1, 8)
    end = (4, 1)
    districts = {1: [(0, 0), (0, 1)], 2: [(2, 0), (4, 1), (6, 2)], 3: [(5, 0), (9, 1)]}
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
