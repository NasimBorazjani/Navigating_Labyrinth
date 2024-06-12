
import heapq

def initialize():
    initial_state = (7, 0)
    goal_state = (2, 9)
    num_rows = 11
    num_cols = 11
    matrix = [[12, 11, 14, 10, 2, 11, 13, 16, 3, 'x', 12], [10, 9, 'x', 8, 'x', 'x', 1, 16, 11, 'x', 15], [1, 18, 1, 'x', 'x', 'x', 'x', 'x', 12, 9, 'x'], [1, 14, 15, 10, 7, 15, 17, 10, 15, 15, 6], [18, 11, 'x', 'x', 'x', 15, 'x', 'x', 1, 1, 'x'], [14, 'x', 'x', 'x', 18, 14, 16, 7, 'x', 1, 'x'], [11, 15, 'x', 'x', 15, 3, 11, 13, 'x', 'x', 'x'], [5, 'x', 'x', 'x', 'x', 'x', 15, 'x', 6, 'x', 'x'], [12, 11, 7, 2, 11, 'x', 10, 2, 17, 'x', 'x'], [7, 'x', 'x', 'x', 4, 'x', 4, 'x', 'x', 5, 'x'], ['x', 19, 10, 7, 'x', 2, 3, 9, 2, 6, 'x']]
    districts = {1: range(0, 3), 2: range(3, 7), 3: range(7, 11)}
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
