
import heapq

def initialize():
    initial_state = (3, 10)
    goal_state = (9, 2)
    num_rows = 13
    num_cols = 13
    matrix = [['x', 17, 14, 18, 'x', 'x', 8, 18, 10, 5, 5, 'x', 'x'], ['x', 'x', 'x', 'x', 17, 18, 17, 17, 6, 12, 'x', 7, 16], [17, 'x', 17, 6, 18, 'x', 10, 13, 10, 19, 15, 4, 13], [15, 5, 15, 3, 17, 3, 'x', 'x', 18, 15, 19, 3, 2], ['x', 'x', 'x', 'x', 2, 10, 'x', 'x', 'x', 18, 14, 5, 12], ['x', 16, 'x', 12, 4, 7, 'x', 'x', 9, 'x', 'x', 'x', 'x'], ['x', 7, 'x', 'x', 16, 2, 9, 1, 3, 'x', 'x', 4, 'x'], [15, 16, 'x', 10, 1, 16, 'x', 'x', 2, 18, 1, 'x', 'x'], ['x', 'x', 8, 3, 'x', 19, 'x', 'x', 'x', 5, 9, 'x', 'x'], ['x', 8, 12, 14, 'x', 'x', 'x', 16, 'x', 8, 'x', 3, 2], [8, 1, 'x', 'x', 'x', 'x', 13, 'x', 'x', 'x', 9, 'x', 12], ['x', 'x', 3, 3, 11, 'x', 'x', 16, 'x', 'x', 5, 'x', 'x'], ['x', 11, 17, 'x', 'x', 'x', 'x', 9, 'x', 'x', 2, 15, 'x']]
    districts = {1: range(0, 4), 2: range(4, 9), 3: range(9, 13)}
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
