
import heapq

def initialize():
    initial_state = (1, 8)
    goal_state = (4, 1)
    num_rows = 10
    num_cols = 10
    matrix = [[13, 'x', 'x', 'x', 'x', 'x', 8, 'x', 'x', 6], ['x', 'x', 'x', 8, 10, 'x', 17, 'x', 15, 14], ['x', 6, 'x', 'x', 'x', 16, 12, 7, 8, 11], ['x', 15, 'x', 1, 11, 19, 9, 17, 'x', 'x'], [18, 20, 16, 19, 12, 1, 'x', 'x', 'x', 5], [11, 'x', 18, 14, 'x', 2, 'x', 9, 8, 1], ['x', 2, 5, 16, 3, 9, 2, 18, 'x', 'x'], ['x', 8, 15, 17, 16, 6, 'x', 3, 'x', 10], [3, 'x', 'x', 'x', 8, 9, 10, 'x', 6, 'x'], [6, 'x', 9, 16, 1, 3, 16, 18, 'x', 'x']]
    districts = {1: range(0, 2), 2: range(2, 5), 3: range(5, 10)}
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
