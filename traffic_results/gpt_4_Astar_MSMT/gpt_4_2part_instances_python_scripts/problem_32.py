
import heapq

def initialize():
    initial_state = (5, 2)
    goal_state = (2, 10)
    num_rows = 11
    num_cols = 11
    matrix = [['x', 'x', 13, 'x', 'x', 7, 'x', 13, 3, 'x', 13], [10, 4, 'x', 4, 12, 2, 'x', 3, 4, 'x', 15], ['x', 3, 'x', 'x', 15, 9, 'x', 'x', 18, 17, 14], [5, 'x', 'x', 'x', 3, 'x', 11, 'x', 17, 9, 17], [8, 3, 13, 'x', 5, 7, 8, 17, 7, 'x', 'x'], ['x', 'x', 13, 2, 2, 11, 6, 8, 'x', 'x', 'x'], ['x', 1, 9, 6, 5, 13, 16, 1, 7, 5, 'x'], [4, 'x', 13, 'x', 10, 18, 3, 'x', 'x', 19, 19], ['x', 'x', 'x', 2, 5, 9, 13, 'x', 7, 1, 'x'], ['x', 'x', 7, 'x', 'x', 5, 19, 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 6, 'x', 19, 'x', 'x', 'x', 'x', 1]]
    districts = {1: range(0, 3), 2: range(3, 5), 3: range(5, 11)}
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
