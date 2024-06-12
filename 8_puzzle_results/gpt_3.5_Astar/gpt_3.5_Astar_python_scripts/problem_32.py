
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[69, 56, 8, 67], [15, 47, 44, 30], [73, '_', 24, 63]]
    goal_state = [[69, 56, 47, 67], [44, 30, 24, 15], [8, '_', 73, 63]]

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = []
    heapq.heappush(queue, (0, 0, [], initial_state))

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state == goal_state:
            return actions

        empty_spot = np.argwhere(np.array(state) == '_')[0]
        empty_row, empty_col = empty_spot[0], empty_spot[1]

        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_row + d_row, empty_col + d_col

            if 0 <= new_row < 3 and 0 <= new_col < 4:
                new_state = [list(row) for row in state]
                new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
                new_state_str = str(new_state)

                new_cost = g + 1

                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state[new_row][new_col]], new_state))

    return None


def heuristic(state, goal_state):
    # The heuristic is the sum of the Manhattan distances of each tile from its goal position
    h = 0
    for i in range(3):
        for j in range(4):
            if state[i][j] != '_':
                value = state[i][j]
                goal_spot = np.argwhere(np.array(goal_state) == value)[0]
                goal_row, goal_col = goal_spot[0], goal_spot[1]
                h += abs(i - goal_row) + abs(j - goal_col)
    return h


print(a_star())
