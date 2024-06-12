
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (6, 2)
    goal_state = (2, 10)
    # Define the map of the city
    city_map = np.array([[19, 12, 'x', 'x', 2, 5, 4, 13, 17, 19, 'x', 2],
                         ['x', 18, 'x', 5, 5, 'x', 'x', 8, 12, 18, 'x', 15],
                         ['x', 9, 4, 10, 7, 20, 'x', 16, 20, 13, 15, 'x'],
                         [8, 'x', 'x', 11, 1, 19, 'x', 14, 6, 'x', 3, 'x'],
                         [10, 'x', 4, 8, 17, 'x', 18, 'x', 7, 'x', 6, 5],
                         ['x', 'x', 3, 1, 8, 18, 'x', 4, 17, 'x', 'x', 13],
                         ['x', 'x', 6, 'x', 'x', 'x', 14, 'x', 'x', 10, 10, 'x'],
                         ['x', 'x', 15, 'x', 'x', 'x', 'x', 'x', 2, 'x', 'x', 'x'],
                         ['x', 'x', 5, 11, 6, 1, 'x', 6, 14, 'x', 'x', 'x'],
                         ['x', 1, 17, 10, 15, 'x', 14, 6, 'x', 'x', 'x', 'x'],
                         [12, 2, 'x', 10, 'x', 'x', 7, 'x', 'x', 'x', 'x', 'x'],
                         ['x', 9, 14, 'x', 9, 18, 14, 'x', 'x', 'x', 6, 'x']])
    num_rows, num_cols = city_map.shape
    # Define the districts
    districts = [range(0, 2), range(2, 6), range(6, 12)]
    # Define the directions in which Ben can move
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # left, right, up, down

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state, {initial_state})]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited_states = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state and all(any(state[0] in district for state in visited_states) for district in districts):
            return actions

        # Generate all possible actions from the current state, which includes moving in any of the 4 directions
        for direction in directions:
            new_state = (state[0] + direction[0], state[1] + direction[1])
            # Check if the new state is valid, ie within the bounds of the city map and not a closed workshop
            if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and
                    city_map[new_state[0]][new_state[1]] != 'x' and new_state not in visited_states):
                # The cost so far is the sum of the travel times, as our objective is to minimize the total travel time
                new_cost = g + city_map[new_state[0]][new_state[1]]
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, visited_states | {new_state}))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben can only move to neighboring workshops and presumes he can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance from the goal workshop to itself is 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
