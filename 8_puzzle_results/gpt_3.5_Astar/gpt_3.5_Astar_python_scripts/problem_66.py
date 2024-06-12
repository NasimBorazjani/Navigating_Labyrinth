
import heapq
import math


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[94, 91, 33, 29, 78], [97, 20, 14, 54, 25], [38, 22, 32, 17, '_']]
    goal_state = [[94, 91, 78, 54, 38], [97, 33, 32, 29, 22], [25, 20, 17, 14, '_']]

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

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
                # Create a new state by swapping the empty spot with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]] = new_state[new_row][new_col]
                new_state[new_row][new_col] = '_'
                new_state_str = str(new_state)
                # Calculate the cost of the new state
                new_cost = g + 1

                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    # Calculate the heuristic cost using the Manhattan distance
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state[empty_spot[0]][empty_spot[1]]], new_state))

    return None


def heuristic(state, goal_state):
    # Calculate the Manhattan distance heuristic between the current state and the goal state
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != '_':
                # Find the position of the current tile in the goal state
                goal_pos = [(r, c) for r in range(len(goal_state)) for c in range(len(goal_state[r])) if goal_state[r][c] == state[i][j]][0]
                # Calculate the Manhattan distance between the current tile and its goal position
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return h


print(a_star())
