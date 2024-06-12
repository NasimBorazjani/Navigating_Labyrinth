
import heapq

def initialize():
    initial_state = (3, 0)
    goal_state = (8, 9)
    num_rows = 13
    num_cols = 13
    matrix = [[16, 9, 19, 14, 16, 19, 6, 'x', 'x', 'x', 16, 18, 'x'], [19, 'x', 'x', 9, 9, 'x', 17, 16, 3, 'x', 'x', 14, 'x'], ['x', 'x', 11, 'x', 5, 'x', 15, 15, 17, 10, 'x', 13, 5], [2, 12, 9, 18, 7, 'x', 'x', 'x', 4, 'x', 10, 'x', 3], [8, 9, 19, 1, 'x', 4, 8, 'x', 17, 6, 'x', 18, 'x'], ['x', 6, 7, 9, 1, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 5, 4, 12, 13, 13, 'x', 'x', 'x', 11, 'x', 5, 9], ['x', 'x', 2, 20, 6, 11, 2, 'x', 'x', 'x', 10, 18, 'x'], ['x', 'x', 1, 18, 1, 17, 2, 3, 10, 12, 11, 'x', 19], ['x', 16, 3, 'x', 'x', 16, 3, 10, 19, 'x', 'x', 9, 'x'], [10, 'x', 'x', 'x', 'x', 1, 10, 13, 'x', 'x', 13, 'x', 'x'], ['x', 'x', 'x', 'x', 13, 'x', 1, 14, 'x', 10, 'x', 'x', 8], ['x', 'x', 'x', 'x', 'x', 9, 2, 18, 19, 14, 10, 'x', 'x']]
    districts = {1: range(0, 4), 2: range(4, 9), 3: range(9, 13)}
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
