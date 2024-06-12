
import heapq

def initialize():
    initial_state = (2, 9)
    goal_state = (5, 2)
    num_rows = 10
    num_cols = 10
    matrix = [['x', 'x', 6, 'x', 'x', 'x', 'x', 15, 'x', 'x'], ['x', 17, 13, 13, 'x', 12, 'x', 3, 10, 2], ['x', 5, 13, 15, 4, 'x', 'x', 20, 6, 2], ['x', 9, 'x', 6, 2, 16, 18, 9, 13, 'x'], ['x', 'x', 15, 17, 'x', 10, 11, 'x', 'x', 'x'], [3, 'x', 3, 17, 8, 'x', 1, 'x', 16, 'x'], ['x', 'x', 13, 15, 'x', 'x', 11, 'x', 'x', 4], ['x', 'x', 12, 1, 'x', 'x', 'x', 14, 11, 'x'], ['x', 14, 'x', 'x', 19, 13, 4, 'x', 'x', 'x'], [1, 'x', 'x', 14, 11, 19, 2, 17, 2, 5]]
    districts = {1: range(0, 3), 2: range(3, 5), 3: range(5, 10)}
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
