
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[10, 81, 46], [87, 74, 72], [36, 45, '_']]
    goal_state = [[87, 81, 74], [46, 45, 36], [10, '_', 72]]
    num_rows = 3
    num_cols = 3

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Find the position of the empty spot in the current state
        empty_spot = np.argwhere(np.array(state) == '_')[0]

        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col

            # Check if the new position is within the bounds of the puzzle
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Create a new state by swapping the empty spot with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                new_state = [tuple(row) for row in new_state]

                # Calculate the cost of the new state
                new_cost = g + 1

                # If the new state has not been visited or the new cost is lower than the previous cost, add it to the queue
                if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                    visited_costs[str(new_state)] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state[empty_spot[0]][empty_spot[1]]], new_state))

    return None


def heuristic(state, goal_state):
    # An admissible and consistent heuristic for this problem is the sum of Manhattan distances of each tile from its goal position
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != '_':
                tile = state[i][j]
                goal_pos = np.argwhere(np.array(goal_state) == tile)[0]
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return h


print(a_star())
