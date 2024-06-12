
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (7, 0)
    goal_state = (3, 8)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([['x', 11, 5, 18, 'x', 14, 7, 'x', 15, 11, 14],
                         ['x', 'x', 'x', 'x', 13, 13, 11, 17, 8, 13, 'x'],
                         ['x', 8, 1, 5, 17, 'x', 4, 8, 20, 7, 4],
                         ['x', 10, 'x', 'x', 18, 1, 'x', 'x', 20, 'x', 'x'],
                         [18, 15, 'x', 6, 'x', 4, 3, 4, 3, 13, 'x'],
                         [5, 1, 'x', 4, 'x', 'x', 'x', 11, 'x', 14, 18],
                         [19, 19, 'x', 'x', 'x', 'x', 15, 'x', 10, 'x', 'x'],
                         [15, 5, 7, 'x', 14, 6, 'x', 'x', 'x', 13, 'x'],
                         [18, 7, 'x', 19, 'x', 12, 'x', 'x', 15, 'x', 'x'],
                         [10, 9, 'x', 1, 'x', 'x', 15, 'x', 11, 'x', 2],
                         ['x', 'x', 8, 'x', 19, 'x', 1, 3, 'x', 'x', 8]])
    num_rows, num_cols = city_map.shape
    # Define the districts of the city
    districts = [(0, 1), (2, 6), (7, 10)]
    # Define the directions in which Ben can move
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0


    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state, [False]*len(districts))]


    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited_districts = heapq.heappop(queue)


        # Check if the current state is the goal state
        if state == goal_state and all(visited_districts):
            return actions


        # Generate all possible actions from the current state, which includes moving in any of the 4 directions
        for d_row, d_col in directions:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the new state would be valid, ie the new coordinates are within the bounds of the city map and the workshop at the new coordinates is not closed
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                # Generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
                new_cost = g + int(city_map[new_row][new_col])
                # Check if the new state is in a new district
                new_visited_districts = visited_districts[:]
                for i, (start, end) in enumerate(districts):
                    if start <= new_row <= end:
                        new_visited_districts[i] = True
                        break


                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben can only move to neighboring workshops and presumes Ben can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
