
import heapq

def initialize():
    initial_state = ((18, 15, 'x', 'x', 1, 'x', 'x', 5, 8, 18, 18, 2, 'x', 11, 8), ('x', 17, 'x', 'x', 2, 'x', 16, 9, 7, 13, 16, 17, 'x', 'x', 'x'), (10, 'x', 1, 14, 1, 10, 15, 4, 'x', 'x', 8, 11, 10, 'x', 'x'), (19, 'x', 'x', 9, 8, 18, 5, 2, 12, 'x', 13, 'x', 'x', 15, 11), (1, 'x', 14, 6, 6, 6, 'x', 'x', 'x', 13, 13, 'x', 'x', 'x', 'x'), (2, 3, 8, 5, 7, 'x', 'x', 'x', 19, 'x', 16, 'x', 'x', 'x', 'x'), ('x', 'x', 17, 18, 'x', 19, 'x', 'x', 'x', 7, 8, 17, 'x', 'x', 'x'), (4, 'x', 4, 14, 17, 6, 'x', 2, 'x', 'x', 15, 6, 'x', 18, 10), (7, 'x', 3, 11, 10, 'x', 'x', 12, 'x', 'x', 8, 'x', 'x', 10, 'x'), (4, 16, 2, 11, 'x', 'x', 14, 'x', 13, 'x', 'x', 'x', 'x', 'x', 'x'), (14, 20, 7, 14, 'x', 'x', 'x', 'x', 'x', 'x', 5, 'x', 10, 16, 'x'), (1, 14, 'x', 'x', 'x', 4, 14, 19, 'x', 18, 'x', 'x', 17, 15, 14), ('x', 'x', 15, 'x', 4, 5, 19, 18, 'x', 19, 11, 3, 12, 'x', 10), (1, 'x', 1, 'x', 'x', 13, 'x', 16, 4, 'x', 'x', 8, 'x', 9, 'x'), ('x', 'x', 12, 11, 7, 'x', 8, 14, 3, 'x', 11, 'x', 14, 13, 'x'))
    num_rows = 14
    num_cols = 15
    start = (1, 11)
    end = (7, 2)
    districts = {1: [(0, 0), (0, 1)], 2: [(2, 0), (9, 1)], 3: [(10, 0), (13, 1)]}
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
