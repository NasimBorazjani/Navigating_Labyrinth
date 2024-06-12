
import heapq

def initialize():
    initial_state = (2, 10)
    goal_state = (5, 2)
    num_rows = 11
    num_cols = 11
    matrix = [[16, 10, 'x', 16, 1, 12, 6, 12, 3, 7, 'x'], ['x', 16, 10, 9, 12, 19, 7, 10, 12, 13, 7], [5, 'x', 9, 'x', 5, 16, 16, 8, 'x', 16, 8], ['x', 4, 14, 'x', 'x', 'x', 'x', 'x', 'x', 7, 18], [13, 12, 16, 14, 'x', 2, 4, 2, 'x', 6, 3], ['x', 11, 20, 'x', 'x', 'x', 1, 'x', 'x', 9, 'x'], ['x', 'x', 8, 10, 'x', 'x', 3, 1, 'x', 'x', 6], ['x', 2, 9, 'x', 8, 13, 'x', 'x', 'x', 12, 11], [12, 'x', 2, 'x', 'x', 1, 6, 'x', 15, 'x', 1], [3, 'x', 'x', 'x', 17, 'x', 18, 4, 1, 'x', 'x'], ['x', 'x', 6, 'x', 'x', 12, 'x', 'x', 'x', 15, 12]]
    districts = {1: range(0, 2), 2: range(2, 5), 3: range(5, 11)}
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
