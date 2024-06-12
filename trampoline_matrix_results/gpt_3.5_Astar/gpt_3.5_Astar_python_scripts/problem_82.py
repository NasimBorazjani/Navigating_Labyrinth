
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1),
                      (1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1),
                      (0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0),
                      (0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0),
                      (1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1),
                      (1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0),
                      (0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0),
                      (1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1),
                      (0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1),
                      (1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
                      (1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1),
                      (0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1),
                      (1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1),
                      (1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0))
    num_rows = 14
    num_cols = 14
    start = (2, 13)
    goal = (8, 0)
    # Define the possible moves Alex can make
    moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    # Initialize a priority queue to store the states to be visited
    queue = []
    # Record the actions taken to reach each state
    actions = []
    # Record the cost to reach each state
    costs = {}
    # Add the initial state to the queue
    heapq.heappush(queue, (0, 0, [start], start))

    while queue:
        _, g, actions, current = heapq.heappop(queue)

        # If Alex reaches the goal state, return the actions taken
        if current == goal and len(actions) == 5:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the eight adjacent trampolines
        for move in moves:
            new_pos = (current[0] + move[0], current[1] + move[1])
            # Check if the new position is within the bounds of the grid and the trampoline is functional
            if 0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and initial_state[new_pos[0]][new_pos[1]] == 0:
                new_actions = actions + [new_pos]
                new_cost = g + 1
                # Add the new state to the queue
                heapq.heappush(queue, (new_cost + heuristic(new_pos, goal), new_cost, new_actions, new_pos))

    return None


def heuristic(current, goal):
    # The heuristic function is the Manhattan distance between the current position and the goal position
    # This heuristic is admissible as it never overestimates the cost to reach the goal
    # It is consistent because the cost of moving from one position to an adjacent position is always 1, which is exactly the decrease in the heuristic value
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


print(a_star())
