
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[88, 52, 85], [98, 96, 83], [50, 80, '_']]
    goal_state = [[98, 96, 88], [85, 83, 80], [52, 50, '_']]

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = []
    heapq.heappush(queue, (0, 0, [], initial_state))

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state == goal_state:
            return actions

        empty_spot = np.argwhere(state == '_')[0]
        possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for move in possible_moves:
            new_state = np.copy(state)
            new_row, new_col = empty_spot + move

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state[empty_spot[0], empty_spot[1]] = new_state[new_row, new_col]
                new_state[new_row, new_col] = '_'
                new_state_str = str(new_state.tolist())

                new_cost = g + 1

                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state[empty_spot[0], empty_spot[1]]], new_state))

    return None


def heuristic(state, goal):
    # The heuristic is the sum of Manhattan distances of each tile from its goal position
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i, j] != '_':
                goal_pos = np.argwhere(goal == state[i, j])[0]
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return h


print(a_star())
