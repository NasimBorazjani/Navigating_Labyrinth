
import heapq

def initialize():
    initial_state = (3, 10)
    goal_state = (5, 1)
    num_rows = 11
    num_cols = 11
    matrix = [['x', 10, 'x', 8, 13, 8, 4, 3, 15, 'x', 17], [9, 'x', 6, 4, 17, 'x', 16, 3, 19, 'x', 'x'], [8, 3, 18, 'x', 'x', 3, 'x', 7, 12, 16, 17], [8, 'x', 'x', 13, 'x', 7, 'x', 8, 'x', 12, 9], [2, 9, 'x', 'x', 9, 4, 18, 'x', 'x', 11, 'x'], [14, 20, 'x', 'x', 'x', 'x', 10, 'x', 'x', 7, 'x'], ['x', 'x', 18, 16, 12, 10, 'x', 'x', 10, 'x', 'x'], ['x', 'x', 16, 'x', 'x', 10, 'x', 'x', 3, 18, 18], ['x', 'x', 'x', 'x', 'x', 'x', 13, 3, 'x', 'x', 'x'], [5, 13, 1, 'x', 'x', 8, 'x', 19, 'x', 'x', 'x'], ['x', 'x', 16, 'x', 'x', 7, 18, 4, 11, 'x', 16]]
    districts = {1: range(0, 2), 2: range(2, 5), 3: range(5, 11)}
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [initial_state], initial_state, {1: False, 2: True, 3: False})]
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
