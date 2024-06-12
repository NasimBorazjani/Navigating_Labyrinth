
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (6, 1)
    goal_state = (2, 6)
    # Define the map of the city
    city_map = np.array([['x', 7, 7, 12, 7, 'x', 13, 1, 18],
                         [9, 18, 'x', 4, 19, 8, 'x', 15, 10],
                         [9, 'x', 10, 5, 5, 9, 8, 'x', 'x'],
                         [14, 4, 19, 9, 14, 'x', 'x', 7, 9],
                         [9, 4, 11, 15, 7, 'x', 17, 3, 'x'],
                         [11, 'x', 2, 18, 15, 15, 'x', 'x', 'x'],
                         ['x', 5, 10, 'x', 'x', 13, 'x', 9, 'x'],
                         [3, 'x', 2, 'x', 12, 'x', 'x', 'x', 4],
                         ['x', 'x', 7, 'x', 19, 'x', 'x', 'x', 9]])
    # Define the districts
    districts = {1: range(0, 3), 2: range(3, 6), 3: range(6, 9)}
    # Define the directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [initial_state], initial_state, {district: False for district in districts})]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state, visited_districts = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state and all(visited_districts.values()):
            return path

        # Generate all possible actions from the current state, which includes moving in any of the 4 directions
        for direction in directions:
            new_state = (state[0] + direction[0], state[1] + direction[1])
            # Check if the new state is valid, ie within the bounds of the city map and not a closed workshop
            if (0 <= new_state[0] < city_map.shape[0] and 0 <= new_state[1] < city_map.shape[1] and
                    city_map[new_state] != 'x'):
                # The cost so far is the sum of the travel times
                new_cost = g + city_map[new_state]
                # Update the visited districts
                new_visited_districts = visited_districts.copy()
                for district, rows in districts.items():
                    if new_state[0] in rows:
                        new_visited_districts[district] = True

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_state], new_state, new_visited_districts))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben can only move to neighboring workshops and presumes he can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor workshop is the same or higher, and the heuristic estimate for the goal workshop is 0, as the distance of the goal workshop from itself would be 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
