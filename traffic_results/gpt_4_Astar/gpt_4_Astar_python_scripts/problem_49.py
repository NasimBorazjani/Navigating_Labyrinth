
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 2d tuples
    initial_state = ((3, 11), (1, 0, 0))
    goal_state = (4, 0)
    num_rows = 12
    num_cols = 12
    # Define the matrix map of the city
    city_map = np.array([['x', 'x', '13', '9', 'x', '15', 'x', 'x', '2', '13', '9', '11'],
                         ['8', 'x', '4', '5', '13', 'x', 'x', '7', '16', 'x', '15', '13'],
                         ['x', 'x', 'x', 'x', '3', 'x', '4', '3', '18', 'x', '11', '18'],
                         ['6', 'x', '14', '5', '16', 'x', '11', 'x', '3', '16', '3', '3'],
                         ['15', '12', 'x', 'x', '10', '3', '2', '14', 'x', '18', 'x', 'x'],
                         ['11', '1', '2', '1', '17', '15', 'x', '2', 'x', '12', 'x', 'x'],
                         ['x', 'x', '3', '15', '16', '1', 'x', 'x', 'x', 'x', 'x', 'x'],
                         ['x', '10', 'x', 'x', 'x', '6', '1', '8', '19', '13', '7', 'x'],
                         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '3'],
                         ['3', '7', '12', 'x', '15', 'x', '19', '13', '17', '14', 'x', 'x'],
                         ['x', 'x', 'x', 'x', '4', '4', '18', 'x', '5', 'x', 'x', '10'],
                         ['x', 'x', '15', '9', '13', '10', '8', '4', '8', '6', '7', '7']])
    # Define the districts of the city
    districts = [range(0, 3), range(3, 6), range(6, 12)]

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

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state[0] == goal_state and all(i for i in state[1]):
            return actions

        # Generate all valid actions from the current state, which includes moving to any of the neighboring workshops
        # Generate the coordinates of the workshops neighboring the current workshop
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state[0][0] + d_row, state[0][1] + d_col
            # Check if the move is valid, ie if the coordinate of the workshop to be moved to is a valid coordinate within the bounds of the city and the workshop is not closed
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                # The move is valid, generate the new state
                new_state = ((new_row, new_col), list(state[1]))
                # Check if the new workshop is in a new district
                for i, district in enumerate(districts):
                    if new_row in district and not new_state[1][i]:
                        new_state[1][i] = 1
                new_state = (new_state[0], tuple(new_state[1]))
                # The cost so far is the sum of the travel times, as our objective is to minimize the travel time
                new_cost = g + int(city_map[new_row][new_col])

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state[0], goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state[0]], new_state))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current workshop from the goal workshop
    # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
