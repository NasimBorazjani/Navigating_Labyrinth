
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (6, 0)
    goal_state = (4, 9)
    # Define the map of the city
    city_map = np.array([[19, 'x', 7, 'x', 12, 'x', 15, 5, 19, 14],
                         [17, 'x', 3, 5, 7, 'x', 'x', 'x', 17, 20],
                         ['x', 11, 15, 8, 'x', 16, 4, 'x', 1, 1],
                         ['x', 8, 19, 4, 3, 3, 3, 17, 8, 15],
                         [13, 10, 17, 17, 6, 1, 'x', 8, 13, 20],
                         [20, 'x', 'x', 'x', 'x', 4, 18, 4, 17, 'x'],
                         [5, 'x', 'x', 10, 'x', 'x', 14, 2, 5, 'x'],
                         [7, 'x', 4, 'x', 'x', 'x', 15, 'x', 'x', 'x'],
                         [18, 'x', 18, 'x', 4, 'x', 'x', 'x', 17, 'x'],
                         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 13, 'x', 'x']])
    # Define the districts
    districts = [set(), set(), set()]
    for i in range(10):
        for j in range(10):
            if city_map[i][j] != 'x':
                if i < 4:
                    districts[0].add((i, j))
                elif i < 6:
                    districts[1].add((i, j))
                else:
                    districts[2].add((i, j))

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[(initial_state, frozenset([0, 1, 2]))] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [initial_state], (initial_state, frozenset([0, 1, 2])))]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, (state, districts_left) = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state and not districts_left:
            return path

        # Generate all valid actions from the current state, which includes moving to any of the neighboring workshops
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the workshop to be moved to is a valid coordinate within the bounds of the city map and the workshop is not closed
            if 0 <= new_row < 10 and 0 <= new_col < 10 and city_map[new_row][new_col] != 'x':
                # The move is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the sum of the travel times, as our objective is to minimize the travel time
                new_cost = g + city_map[new_row][new_col]
                # Update the districts left to visit
                new_districts_left = districts_left.copy()
                for i in districts_left:
                    if new_state in districts[i]:
                        new_districts_left.remove(i)
                        break

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if (new_state, frozenset(new_districts_left)) not in visited_costs or new_cost < visited_costs[(new_state, frozenset(new_districts_left))]:
                    visited_costs[(new_state, frozenset(new_districts_left))] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_state], (new_state, frozenset(new_districts_left))))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current position from the goal position
    # The heuristic relaxes the constraint that the car can only move to neighboring workshops and presumes we can move the car to the goal position directly
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving the car to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if the car is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the car from its goal position would be 0 in the goal state.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
