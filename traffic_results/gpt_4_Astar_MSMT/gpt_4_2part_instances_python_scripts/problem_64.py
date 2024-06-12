
import heapq

def initialize():
    initial_state = (3, 0)
    goal_state = (6, 12)
    num_rows = 13
    num_cols = 13
    matrix = [[8, 'x', 12, 'x', 16, 'x', 'x', 'x', 7, 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 16, 'x', 7, 8, 'x', 17, 'x', 19, 'x'], [7, 'x', 13, 'x', 19, 'x', 6, 'x', 14, 'x', 18, 'x', 19], [9, 20, 2, 'x', 10, 6, 'x', 18, 'x', 'x', 'x', 18, 'x'], ['x', 'x', 8, 12, 7, 14, 13, 9, 8, 6, 14, 11, 7], ['x', 14, 'x', 'x', 'x', 19, 13, 15, 3, 12, 16, 16, 3], ['x', 'x', 'x', 13, 'x', 9, 13, 10, 'x', 14, 'x', 4, 18], [6, 12, 10, 'x', 'x', 18, 7, 20, 18, 'x', 13, 1, 'x'], ['x', 5, 'x', 18, 12, 'x', 'x', 3, 12, 14, 19, 16, 'x'], [10, 'x', 19, 'x', 'x', 'x', 'x', 11, 14, 16, 12, 'x', 8], [8, 'x', 'x', 'x', 'x', 'x', 'x', 9, 16, 15, 'x', 'x', 8], ['x', 'x', 2, 'x', 1, 'x', 'x', 16, 'x', 'x', 3, 'x', 'x'], [9, 'x', 5, 'x', 'x', 15, 'x', 'x', 'x', 7, 15, 9, 'x']]
    districts = {1: range(0, 4), 2: range(4, 6), 3: range(6, 13)}
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
