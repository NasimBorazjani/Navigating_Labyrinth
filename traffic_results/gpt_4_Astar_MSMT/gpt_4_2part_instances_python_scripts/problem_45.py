
import heapq

def initialize():
    initial_state = (3, 10)
    goal_state = (6, 1)
    num_rows = 11
    num_cols = 11
    matrix = [['x', 'x', 17, 12, 12, 10, 9, 9, 18, 'x', 1], ['x', 8, 'x', 9, 'x', 'x', 18, 5, 1, 12, 14], [2, 19, 4, 'x', 'x', 'x', 'x', 'x', 'x', 15, 'x'], [17, 8, 6, 'x', 'x', 10, 15, 'x', 'x', 'x', 13], ['x', 'x', 'x', 9, 17, 'x', 'x', 'x', 'x', 12, 17], ['x', 20, 3, 1, 14, 8, 9, 20, 10, 8, 8], [18, 19, 4, 12, 3, 1, 'x', 'x', 20, 6, 3], [4, 6, 9, 'x', 8, 10, 'x', 'x', 6, 9, 6], [15, 'x', 'x', 'x', 'x', 'x', 16, 'x', 15, 4, 'x'], ['x', 'x', 'x', 4, 'x', 'x', 'x', 13, 'x', 'x', 'x'], ['x', 3, 'x', 'x', 'x', 'x', 1, 'x', 'x', 5, 13]]
    districts = {1: range(0, 4), 2: range(4, 6), 3: range(6, 11)}
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
