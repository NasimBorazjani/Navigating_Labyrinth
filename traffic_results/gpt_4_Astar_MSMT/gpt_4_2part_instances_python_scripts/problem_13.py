
import heapq

def initialize():
    initial_state = (3, 7)
    goal_state = (5, 0)
    num_rows = 9
    num_cols = 9
    matrix = [['x', 'x', 'x', 'x', 9, 'x', 20, 3, 9], [17, 11, 17, 'x', 9, 2, 7, 'x', 15], ['x', 4, 2, 19, 12, 6, 'x', 4, 17], [15, 'x', 'x', 15, 11, 19, 'x', 9, 5], [3, 9, 19, 15, 2, 'x', 'x', 18, 'x'], [19, 5, 9, 11, 9, 'x', 'x', 3, 'x'], ['x', 'x', 2, 8, 8, 'x', 'x', 'x', 19], ['x', 'x', 14, 'x', 'x', 'x', 18, 'x', 18], ['x', 14, 18, 7, 8, 'x', 10, 15, 'x']]
    districts = {1: range(0, 4), 2: range(4, 5), 3: range(5, 9)}
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