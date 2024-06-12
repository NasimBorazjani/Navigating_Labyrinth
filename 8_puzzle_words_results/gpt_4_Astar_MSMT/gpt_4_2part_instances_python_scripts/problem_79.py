
import heapq

def initialize():
    initial_state = (('r', 's', 'c', 'v', 'a'), ('b', 'b', 'y', 'r', 'e'), ('u', 'i', '_', 'n', 'i'), ('p', 'n', 'g', 'i', 'l'), ('l', 'i', 'y', 'n', 'e'))
    num_rows = 5
    num_cols = 5
    goal_state = (('_', 's', 'i', 'v', 'a'), ('b', 'r', 'y', 'c', 'e'), ('b', 'i', 'r', 'n', 'y'), ('p', 'u', 'g', 'i', 'l'), ('l', 'i', 'n', 'n', 'e'))
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
        for (d_row, d_col) in [((- 1), 1), (1, 1), ((- 1), (- 1)), (1, (- 1))]:
            blank_coord = [(i, j) for (i, row) in enumerate(state) for (j, element) in enumerate(row) if (element == '_')][0]
            (new_row, new_col) = ((blank_coord[0] + d_row), (blank_coord[1] + d_col))
            if ((0 <= new_row < num_rows) and (0 <= new_col < num_cols)):
                new_state = [list(row[:]) for row in state]
                (new_state[blank_coord[0]][blank_coord[1]], new_state[new_row][new_col]) = (new_state[new_row][new_col], new_state[blank_coord[0]][blank_coord[1]])
                new_state = tuple((tuple(row) for row in new_state))
                new_cost = (g + 1)
                if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                    visited_costs[new_state] = new_cost
                    if ((d_row == (- 1)) and (d_col == 1)):
                        action = 'up-right'
                    elif ((d_row == 1) and (d_col == 1)):
                        action = 'down-right'
                    elif ((d_row == (- 1)) and (d_col == (- 1))):
                        action = 'up-left'
                    elif ((d_row == 1) and (d_col == (- 1))):
                        action = 'down-left'
                    heapq.heappush(queue, ((g + heuristic(new_state, goal_state)), new_cost, (actions + [action]), new_state))
    return None

def heuristic(state, goal):
    h = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if (state[i][j] != goal[i][j]):
                h += 1
    return h
print(a_star())
