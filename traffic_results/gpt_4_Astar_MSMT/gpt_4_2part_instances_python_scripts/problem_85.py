
import heapq

def initialize():
    initial_state = (10, 12)
    goal_state = (4, 3)
    num_rows = 14
    num_cols = 14
    matrix = [[5, 10, 'x', 'x', 'x', 16, 'x', 'x', 'x', 16, 'x', 10, 8, 'x'], [1, 'x', 13, 'x', 7, 'x', 'x', 'x', 10, 3, 3, 13, 18, 11], [14, 'x', 'x', 'x', 9, 16, 16, 15, 'x', 'x', 15, 'x', 4, 4], [15, 'x', 3, 'x', 'x', 17, 'x', 16, 10, 9, 'x', 6, 16, 17], [12, 8, 'x', 10, 'x', 'x', 13, 10, 'x', 'x', 6, 3, 'x', 1], ['x', 'x', 'x', 5, 8, 9, 6, 14, 1, 'x', 'x', 2, 12, 'x'], [13, 'x', 'x', 'x', 16, 6, 'x', 17, 12, 18, 'x', 17, 8, 'x'], [10, 'x', 14, 15, 'x', 'x', 'x', 20, 'x', 17, 18, 8, 'x', 4], ['x', 11, 3, 'x', 'x', 'x', 'x', 7, 'x', 4, 'x', 'x', 11, 2], [7, 'x', 'x', 10, 'x', 19, 'x', 7, 17, 'x', 'x', 14, 'x', 15], [12, 11, 'x', 'x', 9, 7, 'x', 15, 1, 5, 5, 11, 15, 'x'], ['x', 9, 9, 'x', 'x', 'x', 'x', 8, 'x', 8, 19, 11, 12, 12], ['x', 17, 5, 'x', 'x', 17, 'x', 'x', 12, 'x', 15, 12, 10, 'x'], [18, 'x', 'x', 'x', 3, 'x', 7, 'x', 8, 5, 12, 8, 10, 'x']]
    districts = {1: range(0, 5), 2: range(5, 10), 3: range(10, 14)}
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [initial_state], initial_state, {1: False, 2: False, 3: True})]
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
