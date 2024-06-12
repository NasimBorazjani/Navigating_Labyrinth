
import heapq

def initialize():
    initial_state = (3, 10)
    goal_state = (6, 2)
    num_rows = 11
    num_cols = 11
    matrix = [['x', 10, 2, 'x', 'x', 'x', 3, 'x', 4, 'x', 14], ['x', 'x', 17, 16, 8, 'x', 'x', 'x', 'x', 1, 'x'], [18, 18, 16, 16, 15, 'x', 'x', 17, 12, 16, 15], ['x', 4, 'x', 'x', 18, 9, 'x', 15, 'x', 1, 9], [3, 2, 7, 'x', 'x', 17, 2, 14, 'x', 4, 2], [16, 17, 6, 4, 9, 2, 5, 7, 'x', 'x', 7], ['x', 'x', 12, 'x', 'x', 16, 1, 11, 'x', 'x', 4], ['x', 'x', 13, 'x', 'x', 19, 16, 9, 'x', 'x', 'x'], ['x', 'x', 'x', 9, 7, 'x', 11, 5, 'x', 'x', 'x'], ['x', 2, 'x', 'x', 'x', 4, 5, 'x', 10, 'x', 'x'], ['x', 'x', 'x', 12, 16, 'x', 6, 16, 'x', 18, 7]]
    districts = {1: range(0, 4), 2: range(4, 6), 3: range(6, 11)}
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
