
import heapq

def initialize():
    initial_state = (5, 2)
    goal_state = (8, 14)
    num_rows = 15
    num_cols = 15
    matrix = [['x', 'x', 12, 'x', 18, 3, 2, 15, 6, 11, 13, 'x', 7, 17, 'x'], [13, 'x', 20, 13, 5, 2, 'x', 'x', 10, 12, 19, 19, 16, 'x', 17], [12, 12, 7, 'x', 'x', 'x', 9, 'x', 'x', 10, 10, 18, 4, 'x', 'x'], ['x', 14, 3, 13, 9, 2, 19, 19, 'x', 'x', 'x', 4, 'x', 2, 15], ['x', 14, 2, 'x', 3, 'x', 10, 11, 'x', 4, 'x', 12, 4, 'x', 'x'], ['x', 9, 7, 16, 'x', 'x', 19, 17, 17, 14, 14, 12, 14, 19, 12], [2, 'x', 'x', 7, 15, 'x', 'x', 13, 'x', 8, 1, 1, 'x', 14, 19], [16, 'x', 14, 'x', 'x', 6, 'x', 'x', 16, 'x', 'x', 9, 10, 18, 4], [3, 'x', 'x', 3, 'x', 'x', 'x', 'x', 9, 8, 'x', 9, 14, 'x', 14], ['x', 'x', 'x', 4, 19, 'x', 4, 15, 'x', 'x', 'x', 17, 'x', 'x', 'x'], [16, 17, 'x', 'x', 13, 'x', 18, 5, 'x', 14, 'x', 'x', 'x', 'x', 'x'], [2, 'x', 17, 'x', 'x', 'x', 'x', 'x', 'x', 12, 3, 8, 'x', 2, 9], ['x', 'x', 14, 7, 11, 'x', 'x', 10, 9, 3, 7, 16, 'x', 7, 1], ['x', 12, 14, 1, 'x', 'x', 3, 12, 'x', 7, 'x', 'x', 8, 'x', 'x'], ['x', 2, 'x', 15, 2, 'x', 14, 16, 13, 19, 16, 1, 11, 'x', 'x']]
    districts = {1: range(0, 6), 2: range(6, 8), 3: range(8, 15)}
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
