
import heapq

def initialize():
    initial_state = (3, 11)
    goal_state = (4, 0)
    num_rows = 12
    num_cols = 12
    matrix = [['x', 'x', 13, 9, 'x', 15, 'x', 'x', 2, 13, 9, 11], [8, 'x', 4, 5, 13, 'x', 'x', 7, 16, 'x', 15, 13], ['x', 'x', 'x', 'x', 3, 'x', 4, 3, 18, 'x', 11, 18], [6, 'x', 14, 5, 16, 'x', 11, 'x', 3, 16, 3, 3], [15, 12, 'x', 'x', 10, 3, 2, 14, 'x', 18, 'x', 'x'], [11, 1, 2, 1, 17, 15, 'x', 2, 'x', 12, 'x', 'x'], ['x', 'x', 3, 15, 16, 1, 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 10, 'x', 'x', 'x', 6, 1, 8, 19, 13, 7, 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 3], [3, 7, 12, 'x', 15, 'x', 19, 13, 17, 14, 'x', 'x'], ['x', 'x', 'x', 'x', 4, 4, 18, 'x', 5, 'x', 'x', 10], ['x', 'x', 15, 9, 13, 10, 8, 4, 8, 6, 7, 7]]
    districts = {1: range(0, 3), 2: range(3, 6), 3: range(6, 12)}
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
