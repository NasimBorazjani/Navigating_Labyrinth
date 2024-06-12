
import heapq

def initialize():
    initial_state = (5, 0)
    goal_state = (3, 8)
    num_rows = 10
    num_cols = 10
    matrix = [[15, 'x', 8, 'x', 6, 9, 'x', 'x', 'x', 'x'], [14, 'x', 8, 'x', 14, 'x', 5, 11, 'x', 9], ['x', 17, 8, 'x', 17, 15, 12, 'x', 'x', 13], ['x', 13, 'x', 'x', 2, 'x', 17, 17, 1, 'x'], [6, 'x', 1, 5, 17, 'x', 2, 18, 11, 7], [12, 8, 17, 10, 'x', 'x', 'x', 15, 'x', 16], [12, 12, 'x', 4, 'x', 13, 'x', 10, 'x', 16], ['x', 'x', 10, 'x', 6, 'x', 'x', 'x', 8, 5], ['x', 2, 11, 18, 15, 'x', 11, 'x', 'x', 12], ['x', 'x', 14, 'x', 'x', 7, 14, 15, 18, 9]]
    districts = {1: range(0, 4), 2: range(4, 5), 3: range(5, 10)}
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
