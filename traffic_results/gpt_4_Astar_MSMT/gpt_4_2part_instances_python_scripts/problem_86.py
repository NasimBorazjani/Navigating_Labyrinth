
import heapq

def initialize():
    initial_state = (3, 0)
    goal_state = (5, 12)
    num_rows = 14
    num_cols = 14
    matrix = [['x', 'x', 11, 16, 'x', 'x', 'x', 'x', 4, 'x', 14, 5, 'x', 'x'], [3, 1, 13, 'x', 'x', 14, 11, 'x', 'x', 15, 12, 15, 'x', 'x'], [17, 15, 17, 10, 11, 'x', 7, 1, 1, 14, 'x', 9, 'x', 'x'], [8, 'x', 'x', 13, 2, 12, 'x', 8, 'x', 'x', 9, 13, 19, 5], [4, 'x', 2, 3, 8, 'x', 'x', 17, 'x', 'x', 16, 10, 'x', 'x'], ['x', 'x', 'x', 'x', 3, 13, 14, 16, 18, 11, 4, 19, 20, 'x'], ['x', 11, 'x', 'x', 3, 10, 8, 9, 18, 7, 1, 14, 'x', 6], [11, 'x', 12, 11, 'x', 11, 10, 3, 10, 12, 15, 'x', 11, 'x'], ['x', 'x', 4, 18, 'x', 'x', 13, 'x', 14, 10, 'x', 8, 'x', 17], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 7, 7, 'x', 'x', 18, 19, 18], [19, 4, 'x', 2, 14, 2, 'x', 9, 'x', 10, 7, 17, 4, 12], [13, 2, 'x', 'x', 18, 5, 'x', 11, 'x', 'x', 'x', 18, 'x', 'x'], ['x', 'x', 13, 1, 13, 'x', 2, 'x', 'x', 'x', 'x', 'x', 'x', 14], ['x', 12, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 19, 'x', 'x', 9, 1]]
    districts = {1: range(0, 4), 2: range(4, 7), 3: range(7, 14)}
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
