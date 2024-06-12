
import heapq
import math


def a_star():
    # Define the initial state of the grid and the goal state
    initial_state = ((1, 9), 3)
    goal_state = (8, 3)
    grid = [[1, 0, 0, 1, 0, 1, 1, 0, 1, 1],
            [0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 0, 0, 1, 0]]
  
    # Encoding other variables given in the problem statement
    num_rows = 10
    num_cols = 10
    num_diagonal_jumps = 3


    visited_costs = {}
    visited_costs[initial_state] = 0


    queue = []
    # No actions taken in the initial state
    heapq.heappush(queue, (0, 0, [], initial_state))


    while queue:
        _, g, actions, state = heapq.heappop(queue)


        # If Alex reaches the goal state, return the actions taken
        if state[0] == goal_state:
            return actions


        # Generate all possible actions from the current state, which includes jumping to any of the eight adjacent trampolines
        for d_row in [-1, 0, 1]:
            for d_col in [-1, 0, 1]:
                # Check if the new state would be valid, ie the trampoline must not be broken and the jump must be diagonal
                new_row = state[0][0] + d_row
                new_col = state[0][1] + d_col
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0 and (d_row != 0 and d_col != 0):
                    # Generate the new state
                    new_state = ((new_row, new_col), state[1] - 1)
                    # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the destination
                    new_cost = g + 1
                  
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Calculate the heuristic based on the Euclidean distance to the goal state
                        h = math.sqrt((new_row - goal_state[0])**2 + (new_col - goal_state[1])**2)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
    return None


print(a_star())
