
import heapq

def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 2D tuples
    initial_state = ((11, 11), 0)
    goal_state = (0, 6)
    # Define the map of the park
    park_map = [[1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
                [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1],
                [1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
                [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0],
                [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]
    # Define the possible moves
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    # Define the size of the park
    size = 12

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
        if state[0] == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the eight adjacent trampolines
        for move in moves:
            new_state = (state[0][0] + move[0], state[0][1] + move[1])
            # Check if the new state is valid, ie if the new state is within the bounds of the park and the trampoline is not broken
            if 0 <= new_state[0] < size and 0 <= new_state[1] < size and park_map[new_state[0]][new_state[1]] == 0:
                # The actions is valid, generate the new state
                diagonal_jumps = state[1]
                if move in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
                    diagonal_jumps += 1
                new_state = (new_state, diagonal_jumps)
                # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state 
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[0]], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current position to the goal position
    # The heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps and presumes Alex can move to the goal position by jumping to any of the eight adjacent trampolines
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring trampoline is always 1, which is exactly the decrease in the Manhattan distance, if Alex moves toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance from the goal position to itself would be 0.
    h = abs(state[0][0] - goal[0]) + abs(state[0][1] - goal[1])
    return h

print(a_star())
