
import heapq

def initialize():
    initial_state = (7, 0)
    goal_state = (3, 8)
    num_rows = 12
    num_cols = 12
    matrix = [[17, 9, 11, 5, 19, 4, 18, 'x', 5, 8, 'x', 'x'], [6, 13, 'x', 9, 2, 20, 11, 20, 7, 'x', 'x', 3], [4, 17, 'x', 18, 2, 10, 'x', 16, 'x', 18, 'x', 'x'], [12, 10, 9, 14, 'x', 'x', 12, 6, 1, 2, 'x', 'x'], [5, 'x', 'x', 3, 'x', 4, 9, 14, 8, 'x', 10, 12], [1, 'x', 6, 3, 18, 18, 17, 17, 10, 'x', 'x', 10], [13, 'x', 'x', 'x', 'x', 'x', 14, 'x', 1, 19, 'x', 7], [11, 'x', 'x', 5, 9, 'x', 18, 19, 13, 13, 'x', 10], ['x', 'x', 11, 'x', 17, 'x', 'x', 'x', 14, 17, 'x', 13], [19, 'x', 'x', 'x', 'x', 19, 12, 7, 3, 14, 'x', 9], ['x', 12, 7, 15, 1, 'x', 16, 11, 9, 17, 'x', 'x'], ['x', 'x', 'x', 10, 'x', 1, 7, 'x', 'x', 'x', 6, 12]]
    districts = {1: range(0, 4), 2: range(4, 7), 3: range(7, 12)}
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
