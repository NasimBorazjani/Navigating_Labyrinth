
import heapq

def initialize():
    initial_state = (2, 13)
    goal_state = (5, 1)
    num_rows = 14
    num_cols = 14
    matrix = [['x', 'x', 14, 'x', 3, 'x', 18, 'x', 4, 4, 'x', 'x', 16, 'x'], ['x', 'x', 1, 15, 'x', 18, 'x', 18, 'x', 'x', 'x', 'x', 14, 'x'], ['x', 'x', 7, 14, 'x', 'x', 16, 'x', 'x', 'x', 'x', 5, 19, 15], ['x', 13, 18, 'x', 17, 'x', 6, 8, 'x', 8, 'x', 'x', 13, 'x'], [12, 'x', 15, 'x', 'x', 'x', 'x', 18, 'x', 'x', 'x', 8, 6, 7], [5, 11, 14, 14, 11, 5, 13, 7, 'x', 'x', 10, 12, 17, 17], [14, 'x', 3, 15, 3, 'x', 'x', 17, 12, 7, 19, 15, 4, 5], ['x', 2, 14, 'x', 8, 'x', 9, 19, 16, 14, 17, 12, 'x', 13], ['x', 'x', 2, 15, 'x', 'x', 'x', 2, 14, 17, 3, 4, 'x', 12], [2, 'x', 11, 'x', 'x', 14, 'x', 'x', 16, 'x', 11, 13, 'x', 'x'], [17, 'x', 'x', 2, 9, 14, 8, 'x', 11, 5, 'x', 10, 5, 'x'], [4, 'x', 8, 8, 11, 'x', 16, 'x', 'x', 'x', 15, 'x', 2, 16], ['x', 16, 'x', 'x', 9, 'x', 'x', 'x', 'x', 19, 6, 9, 'x', 'x'], ['x', 14, 9, 'x', 6, 1, 7, 'x', 10, 4, 'x', 'x', 'x', 'x']]
    districts = {1: range(0, 3), 2: range(3, 6), 3: range(6, 14)}
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
