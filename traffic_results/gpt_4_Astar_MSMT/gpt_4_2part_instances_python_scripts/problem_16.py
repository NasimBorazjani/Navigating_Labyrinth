
import heapq

def initialize():
    initial_state = (5, 1)
    goal_state = (3, 9)
    num_rows = 10
    num_cols = 10
    matrix = [['x', 'x', 'x', 16, 1, 13, 17, 7, 14, 'x'], ['x', 10, 'x', 12, 'x', 13, 'x', 8, 19, 4], [9, 13, 'x', 13, 'x', 'x', 15, 'x', 'x', 16], [3, 8, 'x', 16, 12, 'x', 'x', 'x', 'x', 13], [13, 'x', 1, 15, 18, 8, 'x', 10, 'x', 'x'], [8, 1, 2, 14, 'x', 8, 'x', 4, 'x', 11], [14, 13, 15, 'x', 16, 'x', 13, 2, 'x', 19], ['x', 4, 10, 'x', 'x', 16, 'x', 11, 'x', 'x'], ['x', 14, 'x', 'x', 'x', 'x', 'x', 18, 6, 18], ['x', 3, 2, 6, 7, 'x', 'x', 9, 8, 5]]
    districts = {1: range(0, 4), 2: range(4, 6), 3: range(6, 10)}
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
