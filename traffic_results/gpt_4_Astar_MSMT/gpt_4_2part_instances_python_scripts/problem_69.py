
import heapq

def initialize():
    initial_state = (1, 12)
    goal_state = (6, 3)
    num_rows = 13
    num_cols = 13
    matrix = [[17, 'x', 'x', 'x', 5, 'x', 'x', 12, 16, 'x', 'x', 5, 16], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 12, 4, 6], [9, 'x', 'x', 'x', 'x', 'x', 19, 'x', 'x', 13, 6, 11, 19], [1, 'x', 'x', 'x', 13, 'x', 'x', 'x', 3, 2, 7, 4, 3], ['x', 'x', 'x', 14, 19, 20, 10, 13, 14, 2, 'x', 9, 3], [15, 'x', 11, 7, 'x', 11, 6, 16, 'x', 'x', 'x', 8, 19], [19, 16, 4, 8, 5, 5, 5, 11, 10, 17, 9, 'x', 5], ['x', 3, 17, 'x', 'x', 6, 17, 19, 'x', 'x', 14, 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 14, 'x', 10, 14, 13, 'x', 13, 'x'], [15, 5, 4, 'x', 'x', 'x', 'x', 2, 12, 6, 'x', 16, 14], [10, 'x', 'x', 'x', 9, 'x', 'x', 'x', 'x', 'x', 13, 2, 'x'], ['x', 'x', 17, 'x', 'x', 'x', 'x', 7, 'x', 'x', 16, 'x', 'x'], [12, 10, 'x', 15, 16, 'x', 'x', 7, 11, 7, 'x', 17, 'x']]
    districts = {1: range(0, 2), 2: range(2, 6), 3: range(6, 13)}
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
