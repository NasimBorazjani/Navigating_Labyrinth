
import heapq

def initialize():
    initial_state = (7, 5)
    goal_state = (1, 0)
    num_rows = 11
    num_cols = 11
    matrix = [[15, 'x', 12, 'x', 9, 19, 'x', 'x', 13, 'x', 16], [14, 6, 3, 18, 'x', 8, 18, 'x', 'x', 'x', 'x'], [16, 10, 9, 4, 9, 5, 15, 4, 'x', 'x', 2], [5, 9, 'x', 8, 1, 15, 7, 15, 'x', 'x', 'x'], [6, 'x', 3, 'x', 4, 6, 6, 19, 'x', 16, 13], [17, 'x', 11, 5, 18, 11, 18, 'x', 'x', 10, 19], [6, 3, 'x', 'x', 10, 18, 2, 'x', 'x', 'x', 'x'], ['x', 'x', 4, 2, 'x', 13, 7, 'x', 3, 19, 16], ['x', 1, 10, 'x', 15, 'x', 2, 'x', 1, 7, 10], ['x', 'x', 'x', 4, 7, 'x', 7, 'x', 'x', 6, 'x'], [16, 'x', 15, 3, 'x', 8, 'x', 'x', 13, 'x', 14]]
    districts = {1: range(0, 2), 2: range(2, 7), 3: range(7, 11)}
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
