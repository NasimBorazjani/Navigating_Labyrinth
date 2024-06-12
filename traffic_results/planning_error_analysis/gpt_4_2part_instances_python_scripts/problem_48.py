
import heapq

def initialize():
    initial_state = (3, 3)
    goal_state = (8, 11)
    num_rows = 12
    num_cols = 12
    matrix = [[10, 'x', 'x', 1, 1, 'x', 'x', 'x', 'x', 'x', 'x', 'x'], [11, 9, 17, 'x', 14, 3, 'x', 13, 'x', 'x', 6, 'x'], ['x', 5, 'x', 'x', 10, 13, 13, 19, 10, 'x', 1, 12], [6, 'x', 'x', 17, 5, 6, 17, 4, 5, 'x', 1, 'x'], [4, 11, 1, 'x', 'x', 'x', 14, 7, 19, 4, 'x', 6], ['x', 'x', 6, 18, 'x', 'x', 'x', 5, 8, 2, 1, 'x'], [19, 19, 10, 9, 19, 19, 'x', 6, 'x', 1, 14, 11], ['x', 'x', 'x', 18, 11, 'x', 7, 5, 15, 13, 1, 11], ['x', 4, 'x', 8, 'x', 11, 'x', 'x', 9, 'x', 'x', 15], [10, 8, 10, 2, 'x', 'x', 'x', 'x', 'x', 12, 'x', 17], [19, 'x', 3, 11, 'x', 'x', 9, 3, 15, 'x', 5, 17], [18, 'x', 'x', 'x', 11, 14, 'x', 14, 13, 'x', 'x', 8]]
    districts = {1: range(0, 3), 2: range(3, 8), 3: range(8, 12)}
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
