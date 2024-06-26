
import heapq

def initialize():
    initial_state = (6, 0)
    goal_state = (4, 13)
    num_rows = 14
    num_cols = 14
    matrix = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 15, 'x', 'x', 19, 1], ['x', 12, 'x', 19, 'x', 'x', 13, 'x', 14, 13, 8, 'x', 1, 6], ['x', 17, 'x', 19, 5, 4, 'x', 'x', 12, 'x', 'x', 10, 14, 'x'], ['x', 18, 'x', 1, 'x', 14, 'x', 'x', 12, 'x', 11, 4, 4, 7], [2, 15, 'x', 'x', 'x', 14, 'x', 16, 5, 2, 4, 'x', 10, 2], [8, 2, 15, 18, 19, 6, 13, 7, 6, 'x', 'x', 'x', 1, 'x'], [5, 'x', 11, 2, 8, 8, 'x', 1, 10, 8, 13, 7, 12, 18], ['x', 18, 8, 19, 'x', 'x', 16, 11, 2, 'x', 9, 'x', 9, 8], [4, 10, 'x', 12, 12, 13, 13, 2, 13, 'x', 'x', 'x', 8, 18], [1, 'x', 'x', 'x', 5, 12, 18, 16, 5, 17, 'x', 16, 11, 18], [19, 'x', 'x', 'x', 'x', 1, 'x', 'x', 'x', 'x', 10, 19, 'x', 'x'], ['x', 14, 'x', 'x', 'x', 15, 16, 9, 'x', 'x', 'x', 'x', 'x', 'x'], [6, 'x', 16, 18, 6, 'x', 18, 'x', 5, 'x', 'x', 'x', 6, 1], ['x', 'x', 'x', 17, 4, 'x', 6, 'x', 'x', 19, 17, 'x', 19, 15]]
    districts = {1: range(0, 5), 2: range(5, 7), 3: range(7, 14)}
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
