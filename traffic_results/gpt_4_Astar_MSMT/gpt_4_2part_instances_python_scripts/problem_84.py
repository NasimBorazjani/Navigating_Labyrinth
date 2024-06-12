
import heapq

def initialize():
    initial_state = (9, 10)
    goal_state = (2, 3)
    num_rows = 14
    num_cols = 14
    matrix = [['x', 10, 16, 12, 'x', 'x', 'x', 'x', 18, 18, 10, 'x', 'x', 19], [7, 'x', 'x', 11, 5, 13, 6, 'x', 'x', 'x', 'x', 'x', 8, 14], ['x', 15, 6, 20, 4, 9, 16, 9, 16, 'x', 11, 'x', 'x', 9], [1, 16, 'x', 'x', 'x', 6, 15, 1, 10, 10, 9, 4, 'x', 4], ['x', 'x', 'x', 1, 12, 'x', 12, 17, 'x', 'x', 13, 'x', 'x', 2], ['x', 'x', 9, 'x', 'x', 'x', 'x', 17, 'x', 'x', 'x', 'x', 10, 11], [7, 'x', 7, 12, 'x', 'x', 'x', 2, 2, 8, 10, 8, 'x', 'x'], [3, 3, 'x', 16, 11, 'x', 4, 6, 'x', 'x', 4, 17, 13, 16], [4, 15, 'x', 'x', 'x', 'x', 'x', 'x', 11, 19, 16, 'x', 'x', 'x'], [10, 5, 17, 'x', 2, 'x', 'x', 3, 10, 3, 12, 'x', 8, 'x'], ['x', 17, 12, 'x', 'x', 'x', 6, 2, 13, 'x', 'x', 'x', 'x', 'x'], ['x', 10, 'x', 'x', 15, 'x', 'x', 'x', 8, 'x', 3, 'x', 'x', 19], [1, 7, 'x', 'x', 16, 'x', 'x', 'x', 3, 15, 10, 12, 6, 8], ['x', 'x', 'x', 'x', 9, 'x', 'x', 'x', 7, 'x', 'x', 'x', 'x', 8]]
    districts = {1: range(0, 3), 2: range(3, 9), 3: range(9, 14)}
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
