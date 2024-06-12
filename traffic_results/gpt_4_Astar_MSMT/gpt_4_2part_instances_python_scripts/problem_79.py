
import heapq

def initialize():
    initial_state = (4, 12)
    goal_state = (7, 0)
    num_rows = 14
    num_cols = 14
    matrix = [['x', 'x', 17, 7, 'x', 'x', 11, 4, 5, 15, 17, 6, 6, 2], [17, 'x', 'x', 6, 'x', 'x', 'x', 'x', 1, 8, 'x', 'x', 'x', 7], ['x', 'x', 'x', 17, 4, 10, 6, 4, 'x', 8, 16, 11, 'x', 'x'], ['x', 4, 'x', 'x', 10, 'x', 8, 10, 'x', 11, 'x', 'x', 1, 'x'], ['x', 'x', 11, 9, 4, 'x', 8, 8, 'x', 'x', 'x', 16, 13, 8], ['x', 12, 3, 15, 13, 13, 'x', 15, 19, 'x', 2, 2, 6, 'x'], [15, 1, 'x', 'x', 'x', 'x', 5, 4, 'x', 5, 12, 2, 5, 'x'], [20, 13, 7, 18, 8, 18, 5, 2, 17, 7, 11, 'x', 15, 13], [4, 11, 'x', 'x', 10, 9, 'x', 18, 14, 'x', 19, 'x', 'x', 'x'], [19, 'x', 2, 'x', 18, 17, 10, 'x', 'x', 'x', 13, 15, 'x', 10], [16, 5, 2, 3, 13, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 3], ['x', 'x', 'x', 'x', 17, 9, 'x', 'x', 'x', 'x', 'x', 6, 'x', 'x'], [11, 'x', 'x', 9, 14, 'x', 'x', 16, 'x', 15, 13, 13, 15, 1], [9, 'x', 'x', 10, 14, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 1, 19]]
    districts = {1: range(0, 5), 2: range(5, 7), 3: range(7, 14)}
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
