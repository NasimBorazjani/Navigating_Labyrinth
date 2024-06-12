
import heapq

def initialize():
    initial_state = (1, 0)
    goal_state = (8, 10)
    num_rows = 12
    num_cols = 12
    matrix = [[3, 14, 2, 'x', 'x', 'x', 19, 13, 17, 12, 8, 'x'], [1, 2, 13, 1, 4, 19, 'x', 'x', 16, 'x', 'x', 12], [9, 8, 9, 15, 'x', 12, 'x', 'x', 'x', 'x', 'x', 14], [11, 1, 10, 18, 'x', 16, 1, 'x', 12, 'x', 'x', 'x'], [7, 16, 13, 10, 13, 'x', 14, 'x', 'x', 9, 'x', 7], [19, 7, 7, 20, 13, 14, 18, 'x', 'x', 7, 5, 'x'], [4, 'x', 11, 'x', 'x', 2, 7, 1, 5, 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 18, 'x', 1, 'x'], [4, 'x', 'x', 9, 19, 2, 18, 8, 16, 14, 19, 7], ['x', 'x', 'x', 'x', 9, 'x', 17, 17, 1, 2, 2, 15], [18, 'x', 'x', 'x', 'x', 'x', 'x', 11, 10, 'x', 17, 'x'], [9, 'x', 'x', 'x', 10, 3, 'x', 'x', 13, 'x', 2, 'x']]
    districts = {1: range(0, 2), 2: range(2, 8), 3: range(8, 12)}
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
