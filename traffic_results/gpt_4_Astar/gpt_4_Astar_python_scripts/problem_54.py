
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 2d tuples
    initial_state = ((4, 11))
    goal_state = ((9, 2))

    # Encoding other variables given in the problem statement
    num_rows = 12
    num_cols = 12
    district_rows = [range(0, 4), range(4, 9), range(9, 12)]
    visited_districts = [False, False, False]

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state, visited_districts)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited_districts = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state and all(visited_districts):
            return actions

        # Generate all valid actions from the current state, which includes moving to any of the neighboring workshops
        # Generate the coordinates of the neighboring workshops
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the workshop to be moved to is a valid coordinate within the bounds of the city
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city[new_row][new_col] != 'x':
                # The move is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the travel time to the new workshop, as our objective is to minimize the travel time required to reach the goal state
                new_cost = g + city[new_row][new_col]
                # Update the visited districts
                new_visited_districts = visited_districts[:]
                for i, district in enumerate(district_rows):
                    if new_row in district:
                        new_visited_districts[i] = True

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, new_visited_districts))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current workshop from the goal workshop
    # The heuristic relaxes the constraint that a workshop can only be moved to if it is neighboring the current workshop and presumes we can move to the goal workshop directly from the current workshop
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if the workshop is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
    h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
    return h


city = np.array([[19, 14, 16, 4, 15, 16, 15, 'x', 9, 'x', 'x', 'x'],
                 ['x', 7, 12, 6, 'x', 12, 'x', 3, 'x', 14, 5, 9],
                 [1, 12, 'x', 'x', 12, 'x', 'x', 'x', 'x', 'x', 10, 1],
                 ['x', 1, 15, 14, 'x', 2, 13, 'x', 'x', 'x', 10, 9],
                 [7, 'x', 13, 'x', 14, 1, 14, 8, 'x', 'x', 8, 5],
                 [18, 'x', 8, 13, 12, 13, 'x', 12, 3, 'x', 14, 'x'],
                 ['x', 15, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 17, 10],
                 ['x', 5, 'x', 4, 'x', 'x', 'x', 3, 5, 6, 6, 11],
                 ['x', 15, 6, 'x', 4, 18, 'x', 'x', 14, 10, 2, 8],
                 [13, 10, 13, 7, 3, 6, 'x', 'x', 10, 17, 10, 15],
                 [4, 'x', 'x', 7, 19, 4, 13, 13, 12, 'x', 'x', 13],
                 [5, 'x', 'x', 9, 19, 18, 'x', 'x', 16, 'x', 2, 'x']])

print(a_star())
