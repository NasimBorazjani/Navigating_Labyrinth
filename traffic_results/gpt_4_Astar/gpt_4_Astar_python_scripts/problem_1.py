
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (5, 7)
    goal_state = (2, 1)
    # Define the map of the city
    city_map = np.array([[13, 'x', 'x', 3, 10, 20, 3, 'x', 5],
                         ['x', 'x', 'x', 'x', 20, 16, 'x', 'x', 17],
                         [3, 14, 18, 8, 1, 20, 14, 'x', 7],
                         [13, 3, 6, 10, 7, 4, 6, 6, 1],
                         [10, 12, 2, 'x', 11, 'x', 10, 8, 11],
                         ['x', 'x', 'x', 11, 6, 18, 13, 20, 17],
                         ['x', 'x', 16, 'x', 4, 17, 7, 10, 15],
                         ['x', 7, 16, 6, 19, 4, 7, 'x', 'x'],
                         ['x', 11, 18, 'x', 'x', 'x', 3, 8, 'x']])
    # Define the districts
    districts = [set(), set(), set()]
    for i in range(9):
        for j in range(9):
            if city_map[i][j] != 'x':
                if i < 3:
                    districts[0].add((i, j))
                elif i < 5:
                    districts[1].add((i, j))
                else:
                    districts[2].add((i, j))

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [initial_state], initial_state, [initial_state[0] < 3, 3 <= initial_state[0] < 5, 5 <= initial_state[0]])]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited_districts = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state and all(visited_districts):
            return actions

        # Generate all valid actions from the current state, which includes moving to any of the neighboring workshops
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the workshop to be moved to is a valid coordinate within the bounds of the city map and the workshop is not closed
            if 0 <= new_row < 9 and 0 <= new_col < 9 and city_map[new_row][new_col] != 'x':
                # The move is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the sum of the travel times, as our objective is to minimize the total travel time
                new_cost = g + city_map[new_row][new_col]
                new_visited_districts = visited_districts[:]
                new_visited_districts[new_row // 3] = True

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, new_visited_districts))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current position to the goal position
    # The heuristic relaxes the constraint that Ben can only move to neighboring workshops and presumes Ben can move directly to the goal position
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben is moved toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal position from itself would be 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
