
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0),
                     (0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0),
                     (1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0),
                     (1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0),
                     (0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0),
                     (0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0),
                     (1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0),
                     (1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0),
                     (1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1),
                     (1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1),
                     (1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0),
                     (0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1),
                     (0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0),
                     (1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1))
    num_rows = 14
    num_cols = 14
    start = (0, 13)
    goal = (8, 1)
    # Define the possible moves Alex can make
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)
    # Define the number of diagonal jumps Alex must make
    num_diagonal_jumps = 4

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current = heapq.heappop(queue)

        # If Alex reaches the goal position, return the actions taken
        if current == goal:
            return actions

        # Generate all possible actions from the current position, which includes moving to any of the 8 adjacent trampolines
        for move in moves:
            new_pos = (current[0] + move[0], current[1] + move[1])
            # Check if the new position is within the bounds of the grid and the trampoline is functional
            if 0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and initial_state[new_pos[0]][new_pos[1]] == 0:
                # Calculate the new cost and heuristic estimate
                new_cost = g + 1
                h = heuristic(new_pos, goal)
                # If the new position is unvisited or a lower cost path is found, add it to the queue
                if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                    visited_costs[new_pos] = new_cost
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_pos], new_pos))

    return None


def heuristic(current, goal):
    # The heuristic is the Manhattan distance between the current position and the goal position
    # This heuristic is admissible as it never overestimates the cost to reach the goal
    # It is consistent because the cost of moving from one position to an adjacent position is always 1, which is exactly the decrease in the Manhattan distance
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


print(a_star())
