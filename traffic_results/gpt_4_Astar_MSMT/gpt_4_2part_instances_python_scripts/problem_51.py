
import heapq

def initialize():
    initial_state = (6, 2)
    goal_state = (2, 10)
    num_rows = 12
    num_cols = 12
    matrix = [[19, 12, 'x', 'x', 2, 5, 4, 13, 17, 19, 'x', 2], ['x', 18, 'x', 5, 5, 'x', 'x', 8, 12, 18, 'x', 15], ['x', 9, 4, 10, 7, 20, 'x', 16, 20, 13, 15, 'x'], [8, 'x', 'x', 11, 1, 19, 'x', 14, 6, 'x', 3, 'x'], [10, 'x', 4, 8, 17, 'x', 18, 'x', 7, 'x', 6, 5], ['x', 'x', 3, 1, 8, 18, 'x', 4, 17, 'x', 'x', 13], ['x', 'x', 6, 'x', 'x', 'x', 14, 'x', 'x', 10, 10, 'x'], ['x', 'x', 15, 'x', 'x', 'x', 'x', 'x', 2, 'x', 'x', 'x'], ['x', 'x', 5, 11, 6, 1, 'x', 6, 14, 'x', 'x', 'x'], ['x', 1, 17, 10, 15, 'x', 14, 6, 'x', 'x', 'x', 'x'], [12, 2, 'x', 10, 'x', 'x', 7, 'x', 'x', 'x', 'x', 'x'], ['x', 9, 14, 'x', 9, 18, 14, 'x', 'x', 'x', 6, 'x']]
    districts = {1: range(0, 2), 2: range(2, 6), 3: range(6, 12)}
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
