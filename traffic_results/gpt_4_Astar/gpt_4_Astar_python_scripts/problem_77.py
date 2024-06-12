
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 2d tuples
    initial_state = ((6, 1))
    goal_state = ((3, 13))

    # Encoding other variables given in the problem statement
    num_rows = 14
    num_cols = 14
    district_rows = [2, 6, 14]
    district_visited = [False, False, False]

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the swaps required to get to each state in a list; no swaps performed to reach the initial state
    queue = [(0, 0, [], initial_state, district_visited)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, district_visited = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state and all(district_visited):
            return actions

        # Generate all valid actions from the current state, which includes moving in any of the 4 directions
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the new position is a valid coordinate within the bounds of the city
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city[new_row][new_col] != 'x':
                # The move is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the travel time to the new workshop, as our objective is to minimize the travel time
                new_cost = g + int(city[new_row][new_col])
                # Check if the new workshop is in a new district
                new_district_visited = district_visited[:]
                for i in range(len(district_rows)):
                    if new_row < district_rows[i] and not new_district_visited[i]:
                        new_district_visited[i] = True
                        break

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, new_district_visited))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current position to the goal position
    # The heuristic relaxes the constraint that Ben must visit a workshop in each district and presumes Ben can move to the goal position directly
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if Ben is moved toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of the goal position from itself would be 0.
    h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
    return h


city = [['x', '5', '9', '6', '13', '13', '8', '6', '13', 'x', '13', 'x', 'x', 'x'],
        ['3', '10', '16', 'x', 'x', '3', '13', '1', '11', '9', '7', '6', 'x', '18'],
        ['9', '11', '3', 'x', 'x', '6', '13', 'x', '14', 'x', '12', '1', '2', '4'],
        ['x', '17', '13', 'x', '14', '4', '6', '8', 'x', 'x', '1', 'x', '6', '2'],
        ['7', 'x', '11', 'x', '14', 'x', '11', '7', 'x', '5', 'x', '1', '12', 'x'],
        ['x', '20', '20', '19', 'x', '18', '2', '19', '1', '6', '12', 'x', 'x', '16'],
        ['8', '5', '7', '11', 'x', '1', 'x', 'x', 'x', '11', '4', 'x', 'x', '3'],
        ['x', '11', 'x', '11', '11', 'x', 'x', '18', 'x', 'x', 'x', '7', '6', 'x'],
        ['2', '2', '14', '5', '5', 'x', 'x', '11', '19', '16', 'x', '14', '7', '19'],
        ['x', '5', 'x', 'x', '7', 'x', '10', 'x', 'x', 'x', '3', '15', 'x', 'x'],
        ['19', 'x', 'x', 'x', 'x', '8', '3', '19', 'x', '18', 'x', 'x', 'x', '9'],
        ['17', 'x', '19', 'x', 'x', 'x', '5', '3', 'x', 'x', '7', '4', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', '12', '11', 'x', 'x', 'x', 'x', 'x', '6', '6'],
        ['x', 'x', 'x', 'x', 'x', 'x', '4', 'x', 'x', 'x', '7', 'x', '6', '3']]

print(a_star())
