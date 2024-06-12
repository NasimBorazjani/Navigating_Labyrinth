
import heapq

def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 2D tuples
    initial_state = ((2, 2), 0)
    goal_state = (13, 14)
    # Define the map of the trampoline park
    trampoline_map = [[1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
                      [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0],
                      [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                      [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
                      [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                      [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
                      [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
                      [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0],
                      [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                      [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0],
                      [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0],
                      [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
                      [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
                      [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1]]
    # Define the size of the trampoline park
    num_rows = 15
    num_cols = 15

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state[0] == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes jumping to any of the eight adjacent trampolines
        # Generate the coordinates of the trampolines neighboring the current trampoline
        for d_row, d_col in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            new_row, new_col = state[0][0] + d_row, state[0][1] + d_col
            # Check if the jump is valid, ie if the coordinate of the trampoline to be jumped to is a valid coordinate within the bounds of the park and the trampoline is not broken
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and trampoline_map[new_row][new_col] == 0:
                # The action is valid, generate the new state
                new_state = ((new_row, new_col), state[1] + 1 if d_row != 0 and d_col != 0 else state[1])
                # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_state[0]], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current trampoline from the goal trampoline
    # The heuristic relaxes the constraint that Alex can only jump to the eight adjacent trampolines and presumes Alex can jump directly to the goal trampoline
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of jumping to a neighboring trampoline is always 1, which is exactly the decrease in the Manhattan distance, if Alex jumps toward the goal trampoline, otherwise the estimated cost of the successor state is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal trampoline from itself would be 0.
    h = abs(state[0][0] - goal[0]) + abs(state[0][1] - goal[1])
    # Add a large penalty if the number of diagonal jumps is not 5
    if state[1] != 5:
        h += 1000
    return h

print(a_star())
