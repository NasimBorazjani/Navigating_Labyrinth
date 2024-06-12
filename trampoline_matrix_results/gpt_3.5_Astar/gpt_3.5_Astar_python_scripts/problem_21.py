
import heapq
import math


def a_star():
    # Define the initial state of the grid and the goal state
    initial_state = ((1, 9), 3)
    goal_state = (5, 0)
    grid = [[0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
            [0, 0, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 1, 0],
            [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 0, 0, 1, 1, 1, 1, 1]]
    
    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_state))

    while queue:
        _, g, actions, state = heappop(queue)

        # If Alex reaches the goal state, return the actions taken
        if state[0] == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 8 adjacent trampolines
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row = state[0][0] + i
                new_col = state[0][1] + j
                # Check if the new position is within the grid and not broken
                if 0 <= new_row < 10 and 0 <= new_col < 10 and grid[new_row][new_col] == 0:
                    # Calculate the new number of diagonal jumps
                    new_diagonal_jumps = state[1] - 1 if i != 0 and j != 0 else state[1]
                    new_state = ((new_row, new_col), new_diagonal_jumps)
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal_state)
                        heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
    return None


def heuristic(state, goal):
    # The heuristic is the Euclidean distance between the current position and the goal position
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as the shortest path between two points is a straight line
    # The heuristic is consistent because the cost of moving from one position to an adjacent position is always 1, which is exactly the decrease in the heuristic estimate, if the position is moved towards the goal position
    h = math.sqrt((state[0][0] - goal[0]) ** 2 + (state[0][1] - goal[1]) ** 2)
    return h


print(a_star())
