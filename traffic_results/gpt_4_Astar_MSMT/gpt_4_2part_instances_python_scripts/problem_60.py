
import heapq

def initialize():
    initial_state = (3, 0)
    goal_state = (9, 7)
    num_rows = 12
    num_cols = 12
    matrix = [[16, 'x', 5, 6, 'x', 14, 12, 'x', 'x', 'x', 6, 'x'], [17, 'x', 'x', 'x', 5, 'x', 5, 7, 'x', 'x', 8, 'x'], [3, 19, 'x', 'x', 'x', 'x', 18, 'x', 13, 7, 'x', 'x'], [13, 'x', 4, 'x', 'x', 8, 7, 4, 'x', 15, 'x', 'x'], [5, 17, 18, 12, 3, 'x', 14, 2, 4, 18, 'x', 1], [4, 10, 1, 19, 10, 'x', 'x', 17, 'x', 17, 16, 4], [7, 'x', 16, 'x', 'x', 1, 3, 'x', 13, 13, 'x', 'x'], ['x', 'x', 9, 1, 7, 18, 16, 3, 'x', 4, 'x', 'x'], [2, 'x', 13, 10, 'x', 4, 'x', 'x', 'x', 'x', 'x', 12], ['x', 'x', 'x', 18, 8, 4, 'x', 11, 'x', 14, 18, 'x'], ['x', 19, 2, 'x', 2, 6, 5, 18, 'x', 5, 'x', 'x'], ['x', 2, 'x', 7, 'x', 'x', 8, 7, 'x', 11, 16, 'x']]
    districts = {1: range(0, 4), 2: range(4, 9), 3: range(9, 12)}
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
