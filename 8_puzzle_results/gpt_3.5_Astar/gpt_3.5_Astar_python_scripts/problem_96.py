
import heapq
import math
import numpy as np


def a_star():
    # Define the initial state of the puzzle as a 2d tuple
    initial_state = ((99, 98, 87, 84, 72, 64), (60, 59, 19, 57, '_', 53), (33, 22, 18, 48, 16, 37))
    goal_state = ((99, 98, 87, 84, 72, 64), (60, 59, 48, 57, 53, 37), (33, 22, 19, 18, 16, '_'))

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken
        if state == goal_state:
            return actions

        # Find the position of the empty spot in the current state
        empty_spot = [(i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell == '_'][0]

        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col

            # Check if the new position is within the bounds of the puzzle
            if 0 <= new_row < 3 and 0 <= new_col < 6:
                # Generate the new state by swapping the empty spot with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                new_state = tuple(tuple(row) for row in new_state)
                # The cost of the new state is the value of the tile swapped with the empty spot
                new_cost = g + new_state[new_row][new_col]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state[new_row][new_col]], new_state))
    return None


def heuristic(state, goal_state):
    # An admissible and consistent heuristic for this problem is the sum of Manhattan distances of each tile from its goal position
    # The heuristic relaxes the constraint that only the empty spot can be moved, assuming that any tile can be moved to the empty spot
    # It is admissible because the sum of Manhattan distances is always less than or equal to the actual cost to reach the goal state
    # It is consistent because moving a tile to the empty spot reduces the heuristic cost of the successor node by at most 1 (equal to the cost of reaching the successor node), which is equal to the cost of moving the tile
    h = 0
    for i in range(3):
        for j in range(6):
            if state[i][j] != '_':
                goal_pos = [(k, l) for k, row in enumerate(goal_state) for l, cell in enumerate(row) if cell == state[i][j]][0]
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return h


print(a_star())
