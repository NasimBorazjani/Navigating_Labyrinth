
import heapq

def initialize():
    initial_state = (7, 7)
    goal_state = (1, 2)
    num_rows = 9
    num_cols = 9
    matrix = [[10, 14, 4, 16, 'x', 17, 5, 'x', 'x'], [5, 20, 16, 3, 1, 8, 'x', 16, 19], [1, 'x', 5, 13, 3, 15, 19, 15, 'x'], ['x', 16, 13, 20, 'x', 8, 'x', 'x', 'x'], ['x', 16, 'x', 17, 11, 1, 'x', 15, 'x'], [10, 'x', 14, 11, 5, 7, 12, 'x', 5], [7, 'x', 15, 'x', 15, 8, 3, 6, 7], ['x', 12, 14, 'x', 'x', 'x', 16, 3, 13], [19, 5, 10, 'x', 'x', 'x', 9, 7, 14]]
    districts = {1: range(0, 2), 2: range(2, 7), 3: range(7, 9)}
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
