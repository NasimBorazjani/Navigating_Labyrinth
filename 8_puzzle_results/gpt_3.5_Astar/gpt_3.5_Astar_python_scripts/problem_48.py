
import heapq
import math
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[79, 98, 87, 83], [56, 76, 65, 91], [25, '_', 36, 70]]
    goal_state = [[98, 91, 87, 83], [79, 76, 70, 65], [56, 36, 25, '_']]

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Find the position of the empty spot in the current state
        empty_spot = [(i, j) for i in range(3) for j in range(4) if state[i][j] == '_'][0]

        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col

            # Check if the new position is valid
            if 0 <= new_row < 3 and 0 <= new_col < 4:
                # Create a new state by swapping the empty spot with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]] = new_state[new_row][new_col]
                new_state[new_row][new_col] = '_'
                new_state_str = str(new_state)

                # Calculate the cost of the new state
                new_cost = g + 1

                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    # Add the number on the tile swapped with the empty spot to the actions list
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state[empty_spot[0]][empty_spot[1]]], new_state))

    return None


def heuristic(state, goal_state):
    # An admissible and consistent heuristic for this problem is the sum of Manhattan distances of each tile from its goal position
    # The heuristic relaxes the constraint that only the empty spot can be moved, as it considers the distance of each tile from its goal position
    # It is admissible because the sum of Manhattan distances is always less than or equal to the actual number of moves required to reach the goal state
    # It is consistent because moving a tile closer to its goal position reduces the heuristic cost of the successor node by at most 1 (equal to the cost of reaching the successor node)
    h = 0
    for i in range(3):
        for j in range(4):
            if state[i][j] != '_':
                # Find the goal position of the tile
                goal_pos = [(k, l) for k in range(3) for l in range(4) if goal_state[k][l] == state[i][j]][0]
                # Calculate the Manhattan distance of the tile from its goal position
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return h


print(a_star())
