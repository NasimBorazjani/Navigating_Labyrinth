
import heapq

def initialize():
    initial_state = ((19, 12, 'x', 'x', 2, 5, 4, 13, 17, 19, 'x', 2), ('x', 18, 'x', 5, 5, 'x', 'x', 8, 12, 18, 'x', 15), ('x', 9, 4, 10, 7, 20, 'x', 16, 20, 13, 15, 'x'), (8, 'x', 'x', 11, 1, 19, 'x', 14, 6, 'x', 3, 'x'), (10, 'x', 4, 8, 17, 'x', 18, 'x', 7, 'x', 6, 5), ('x', 'x', 3, 1, 8, 18, 'x', 4, 17, 'x', 'x', 13), ('x', 'x', 6, 'x', 'x', 'x', 14, 'x', 'x', 10, 10, 'x'), ('x', 'x', 15, 'x', 'x', 'x', 'x', 'x', 2, 'x', 'x', 'x'), ('x', 'x', 5, 11, 6, 1, 'x', 6, 14, 'x', 'x', 'x'), ('x', 1, 17, 10, 15, 'x', 14, 6, 'x', 'x', 'x', 'x'), (12, 2, 'x', 10, 'x', 'x', 7, 'x', 'x', 'x', 'x', 'x'), ('x', 9, 14, 'x', 9, 18, 14, 'x', 'x', 'x', 6, 'x'))
    num_rows = 12
    num_cols = 12
    start = (6, 2)
    end = (2, 10)
    districts = {1: [(0, 0), (1, 1)], 2: [(2, 0), (5, 1), (6, 2), (11, 3)], 3: [(7, 0), (10, 1)]}
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
