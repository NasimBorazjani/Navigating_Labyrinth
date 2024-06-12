
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (3, 0)
    goal_state = (5, 12)
    # Define the map of the city as a 2d tuple
    city_map = (('x', 'x', '11', '16', 'x', 'x', 'x', 'x', '4', 'x', '14', '5', 'x', 'x'),
                ('3', '1', '13', 'x', 'x', '14', '11', 'x', 'x', '15', '12', '15', 'x', 'x'),
                ('17', '15', '17', '10', '11', 'x', '7', '1', '1', '14', 'x', '9', 'x', 'x'),
                ('8', 'x', 'x', '13', '2', '12', 'x', '8', 'x', 'x', '9', '13', '19', '5'),
                ('4', 'x', '2', '3', '8', 'x', 'x', '17', 'x', 'x', '16', '10', 'x', 'x'),
                ('x', 'x', 'x', 'x', '3', '13', '14', '16', '18', '11', '4', '19', '20', 'x'),
                ('x', '11', 'x', 'x', '3', '10', '8', '9', '18', '7', '1', '14', 'x', '6'),
                ('11', 'x', '12', '11', 'x', '11', '10', '3', '10', '12', '15', 'x', '11', 'x'),
                ('x', 'x', '4', '18', 'x', 'x', '13', 'x', '14', '10', 'x', '8', 'x', '17'),
                ('x', 'x', 'x', 'x', 'x', 'x', 'x', '7', '7', 'x', 'x', '18', '19', '18'),
                ('19', '4', 'x', '2', '14', '2', 'x', '9', 'x', '10', '7', '17', '4', '12'),
                ('13', '2', 'x', 'x', '18', '5', 'x', '11', 'x', 'x', 'x', '18', 'x', 'x'),
                ('x', 'x', '13', '1', '13', 'x', '2', 'x', 'x', 'x', 'x', 'x', 'x', '14'),
                ('x', '12', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '19', 'x', 'x', '9', '1'))
    num_rows = len(city_map)
    num_cols = len(city_map[0])
    # Define the districts of the city
    districts = [range(0, 4), range(4, 7), range(7, 14)]
    # Define the set of valid numbers that could be in the grid
    numbers = set(range(29, 54))

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state, {initial_state})]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            # Check if Ben has visited at least 1 workshop in each district
            if all(any(workshop[0] in district for workshop in visited) for district in districts):
                return actions

        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the workshop to move to is a valid coordinate within the bounds of the city and the workshop is not closed
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                # The new state is the coordinates of the workshop moved to
                new_state = (new_row, new_col)
                # The cost so far is the travel time to the new workshop, as the task is to minimize the travel time
                new_cost = g + int(city_map[new_row][new_col])

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, visited | {new_state}))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current workshop to the goal workshop
    # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the travel time to reach the goal workshop and is admissible
    # The heuristic is consistent because the travel time to move to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated travel time of the successor state is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
