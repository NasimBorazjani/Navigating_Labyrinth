
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1),
                      (1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1),
                      (0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1),
                      (1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0),
                      (1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0),
                      (1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1),
                      (1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1),
                      (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
                      (0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1),
                      (1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1),
                      (1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1))
    num_rows = 11
    num_cols = 11
    start = (1, 9)
    goal = (8, 0)
    # Define the possible moves Alex can make, including diagonal jumps
    moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]
    # Define the number of diagonal jumps Alex must make
    num_diagonal_jumps = 3

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current_pos = heapq.heappop(queue)

        # If Alex reaches the goal position, return the actions taken
        if current_pos == goal:
            return actions

        # Generate all possible actions from the current position, which includes moving to any of the eight adjacent trampolines
        for move in moves:
            new_pos = (current_pos[0] + move[0], current_pos[1] + move[1])
            # Check if the new position is within the bounds of the grid
            if 0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols:
                # Check if the new position is not a broken trampoline
                if initial_state[new_pos[0]][new_pos[1]] == 0:
                    # Calculate the number of diagonal jumps made so far
                    num_diagonal_jumps_made = sum([1 for action in actions if abs(action[0] - current_pos[0]) == 1 and abs(action[1] - current_pos[1]) == 1])
                    # Check if the number of diagonal jumps made does not exceed the limit
                    if num_diagonal_jumps_made < num_diagonal_jumps:
                        new_cost = g + 1
                        if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                            visited_costs[new_pos] = new_cost
                            # Add the action to the queue with the updated cost
                            heapq.heappush(queue, (new_cost + heuristic(new_pos, goal), new_cost, actions + [new_pos], new_pos))

    return None


def heuristic(current_pos, goal):
    # The heuristic function is the Manhattan distance between the current position and the goal position
    # This heuristic is admissible as it never overestimates the cost to reach the goal
    # It is consistent because the cost of moving from one position to an adjacent position is always 1, which is exactly the decrease in the heuristic estimate
    return abs(current_pos[0] - goal[0]) + abs(current_pos[1] - goal[1])


print(a_star())
