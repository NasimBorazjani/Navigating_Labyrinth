
import heapq

def initialize():
    initial_state = (3, 8)
    goal_state = (8, 0)
    num_rows = 13
    num_cols = 13
    matrix = [['x', 14, 15, 10, 'x', 14, 'x', 'x', 18, 6, 'x', 'x', 4], [6, 'x', 'x', 'x', 1, 'x', 15, 'x', 'x', 2, 'x', 17, 'x'], ['x', 4, 'x', 17, 3, 14, 4, 2, 'x', 3, 'x', 11, 'x'], [6, 6, 'x', 19, 'x', 13, 'x', 11, 13, 6, 3, 'x', 'x'], [3, 10, 11, 'x', 'x', 4, 4, 1, 19, 'x', 'x', 'x', 17], [8, 'x', 'x', 8, 11, 18, 17, 19, 18, 'x', 1, 1, 'x'], [14, 14, 1, 19, 6, 'x', 19, 19, 18, 9, 'x', 12, 18], [17, 6, 8, 'x', 1, 14, 19, 13, 'x', 'x', 9, 'x', 3], [16, 4, 'x', 'x', 'x', 9, 5, 'x', 'x', 'x', 18, 'x', 'x'], ['x', 'x', 10, 'x', 18, 'x', 1, 'x', 'x', 12, 9, 8, 3], ['x', 13, 17, 'x', 'x', 'x', 5, 8, 1, 'x', 1, 10, 'x'], [10, 11, 'x', 12, 'x', 6, 11, 'x', 9, 9, 15, 'x', 10], [5, 15, 1, 'x', 8, 5, 'x', 6, 'x', 9, 18, 'x', 'x']]
    districts = {1: range(0, 4), 2: range(4, 8), 3: range(8, 13)}
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
