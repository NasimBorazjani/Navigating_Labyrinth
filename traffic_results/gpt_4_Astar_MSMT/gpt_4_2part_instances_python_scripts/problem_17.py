
import heapq

def initialize():
    initial_state = (7, 9)
    goal_state = (3, 2)
    num_rows = 10
    num_cols = 10
    matrix = [[16, 2, 16, 'x', 4, 'x', 'x', 1, 16, 'x'], ['x', 'x', 19, 'x', 3, 'x', 5, 'x', 'x', 'x'], ['x', 'x', 'x', 3, 'x', 'x', 2, 'x', 10, 'x'], [11, 5, 20, 'x', 1, 3, 1, 'x', 9, 'x'], ['x', 'x', 8, 19, 'x', 16, 9, 'x', 16, 15], ['x', 3, 5, 10, 'x', 'x', 'x', 4, 1, 'x'], [9, 18, 10, 17, 5, 6, 'x', 'x', 'x', 5], ['x', 'x', 14, 5, 18, 'x', 'x', 1, 15, 1], [13, 'x', 13, 13, 14, 2, 19, 12, 'x', 1], [9, 6, 'x', 4, 12, 1, 13, 8, 2, 13]]
    districts = {1: range(0, 4), 2: range(4, 7), 3: range(7, 10)}
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
