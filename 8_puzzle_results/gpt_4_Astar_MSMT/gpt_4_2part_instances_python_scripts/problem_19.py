
import heapq

def initialize():
    initial_state = (('89', '69', '35'), ('16', '14', '64'), ('_', '23', '32'))
    num_rows = 3
    num_cols = 3
    goal_state = (('89', '69', '64'), ('35', '32', '23'), ('16', '14', '_'))
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, num_rows, num_cols, goal_state, visited_costs, queue)

def a_star():
    (initial_state, num_rows, num_cols, goal_state, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        if (state == goal_state):
            return actions
        empty_spot_coord = [(i, j) for (i, row) in enumerate(state) for (j, element) in enumerate(row) if (element == '_')][0]
        for (d_row, d_col) in [(0, (- 1)), (0, 1), (1, 0), ((- 1), 0)]:
            (new_row, new_col) = ((empty_spot_coord[0] + d_row), (empty_spot_coord[1] + d_col))
            if ((0 <= new_row < num_rows) and (0 <= new_col < num_cols)):
                new_state = [list(row[:]) for row in state]
                (new_state[empty_spot_coord[0]][empty_spot_coord[1]], new_state[new_row][new_col]) = (new_state[new_row][new_col], new_state[empty_spot_coord[0]][empty_spot_coord[1]])
                new_state = tuple((tuple(row) for row in new_state))
                new_cost = (g + 1)
                if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, ((g + heuristic(new_state, goal_state)), new_cost, (actions + [int(new_state[empty_spot_coord[0]][empty_spot_coord[1]])]), new_state))
    return None

def heuristic(state, goal):
    h = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if (state[i][j] != '_'):
                goal_coord = [(x, y) for (x, row) in enumerate(goal) for (y, element) in enumerate(row) if (element == state[i][j])][0]
                h += (abs((i - goal_coord[0])) + abs((j - goal_coord[1])))
    return h
print(a_star())
