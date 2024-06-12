
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 2d tuples
    initial_state = ((6, 10))
    goal_state = ((3, 2))

    # Encoding other variables given in the problem statement
    num_rows = 11
    num_cols = 11
    map = np.array([[14, 'x', 11, 'x', 'x', 8, 15, 17, 18, 'x', 11],
                    [13, 9, 2, 7, 9, 12, 7, 'x', 'x', 'x', 12],
                    ['x', 2, 8, 13, 5, 'x', 'x', 7, 18, 'x', 'x'],
                    [19, 6, 1, 6, 19, 13, 14, 'x', 'x', 17, 'x'],
                    ['x', 9, 6, 'x', 'x', 14, 10, 'x', 'x', 5, 'x'],
                    [12, 'x', 'x', 'x', 7, 17, 11, 'x', 'x', 1, 'x'],
                    ['x', 16, 'x', 2, 11, 15, 6, 'x', 14, 14, 4],
                    ['x', 15, 14, 11, 'x', 17, 20, 18, 4, 16, 8],
                    ['x', 3, 6, 4, 1, 5, 'x', 'x', 3, 7, 9],
                    [18, 14, 3, 4, 'x', 'x', 'x', 12, 15, 10, 'x'],
                    ['x', 8, 'x', 1, 18, 'x', 'x', 'x', 'x', 'x', 'x']])
    district1 = set((i, j) for i in range(4) for j in range(num_cols) if map[i][j] != 'x')
    district2 = set((i, j) for i in range(4, 6) for j in range(num_cols) if map[i][j] != 'x')
    district3 = set((i, j) for i in range(6, num_rows) for j in range(num_cols) if map[i][j] != 'x')

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state, set([initial_state]))]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited = heapq.heappop(queue)

        # Check if the current state is the goal state
        # The goal state is where Ben has visited at least 1 workshop in each district and reached the destination
        if state == goal_state and visited & district1 and visited & district2 and visited & district3:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the workshop to move to is a valid coordinate within the bounds of the city and the workshop is open
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and map[new_row][new_col] != 'x':
                # The action is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the sum of the travel times, as our objective is to minimize the travel time
                new_cost = g + map[new_row][new_col]
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, visited | set([new_state])))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current position from the goal position
    # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move directly to the goal position
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring coordinate is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben is moved toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal position from itself would be 0.
    h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
    return h


print(a_star())
