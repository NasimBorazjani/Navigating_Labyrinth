
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (3, 1)
    goal_state = (5, 10)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([[15, 8, 18, 3, 19, 'x', 17, 'x', 'x', 'x', 'x'],
                         [19, 16, 'x', 18, 20, 2, 5, 7, 11, 12, 3],
                         [18, 'x', 18, 1, 2, 'x', 'x', 'x', 12, 16, 4],
                         [9, 20, 4, 19, 5, 15, 'x', 'x', 'x', 6, 4],
                         ['x', 18, 8, 1, 'x', 7, 1, 7, 10, 1, 4],
                         ['x', 18, 'x', 18, 19, 9, 18, 5, 15, 1, 7],
                         [3, 'x', 12, 14, 'x', 'x', 'x', 'x', 1, 'x', 'x'],
                         ['x', 12, 6, 'x', 6, 'x', 1, 'x', 1, 7, 'x'],
                         ['x', 5, 10, 14, 2, 'x', 'x', 7, 11, 3, 'x'],
                         [6, 9, 13, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 3],
                         [19, 12, 'x', 15, 'x', 14, 'x', 9, 'x', 'x', 19]])
    num_rows = city_map.shape[0]
    num_cols = city_map.shape[1]
    # Define the districts of the city
    districts = [range(0, 3), range(3, 5), range(5, 11)]
    # Define the set of workshops visited in each district
    visited_districts = [set() for _ in range(len(districts))]

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the path to get to each state in a list; the path to reach the initial state is just the initial state itself
    queue = [(0, 0, [initial_state], initial_state, visited_districts)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state, visited_districts = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state and all(visited_districts):
            return path

        # Generate all valid actions from the current state, which includes moving to any of the 4 neighboring workshops
        # Generate the coordinates of the neighboring workshops
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            neighbor_row, neighbor_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the neighboring workshop is a valid coordinate within the bounds of the city map and the workshop is not closed
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols and city_map[neighbor_row, neighbor_col] != 'x':
                # The move is valid, generate the new state
                new_state = (neighbor_row, neighbor_col)
                # The cost so far is the sum of the travel times from the initial state to the current state, as our objective is to minimize the total travel time
                new_cost = g + int(city_map[state[0], state[1]])
                # Update the set of visited workshops in each district
                new_visited_districts = visited_districts[:]
                for i, district in enumerate(districts):
                    if neighbor_row in district:
                        new_visited_districts[i].add(new_state)

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, path + [new_state], new_state, new_visited_districts))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
