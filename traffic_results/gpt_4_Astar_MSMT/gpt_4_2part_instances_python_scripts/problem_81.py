
import heapq

def initialize():
    initial_state = (2, 0)
    goal_state = (6, 11)
    num_rows = 14
    num_cols = 14
    matrix = [[8, 15, 3, 10, 6, 15, 'x', 4, 'x', 'x', 'x', 'x', 'x', 4], [3, 'x', 14, 8, 16, 19, 'x', 18, 4, 'x', 2, 'x', 6, 'x'], [18, 18, 'x', 4, 'x', 17, 11, 10, 17, 9, 'x', 4, 1, 5], ['x', 2, 'x', 12, 1, 'x', 13, 17, 14, 15, 17, 'x', 15, 'x'], ['x', 'x', 'x', 15, 'x', 2, 2, 11, 7, 'x', 5, 7, 4, 18], [16, 'x', 5, 'x', 19, 12, 5, 9, 13, 16, 9, 'x', 3, 'x'], ['x', 'x', 'x', 'x', 14, 18, 'x', 16, 13, 'x', 1, 5, 10, 'x'], [3, 11, 'x', 1, 8, 'x', 'x', 'x', 18, 8, 11, 'x', 'x', 6], [19, 2, 'x', 19, 5, 'x', 'x', 'x', 9, 'x', 6, 'x', 'x', 4], ['x', 2, 'x', 10, 9, 15, 'x', 'x', 'x', 16, 'x', 8, 'x', 'x'], [18, 8, 10, 'x', 3, 'x', 11, 'x', 17, 'x', 17, 'x', 'x', 'x'], [14, 12, 'x', 2, 'x', 19, 2, 19, 14, 'x', 'x', 'x', 3, 'x'], [7, 'x', 'x', 'x', 'x', 'x', 'x', 9, 8, 7, 'x', 15, 2, 'x'], ['x', 'x', 15, 'x', 'x', 15, 16, 'x', 'x', 'x', 19, 'x', 13, 1]]
    districts = {1: range(0, 3), 2: range(3, 6), 3: range(6, 14)}
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
