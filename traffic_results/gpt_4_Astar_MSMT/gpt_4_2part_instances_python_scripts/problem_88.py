
import heapq

def initialize():
    initial_state = (3, 1)
    goal_state = (5, 13)
    num_rows = 14
    num_cols = 14
    matrix = [['x', 7, 'x', 13, 8, 2, 15, 2, 5, 15, 6, 4, 7, 'x'], ['x', 6, 19, 17, 5, 13, 15, 2, 11, 5, 'x', 'x', 9, 8], [16, 12, 10, 7, 8, 19, 19, 9, 5, 10, 2, 'x', 'x', 12], ['x', 1, 19, 20, 'x', 3, 4, 18, 'x', 'x', 10, 1, 12, 2], ['x', 1, 4, 1, 1, 10, 4, 'x', 12, 'x', 5, 10, 3, 8], ['x', 'x', 'x', 7, 'x', 'x', 16, 12, 'x', 'x', 'x', 13, 6, 10], ['x', 'x', 11, 12, 13, 15, 8, 'x', 12, 1, 16, 14, 8, 15], ['x', 11, 'x', 15, 'x', 'x', 'x', 'x', 'x', 'x', 5, 'x', 'x', 14], [1, 'x', 'x', 8, 'x', 13, 17, 'x', 3, 12, 'x', 'x', 'x', 'x'], [14, 3, 'x', 4, 'x', 'x', 'x', 12, 'x', 7, 'x', 'x', 'x', 'x'], ['x', 5, 15, 'x', 10, 17, 'x', 'x', 6, 9, 2, 'x', 'x', 'x'], [1, 7, 17, 1, 'x', 'x', 'x', 'x', 11, 'x', 'x', 'x', 'x', 12], ['x', 'x', 14, 18, 8, 19, 19, 16, 'x', 6, 5, 16, 17, 7], ['x', 'x', 'x', 'x', 'x', 'x', 19, 17, 'x', 'x', 2, 12, 'x', 'x']]
    districts = {1: range(0, 4), 2: range(4, 6), 3: range(6, 14)}
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
