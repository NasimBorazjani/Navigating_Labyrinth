
import heapq

def initialize():
    initial_state = (7, 1)
    goal_state = (2, 10)
    num_rows = 13
    num_cols = 13
    matrix = [['x', 9, 4, 8, 'x', 'x', 4, 'x', 8, 12, 'x', 'x', 14], [17, 'x', 3, 'x', 6, 'x', 12, 2, 'x', 'x', 'x', 5, 19], ['x', 8, 8, 'x', 5, 'x', 15, 14, 14, 3, 10, 12, 3], [4, 'x', 16, 'x', 'x', 11, 12, 'x', 'x', 6, 5, 18, 19], ['x', 4, 9, 17, 'x', 'x', 'x', 13, 4, 7, 'x', 2, 16], [3, 6, 'x', 'x', 'x', 10, 5, 'x', 18, 10, 9, 20, 4], ['x', 'x', 'x', 14, 18, 'x', 'x', 'x', 'x', 16, 'x', 'x', 4], [14, 12, 'x', 4, 12, 11, 19, 'x', 3, 2, 'x', 13, 'x'], [19, 6, 2, 18, 'x', 'x', 8, 7, 1, 12, 19, 'x', 'x'], ['x', 9, 16, 17, 5, 12, 19, 8, 'x', 3, 10, 'x', 'x'], ['x', 10, 3, 'x', 14, 16, 2, 16, 4, 10, 18, 15, 'x'], [15, 5, 5, 'x', 13, 'x', 3, 7, 'x', 4, 1, 17, 15], [5, 2, 6, 'x', 'x', 'x', 'x', 8, 16, 'x', 'x', 'x', 'x']]
    districts = {1: range(0, 3), 2: range(3, 8), 3: range(8, 13)}
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
