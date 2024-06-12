
import heapq

def initialize():
    initial_state = ((12, 11, 14, 10, 2, 11, 13, 16, 3, 'x', 12), (10, 9, 'x', 8, 'x', 'x', 1, 16, 11, 'x', 15), (1, 18, 1, 'x', 'x', 'x', 'x', 'x', 12, 9, 'x'), (1, 14, 15, 10, 7, 15, 17, 10, 15, 15, 6), (18, 11, 'x', 'x', 'x', 15, 'x', 'x', 1, 1, 'x'), (14, 'x', 'x', 'x', 18, 14, 16, 7, 'x', 1, 'x'), (11, 15, 'x', 'x', 15, 3, 11, 13, 'x', 'x', 'x'), (5, 'x', 'x', 'x', 'x', 'x', 15, 'x', 6, 'x', 'x'), (12, 11, 7, 2, 11, 'x', 10, 2, 17, 'x', 'x'), (7, 'x', 'x', 'x', 4, 'x', 4, 'x', 'x', 5, 'x'), ('x', 19, 10, 7, 'x', 2, 3, 9, 2, 6, 'x'))
    num_rows = 11
    num_cols = 11
    start = (7, 0)
    end = (2, 9)
    districts = {1: [(0, 0), (0, 1), (0, 2)], 2: [(3, 0), (6, 1), (10, 2)], 3: [(7, 0), (10, 1)]}
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
