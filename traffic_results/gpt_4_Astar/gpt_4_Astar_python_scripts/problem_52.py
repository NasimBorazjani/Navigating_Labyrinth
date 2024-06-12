
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 2d tuples
    initial_state = ((8, 1))
    goal_state = ((5, 11))

    # Encoding other variables given in the problem statement
    num_rows = 12
    num_cols = 12
    district_rows = [4, 8, 11]
    city_map = np.array([['x', 3, 11, 7, 'x', 'x', 1, 3, 'x', 'x', 'x', 3],
                         ['x', 10, 'x', 'x', 3, 9, 7, 8, 'x', 2, 'x', 17],
                         [6, 16, 'x', 18, 10, 5, 'x', 6, 'x', 'x', 7, 'x'],
                         ['x', 10, 'x', 8, 13, 10, 'x', 'x', 'x', 'x', 6, 13],
                         [6, 11, 3, 16, 8, 15, 'x', 'x', 'x', 13, 12, 20],
                         [15, 'x', 16, 'x', 17, 13, 'x', 'x', 8, 6, 19, 9],
                         [14, 10, 16, 14, 'x', 'x', 10, 11, 19, 15, 17, 'x'],
                         ['x', 'x', 'x', 'x', 18, 13, 14, 19, 12, 1, 3, 'x'],
                         [15, 1, 3, 17, 4, 18, 'x', 18, 2, 7, 12, 'x'],
                         [19, 'x', 13, 17, 2, 14, 8, 'x', 'x', 8, 16, 'x'],
                         ['x', 19, 'x', 15, 'x', 18, 'x', 13, 'x', 13, 'x', 'x'],
                         [7, 14, 2, 'x', 10, 3, 'x', 'x', 2, 5, 10, 'x']])

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state, [False, False, False])]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, districts_visited = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state and all(districts_visited):
            return actions

        # Generate all valid actions from the current state, which includes moving in any of the 4 directions
        # Generate the coordinates of the neighboring cells
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the cell to be moved to is a valid coordinate within the bounds of the city map and the cell is not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                # The move is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the sum of the travel times, as our objective is to minimize the travel time
                new_cost = g + city_map[new_row][new_col]
                # Check if the new state is in a new district
                new_districts_visited = districts_visited[:]
                if new_row <= district_rows[0]:
                    new_districts_visited[0] = True
                elif new_row <= district_rows[1]:
                    new_districts_visited[1] = True
                else:
                    new_districts_visited[2] = True

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, new_districts_visited))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current position from the goal position
    # The heuristic relaxes the constraint that Ben's car can only move to a neighboring cell and presumes Ben's car can move to the goal position directly
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the car is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of the car from its goal position would be 0 in the goal state.
    h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
    return h


print(a_star())
