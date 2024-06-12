
import heapq

def initialize():
    initial_state = (1, 13)
    goal_state = (7, 4)
    num_rows = 14
    num_cols = 14
    matrix = [[15, 19, 13, 4, 'x', 'x', 13, 7, 16, 6, 'x', 'x', 17, 'x'], [2, 2, 'x', 7, 'x', 12, 12, 'x', 19, 'x', 10, 4, 14, 2], [11, 'x', 'x', 3, 7, 'x', 7, 'x', 'x', 6, 'x', 19, 'x', 1], ['x', 'x', 11, 'x', 3, 'x', 17, 'x', 1, 20, 17, 8, 15, 1], ['x', 'x', 13, 'x', 12, 17, 5, 4, 'x', 16, 9, 'x', 19, 14], ['x', 16, 'x', 'x', 13, 17, 14, 6, 2, 17, 19, 6, 13, 6], ['x', 1, 'x', 'x', 3, 10, 2, 18, 7, 8, 'x', 8, 'x', 'x'], [12, 2, 1, 6, 11, 7, 10, 'x', 'x', 'x', 4, 2, 8, 'x'], ['x', 'x', 'x', 13, 16, 2, 'x', 6, 9, 2, 11, 7, 14, 6], ['x', 'x', 'x', 'x', 'x', 11, 'x', 16, 'x', 'x', 'x', 'x', 'x', 3], ['x', 'x', 'x', 'x', 10, 'x', 3, 'x', 18, 9, 'x', 'x', 'x', 15], ['x', 'x', 11, 9, 3, 'x', 'x', 16, 'x', 5, 'x', 4, 10, 'x'], [18, 1, 13, 'x', 7, 'x', 7, 5, 'x', 11, 10, 2, 'x', 2], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 11, 'x', 10, 'x', 'x', 14, 6]]
    districts = {1: range(0, 2), 2: range(2, 7), 3: range(7, 14)}
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [initial_state], initial_state, {1: True, 2: False, 3: False})]
    return (initial_state, goal_state, num_rows, num_cols, matrix, districts, visited_costs, queue)

def a_star():
    (initial_state, goal_state, num_rows, num_cols, matrix, districts, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state, visited_districts) = heapq.heappop(queue)
        if ((state == goal_state) and all(visited_districts.values())):
            return actions
        for (d_row, d_col) in [(0, (- 1)), (0, 1), (1, 0), ((- 1), 0)]:
            (new_row, new_col) = ((state[0] + d_row), (state[1] + d_col))
            if ((0 <= new_row < num_rows) and (0 <= new_col < num_cols) and (matrix[new_row][new_col] != 'x')):
                new_state = (new_row, new_col)
                new_cost = (g + matrix[new_row][new_col])
                new_visited_districts = visited_districts.copy()
                for (district, rows) in districts.items():
                    if (new_row in rows):
                        new_visited_districts[district] = True
                if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, ((g + heuristic(new_state, goal_state)), new_cost, (actions + [new_state]), new_state, new_visited_districts))
    return None

def heuristic(state, goal):
    h = (abs((state[0] - goal[0])) + abs((state[1] - goal[1])))
    return h
print(a_star())
