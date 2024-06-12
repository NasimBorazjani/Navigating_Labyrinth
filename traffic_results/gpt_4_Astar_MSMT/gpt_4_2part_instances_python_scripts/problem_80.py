
import heapq

def initialize():
    initial_state = (1, 10)
    goal_state = (7, 2)
    num_rows = 14
    num_cols = 14
    matrix = [['x', 'x', 8, 16, 3, 'x', 15, 17, 2, 'x', 'x', 5, 'x', 'x'], ['x', 'x', 17, 'x', 13, 'x', 4, 'x', 13, 3, 3, 6, 11, 'x'], ['x', 'x', 8, 'x', 14, 1, 15, 11, 'x', 18, 12, 'x', 'x', 'x'], ['x', 13, 19, 4, 13, 2, 13, 3, 'x', 1, 20, 18, 'x', 15], [13, 'x', 1, 'x', 11, 'x', 8, 14, 4, 11, 3, 'x', 'x', 'x'], [12, 11, 16, 1, 1, 'x', 5, 1, 'x', 9, 'x', 'x', 1, 'x'], [8, 'x', 6, 15, 'x', 7, 19, 13, 2, 'x', 3, 3, 'x', 2], [18, 'x', 19, 15, 2, 'x', 'x', 18, 2, 'x', 10, 'x', 'x', 1], [3, 4, 'x', 19, 'x', 6, 'x', 7, 'x', 'x', 'x', 'x', 15, 'x'], ['x', 'x', 'x', 16, 7, 17, 11, 'x', 7, 'x', 'x', 'x', 'x', 15], ['x', 9, 'x', 'x', 'x', 19, 19, 7, 3, 12, 14, 11, 16, 7], [8, 19, 15, 1, 'x', 14, 'x', 1, 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 14, 'x', 'x', 'x', 'x', 'x', 18, 'x', 'x', 2, 11, 7, 'x'], ['x', 'x', 'x', 'x', 'x', 3, 11, 12, 'x', 'x', 'x', 2, 6, 'x']]
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
