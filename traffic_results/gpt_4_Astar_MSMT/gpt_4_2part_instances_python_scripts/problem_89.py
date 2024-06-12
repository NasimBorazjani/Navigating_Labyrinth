
import heapq

def initialize():
    initial_state = (3, 13)
    goal_state = (4, 0)
    num_rows = 14
    num_cols = 14
    matrix = [['x', 'x', 'x', 7, 11, 16, 13, 19, 15, 'x', 19, 'x', 'x', 16], [9, 'x', 14, 'x', 7, 3, 'x', 'x', 17, 9, 'x', 'x', 'x', 19], ['x', 11, 6, 18, 'x', 19, 4, 'x', 'x', 'x', 19, 12, 4, 17], [5, 12, 15, 3, 'x', 'x', 'x', 'x', 7, 'x', 11, 17, 20, 20], [6, 'x', 11, 15, 11, 17, 16, 5, 'x', 3, 4, 20, 'x', 14], ['x', 11, 'x', 6, 'x', 16, 2, 18, 5, 11, 'x', 14, 4, 7], ['x', 6, 'x', 17, 'x', 'x', 15, 7, 'x', 2, 3, 16, 7, 15], [7, 'x', 'x', 8, 1, 'x', 'x', 'x', 14, 'x', 'x', 18, 'x', 19], [13, 'x', 'x', 'x', 'x', 2, 9, 19, 'x', 16, 11, 5, 'x', 11], ['x', 17, 15, 18, 'x', 7, 'x', 15, 13, 'x', 14, 2, 'x', 19], ['x', 'x', 'x', 14, 7, 19, 'x', 'x', 9, 9, 'x', 'x', 'x', 'x'], ['x', 3, 13, 15, 18, 17, 'x', 'x', 9, 4, 'x', 12, 10, 14], [15, 'x', 6, 19, 19, 19, 'x', 1, 8, 4, 17, 14, 'x', 'x'], [8, 'x', 14, 7, 12, 6, 8, 'x', 5, 'x', 11, 11, 'x', 'x']]
    districts = {1: range(0, 4), 2: range(4, 6), 3: range(6, 14)}
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
