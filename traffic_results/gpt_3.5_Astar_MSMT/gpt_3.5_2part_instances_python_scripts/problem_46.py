
import heapq

def initialize():
    initial_state = ((3, 14, 2, 'x', 'x', 'x', 19, 13, 17, 12, 8, 'x'), (1, 2, 13, 1, 4, 19, 'x', 'x', 16, 'x', 'x', 12), (9, 8, 9, 15, 'x', 12, 'x', 'x', 'x', 'x', 'x', 14), (11, 1, 10, 18, 'x', 16, 1, 'x', 12, 'x', 'x', 'x'), (7, 16, 13, 10, 13, 'x', 14, 'x', 'x', 9, 'x', 7), (19, 7, 7, 20, 13, 14, 18, 'x', 'x', 7, 5, 'x'), (4, 'x', 11, 'x', 'x', 2, 7, 1, 5, 'x', 'x', 'x'), ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 18, 'x', 1, 'x'), (4, 'x', 'x', 9, 19, 2, 18, 8, 16, 14, 19, 7), ('x', 'x', 'x', 'x', 9, 'x', 17, 17, 1, 2, 2, 15), (18, 'x', 'x', 'x', 'x', 'x', 'x', 11, 10, 'x', 17, 'x'), (9, 'x', 'x', 'x', 10, 3, 'x', 'x', 13, 'x', 2, 'x'))
    num_rows = 12
    num_cols = 12
    start = (1, 0)
    end = (8, 10)
    districts = {1: [(0, 0), (1, 0)], 2: [(2, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0)], 3: [(8, 0), (9, 0), (10, 0), (11, 0)]}
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
