
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (7, 2)
    goal_state = (4, 14)
    # Define the map of the city
    city_map = np.array([['x', 'x', '7', '18', '11', '4', '9', 'x', '15', 'x', 'x', 'x', '1', 'x', 'x'],
                         ['x', 'x', '14', 'x', '10', 'x', 'x', 'x', '8', 'x', 'x', '16', '1', 'x', 'x'],
                         ['17', '17', 'x', 'x', 'x', 'x', 'x', '7', '6', '12', 'x', 'x', 'x', '7', 'x'],
                         ['x', 'x', 'x', 'x', '10', 'x', 'x', '18', '1', '11', '4', 'x', '13', '10', '16'],
                         ['x', 'x', 'x', '12', '1', 'x', 'x', 'x', '2', '7', '1', 'x', '2', 'x', '5'],
                         ['x', 'x', '8', 'x', '12', 'x', 'x', '5', '17', 'x', '2', 'x', '4', '10', '18'],
                         ['x', 'x', '4', '19', '1', 'x', '18', '7', 'x', '10', '3', 'x', '19', '16', '19'],
                         ['6', '12', '15', '16', '5', '9', '16', '18', '10', '15', '5', 'x', '5', '14', 'x'],
                         ['x', '16', '8', '17', '12', '11', '16', '8', '9', '9', '7', '4', '5', '20', '3'],
                         ['19', '17', '15', 'x', 'x', '17', 'x', '3', '2', '2', '11', '7', '8', '16', '1'],
                         ['13', '4', '17', 'x', 'x', 'x', 'x', '5', 'x', '18', '16', '15', '19', '4', 'x'],
                         ['11', 'x', 'x', 'x', 'x', '12', 'x', 'x', 'x', 'x', 'x', 'x', '19', 'x', 'x'],
                         ['18', 'x', 'x', 'x', '9', '19', 'x', '16', '6', 'x', '9', '3', '16', '15', 'x'],
                         ['x', 'x', 'x', '10', 'x', 'x', '4', '3', 'x', '3', 'x', '16', '18', 'x', '12'],
                         ['x', '13', 'x', 'x', 'x', 'x', 'x', '10', '5', 'x', '17', 'x', 'x', '7', 'x']])
    num_rows, num_cols = city_map.shape
    # Define the districts
    districts = [range(0, 5), range(5, 9), range(9, 15)]
    # Define the directions in which Ben can move
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state, [False, False, False])]
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
            if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and
                    city_map[new_state[0]][new_state[1]] != 'x'):
                # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
                new_cost = g + int(city_map[new_state[0]][new_state[1]])
                # Check if the new state is in a new district
                new_visited_districts = visited_districts[:]
                for i, district in enumerate(districts):
                    if new_state[0] in district:
                        new_visited_districts[i] = True
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, new_visited_districts))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben can only move to a neighboring crossroad and presumes he can move directly to the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring crossroad is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state, otherwise the estimated cost of the successor state is the same or higher, and the heuristic estimate for the goal state is 0, as the distance from the goal state to itself is 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
