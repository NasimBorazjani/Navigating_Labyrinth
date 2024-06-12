
import heapq

def initialize():
    initial_state = (8, 1)
    goal_state = (5, 11)
    num_rows = 12
    num_cols = 12
    matrix = [['x', 3, 11, 7, 'x', 'x', 1, 3, 'x', 'x', 'x', 3], ['x', 10, 'x', 'x', 3, 9, 7, 8, 'x', 2, 'x', 17], [6, 16, 'x', 18, 10, 5, 'x', 6, 'x', 'x', 7, 'x'], ['x', 10, 'x', 8, 13, 10, 'x', 'x', 'x', 'x', 6, 13], [6, 11, 3, 16, 8, 15, 'x', 'x', 'x', 13, 12, 20], [15, 'x', 16, 'x', 17, 13, 'x', 'x', 8, 6, 19, 9], [14, 10, 16, 14, 'x', 'x', 10, 11, 19, 15, 17, 'x'], ['x', 'x', 'x', 'x', 18, 13, 14, 19, 12, 1, 3, 'x'], [15, 1, 3, 17, 4, 18, 'x', 18, 2, 7, 12, 'x'], [19, 'x', 13, 17, 2, 14, 8, 'x', 'x', 8, 16, 'x'], ['x', 19, 'x', 15, 'x', 18, 'x', 13, 'x', 13, 'x', 'x'], [7, 14, 2, 'x', 10, 3, 'x', 'x', 2, 5, 10, 'x']]
    districts = {1: range(0, 5), 2: range(5, 9), 3: range(9, 12)}
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
