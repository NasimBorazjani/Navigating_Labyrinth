
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[88, 59, 84, 71, 80], [72, 79, 74, 96, 51], ['_', 28, 25, 24, 19]]
    goal_state = [[88, 79, 74, 71, 80], [72, 59, 51, 96, 84], [25, 24, 19, 28, '_']]

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state == goal_state:
            return actions

        empty_spot = np.argwhere(np.array(state) == '_')[0]

        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col

            if 0 <= new_row < 3 and 0 <= new_col < 5:
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]] = new_state[new_row][new_col]
                new_state[new_row][new_col] = '_'
                new_state_str = str(new_state)

                new_cost = g + 1

                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state[empty_spot[0]][empty_spot[1]]], new_state))

    return None


def heuristic(state, goal_state):
    # The heuristic is the sum of the Manhattan distances of each tile from its goal position
    h = 0
    for i in range(3):
        for j in range(5):
            if state[i][j] != '_':
                goal_pos = np.argwhere(np.array(goal_state) == state[i][j])[0]
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return h


print(a_star())
