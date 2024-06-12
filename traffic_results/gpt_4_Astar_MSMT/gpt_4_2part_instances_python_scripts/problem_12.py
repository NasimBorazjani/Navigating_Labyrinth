
import heapq

def initialize():
    initial_state = (3, 1)
    goal_state = (5, 8)
    num_rows = 9
    num_cols = 9
    matrix = [[19, 'x', 17, 14, 3, 'x', 10, 5, 2], ['x', 'x', 1, 'x', 'x', 'x', 19, 7, 1], [16, 12, 'x', 3, 19, 2, 14, 1, 14], ['x', 1, 16, 'x', 12, 3, 13, 'x', 3], ['x', 'x', 7, 19, 10, 'x', 5, 'x', 19], [5, 'x', 'x', 6, 14, 'x', 'x', 10, 12], ['x', 'x', 'x', 'x', 18, 'x', 'x', 15, 12], ['x', 'x', 16, 8, 'x', 3, 4, 'x', 'x'], ['x', 'x', 'x', 16, 'x', 'x', 8, 14, 7]]
    districts = {1: range(0, 4), 2: range(4, 5), 3: range(5, 9)}
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
