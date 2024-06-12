
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
                      (1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1),
                      (1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1),
                      (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1),
                      (1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1),
                      (0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0),
                      (1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1),
                      (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1),
                      (1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1),
                      (1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1),
                      (1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1),
                      (1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1))
    num_rows = 12
    num_cols = 12
    start = (11, 9)
    goal = (0, 3)
    # Define the possible moves Alex can make
    moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current = heapq.heappop(queue)

        # If Alex reaches the goal position, return the actions taken
        if current == goal:
            return actions

        # Generate all possible actions from the current position, which includes moving to any of the eight adjacent trampolines
        for move in moves:
            new_row = current[0] + move[0]
            new_col = current[1] + move[1]
            # Check if the new position is within the bounds of the grid and is not a broken trampoline
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] == 0:
                new_pos = (new_row, new_col)
                # Alex must make exactly 4 diagonal jumps, so check if the move is diagonal
                if abs(new_row - current[0]) == 1 and abs(new_col - current[1]) == 1:
                    new_cost = g + 1
                else:
                    new_cost = g
                # If the new position is unvisited or we found a new path with a lower cost to reach this position, add it to the queue of unvisited positions
                if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                    visited_costs[new_pos] = new_cost
                    h = heuristic(new_pos, goal)
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_pos], new_pos))
    return None


def heuristic(current, goal):
    # An admissible and consistent heuristic is the Manhattan distance between the current position and the goal position
    # This heuristic is admissible because the shortest path between two points in a grid is the Manhattan distance, which never overestimates the cost to reach the goal
    # The heuristic is consistent because the cost of moving from one position to a neighboring position is always 1, which is exactly the decrease in the Manhattan distance, making the heuristic estimate for the goal state 0
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


print(a_star())
