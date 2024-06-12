
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[35, 92, '_'], [32, 44, 94], [97, 75, 58]]
    goal_state = [[94, 92, 97], [75, 58, 44], [35, 32, '_']]

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Find the position of the empty spot in the puzzle
        empty_spot = np.argwhere(np.array(state) == '_')[0]

        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col

            # Check if the new position is within the bounds of the puzzle
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                # Create a new state by swapping the empty spot with the neighboring tile
                new_state = [row[:] for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                new_state_str = str(new_state)
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue
                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state[new_row][new_col]], new_state))
    return None


def heuristic(state, goal_state):
    # An admissible and consistent heuristic for this problem is the sum of Manhattan distances of each tile from its goal position
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != '_':
                tile = state[i][j]
                goal_pos = np.argwhere(np.array(goal_state) == tile)[0]
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return h


print(a_star())
