
import heapq

def initialize():
    initial_state = (9, 1)
    goal_state = (7, 14)
    num_rows = 15
    num_cols = 15
    matrix = [[17, 8, 'x', 3, 'x', 13, 'x', 'x', 14, 11, 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 7, 'x', 'x', 13, 'x', 'x', 'x', 'x', 'x', 16, 'x', 13], ['x', 'x', 2, 'x', 'x', 12, 10, 'x', 'x', 'x', 2, 'x', 'x', 5, 17], [4, 3, 'x', 14, 'x', 'x', 16, 'x', 'x', 'x', 1, 'x', 'x', 'x', 'x'], [9, 'x', 18, 11, 19, 5, 'x', 'x', 'x', 'x', 'x', 'x', 3, 'x', 'x'], ['x', 14, 'x', 4, 14, 12, 1, 'x', 13, 7, 10, 8, 8, 6, 9], [7, 10, 'x', 18, 15, 8, 13, 14, 15, 'x', 'x', 'x', 13, 'x', 17], [17, 7, 19, 15, 20, 19, 'x', 15, 13, 'x', 9, 'x', 11, 'x', 1], ['x', 9, 6, 17, 14, 'x', 16, 'x', 19, 11, 'x', 14, 11, 'x', 'x'], ['x', 18, 8, 2, 14, 2, 4, 'x', 4, 4, 4, 'x', 'x', 8, 19], ['x', 'x', 5, 'x', 'x', 'x', 1, 5, 'x', 11, 'x', 'x', 1, 14, 'x'], ['x', 'x', 'x', 'x', 5, 'x', 10, 'x', 'x', 'x', 'x', 10, 18, 'x', 19], ['x', 'x', 2, 'x', 1, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 6, 16], ['x', 12, 1, 12, 'x', 'x', 15, 7, 18, 15, 13, 19, 'x', 2, 'x'], ['x', 13, 8, 19, 5, 1, 'x', 13, 'x', 'x', 'x', 17, 'x', 3, 'x']]
    districts = {1: range(0, 6), 2: range(6, 9), 3: range(9, 15)}
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
