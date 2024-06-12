
import heapq
import math


def a_star():
    # Define the initial state of the trampoline park as a 2d tuple
    initial_state = ((1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0),
                     (1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0),
                     (0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0),
                     (1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1),
                     (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
                     (0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0),
                     (0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1),
                     (0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1),
                     (0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0),
                     (0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0),
                     (0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1),
                     (0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0))
    num_rows = 12
    num_cols = 12
    start = (1, 7)
    goal = (10, 0)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, position = heapq.heappop(queue)

        # If Alex reaches the destination, return the sequence of trampolines he jumped on
        if position == goal:
            return actions

        # Generate all possible actions from the current position, which includes moving to any of the 8 adjacent trampolines
        for d_row in [-1, 0, 1]:
            for d_col in [-1, 0, 1]:
                new_row = position[0] + d_row
                new_col = position[1] + d_col
                # Check if the new position is within the bounds of the grid and the trampoline is functional
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] == 0:
                    # Calculate the cost of moving to the new position
                    new_cost = g + math.sqrt(d_row**2 + d_col**2)
                    new_position = (new_row, new_col)
                    # If the new position is unvisited or we found a new path with a lower cost to reach this position, add it to the queue of unvisited positions
                    if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                        visited_costs[new_position] = new_cost
                        # Add the new position to the queue with updated cost and actions
                        heapq.heappush(queue, (new_cost + heuristic(new_position, goal), new_cost, actions + [new_position], new_position))

    return None


def heuristic(position, goal):
    # An admissible and consistent heuristic is the Euclidean distance between the current position and the goal position
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as the shortest path between two points is a straight line
    # The heuristic is consistent because the cost of moving from one position to a neighboring position is always 1, which is less than the Euclidean distance between the two positions
    h = math.sqrt((position[0] - goal[0])**2 + (position[1] - goal[1])**2)
    return h


print(a_star())
