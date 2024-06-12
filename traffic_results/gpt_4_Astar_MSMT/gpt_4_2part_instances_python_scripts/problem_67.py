
import heapq

def initialize():
    initial_state = (2, 3)
    goal_state = (8, 10)
    num_rows = 13
    num_cols = 13
    matrix = [['x', 'x', 10, 'x', 'x', 'x', 3, 'x', 'x', 'x', 'x', 'x', 'x'], [6, 19, 'x', 'x', 'x', 12, 'x', 'x', 3, 'x', 'x', 'x', 'x'], [5, 3, 7, 7, 'x', 7, 9, 'x', 18, 'x', 'x', 'x', 'x'], [1, 4, 19, 19, 16, 6, 'x', 2, 10, 'x', 1, 7, 'x'], [14, 10, 'x', 'x', 2, 3, 5, 3, 13, 7, 'x', 8, 'x'], ['x', 8, 11, 14, 18, 'x', 'x', 16, 15, 8, 'x', 10, 'x'], ['x', 17, 'x', 'x', 15, 'x', 'x', 1, 17, 9, 7, 'x', 10], [18, 6, 14, 4, 12, 12, 'x', 12, 5, 'x', 'x', 5, 18], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 7, 17, 4, 16, 'x', 'x'], ['x', 6, 17, 'x', 'x', 'x', 'x', 'x', 15, 'x', 'x', 12, 'x'], [14, 'x', 'x', 12, 3, 11, 'x', 'x', 'x', 'x', 'x', 'x', 17], ['x', 16, 'x', 'x', 'x', 3, 5, 19, 'x', 16, 14, 'x', 19], [13, 'x', 11, 'x', 3, 16, 'x', 1, 'x', 'x', 1, 'x', 'x']]
    districts = {1: range(0, 3), 2: range(3, 8), 3: range(8, 13)}
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
