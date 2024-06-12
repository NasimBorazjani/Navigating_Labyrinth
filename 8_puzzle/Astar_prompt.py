import heapq

def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 3x3 tuples
    initial_state = ((55, 43, 17), (97, 35, 9), (12, 25, '_'))
    goal_state = ((97, 55, 43), (35, 25, 17), (12, 9, '_'))    
    
    # Encoding other variables given in the problem statement
    num_rows = 3
    num_cols = 3

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal 
    # Record the swaps required to get to each state in a list; no swaps perfomed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states 
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state:
            return actions

        # Generate all valid actions from the current state, which includes swapping any of the tiles neighboring the empty spot, with the empty spot
        # Generate the coordinates of the tiles neighbouring "_"
        empty_row, empty_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == '_'][0]
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            swap_row, swap_col = empty_row + d_row, empty_col + d_col
            # Check if the swap is valid, ie if the coordinate of the tile to be swapped is a valid coordinate within the bounds of the board
            if 0 <= swap_row < num_rows and 0 <= swap_col < num_cols:
                # The actions is valid, generate the new state
                new_state = [list(row[:]) for row in state]
                number_to_be_swapped = new_state[swap_row][swap_col]
                # Do the swap
                new_state[empty_row][empty_col], new_state[swap_row][swap_col] = new_state[swap_row][swap_col], new_state[empty_row][empty_col]
                new_state = tuple(tuple(row) for row in new_state)
                # The cost so far is the number of swaps made, as our objective is to minimize the number of swaps required to reach the goal state  
                new_cost = g + 1
                
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [number_to_be_swapped], new_state))
                    
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each tile from its goal position
    # The heuristic relaxes the constraint that a tile can only be swapped with the empty spot and presumes we can move the tiles to their goal position by swapping them with any of the other tiles
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving a tile to a neighbouring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the tile is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            # Can't compare integers with "_" when finding the goal position of each tile, thus ignore the "_" tile
            if state[i][j] != '_':
                # Get goal position of each tile
                goal_row, goal_col = [(x, y) for x in range(len(goal)) for y in range(len(goal[x])) if goal[x][y] == state[i][j]][0]
                # Add the the Manhattan distance of the current and goal coordinates of teh tile to the estimate
                h += abs(i - goal_row) + abs(j - goal_col)
    return h

print(a_star())