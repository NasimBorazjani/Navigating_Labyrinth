
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (5, 0)
    goal_state = (3, 8)
    # Define the map of the city
    city_map = np.array([[15, 'x', 8, 'x', 6, 9, 'x', 'x', 'x', 'x'],
                         [14, 'x', 8, 'x', 14, 'x', 5, 11, 'x', 9],
                         ['x', 17, 8, 'x', 17, 15, 12, 'x', 'x', 13],
                         ['x', 13, 'x', 'x', 2, 'x', 17, 17, 1, 'x'],
                         [6, 'x', 1, 5, 17, 'x', 2, 18, 11, 7],
                         [12, 8, 17, 10, 'x', 'x', 'x', 15, 'x', 16],
                         [12, 12, 'x', 4, 'x', 13, 'x', 10, 'x', 16],
                         ['x', 'x', 10, 'x', 6, 'x', 'x', 'x', 8, 5],
                         ['x', 2, 11, 18, 15, 'x', 11, 'x', 'x', 12],
                         ['x', 'x', 14, 'x', 'x', 7, 14, 15, 18, 9]])
    # Define the districts
    districts = [set(range(0, 4)), set(range(4, 5)), set(range(5, 10))]

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [initial_state], initial_state, set([district for district in districts if initial_state[0] in district]))]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited_districts = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state and len(visited_districts) == len(districts):
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the workshop to move to is a valid coordinate within the bounds of the city map and the workshop is not closed
            if 0 <= new_row < city_map.shape[0] and 0 <= new_col < city_map.shape[1] and city_map[new_row][new_col] != 'x':
                # The move is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the sum of the travel times, as our objective is to minimize the travel time
                new_cost = g + city_map[new_row][new_col]
                # Update the visited districts
                new_visited_districts = visited_districts.copy()
                for district in districts:
                    if new_row in district:
                        new_visited_districts.add(district)

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, new_visited_districts))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current position from the goal position
    # The heuristic relaxes the constraint that the car can only move to a neighboring workshop and presumes we can move the car to the goal position directly
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving the car to a neighboring coordinate is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if the car is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the car from its goal position would be 0 in the goal state.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
