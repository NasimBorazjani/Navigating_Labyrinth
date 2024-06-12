
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (3, 10)
    goal_state = (6, 2)
    # Define the map of the city
    city_map = np.array([['x', 10, 2, 'x', 'x', 'x', 3, 'x', 4, 'x', 14],
                         ['x', 'x', 17, 16, 8, 'x', 'x', 'x', 'x', 1, 'x'],
                         [18, 18, 16, 16, 15, 'x', 'x', 17, 12, 16, 15],
                         ['x', 4, 'x', 'x', 18, 9, 'x', 15, 'x', 1, 9],
                         [3, 2, 7, 'x', 'x', 17, 2, 14, 'x', 4, 2],
                         [16, 17, 6, 4, 9, 2, 5, 7, 'x', 'x', 7],
                         ['x', 'x', 12, 'x', 'x', 16, 1, 11, 'x', 'x', 4],
                         ['x', 'x', 13, 'x', 'x', 19, 16, 9, 'x', 'x', 'x'],
                         ['x', 'x', 'x', 9, 7, 'x', 11, 5, 'x', 'x', 'x'],
                         ['x', 2, 'x', 'x', 'x', 4, 5, 'x', 10, 'x', 'x'],
                         ['x', 'x', 'x', 12, 16, 'x', 6, 16, 'x', 18, 7]])
    # Define the districts
    districts = [(0, 3), (4, 5), (6, 10)]
    # Define the directions
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
        for direction in directions:
            new_state = (state[0] + direction[0], state[1] + direction[1])
            # Check if the new state is valid, ie within the bounds of the city map and not a closed workshop
            if (0 <= new_state[0] < city_map.shape[0] and 0 <= new_state[1] < city_map.shape[1] and
                city_map[new_state[0]][new_state[1]] != 'x'):
                # The cost so far is the sum of the travel times, as our objective is to minimize the total travel time
                new_cost = g + int(city_map[new_state[0]][new_state[1]])
                # Check if the new state is in a new district
                new_visited_districts = visited_districts[:]
                for i, district in enumerate(districts):
                    if district[0] <= new_state[0] <= district[1]:
                        new_visited_districts[i] = True
                        break

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, new_visited_districts))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben can only move to neighboring workshops and presumes he can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor state is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
