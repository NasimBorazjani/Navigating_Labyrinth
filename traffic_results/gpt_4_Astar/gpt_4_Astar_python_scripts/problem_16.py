
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (5, 1)
    goal_state = (3, 9)
    # Define the map of the city
    city_map = np.array([['x', 'x', 'x', '16', '1', '13', '17', '7', '14', 'x'],
                         ['x', '10', 'x', '12', 'x', '13', 'x', '8', '19', '4'],
                         ['9', '13', 'x', '13', 'x', 'x', '15', 'x', 'x', '16'],
                         ['3', '8', 'x', '16', '12', 'x', 'x', 'x', 'x', '13'],
                         ['13', 'x', '1', '15', '18', '8', 'x', '10', 'x', 'x'],
                         ['8', '1', '2', '14', 'x', '8', 'x', '4', 'x', '11'],
                         ['14', '13', '15', 'x', '16', 'x', '13', '2', 'x', '19'],
                         ['x', '4', '10', 'x', 'x', '16', 'x', '11', 'x', 'x'],
                         ['x', '14', 'x', 'x', 'x', 'x', 'x', '18', '6', '18'],
                         ['x', '3', '2', '6', '7', 'x', 'x', '9', '8', '5']])
    # Define the districts
    districts = [set(range(0, 4)), set(range(4, 6)), set(range(6, 10))]

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state, [initial_state[0] in district for district in districts])]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited_districts = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state and all(visited_districts):
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring cells
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the cell to move to is a valid coordinate within the bounds of the city map and the cell is not a closed workshop
            if 0 <= new_row < 10 and 0 <= new_col < 10 and city_map[new_row][new_col] != 'x':
                # The move is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the sum of the travel times, as our objective is to minimize the travel time
                new_cost = g + int(city_map[new_row][new_col])
                # Update the districts visited
                new_visited_districts = visited_districts[:]
                for i, district in enumerate(districts):
                    if new_row in district:
                        new_visited_districts[i] = True

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, new_visited_districts))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben can only move to a neighboring cell and presumes Ben can move directly to the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring coordinate is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself would be 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
