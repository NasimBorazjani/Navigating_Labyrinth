
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1),
                      (0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1),
                      (0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1),
                      (1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1),
                      (0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0),
                      (0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0),
                      (1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0),
                      (0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0),
                      (0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0),
                      (1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1),
                      (1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1),
                      (1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0),
                      (1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1))
    num_rows = 13
    num_cols = 13
    start = (8, 12)
    goal = (1, 1)
    # Define the possible moves Alex can make
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    # Define the number of diagonal jumps Alex must make
    num_diagonal_jumps = 4

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current_pos = heapq.heappop(queue)

        # If Alex reaches the goal position with exactly 4 diagonal jumps, return the actions taken
        if current_pos == goal and len([action for action in actions if action in [(1, 1), (-1, -1), (1, -1), (-1, 1)]]) == num_diagonal_jumps:
            return actions

        # Generate all possible actions from the current position, which includes moving to any of the 8 adjacent trampolines
        for move in moves:
            new_pos = (current_pos[0] + move[0], current_pos[1] + move[1])
            # Check if the new position is within the bounds of the grid and the trampoline is functional
            if 0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and initial_state[new_pos[0]][new_pos[1]] == 0:
                new_cost = g + 1
                # If the new position is unvisited or we found a new path with a lower cost to reach this position, add it to the queue of unvisited positions
                if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                    visited_costs[new_pos] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_pos, goal, num_diagonal_jumps), new_cost, actions + [move], new_pos))

    return None


def heuristic(current_pos, goal, num_diagonal_jumps):
    # A heuristic function that calculates the Manhattan distance between the current position and the goal position
    # The heuristic is admissible because the Manhattan distance is the minimum number of moves required to reach the goal position
    # The heuristic is consistent because the cost of moving to a neighboring position is always 1, which is exactly the decrease in the Manhattan distance
    return abs(current_pos[0] - goal[0]) + abs(current_pos[1] - goal[1])


print(a_star())
