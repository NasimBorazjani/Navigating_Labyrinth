
import heapq

def initialize():
    initial_state = (5, 10)
    goal_state = (3, 0)
    num_rows = 11
    num_cols = 11
    matrix = [[19, 7, 11, 'x', 3, 18, 8, 'x', 'x', 'x', 'x'], [12, 18, 6, 1, 13, 12, 14, 11, 13, 5, 19], [11, 10, 10, 18, 15, 'x', 12, 'x', 4, 17, 10], [4, 3, 3, 7, 'x', 19, 'x', 'x', 'x', 12, 9], ['x', 'x', 6, 19, 'x', 4, 14, 'x', 9, 4, 15], [4, 7, 6, 5, 8, 'x', 15, 3, 'x', 16, 3], [13, 'x', 'x', 1, 9, 1, 9, 'x', 'x', 'x', 'x'], [2, 13, 5, 9, 5, 'x', 6, 'x', 18, 'x', 3], [19, 'x', 2, 9, 4, 13, 'x', 'x', 'x', 16, 6], ['x', 'x', 'x', 12, 'x', 7, 9, 3, 9, 8, 1], ['x', 10, 'x', 12, 3, 6, 'x', 4, 12, 4, 'x']]
    districts = {1: range(0, 4), 2: range(4, 5), 3: range(5, 11)}
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state, {1: False, 2: False, 3: True})]
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
