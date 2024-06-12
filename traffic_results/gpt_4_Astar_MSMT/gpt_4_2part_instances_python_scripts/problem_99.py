
import heapq

def initialize():
    initial_state = (4, 14)
    goal_state = (8, 3)
    num_rows = 15
    num_cols = 15
    matrix = [[7, 6, 11, 'x', 'x', 'x', 19, 'x', 9, 15, 12, 8, 10, 15, 5], [9, 14, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 18, 2, 11, 'x', 10], [14, 5, 'x', 'x', 4, 4, 12, 'x', 18, 'x', 17, 11, 3, 18, 19], [18, 17, 'x', 8, 'x', 'x', 9, 'x', 'x', 8, 19, 10, 'x', 'x', 'x'], [7, 'x', 'x', 11, 4, 'x', 'x', 10, 1, 2, 3, 12, 8, 12, 15], ['x', 3, 7, 8, 'x', 'x', 'x', 'x', 4, 16, 13, 19, 14, 10, 13], [18, 1, 2, 'x', 16, 20, 5, 'x', 2, 4, 20, 12, 14, 18, 16], [1, 'x', 1, 'x', 15, 19, 11, 9, 19, 16, 'x', 'x', 'x', 'x', 19], ['x', 8, 'x', 1, 7, 'x', 2, 3, 'x', 'x', 'x', 'x', 1, 3, 'x'], [6, 16, 'x', 3, 'x', 18, 'x', 2, 18, 'x', 'x', 16, 'x', 'x', 8], ['x', 9, 'x', 5, 2, 'x', 'x', 'x', 'x', 17, 'x', 6, 18, 14, 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 18, 'x', 'x', 3, 'x', 10, 'x', 'x'], ['x', 2, 15, 'x', 5, 15, 18, 8, 19, 'x', 'x', 'x', 'x', 'x', 10], ['x', 'x', 4, 'x', 7, 2, 2, 'x', 19, 'x', 'x', 'x', 'x', 'x', 'x'], [17, 'x', 'x', 'x', 5, 'x', 'x', 'x', 4, 1, 18, 'x', 9, 2, 8]]
    districts = {1: range(0, 5), 2: range(5, 8), 3: range(8, 15)}
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
