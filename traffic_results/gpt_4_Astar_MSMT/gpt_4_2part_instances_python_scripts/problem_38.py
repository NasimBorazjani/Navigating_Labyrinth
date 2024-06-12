
import heapq

def initialize():
    initial_state = (3, 6)
    goal_state = (8, 0)
    num_rows = 11
    num_cols = 11
    matrix = [['x', 'x', 'x', 3, 'x', 'x', 16, 'x', 2, 16, 3], [8, 'x', 8, 5, 'x', 'x', 10, 'x', 19, 4, 'x'], ['x', 'x', 18, 1, 16, 'x', 9, 15, 'x', 'x', 11], ['x', 'x', 17, 16, 4, 19, 2, 'x', 1, 11, 'x'], [9, 'x', 5, 16, 18, 'x', 'x', 7, 'x', 18, 6], ['x', 15, 7, 'x', 'x', 'x', 19, 8, 9, 17, 'x'], ['x', 15, 19, 'x', 'x', 'x', 6, 2, 6, 'x', 5], ['x', 12, 11, 3, 11, 4, 'x', 'x', 'x', 3, 'x'], [18, 12, 4, 'x', 3, 10, 'x', 3, 'x', 7, 14], [15, 11, 12, 'x', 13, 2, 'x', 'x', 5, 14, 11], ['x', 'x', 15, 'x', 16, 4, 10, 13, 'x', 'x', 4]]
    districts = {1: range(0, 4), 2: range(4, 8), 3: range(8, 11)}
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
