
import heapq

def initialize():
    initial_state = (6, 0)
    goal_state = (4, 9)
    num_rows = 10
    num_cols = 10
    matrix = [[19, 'x', 7, 'x', 12, 'x', 15, 5, 19, 14], [17, 'x', 3, 5, 7, 'x', 'x', 'x', 17, 20], ['x', 11, 15, 8, 'x', 16, 4, 'x', 1, 1], ['x', 8, 19, 4, 3, 3, 3, 17, 8, 15], [13, 10, 17, 17, 6, 1, 'x', 8, 13, 20], [20, 'x', 'x', 'x', 'x', 4, 18, 4, 17, 'x'], [5, 'x', 'x', 10, 'x', 'x', 14, 2, 5, 'x'], [7, 'x', 4, 'x', 'x', 'x', 15, 'x', 'x', 'x'], [18, 'x', 18, 'x', 4, 'x', 'x', 'x', 17, 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 13, 'x', 'x']]
    districts = {1: range(0, 4), 2: range(4, 6), 3: range(6, 10)}
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
