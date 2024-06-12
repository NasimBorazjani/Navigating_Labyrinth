
import heapq
import math


def a_star():
    # Define the initial state of the puzzle
    initial_state = [['_', 83, 11, 57, 59], [89, 61, 99, 76, 63], [42, 35, 25, 48, 54]]
    goal_state = [[99, 89, 83, 76, 63], [61, 59, 57, 54, 48], [42, 35, 25, 11, '_']]

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
        empty_spot = [(i, j) for i in range(3) for j in range(5) if state[i][j] == '_'][0]

        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col
            # Check if the new position is valid
            if 0 <= new_row < 3 and 0 <= new_col < 5:
                # Generate the new state by swapping the empty spot with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                new_state = [tuple(row) for row in new_state]
                # The cost of the new state is the number on the tile that was swapped with the empty spot
                new_cost = g + new_state[new_row][new_col]

                if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                    visited_costs[str(new_state)] = new_cost
                    # Add the number on the tile that was swapped to the actions list
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state[new_row][new_col]], new_state))
    return None


def heuristic(state, goal_state):
    # An admissible and consistent heuristic for this problem is the sum of Manhattan distances of each tile from its goal position
    # This heuristic relaxes the constraint that only the empty spot can be moved, as it considers the distance of each tile from its goal position
    # It is admissible because it never overestimates the cost to reach the goal state, as each tile must be moved at least the Manhattan distance to reach its goal position
    # It is consistent because moving a tile closer to its goal position reduces the heuristic cost of the successor node by at most 1 (equal to the cost of reaching the successor node), which is equal to the cost of moving the tile
    h = 0
    for i in range(3):
        for j in range(5):
            if state[i][j] != '_':
                # Find the goal position of the tile
                goal_pos = [(k, l) for k in range(3) for l in range(5) if goal_state[k][l] == state[i][j]][0]
                # Calculate the Manhattan distance of the tile from its goal position
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return h


print(a_star())
