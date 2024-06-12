
import heapq

def initialize():
    initial_state = ((8, 'x', 8, 'x', 5, 19, 12, 19, 7), ('x', 6, 19, 17, 20, 'x', 'x', 14, 14), (12, 14, 7, 1, 15, 'x', 8, 8, 'x'), ('x', 9, 'x', 'x', 4, 7, 7, 'x', 'x'), ('x', 'x', 'x', 11, 10, 'x', 'x', 5, 'x'), (x, 11, 18, 'x', 19, 'x', 1, 18, 1), (19, 'x', 7, 'x', 9, 3, 'x', 7, 12), ('x', 17, 9, 'x', 6, 'x', 6, 'x', 'x'), (4, 17, 5, 'x', 7, 5, 17, 12, 'x'), (15, 2, 13, 'x', 14, 'x', 'x', 17, 'x'))
    num_rows = 10
    num_cols = 9
    start = (4, 14)
    end = (7, 1)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)], 2: [(5, 0), (5, 1)], 3: [(7, 0), (8, 1)]}
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
