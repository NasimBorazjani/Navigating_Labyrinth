
import heapq

def initialize():
    initial_state = (7, 8)
    goal_state = (2, 1)
    num_rows = 11
    num_cols = 11
    matrix = [['x', 18, 'x', 5, 'x', 6, 5, 'x', 6, 17, 'x'], ['x', 'x', 1, 5, 9, 13, 'x', 2, 'x', 'x', 2], ['x', 17, 12, 'x', 'x', 'x', 5, 'x', 'x', 17, 'x'], [9, 3, 13, 8, 'x', 7, 'x', 'x', 4, 2, 'x'], [11, 17, 'x', 10, 'x', 'x', 'x', 'x', 17, 15, 11], ['x', 10, 10, 14, 9, 7, 1, 5, 'x', 'x', 7], ['x', 5, 6, 12, 8, 9, 4, 'x', 'x', 4, 9], [11, 'x', 4, 13, 14, 'x', 12, 17, 13, 'x', 'x'], ['x', 8, 'x', 19, 11, 7, 7, 19, 15, 14, 7], [11, 8, 'x', 11, 10, 16, 'x', 'x', 9, 'x', 5], [9, 4, 'x', 'x', 1, 11, 14, 'x', 'x', 'x', 10]]
    districts = {1: range(0, 3), 2: range(3, 8), 3: range(8, 11)}
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
