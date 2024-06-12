
import heapq

def initialize():
    initial_state = (2, 0)
    goal_state = (6, 14)
    num_rows = 15
    num_cols = 15
    matrix = [[6, 6, 2, 'x', 13, 'x', 'x', 'x', 'x', 11, 'x', 'x', 'x', 3, 'x'], [6, 11, 'x', 14, 'x', 'x', 'x', 1, 5, 6, 1, 19, 2, 7, 14], [16, 4, 12, 13, 17, 4, 'x', 'x', 'x', 14, 'x', 'x', 9, 9, 13], ['x', 11, 6, 14, 'x', 16, 'x', 1, 10, 18, 11, 'x', 'x', 13, 'x'], ['x', 'x', 14, 4, 19, 1, 2, 16, 15, 'x', 15, 'x', 'x', 'x', 'x'], [13, 6, 16, 13, 5, 9, 'x', 6, 10, 3, 1, 14, 'x', 17, 'x'], ['x', 'x', 19, 8, 'x', 2, 4, 'x', 'x', 4, 9, 13, 13, 11, 5], ['x', 11, 17, 19, 11, 18, 'x', 8, 'x', 'x', 17, 17, 13, 9, 15], [11, 4, 'x', 3, 3, 8, 5, 'x', 'x', 'x', 20, 19, 'x', 'x', 12], [2, 'x', 'x', 'x', 'x', 16, 7, 13, 4, 'x', 7, 16, 'x', 5, 1], [14, 9, 'x', 'x', 'x', 'x', 'x', 'x', 19, 'x', 14, 20, 11, 16, 'x'], [3, 'x', 1, 'x', 13, 'x', 9, 'x', 15, 19, 4, 'x', 'x', 'x', 2], ['x', 8, 'x', 'x', 'x', 6, 'x', 16, 'x', 'x', 'x', 'x', 2, 17, 18], ['x', 'x', 11, 'x', 'x', 14, 6, 'x', 15, 'x', 'x', 18, 'x', 'x', 'x'], [8, 'x', 5, 1, 7, 14, 'x', 'x', 'x', 'x', 14, 7, 'x', 8, 'x']]
    districts = {1: range(0, 3), 2: range(3, 9), 3: range(9, 15)}
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
