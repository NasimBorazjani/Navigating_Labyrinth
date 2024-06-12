
import heapq

def initialize():
    initial_state = (5, 7)
    goal_state = (2, 1)
    num_rows = 9
    num_cols = 9
    matrix = [[13, 'x', 'x', 3, 10, 20, 3, 'x', 5], ['x', 'x', 'x', 'x', 20, 16, 'x', 'x', 17], [3, 14, 18, 8, 1, 20, 14, 'x', 7], [13, 3, 6, 10, 7, 4, 6, 6, 1], [10, 12, 2, 'x', 11, 'x', 10, 8, 11], ['x', 'x', 'x', 11, 6, 18, 13, 20, 17], ['x', 'x', 16, 'x', 4, 17, 7, 10, 15], ['x', 7, 16, 6, 19, 4, 7, 'x', 'x'], ['x', 11, 18, 'x', 'x', 'x', 3, 8, 'x']]
    districts = {1: range(0, 3), 2: range(3, 5), 3: range(5, 9)}
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
