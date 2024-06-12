
import heapq

def initialize():
    initial_state = (6, 1)
    goal_state = (2, 6)
    num_rows = 9
    num_cols = 9
    matrix = [['x', 7, 7, 12, 7, 'x', 13, 1, 18], [9, 18, 'x', 4, 19, 8, 'x', 15, 10], [9, 'x', 10, 5, 5, 9, 8, 'x', 'x'], [14, 4, 19, 9, 14, 'x', 'x', 7, 9], [9, 4, 11, 15, 7, 'x', 17, 3, 'x'], [11, 'x', 2, 18, 15, 15, 'x', 'x', 'x'], ['x', 5, 10, 'x', 'x', 13, 'x', 9, 'x'], [3, 'x', 2, 'x', 12, 'x', 'x', 'x', 4], ['x', 'x', 7, 'x', 19, 'x', 'x', 'x', 9]]
    districts = {1: range(0, 3), 2: range(3, 6), 3: range(6, 9)}
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
