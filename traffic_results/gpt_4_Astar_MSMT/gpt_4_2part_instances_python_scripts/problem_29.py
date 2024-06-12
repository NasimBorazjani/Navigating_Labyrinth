
import heapq

def initialize():
    initial_state = (3, 9)
    goal_state = (6, 1)
    num_rows = 10
    num_cols = 10
    matrix = [['x', 'x', 'x', 4, 6, 'x', 9, 15, 11, 2], [19, 'x', 14, 3, 10, 18, 'x', 'x', 'x', 1], ['x', 9, 'x', 11, 7, 14, 'x', 'x', 16, 18], ['x', 5, 4, 5, 2, 4, 7, 5, 19, 14], ['x', 3, 20, 'x', 5, 16, 'x', 'x', 1, 9], ['x', 3, 15, 9, 4, 'x', 'x', 'x', 'x', 4], [11, 18, 19, 8, 17, 9, 'x', 10, 10, 19], ['x', 'x', 'x', 17, 7, 'x', 'x', 7, 12, 8], ['x', 'x', 11, 19, 'x', 13, 10, 13, 'x', 'x'], [18, 'x', 'x', 'x', 6, 10, 7, 'x', 8, 'x']]
    districts = {1: range(0, 4), 2: range(4, 6), 3: range(6, 10)}
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
