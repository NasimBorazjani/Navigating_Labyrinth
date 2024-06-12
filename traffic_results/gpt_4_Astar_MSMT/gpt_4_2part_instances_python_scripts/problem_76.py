
import heapq

def initialize():
    initial_state = (4, 3)
    goal_state = (8, 13)
    num_rows = 14
    num_cols = 14
    matrix = [['x', 12, 8, 4, 4, 16, 8, 'x', 'x', 17, 18, 9, 'x', 16], [2, 9, 'x', 1, 4, 13, 20, 11, 2, 'x', 11, 7, 14, 12], ['x', 'x', 'x', 'x', 17, 15, 8, 12, 'x', 'x', 7, 'x', 'x', 'x'], [2, 2, 'x', 5, 14, 'x', 1, 5, 4, 14, 7, 'x', 'x', 'x'], [19, 'x', 11, 1, 19, 19, 12, 'x', 12, 13, 5, 3, 17, 17], ['x', 'x', 'x', 'x', 'x', 1, 'x', 'x', 4, 'x', 'x', 'x', 8, 19], [6, 'x', 10, 'x', 7, 1, 11, 'x', 'x', 3, 'x', 3, 2, 'x'], [19, 'x', 3, 11, 'x', 6, 11, 'x', 12, 14, 10, 'x', 11, 18], [13, 'x', 'x', 'x', 'x', 'x', 4, 'x', 'x', 'x', 'x', 'x', 10, 5], [19, 'x', 'x', 16, 'x', 'x', 18, 'x', 8, 'x', 2, 11, 'x', 12], ['x', 14, 'x', 6, 'x', 18, 'x', 11, 'x', 'x', 14, 11, 2, 'x'], ['x', 'x', 6, 8, 10, 8, 14, 'x', 'x', 13, 'x', 10, 'x', 19], ['x', 19, 'x', 7, 12, 17, 'x', 15, 'x', 16, 19, 'x', 5, 'x'], [8, 'x', 17, 'x', 'x', 5, 15, 'x', 'x', 16, 1, 'x', 'x', 17]]
    districts = {1: range(0, 3), 2: range(3, 8), 3: range(8, 14)}
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [initial_state], initial_state, {1: False, 2: True, 3: False})]
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
