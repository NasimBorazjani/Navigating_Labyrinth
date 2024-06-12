
import heapq

def initialize():
    initial_state = (2, 0)
    goal_state = (7, 8)
    num_rows = 12
    num_cols = 12
    matrix = [[4, 1, 20, 15, 9, 'x', 8, 6, 'x', 'x', 14, 'x'], [5, 11, 9, 12, 10, 4, 15, 18, 7, 'x', 'x', 13], [15, 9, 1, 'x', 18, 3, 1, 19, 'x', 'x', 17, 17], ['x', 17, 11, 10, 'x', 19, 8, 'x', 'x', 'x', 'x', 7], [5, 'x', 1, 'x', 14, 13, 4, 8, 5, 'x', 13, 14], [16, 6, 'x', 'x', 'x', 17, 'x', 15, 4, 'x', 'x', 15], ['x', 'x', 'x', 15, 'x', 19, 10, 'x', 16, 18, 11, 1], [6, 8, 'x', 3, 'x', 5, 5, 'x', 3, 8, 9, 14], [10, 14, 'x', 'x', 'x', 'x', 'x', 'x', 6, 2, 'x', 'x'], [12, 'x', 'x', 6, 11, 4, 'x', 'x', 12, 'x', 4, 16], [4, 'x', 'x', 'x', 11, 'x', 'x', 'x', 18, 16, 'x', 10], ['x', 6, 'x', 'x', 11, 'x', 5, 13, 8, 1, 17, 9]]
    districts = {1: range(0, 2), 2: range(2, 7), 3: range(7, 12)}
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
