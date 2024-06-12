
import heapq

def initialize():
    initial_state = (3, 7)
    goal_state = (7, 0)
    num_rows = 11
    num_cols = 11
    matrix = [[10, 'x', 19, 11, 'x', 'x', 6, 12, 'x', 'x', 'x'], [2, 9, 10, 'x', 'x', 10, 17, 'x', 'x', 11, 5], ['x', 15, 8, 9, 'x', 7, 17, 20, 'x', 'x', 13], [1, 9, 15, 14, 9, 9, 13, 7, 12, 'x', 10], [9, 'x', 17, 'x', 'x', 7, 'x', 'x', 1, 'x', 14], [16, 18, 11, 'x', 14, 18, 9, 13, 'x', 'x', 'x'], [9, 3, 5, 8, 17, 15, 19, 'x', 3, 'x', 14], [2, 13, 'x', 'x', 17, 13, 14, 18, 9, 'x', 6], [3, 'x', 18, 6, 'x', 14, 'x', 'x', 'x', 8, 19], [2, 4, 'x', 'x', 'x', 'x', 3, 4, 'x', 19, 'x'], ['x', 'x', 'x', 'x', 11, 'x', 'x', 'x', 'x', 5, 5]]
    districts = {1: range(0, 3), 2: range(3, 7), 3: range(7, 11)}
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state, {1: False, 2: True, 3: False})]
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
