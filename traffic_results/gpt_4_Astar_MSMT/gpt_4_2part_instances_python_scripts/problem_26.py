
import heapq

def initialize():
    initial_state = (5, 9)
    goal_state = (3, 1)
    num_rows = 10
    num_cols = 10
    matrix = [[7, 'x', 19, 11, 6, 'x', 4, 15, 9, 3], ['x', 'x', 13, 'x', 8, 17, 'x', 'x', 12, 16], ['x', 'x', 2, 'x', 15, 8, 'x', 13, 4, 'x'], [13, 11, 3, 3, 3, 'x', 'x', 'x', 'x', 'x'], [1, 16, 14, 6, 14, 17, 4, 9, 1, 'x'], ['x', 4, 9, 'x', 17, 17, 'x', 13, 2, 9], ['x', 'x', 'x', 'x', 5, 14, 17, 12, 7, 14], ['x', 15, 1, 6, 'x', 'x', 5, 'x', 'x', 1], ['x', 'x', 19, 'x', 'x', 'x', 'x', 'x', 13, 8], ['x', 6, 9, 12, 8, 8, 'x', 18, 'x', 'x']]
    districts = {1: range(0, 4), 2: range(4, 5), 3: range(5, 10)}
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
