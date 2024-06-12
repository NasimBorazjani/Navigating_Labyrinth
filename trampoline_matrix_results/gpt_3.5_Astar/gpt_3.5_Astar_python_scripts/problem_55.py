
import heapq
import math


def a_star():
    # Define the initial state of the trampoline park as a 2d tuple
    initial_state = ((1, 11), (9, 0))
    num_rows = 12
    num_cols = 12
    park = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1]]
  
    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If Alex has made exactly 4 diagonal jumps and reached the destination, return the actions taken
        if state[0] == (9, 0) and len(actions) == 4:
            return actions

        # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row = state[0][0] + i
                new_col = state[0][1] + j
                # Check if the new position is within the bounds of the park and the trampoline is functional
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and park[new_row][new_col] == 0:
                    # Check if the jump is diagonal
                    if abs(i) == 1 and abs(j) == 1:
                        # The new state is updated with the new position
                        new_state = ((new_row, new_col), state[1])
                        # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required
                        new_cost = g + 1
                        # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            # Calculate the heuristic cost to reach the destination
                            h = heuristic(new_state, state[1])
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
    return None


def heuristic(state, destination):
    # The heuristic function calculates the Manhattan distance between the current position and the destination
    # This heuristic is admissible because the shortest path between two points on a grid is the Manhattan distance
    # The heuristic is consistent because the cost of moving from one position to an adjacent position is always 1, which is exactly the decrease in the heuristic estimate
    h = abs(state[0][0] - destination[0]) + abs(state[0][1] - destination[1])
    return h


print(a_star())
