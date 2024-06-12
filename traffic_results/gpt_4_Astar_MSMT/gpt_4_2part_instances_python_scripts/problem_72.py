
import heapq

def initialize():
    initial_state = (6, 12)
    goal_state = (5, 0)
    num_rows = 13
    num_cols = 13
    matrix = [['x', 'x', 'x', 'x', 9, 1, 14, 'x', 'x', 'x', 11, 15, 12], [2, 'x', 18, 'x', 14, 'x', 11, 3, 'x', 'x', 'x', 'x', 'x'], [10, 'x', 3, 'x', 'x', 'x', 8, 6, 'x', 10, 9, 7, 'x'], [1, 18, 2, 6, 'x', 'x', 1, 5, 'x', 'x', 6, 'x', 'x'], [4, 14, 12, 3, 2, 2, 15, 8, 19, 3, 18, 'x', 'x'], [5, 6, 2, 2, 13, 'x', 7, 3, 12, 'x', 16, 10, 5], ['x', 2, 13, 'x', 'x', 9, 5, 'x', 'x', 'x', 7, 10, 11], [17, 10, 3, 11, 4, 'x', 'x', 19, 'x', 5, 'x', 'x', 9], [13, 'x', 'x', 'x', 'x', 9, 13, 4, 7, 'x', 13, 10, 'x'], ['x', 'x', 'x', 9, 'x', 8, 8, 14, 'x', 'x', 19, 'x', 'x'], [6, 'x', 'x', 'x', 'x', 'x', 1, 11, 'x', 4, 13, 'x', 'x'], ['x', 'x', 'x', 11, 11, 'x', 9, 16, 12, 'x', 6, 'x', 5], [16, 19, 14, 'x', 5, 13, 'x', 'x', 'x', 'x', 'x', 13, 'x']]
    districts = {1: range(0, 4), 2: range(4, 6), 3: range(6, 13)}
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
