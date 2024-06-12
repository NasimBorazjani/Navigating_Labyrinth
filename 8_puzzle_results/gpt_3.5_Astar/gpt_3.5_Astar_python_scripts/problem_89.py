
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[71, 36, 63, 32, 15], [20, 21, 65, '_', 54], [45, 96, 29, 31, 55]]
    goal_state = [[71, 65, 55, 54, 45], [36, 32, 31, 29, 21], [20, 15, '_', 96, 63]]

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
            if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
                # Create a new state by swapping the empty spot with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                new_state_str = str(new_state)
                # Calculate the cost of the new state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue
                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state[new_row][new_col]], new_state))

    return None


def heuristic(state, goal_state):
    # An admissible and consistent heuristic for this problem is the number of misplaced tiles in the current state compared to the goal state
    # This heuristic relaxes the constraint that only the empty spot can be moved, as it counts the number of misplaced tiles
    # It is admissible because it never overestimates the cost to reach the goal, as each misplaced tile must be moved at least once
    # It's consistent because moving a tile closer to its goal position reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
    # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
    h = sum([1 for i in range(len(state)) for j in range(len(state[0])) if state[i][j] != goal_state[i][j]])
    return h


print(a_star())
