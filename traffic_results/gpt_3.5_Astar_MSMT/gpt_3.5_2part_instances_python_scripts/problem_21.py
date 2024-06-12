
import heapq

def initialize():
    initial_state = ((15, 4, 9, 10, 19, 'x', 12, 4, 'x', 15), (12, 19, 11, 'x', 'x', 'x', 'x', 7, 6, 3), (4, 'x', 8, 'x', 'x', 19, 'x', 11, 1, 6), ('x', 'x', 5, 'x', 'x', 'x', 12, 6, 6, 'x'), ('x', 14, 'x', 'x', 14, 11, 2, 9, 6, 14), (8, 8, 5, 17, 7, 'x', 1, 2, 'x', 6), (18, 'x', 'x', 15, 'x', 15, 4, 'x', 'x', 7), (19, 'x', 10, 18, 14, 'x', 14, 9, 8, 6), (19, 'x', 14, 'x', 10, 8, 15, 'x', 15, 'x'), (12, 1, 'x', 5, 3, 3, 'x', 'x', 'x', 'x'))
    num_rows = 10
    num_cols = 10
    start = (1, 9)
    end = (6, 3)
    districts = {1: [(0, 0), (1, 0)], 2: [(2, 0), (6, 0), (7, 0), (8, 0), (9, 0)], 3: [(3, 0), (4, 0), (5, 0)]}
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
