
import heapq

def initialize():
    initial_state = (1, 9)
    goal_state = (6, 3)
    num_rows = 10
    num_cols = 10
    matrix = [[15, 4, 9, 10, 19, 'x', 12, 4, 'x', 15], [12, 19, 11, 'x', 'x', 'x', 'x', 7, 6, 3], [4, 'x', 8, 'x', 'x', 19, 'x', 11, 1, 6], ['x', 'x', 5, 'x', 'x', 'x', 12, 6, 6, 'x'], ['x', 14, 'x', 'x', 14, 11, 2, 9, 6, 14], [8, 8, 5, 17, 7, 'x', 1, 2, 'x', 6], [18, 'x', 'x', 15, 'x', 15, 4, 'x', 'x', 7], [19, 'x', 10, 18, 14, 'x', 14, 9, 8, 6], [19, 'x', 14, 'x', 10, 8, 15, 'x', 15, 'x'], [12, 1, 'x', 5, 3, 3, 'x', 'x', 'x', 'x']]
    districts = {1: range(0, 2), 2: range(2, 7), 3: range(7, 10)}
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
