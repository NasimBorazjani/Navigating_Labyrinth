
import heapq

def initialize():
    initial_state = (6, 1)
    goal_state = (3, 13)
    num_rows = 14
    num_cols = 14
    matrix = [['x', 5, 9, 6, 13, 13, 8, 6, 13, 'x', 13, 'x', 'x', 'x'], [3, 10, 16, 'x', 'x', 3, 13, 1, 11, 9, 7, 6, 'x', 18], [9, 11, 3, 'x', 'x', 6, 13, 'x', 14, 'x', 12, 1, 2, 4], ['x', 17, 13, 'x', 14, 4, 6, 8, 'x', 'x', 1, 'x', 6, 2], [7, 'x', 11, 'x', 14, 'x', 11, 7, 'x', 5, 'x', 1, 12, 'x'], ['x', 20, 20, 19, 'x', 18, 2, 19, 1, 6, 12, 'x', 'x', 16], [8, 5, 7, 11, 'x', 1, 'x', 'x', 'x', 11, 4, 'x', 'x', 3], ['x', 11, 'x', 11, 11, 'x', 'x', 18, 'x', 'x', 'x', 7, 6, 'x'], [2, 2, 14, 5, 5, 'x', 'x', 11, 19, 16, 'x', 14, 7, 19], ['x', 5, 'x', 'x', 7, 'x', 10, 'x', 'x', 'x', 3, 15, 'x', 'x'], [19, 'x', 'x', 'x', 'x', 8, 3, 19, 'x', 18, 'x', 'x', 'x', 9], [17, 'x', 19, 'x', 'x', 'x', 5, 3, 'x', 'x', 7, 4, 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 12, 11, 'x', 'x', 'x', 'x', 'x', 6, 6], ['x', 'x', 'x', 'x', 'x', 'x', 4, 'x', 'x', 'x', 7, 'x', 6, 3]]
    districts = {1: range(0, 2), 2: range(2, 6), 3: range(6, 14)}
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
