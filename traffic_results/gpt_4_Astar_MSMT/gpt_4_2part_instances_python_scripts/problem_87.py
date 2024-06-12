
import heapq

def initialize():
    initial_state = (3, 0)
    goal_state = (6, 12)
    num_rows = 14
    num_cols = 14
    matrix = [['x', 6, 19, 13, 'x', 16, 11, 6, 14, 15, 7, 'x', 'x', 'x'], ['x', 6, 16, 15, 'x', 19, 16, 18, 'x', 8, 10, 'x', 'x', 'x'], ['x', 5, 10, 14, 2, 'x', 'x', 'x', 11, 'x', 11, 'x', 'x', 'x'], [6, 13, 15, 10, 'x', 'x', 'x', 'x', 19, 'x', 'x', 'x', 2, 'x'], ['x', 15, 10, 6, 6, 8, 10, 9, 11, 'x', 'x', 'x', 16, 'x'], ['x', 'x', 'x', 8, 15, 12, 10, 19, 1, 18, 19, 4, 'x', 10], [1, 17, 'x', 'x', 6, 8, 4, 'x', 15, 8, 10, 6, 4, 'x'], ['x', 'x', 'x', 'x', 13, 'x', 5, 'x', 9, 10, 'x', 'x', 'x', 'x'], [12, 'x', 11, 'x', 13, 'x', 11, 7, 5, 13, 'x', 'x', 6, 15], ['x', 18, 19, 'x', 'x', 'x', 3, 'x', 16, 11, 'x', 15, 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 2, 15, 'x', 'x', 8, 'x', 'x', 'x'], [11, 'x', 6, 13, 12, 'x', 12, 'x', 'x', 9, 'x', 17, 'x', 'x'], ['x', 1, 'x', 18, 18, 3, 'x', 11, 13, 1, 13, 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 6, 'x', 'x', 8, 'x', 'x', 'x', 4, 11]]
    districts = {1: range(0, 3), 2: range(3, 6), 3: range(6, 14)}
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
