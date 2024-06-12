
import heapq

def initialize():
    initial_state = ((3, 11, 7, 'x', 'x', 1, 3, 'x', 'x', 'x', 3), (10, 'x', 3, 9, 7, 8, 'x', 2, 17, 'x', 'x'), (6, 16, 'x', 18, 10, 5, 6, 'x', 7, 'x', 7), ('x', 10, 8, 13, 10, 'x', 'x', 'x', 6, 13, 'x'), (6, 11, 3, 16, 8, 15, 'x', 'x', 13, 12, 20), (15, 'x', 16, 17, 13, 'x', 8, 6, 19, 9, 'x'), (14, 10, 16, 14, 'x', 10, 11, 19, 15, 17, 'x'), ('x', 'x', 18, 13, 14, 19, 12, 1, 3, 'x', 'x'), (15, 1, 3, 17, 4, 18, 'x', 2, 7, 12, 'x'), (19, 'x', 13, 17, 2, 14, 8, 'x', 8, 16, 'x'), ('x', 19, 15, 'x', 18, 'x', 13, 13, 'x', 'x', 'x'), (7, 14, 2, 'x', 10, 3, 'x', 2, 5, 10, 'x'))
    num_rows = 12
    num_cols = 11
    start = (8, 1)
    end = (5, 11)
    districts = {1: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)], 2: [(5, 0), (6, 0), (7, 0), (8, 0)], 3: [(9, 0), (10, 1), (11, 2)]}
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
