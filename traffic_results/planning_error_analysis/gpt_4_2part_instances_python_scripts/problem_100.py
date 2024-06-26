
import heapq

def initialize():
    initial_state = (4, 0)
    goal_state = (9, 11)
    num_rows = 15
    num_cols = 15
    matrix = [['x', 2, 16, 'x', 9, 'x', 14, 'x', 8, 'x', 16, 'x', 'x', 4, 8], [9, 'x', 4, 'x', 'x', 7, 11, 'x', 'x', 13, 'x', 'x', 6, 11, 'x'], ['x', 'x', 10, 14, 'x', 'x', 18, 'x', 'x', 'x', 'x', 'x', 6, 16, 'x'], ['x', 14, 'x', 1, 'x', 7, 5, 16, 'x', 19, 'x', 'x', 10, 7, 'x'], [1, 3, 'x', 19, 7, 2, 17, 'x', 'x', 6, 'x', 'x', 'x', 10, 14], [14, 'x', 'x', 'x', 12, 'x', 16, 5, 8, 12, 17, 2, 19, 'x', 5], [9, 9, 8, 15, 18, 'x', 16, 'x', 10, 'x', 'x', 14, 'x', 'x', 'x'], [18, 20, 'x', 'x', 11, 2, 17, 6, 'x', 18, 8, 'x', 6, 16, 'x'], [12, 'x', 'x', 'x', 'x', 7, 14, 4, 8, 12, 3, 'x', 15, 13, 2], [16, 'x', 'x', 'x', 12, 'x', 8, 1, 7, 7, 12, 17, 2, 2, 7], ['x', 13, 3, 3, 1, 'x', 6, 14, 20, 8, 'x', 4, 10, 17, 'x'], [1, 8, 'x', 16, 'x', 'x', 'x', 9, 'x', 'x', 10, 'x', 'x', 5, 8], ['x', 'x', 1, 'x', 'x', 6, 'x', 'x', 'x', 7, 16, 'x', 'x', 'x', 'x'], [14, 'x', 'x', 10, 18, 'x', 6, 13, 'x', 'x', 'x', 'x', 'x', 15, 'x'], ['x', 8, 2, 'x', 17, 'x', 12, 16, 11, 4, 4, 'x', 'x', 17, 'x']]
    districts = {1: range(0, 5), 2: range(5, 10), 3: range(10, 15)}
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
