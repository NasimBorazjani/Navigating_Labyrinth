
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (3, 9)
    goal_state = (7, 1)
    # Define the map of the city
    city_map = np.array([[9, 4, 16, 7, 'x', 2, 'x', 'x', 14, 'x', 'x', 'x'],
                         ['x', 15, 10, 5, 12, 16, 'x', 'x', 'x', 3, 12, 18],
                         [12, 'x', 'x', 'x', 9, 16, 3, 9, 'x', 'x', 'x', 7],
                         [10, 6, 3, 10, 'x', 'x', 1, 17, 'x', 12, 12, 'x'],
                         [11, 8, 15, 'x', 8, 16, 'x', 'x', 5, 15, 12, 7],
                         ['x', 'x', 'x', 'x', 6, 'x', 11, 19, 17, 17, 10, 20],
                         ['x', 3, 17, 17, 'x', 'x', 18, 4, 'x', 'x', 9, 4],
                         ['x', 1, 5, 17, 8, 15, 4, 17, 5, 6, 9, 11],
                         ['x', 'x', 4, 5, 17, 18, 3, 'x', 9, 1, 11, 2],
                         ['x', 'x', 5, 3, 4, 14, 14, 1, 17, 3, 12, 12],
                         ['x', 15, 9, 7, 3, 'x', 'x', 'x', 'x', 'x', 17, 'x'],
                         ['x', 'x', 13, 16, 6, 'x', 6, 'x', 'x', 'x', 'x', 'x']])
    # Define the districts
    districts = [(0, 3), (4, 8), (9, 11)]
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
                # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
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
    # The heuristic relaxes the constraint that Ben's car can only move to a neighboring crossroad and presumes Ben's car can move directly to the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring crossroad is always 1, which is exactly the decrease in the Manhattan distance, if Ben's car is moved toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself would be 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
