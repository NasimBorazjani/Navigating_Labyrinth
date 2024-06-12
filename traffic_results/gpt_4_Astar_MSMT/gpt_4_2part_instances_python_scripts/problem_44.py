
import heapq

def initialize():
    initial_state = (8, 10)
    goal_state = (3, 4)
    num_rows = 11
    num_cols = 11
    matrix = [['x', 16, 5, 13, 'x', 'x', 2, 'x', 6, 'x', 'x'], ['x', 'x', 17, 'x', 15, 'x', 10, 'x', 5, 17, 'x'], ['x', 'x', 'x', 'x', 15, 3, 10, 2, 4, 13, 14], ['x', 'x', 'x', 'x', 17, 2, 4, 'x', 1, 4, 5], [2, 'x', 'x', 2, 6, 17, 'x', 'x', 'x', 4, 19], [19, 5, 'x', 'x', 'x', 'x', 10, 12, 1, 18, 10], ['x', 3, 'x', 12, 'x', 10, 15, 11, 'x', 4, 15], [2, 'x', 11, 9, 'x', 12, 11, 'x', 15, 10, 6], [19, 'x', 16, 5, 'x', 'x', 'x', 11, 'x', 11, 8], [12, 2, 'x', 3, 'x', 4, 'x', 'x', 15, 'x', 'x'], ['x', 'x', 18, 16, 'x', 'x', 4, 'x', 12, 13, 'x']]
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
