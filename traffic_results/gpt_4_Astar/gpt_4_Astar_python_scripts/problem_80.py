
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 2d tuples
    initial_state = ((1, 10))
    goal_state = ((7, 2))

    # Encoding other variables given in the problem statement
    num_rows = 14
    num_cols = 14
    district1 = range(0, 2)
    district2 = range(2, 7)
    district3 = range(7, 14)
    districts = [district1, district2, district3]
    visited_districts = set()

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state, visited_districts)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited_districts = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state and len(visited_districts) == 3:
            return actions

        # Generate all valid actions from the current state, which includes moving to any of the neighboring workshops
        # Generate the coordinates of the workshops neighboring the current workshop
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the workshop to be moved to is a valid coordinate within the bounds of the city
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city[new_row][new_col] != 'x':
                # The move is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the travel time to the new workshop, as our objective is to minimize the travel time required to reach the goal state
                new_cost = g + city[new_row][new_col]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    new_visited_districts = visited_districts.copy()
                    for i, district in enumerate(districts):
                        if new_row in district:
                            new_visited_districts.add(i)
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, new_visited_districts))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current workshop from the goal workshop
    # The heuristic relaxes the constraint that a workshop can only be moved to if it is neighboring the current workshop and presumes we can move to the goal workshop directly from the current workshop
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if the workshop is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
    h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
    return h


city = np.array([['x', 'x', 8, 16, 3, 'x', 15, 17, 2, 'x', 'x', 5, 'x', 'x'],
                 ['x', 'x', 17, 'x', 13, 'x', 4, 'x', 13, 3, 3, 6, 11, 'x'],
                 ['x', 'x', 8, 'x', 14, 1, 15, 11, 'x', 18, 12, 'x', 'x', 'x'],
                 ['x', 13, 19, 4, 13, 2, 13, 3, 'x', 1, 20, 18, 'x', 15],
                 [13, 'x', 1, 'x', 11, 'x', 8, 14, 4, 11, 3, 'x', 'x', 'x'],
                 [12, 11, 16, 1, 1, 'x', 5, 1, 'x', 9, 'x', 'x', 1, 'x'],
                 [8, 'x', 6, 15, 'x', 7, 19, 13, 2, 'x', 3, 3, 'x', 2],
                 [18, 'x', 19, 15, 2, 'x', 'x', 18, 2, 'x', 10, 'x', 'x', 1],
                 [3, 4, 'x', 19, 'x', 6, 'x', 7, 'x', 'x', 'x', 'x', 15, 'x'],
                 ['x', 'x', 'x', 16, 7, 17, 11, 'x', 7, 'x', 'x', 'x', 'x', 15],
                 ['x', 9, 'x', 'x', 'x', 19, 19, 7, 3, 12, 14, 11, 16, 7],
                 [8, 19, 15, 1, 'x', 14, 'x', 1, 'x', 'x', 'x', 'x', 'x', 'x'],
                 ['x', 14, 'x', 'x', 'x', 'x', 'x', 18, 'x', 'x', 2, 11, 7, 'x'],
                 ['x', 'x', 'x', 'x', 'x', 3, 11, 12, 'x', 'x', 'x', 2, 6, 'x']])

print(a_star())
