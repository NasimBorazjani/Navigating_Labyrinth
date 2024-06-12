
import heapq

def initialize():
    initial_state = (4, 11)
    goal_state = (9, 2)
    num_rows = 12
    num_cols = 12
    matrix = [[19, 14, 16, 4, 15, 16, 15, 'x', 9, 'x', 'x', 'x'], ['x', 7, 12, 6, 'x', 12, 'x', 3, 'x', 14, 5, 9], [1, 12, 'x', 'x', 12, 'x', 'x', 'x', 'x', 'x', 10, 1], ['x', 1, 15, 14, 'x', 2, 13, 'x', 'x', 'x', 10, 9], [7, 'x', 13, 'x', 14, 1, 14, 8, 'x', 'x', 8, 5], [18, 'x', 8, 13, 12, 13, 'x', 12, 3, 'x', 14, 'x'], ['x', 15, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 17, 10], ['x', 5, 'x', 4, 'x', 'x', 'x', 3, 5, 6, 6, 11], ['x', 15, 6, 'x', 4, 18, 'x', 'x', 14, 10, 2, 8], [13, 10, 13, 7, 3, 6, 'x', 'x', 10, 17, 10, 15], [4, 'x', 'x', 7, 19, 4, 13, 13, 12, 'x', 'x', 13], [5, 'x', 'x', 9, 19, 18, 'x', 'x', 16, 'x', 2, 'x']]
    districts = {1: range(0, 4), 2: range(4, 9), 3: range(9, 12)}
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
