
import heapq

def initialize():
    initial_state = ((9, 0), 3)
    goal_state = ((1, 5), 0)
    num_rows = 10
    num_cols = 10
    park_map = [[1, 1, 1, 0, 0, 0, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 0, 1, 0, 1, 1], [1, 0, 0, 0, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 1, 1, 1, 0, 1], [1, 1, 0, 0, 0, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0, 1, 1, 0], [1, 0, 0, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0, 1, 1]]
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [initial_state[0]], initial_state)]
    return (initial_state, goal_state, num_rows, num_cols, park_map, visited_costs, queue)

def a_star():
    (initial_state, goal_state, num_rows, num_cols, park_map, diagonal_jumps, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, (state, diagonal_jumps_left)) = heapq.heappop(queue)
        if ((state == goal_state) and (diagonal_jumps_left == 0)):
            return actions
        for (d_row, d_col) in [(0, (- 1)), (0, 1), (1, 0), ((- 1), 0), (1, 1), ((- 1), (- 1)), (1, (- 1)), ((- 1), 1)]:
            (new_row, new_col) = ((state[0] + d_row), (state[1] + d_col))
            if ((0 <= new_row < num_rows) and (0 <= new_col < num_cols) and (park_map[new_row][new_col] == 0)):
                new_state = (new_row, new_col)
                new_cost = (g + 1)
                if ((d_row != 0) and (d_col != 0)):
                    new_diagonal_jumps_left = (diagonal_jumps_left - 1)
                else:
                    new_diagonal_jumps_left = diagonal_jumps_left
                if (((new_state, new_diagonal_jumps_left) not in visited_costs) or (new_cost < visited_costs[(new_state, new_diagonal_jumps_left)])):
                    visited_costs[(new_state, new_diagonal_jumps_left)] = new_cost
                    heapq.heappush(queue, ((new_cost + heuristic(new_state, goal_state)), new_cost, (actions + [new_state]), (new_state, new_diagonal_jumps_left)))
    return None

def heuristic(state, goal):
    h = (abs((state[0] - goal[0])) + abs((state[1] - goal[1])))
    return h
print(a_star())
