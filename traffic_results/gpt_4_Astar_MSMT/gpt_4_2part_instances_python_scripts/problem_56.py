
import heapq

def initialize():
    initial_state = (6, 9)
    goal_state = (3, 0)
    num_rows = 12
    num_cols = 12
    matrix = [[2, 'x', 'x', 14, 'x', 19, 6, 'x', 'x', 14, 18, 'x'], ['x', 10, 1, 15, 'x', 'x', 'x', 'x', 17, 2, 9, 12], [13, 14, 'x', 2, 'x', 'x', 10, 10, 'x', 'x', 'x', 'x'], [9, 17, 3, 15, 4, 4, 'x', 9, 15, 16, 'x', 9], [10, 7, 3, 8, 'x', 7, 'x', 16, 3, 7, 'x', 'x'], [16, 20, 16, 19, 18, 3, 'x', 'x', 11, 14, 5, 'x'], [14, 13, 8, 14, 12, 19, 6, 3, 19, 10, 11, 'x'], ['x', 18, 'x', 'x', 4, 19, 6, 14, 15, 17, 7, 'x'], ['x', 2, 'x', 'x', 'x', 'x', 'x', 7, 'x', 19, 'x', 'x'], ['x', 3, 14, 1, 'x', 18, 4, 12, 'x', 3, 10, 'x'], [2, 'x', 16, 13, 'x', 17, 'x', 'x', 17, 16, 4, 10], ['x', 4, 10, 'x', 'x', 'x', 7, 'x', 19, 7, 'x', 'x']]
    districts = {1: range(0, 4), 2: range(4, 7), 3: range(7, 12)}
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
