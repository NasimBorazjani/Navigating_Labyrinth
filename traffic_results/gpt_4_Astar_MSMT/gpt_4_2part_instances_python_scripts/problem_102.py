
import heapq

def initialize():
    initial_state = (5, 0)
    goal_state = (7, 13)
    num_rows = 15
    num_cols = 15
    matrix = [['x', 13, 'x', 'x', 'x', 'x', 3, 4, 'x', 'x', 9, 'x', 18, 7, 2], [1, 10, 17, 'x', 'x', 'x', 11, 13, 'x', 10, 'x', 9, 13, 'x', 'x'], ['x', 'x', 7, 18, 'x', 'x', 'x', 'x', 7, 'x', 'x', 'x', 1, 'x', 16], [10, 'x', 'x', 'x', 13, 'x', 2, 9, 'x', 'x', 8, 'x', 'x', 5, 'x'], ['x', 7, 12, 'x', 1, 18, 14, 'x', 7, 'x', 'x', 16, 'x', 'x', 19], [5, 1, 13, 17, 11, 14, 16, 'x', 14, 'x', 18, 5, 'x', 18, 'x'], ['x', 15, 19, 4, 'x', 13, 'x', 5, 'x', 'x', 18, 'x', 17, 'x', 'x'], [3, 7, 'x', 'x', 'x', 12, 'x', 'x', 17, 4, 'x', 13, 19, 3, 10], [11, 'x', 'x', 'x', 'x', 2, 2, 19, 13, 4, 7, 17, 16, 'x', 17], [12, 5, 4, 'x', 'x', 'x', 'x', 12, 8, 11, 'x', 17, 14, 19, 2], [4, 10, 'x', 'x', 6, 11, 16, 17, 'x', 'x', 18, 'x', 17, 'x', 'x'], ['x', 'x', 'x', 'x', 11, 9, 18, 17, 12, 'x', 'x', 'x', 'x', 'x', 1], [18, 13, 7, 'x', 'x', 5, 4, 13, 'x', 'x', 19, 12, 1, 18, 'x'], [15, 'x', 17, 'x', 'x', 'x', 17, 'x', 'x', 'x', 10, 'x', 15, 16, 'x'], ['x', 'x', 11, 15, 'x', 'x', 12, 16, 12, 13, 18, 'x', 17, 8, 15]]
    districts = {1: range(0, 6), 2: range(6, 7), 3: range(7, 15)}
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state, {1: True, 2: False, 3: False})]
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
