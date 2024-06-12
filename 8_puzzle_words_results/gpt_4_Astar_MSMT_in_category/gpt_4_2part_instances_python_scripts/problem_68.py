
import heapq

def initialize():
    initial_state = (('e', 's', '_', 't'), ('l', 'o', 'e', 'm'), ('c', 'a', 'o', 'k'), ('p', 'p', 'g', 'e'), ('d', 'r', 'a', 'w'))
    goal_state = (('_', 'a', 't', ' '), ('l', 'e', 'e', 'p'), ('m', 'a', 'c', 'k'), ('p', 'o', 'g', 'o'), ('d', 'r', 'e', 'w'))
    num_rows = 5
    num_cols = 4
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, goal_state, num_rows, num_cols, visited_costs, queue)

def a_star():
    (initial_state, goal_state, num_rows, num_cols, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        if (state == goal_state):
            return actions
        (empty_row, empty_col) = [(i, j) for i in range(num_rows) for j in range(num_cols) if (state[i][j] == '_')][0]
        for (d_row, d_col) in [((- 1), 1), (1, 1), ((- 1), (- 1)), (1, (- 1))]:
            (swap_row, swap_col) = ((empty_row + d_row), (empty_col + d_col))
            if ((0 <= swap_row < num_rows) and (0 <= swap_col < num_cols)):
                new_state = [list(row[:]) for row in state]
                (new_state[empty_row][empty_col], new_state[swap_row][swap_col]) = (new_state[swap_row][swap_col], new_state[empty_row][empty_col])
                new_state = tuple((tuple(row) for row in new_state))
                new_cost = (g + 1)
                if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                    visited_costs[new_state] = new_cost
                    if ((d_row == (- 1)) and (d_col == 1)):
                        direction = 'up-right'
                    elif ((d_row == 1) and (d_col == 1)):
                        direction = 'down-right'
                    elif ((d_row == (- 1)) and (d_col == (- 1))):
                        direction = 'up-left'
                    elif ((d_row == 1) and (d_col == (- 1))):
                        direction = 'down-left'
                    heapq.heappush(queue, ((new_cost + heuristic(new_state, goal_state)), new_cost, (actions + [direction]), new_state))
    return None

def heuristic(state, goal):
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if (state[i][j] != '_'):
                (goal_row, goal_col) = [(x, y) for x in range(len(goal)) for y in range(len(goal[x])) if (goal[x][y] == state[i][j])][0]
                h += (abs((i - goal_row)) + abs((j - goal_col)))
    return h
print(a_star())
