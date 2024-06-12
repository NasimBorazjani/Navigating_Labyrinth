
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((1, 0), (0, 0, 1, 0, 1, 1, 0, 0, 0), (0, 0, 0, 1, 1, 1, 0, 1, 1), (0, 1, 0, 0, 0, 0, 1, 0, 1), (0, 1, 1, 1, 0, 0, 1, 1, 0), (0, 1, 1, 1, 1, 0, 0, 1, 1), (1, 0, 1, 1, 0, 1, 0, 0, 0), (0, 1, 1, 1, 1, 0, 0, 0, 0), (1, 1, 0, 1, 1, 0, 1, 0, 0), (0, 1, 1, 1, 1, 1, 0, 0, 0))
    num_rows = 9
    num_cols = 9
    goal_state = (5, 8)
    # Define the possible moves Alex can make, including diagonal jumps
    moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state[0]] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [initial_state[0]])]
    
    while queue:
        _, g, path = heapq.heappop(queue)
        current_position = path[-1]
        
        # If Alex reaches the goal state, return the path
        if current_position == goal_state:
            return path
        
        # Generate all possible moves from the current position
        for move in moves:
            new_position = (current_position[0] + move[0], current_position[1] + move[1])
            # Check if the new position is within the bounds of the grid and is not a broken trampoline
            if 0 <= new_position[0] < num_rows and 0 <= new_position[1] < num_cols and initial_state[new_position[0] + 1][new_position[1] + 1] == 0:
                new_path = path + [new_position]
                # Calculate the cost of the new path
                new_cost = g + 1 + math.sqrt((new_position[0] - goal_state[0]) ** 2 + (new_position[1] - goal_state[1]) ** 2)
                
                # If the new position is unvisited or we found a new path with a lower cost to reach this position, add it to the queue of unvisited states
                if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                    visited_costs[new_position] = new_cost
                    heapq.heappush(queue, (new_cost, g + 1, new_path))
    
    return None


print(a_star())
