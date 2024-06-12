
import heapq

def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 2D tuples
    initial_state = (8, 1)
    goal_state = (1, 9)
    # Define the map of the park
    park_map = [[1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                [1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
                [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
                [1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                [0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 0, 0, 0, 1, 1, 0]]
    # Define the size of the park
    park_size = 10
    # Define the directions of movement
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    # Define the diagonal directions
    diagonal_directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], 0, initial_state)]
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, diagonal_jumps, state = heapq.heappop(queue)
        # If the current state is the goal state and the number of diagonal jumps is exactly 3, return the actions
        if state == goal_state and diagonal_jumps == 3:
            return actions
        # Generate all possible actions from the current state, which includes moving to any of the eight adjacent trampolines
        for direction in directions:
            new_state = (state[0] + direction[0], state[1] + direction[1])
            # Check if the new state is valid, ie within the bounds of the park and not a broken trampoline
            if (0 <= new_state[0] < park_size and 0 <= new_state[1] < park_size and park_map[new_state[0]][new_state[1]] == 0):
                # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state
                new_cost = g + 1
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # If the direction of movement is diagonal, increment the number of diagonal jumps
                    new_diagonal_jumps = diagonal_jumps + 1 if direction in diagonal_directions else diagonal_jumps
                    # If the number of diagonal jumps is less than or equal to 3, add the new state to the queue
                    if new_diagonal_jumps <= 3:
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_diagonal_jumps, new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Alex can only move to adjacent trampolines and presumes he can move directly to the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring trampoline is always 1, which is exactly the decrease in the Manhattan distance, if Alex moves toward the goal state, otherwise the estimated cost of the successor state is the same or higher, and the heuristic estimate for the goal state is 0, as the distance from the goal state to itself is 0
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

print(a_star())
