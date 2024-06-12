
import heapq

def initialize():
    initial_state = (7, 12)
    goal_state = (2, 0)
    num_rows = 14
    num_cols = 14
    matrix = [['x', 'x', 'x', 16, 11, 12, 'x', 'x', 17, 3, 'x', 'x', 4, 6], [4, 17, 'x', 'x', 3, 'x', 'x', 1, 9, 11, 12, 4, 'x', 'x'], [5, 'x', 'x', 7, 14, 4, 5, 7, 13, 4, 7, 'x', 'x', 'x'], [6, 6, 19, 3, 15, 'x', 'x', 'x', 'x', 4, 10, 19, 2, 4], [3, 16, 8, 'x', 5, 'x', 12, 17, 16, 'x', 9, 5, 6, 'x'], [17, 2, 'x', 'x', 16, 'x', 5, 'x', 'x', 5, 17, 7, 2, 5], [19, 'x', 'x', 'x', 'x', 2, 15, 15, 'x', 3, 11, 'x', 4, 'x'], ['x', 'x', 11, 'x', 'x', 17, 5, 'x', 5, 'x', 'x', 19, 6, 'x'], [16, 17, 16, 'x', 12, 'x', 2, 18, 9, 7, 'x', 13, 'x', 'x'], [18, 11, 'x', 'x', 19, 5, 'x', 'x', 18, 4, 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 2, 5, 4, 12, 3, 'x', 4, 14, 7, 19], [18, 'x', 'x', 'x', 7, 17, 'x', 'x', 3, 15, 'x', 16, 'x', 10], ['x', 11, 15, 'x', 'x', 'x', 'x', 'x', 2, 13, 'x', 'x', 'x', 3], [4, 8, 'x', 'x', 'x', 'x', 12, 13, 'x', 'x', 19, 'x', 6, 'x']]
    districts = {1: range(0, 3), 2: range(3, 7), 3: range(7, 14)}
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
