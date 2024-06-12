
import heapq

def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 2D tuples
    initial_state = ((8, 8), 0)
    goal_state = (2, 1)
    # Define the map of the trampoline park
    park_map = [[0, 1, 0, 1, 0, 1, 1, 1, 0],
                [1, 0, 1, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 1, 1, 0, 1, 1],
                [1, 0, 0, 0, 0, 1, 1, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 1, 0],
                [1, 0, 0, 0, 1, 1, 1, 0, 1],
                [0, 1, 0, 0, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 1, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 0, 0, 1, 0]]
    # Define the possible moves Alex can make
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [(8, 8)], initial_state)]
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, (x, y, diagonal_jumps) = heapq.heappop(queue)
        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if (x, y) == goal_state and diagonal_jumps == 3:
            return path
        # Generate all valid actions from the current state, which includes moving to any of the eight adjacent trampolines
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            # Check if the move is valid, ie if the new position is a valid coordinate within the bounds of the park and the trampoline is not broken
            if 0 <= new_x < 9 and 0 <= new_y < 9 and park_map[new_x][new_y] == 0:
                # The action is valid, generate the new state
                new_diagonal_jumps = diagonal_jumps
                if dx != 0 and dy != 0:
                    new_diagonal_jumps += 1
                new_state = (new_x, new_y, new_diagonal_jumps)
                # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state 
                new_cost = g + 1
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = abs(goal_state[0] - new_x) + abs(goal_state[1] - new_y) + abs(3 - new_diagonal_jumps)
                    heapq.heappush(queue, (new_cost + h, new_cost, path + [(new_x, new_y)], new_state))
    return None

print(a_star())
