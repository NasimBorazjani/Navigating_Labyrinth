
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[92, 75, 100, 61, 43, 87], [64, 34, 55, 90, 20, 86], [36, '_', 32, 5, 42, 83]]
    goal_state = [[100, 92, 87, 86, 83, 75], [64, 61, 55, 43, 42, 36], [34, 32, 20, 5, '_', 90]]

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
            if 0 <= new_row < 3 and 0 <= new_col < 6:
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
    # An admissible and consistent heuristic for this problem is the number of tiles that are not in their correct position
    # This heuristic relaxes the constraint that only the empty spot can be moved, as it considers the number of misplaced tiles
    # It is admissible because it never overestimates the cost to reach the goal state, as each misplaced tile must be moved at least once
    # It is consistent because moving a tile to its correct position reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
    h = sum([1 for i in range(3) for j in range(6) if state[i][j] != goal_state[i][j]])
    return h


print(a_star())
