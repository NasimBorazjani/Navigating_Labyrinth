
import heapq

def initialize():
    initial_state = (9, 3)
    goal_state = (4, 14)
    num_rows = 15
    num_cols = 15
    matrix = [['x', 19, 4, 'x', 17, 11, 'x', 'x', 18, 7, 'x', 8, 20, 'x', 1], ['x', 16, 'x', 1, 9, 1, 'x', 8, 16, 'x', 15, 7, 1, 'x', 'x'], [7, 'x', 9, 9, 9, 'x', 18, 'x', 15, 13, 10, 'x', 19, 16, 9], ['x', 'x', 'x', 6, 'x', 'x', 7, 10, 18, 17, 'x', 8, 9, 6, 5], [4, 17, 'x', 'x', 19, 5, 20, 1, 15, 18, 'x', 'x', 5, 8, 2], ['x', 'x', 'x', 3, 10, 19, 17, 20, 'x', 'x', 'x', 3, 'x', 5, 'x'], ['x', 'x', 'x', 3, 8, 2, 'x', 'x', 7, 19, 'x', 'x', 1, 19, 9], ['x', 19, 16, 6, 5, 19, 'x', 'x', 'x', 12, 'x', 3, 8, 10, 'x'], [13, 2, 'x', 18, 'x', 'x', 5, 'x', 'x', 'x', 13, 1, 'x', 'x', 6], [19, 8, 8, 10, 'x', 'x', 'x', 12, 14, 5, 14, 2, 6, 'x', 'x'], ['x', 'x', 'x', 12, 18, 'x', 'x', 'x', 'x', 'x', 'x', 16, 'x', 19, 'x'], [11, 'x', 12, 'x', 'x', 5, 'x', 15, 8, 'x', 9, 'x', 'x', 'x', 'x'], [9, 'x', 4, 'x', 'x', 'x', 'x', 2, 18, 'x', 11, 'x', 11, 'x', 19], [13, 'x', 17, 1, 'x', 14, 'x', 'x', 'x', 'x', 16, 'x', 2, 'x', 'x'], [3, 16, 'x', 'x', 3, 11, 'x', 15, 'x', 'x', 'x', 'x', 'x', 16, 'x']]
    districts = {1: range(0, 4), 2: range(4, 9), 3: range(9, 15)}
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
