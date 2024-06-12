
import heapq

def initialize():
    initial_state = (3, 9)
    goal_state = (7, 1)
    num_rows = 12
    num_cols = 12
    matrix = [[12, 17, 10, 'x', 'x', 'x', 'x', 9, 15, 5, 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 12, 20, 9, 19, 8, 12, 11], [9, 'x', 'x', 2, 'x', 2, 1, 9, 8, 14, 16, 'x'], [19, 'x', 1, 20, 7, 9, 18, 'x', 18, 7, 'x', 'x'], [5, 2, 11, 9, 'x', 5, 4, 16, 'x', 1, 'x', 10], [10, 8, 8, 4, 11, 11, 'x', 'x', 5, 'x', 'x', 'x'], [15, 15, 'x', 'x', 13, 5, 19, 'x', 'x', 15, 'x', 'x'], [15, 16, 9, 18, 'x', 'x', 16, 'x', 'x', 'x', 5, 12], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 14, 14, 'x', 'x', 15, 6, 6, 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 8, 14, 'x', 5, 'x', 'x', 15], ['x', 6, 15, 'x', 'x', 'x', 'x', 'x', 'x', 8, 'x', 'x']]
    districts = {1: range(0, 4), 2: range(4, 7), 3: range(7, 12)}
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
