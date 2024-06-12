
import heapq
import math


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[26, 39, 50, 35], ['_', 67, 2, 71], [48, 41, 37, 56]]
    goal_state = [[71, 67, 56, 50], [48, 41, 39, 39], [37, 35, 26, '_']]

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_state))

    while queue:
        _, g, actions, state = heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Find the position of the empty spot in the current state
        empty_spot = None
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == '_':
                    empty_spot = (i, j)
                    break
            if empty_spot:
                break

        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col
            # Check if the new position is within the bounds of the puzzle
            if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
                # Generate the new state by swapping the empty spot with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]] = new_state[new_row][new_col]
                new_state[new_row][new_col] = '_'
                new_state_str = str(new_state)
                # The cost of the new state is the number on the tile that was swapped with the empty spot
                new_cost = g + new_state[empty_spot[0]][empty_spot[1]]

                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    # Calculate the heuristic cost from the current state to the goal state
                    h = heuristic(new_state, goal_state)
                    heappush(queue, (g + h, new_cost, actions + [new_state[empty_spot[0]][empty_spot[1]]], new_state))

    return None


def heuristic(state, goal_state):
    # An admissible and consistent heuristic for this problem is the sum of Manhattan distances of each tile from its goal position
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != '_':
                # Find the goal position of the tile
                goal_pos = [(k, l) for k in range(len(goal_state)) for l in range(len(goal_state[k])) if goal_state[k][l] == state[i][j]][0]
                # Calculate the Manhattan distance
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return h


print(a_star())
