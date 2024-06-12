
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 2d tuples
    initial_state = ((1, 11),)
    goal_state = ((7, 2),)
    # Define the map of the city
    city_map = np.array([[18, 15, 'x', 'x', 1, 'x', 'x', 5, 8, 18, 18, 2, 'x', 11, 8],
                         ['x', 17, 'x', 'x', 2, 'x', 16, 9, 7, 13, 16, 17, 'x', 'x', 'x'],
                         [10, 'x', 1, 14, 1, 10, 15, 4, 'x', 'x', 8, 11, 10, 'x', 'x'],
                         [19, 'x', 'x', 9, 8, 18, 5, 2, 12, 'x', 13, 'x', 'x', 15, 11],
                         [1, 'x', 14, 6, 6, 6, 'x', 'x', 'x', 13, 13, 'x', 'x', 'x', 'x'],
                         [2, 3, 8, 5, 7, 'x', 'x', 'x', 19, 'x', 16, 'x', 'x', 'x', 'x'],
                         ['x', 'x', 17, 18, 'x', 19, 'x', 'x', 'x', 7, 8, 17, 'x', 'x', 'x'],
                         [4, 'x', 4, 14, 17, 6, 'x', 2, 'x', 'x', 15, 6, 'x', 18, 10],
                         [7, 'x', 3, 11, 10, 'x', 'x', 12, 'x', 'x', 8, 'x', 'x', 10, 'x'],
                         [4, 16, 2, 11, 'x', 'x', 14, 'x', 13, 'x', 'x', 'x', 'x', 'x', 'x'],
                         [14, 20, 7, 14, 'x', 'x', 'x', 'x', 'x', 'x', 5, 'x', 10, 16, 'x'],
                         [1, 14, 'x', 'x', 'x', 4, 14, 19, 'x', 18, 'x', 'x', 17, 15, 14],
                         ['x', 'x', 15, 'x', 4, 5, 19, 18, 'x', 19, 11, 3, 12, 'x', 10],
                         [1, 'x', 1, 'x', 'x', 13, 'x', 16, 4, 'x', 'x', 8, 'x', 9, 'x'],
                         ['x', 'x', 12, 11, 7, 'x', 8, 14, 3, 'x', 11, 'x', 14, 13, 'x']])
    num_rows = len(city_map)
    num_cols = len(city_map[0])
    # Define the districts
    districts = [range(0, 2), range(2, 10), range(10, 15)]

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

        # Check if the current state is the goal state
        # The goal state is where the last workshop in the state is the destination and the state includes at least 1 workshop from each district
        if state[-1] == goal_state and all(any(workshop[0] in district for workshop in state) for district in districts):
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops from the current workshop
        # Generate the coordinates of the workshops neighboring the current workshop
        current_workshop = state[-1]
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_workshop = (current_workshop[0] + d_row, current_workshop[1] + d_col)
            # Check if the move is valid, ie if the coordinate of the new workshop is a valid coordinate within the bounds of the city and the workshop is not closed
            if 0 <= new_workshop[0] < num_rows and 0 <= new_workshop[1] < num_cols and city_map[new_workshop] != 'x':
                # The move is valid, generate the new state
                new_state = state + (new_workshop,)
                # The cost so far is the sum of the travel times from the workshops visited, as our objective is to minimize the total travel time
                new_cost = g + int(city_map[new_workshop])

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_workshop, goal_state), new_cost, actions + [new_workshop], new_state))
    return None


def heuristic(workshop, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current workshop from the goal workshop
    # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
    return abs(workshop[0] - goal[0]) + abs(workshop[1] - goal[1])


print(a_star())
