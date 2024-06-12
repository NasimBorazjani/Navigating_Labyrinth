
import heapq

def initialize():
    initial_state = (4, 14)
    goal_state = (7, 1)
    num_rows = 15
    num_cols = 15
    matrix = [['x', 'x', 'x', 'x', 2, 19, 'x', 'x', 15, 'x', 'x', 2, 17, 18, 18], ['x', 'x', 2, 18, 3, 17, 1, 'x', 'x', 'x', 6, 'x', 'x', 7, 9], ['x', 'x', 2, 10, 3, 'x', 6, 11, 5, 7, 8, 17, 'x', 12, 6], ['x', 14, 13, 9, 3, 'x', 18, 'x', 17, 16, 14, 8, 9, 'x', 13], ['x', 'x', 'x', 17, 'x', 16, 9, 3, 1, 'x', 5, 20, 2, 2, 6], [8, 'x', 8, 'x', 5, 19, 12, 19, 7, 1, 5, 4, 11, 13, 16], ['x', 6, 19, 17, 20, 'x', 'x', 14, 14, 'x', 'x', 3, 20, 13, 3], [12, 14, 7, 1, 15, 'x', 8, 8, 'x', 'x', 'x', 15, 'x', 'x', 'x'], ['x', 9, 'x', 'x', 4, 7, 7, 'x', 'x', 13, 7, 7, 'x', 6, 'x'], ['x', 'x', 'x', 11, 10, 'x', 'x', 'x', 5, 'x', 7, 14, 'x', 19, 'x'], ['x', 11, 18, 'x', 19, 'x', 1, 18, 1, 8, 'x', 'x', 'x', 12, 15], [19, 'x', 7, 'x', 9, 3, 'x', 7, 12, 13, 19, 13, 'x', 9, 'x'], ['x', 17, 9, 'x', 6, 'x', 6, 'x', 'x', 11, 'x', 19, 'x', 'x', 'x'], [4, 17, 5, 'x', 7, 5, 17, 12, 'x', 16, 8, 'x', 'x', 17, 'x'], [15, 2, 13, 'x', 14, 'x', 'x', 17, 'x', 'x', 1, 'x', 19, 1, 17]]
    districts = {1: range(0, 5), 2: range(5, 7), 3: range(7, 15)}
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
