
import heapq

def initialize():
    initial_state = (7, 0)
    goal_state = (4, 13)
    num_rows = 15
    num_cols = 15
    matrix = [['x', 3, 1, 19, 8, 1, 4, 18, 15, 17, 4, 3, 'x', 3, 'x'], ['x', 11, 'x', 'x', 'x', 12, 'x', 19, 15, 4, 'x', 'x', 'x', 'x', 'x'], [4, 1, 'x', 8, 'x', 12, 17, 'x', 14, 4, 9, 11, 13, 6, 19], [2, 'x', 6, 14, 15, 'x', 18, 9, 'x', 10, 10, 'x', 'x', 1, 'x'], ['x', 11, 'x', 8, 'x', 5, 'x', 8, 7, 6, 'x', 'x', 13, 6, 'x'], ['x', 'x', 'x', 17, 'x', 13, 'x', 'x', 'x', 'x', 18, 19, 5, 'x', 'x'], ['x', 12, 18, 'x', 'x', 'x', 19, 'x', 12, 'x', 11, 7, 19, 12, 'x'], [6, 6, 'x', 6, 4, 'x', 18, 'x', 'x', 15, 18, 'x', 6, 8, 'x'], [10, 10, 'x', 'x', 6, 4, 11, 19, 'x', 9, 'x', 2, 'x', 3, 14], ['x', 18, 14, 10, 'x', 1, 'x', 6, 'x', 15, 'x', 6, 'x', 14, 'x'], ['x', 'x', 7, 10, 'x', 2, 'x', 7, 14, 4, 11, 'x', 'x', 'x', 'x'], [12, 'x', 6, 'x', 8, 5, 6, 6, 8, 'x', 'x', 'x', 'x', 4, 7], ['x', 'x', 1, 8, 10, 4, 10, 17, 19, 11, 2, 'x', 'x', 'x', 16], ['x', 'x', 'x', 17, 8, 19, 'x', 14, 'x', 17, 17, 5, 7, 6, 7], [1, 'x', 14, 'x', 3, 'x', 18, 6, 18, 8, 'x', 13, 10, 'x', 'x']]
    districts = {1: range(0, 5), 2: range(5, 9), 3: range(9, 15)}
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [initial_state], initial_state, {1: False, 2: False, 3: False})]
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
