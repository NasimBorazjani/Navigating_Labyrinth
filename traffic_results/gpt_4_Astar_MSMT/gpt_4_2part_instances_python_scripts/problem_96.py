
import heapq

def initialize():
    initial_state = (8, 13)
    goal_state = (3, 3)
    num_rows = 15
    num_cols = 15
    matrix = [['x', 9, 'x', 10, 'x', 11, 13, 5, 4, 'x', 'x', 19, 13, 'x', 'x'], ['x', 6, 3, 8, 18, 8, 1, 5, 2, 'x', 'x', 17, 'x', 'x', 'x'], ['x', 'x', 11, 5, 'x', 11, 13, 20, 7, 'x', 'x', 'x', 'x', 15, 4], ['x', 3, 'x', 14, 4, 20, 4, 15, 12, 12, 4, 'x', 8, 4, 'x'], [4, 1, 'x', 9, 17, 'x', 17, 'x', 11, 16, 6, 12, 'x', 18, 'x'], [8, 5, 17, 'x', 'x', 1, 'x', 'x', 'x', 19, 14, 2, 1, 'x', 'x'], [11, 9, 'x', 'x', 14, 'x', 'x', 'x', 'x', 'x', 'x', 2, 12, 4, 16], ['x', 'x', 2, 'x', 'x', 6, 6, 8, 'x', 11, 18, 11, 10, 'x', 'x'], ['x', 'x', 'x', 16, 'x', 7, 'x', 'x', 'x', 'x', 7, 11, 18, 9, 17], [13, 19, 13, 'x', 18, 'x', 14, 'x', 14, 14, 'x', 'x', 20, 15, 15], ['x', 'x', 'x', 'x', 17, 'x', 8, 'x', 'x', 'x', 'x', 'x', 6, 11, 'x'], [5, 'x', 7, 'x', 15, 'x', 'x', 19, 1, 'x', 'x', 10, 'x', 'x', 18], [11, 19, 'x', 18, 'x', 5, 'x', 19, 16, 'x', 'x', 13, 'x', 'x', 5], [8, 16, 6, 13, 1, 'x', 14, 4, 'x', 'x', 'x', 1, 'x', 'x', 5], ['x', 19, 5, 'x', 'x', 'x', 12, 5, 9, 16, 11, 9, 14, 'x', 'x']]
    districts = {1: range(0, 4), 2: range(4, 8), 3: range(8, 15)}
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
