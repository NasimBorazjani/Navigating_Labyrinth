
import heapq

def initialize():
    initial_state = (5, 2)
    goal_state = (9, 13)
    num_rows = 15
    num_cols = 15
    matrix = [['x', 'x', 'x', 'x', 9, 'x', 14, 17, 'x', 13, 3, 'x', 13, 10, 18], [1, 'x', 11, 12, 14, 13, 8, 'x', 5, 7, 'x', 'x', 'x', 'x', 'x'], [3, 'x', 'x', 18, 11, 16, 'x', 'x', 'x', 'x', 1, 'x', 15, 12, 10], ['x', 10, 'x', 3, 2, 15, 14, 'x', 'x', 'x', 17, 'x', 6, 1, 'x'], [8, 10, 'x', 'x', 'x', 'x', 1, 19, 6, 'x', 17, 2, 'x', 'x', 'x'], ['x', 6, 15, 2, 17, 2, 11, 5, 9, 'x', 12, 15, 'x', 'x', 16], ['x', 'x', 8, 'x', 14, 'x', 13, 20, 17, 12, 19, 9, 'x', 'x', 'x'], [13, 10, 1, 4, 11, 3, 15, 'x', 'x', 3, 14, 20, 'x', 6, 'x'], ['x', 11, 16, 9, 19, 18, 12, 2, 'x', 'x', 1, 10, 'x', 'x', 'x'], ['x', 13, 18, 18, 7, 'x', 'x', 'x', 'x', 18, 5, 6, 'x', 7, 3], ['x', 'x', 'x', 18, 6, 16, 10, 18, 9, 19, 'x', 3, 5, 3, 4], [14, 18, 4, 1, 17, 'x', 7, 'x', 3, 16, 11, 'x', 17, 11, 1], ['x', 'x', 12, 16, 'x', 14, 9, 'x', 'x', 'x', 13, 1, 'x', 'x', 19], [19, 'x', 3, 'x', 8, 'x', 'x', 'x', 3, 'x', 'x', 'x', 17, 9, 8], [15, 'x', 2, 8, 9, 13, 'x', 14, 'x', 6, 'x', 19, 'x', 'x', 5]]
    districts = {1: range(0, 5), 2: range(5, 10), 3: range(10, 15)}
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
