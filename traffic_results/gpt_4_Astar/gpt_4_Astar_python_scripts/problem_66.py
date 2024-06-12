
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 2d tuples
    initial_state = ((3, 10))
    goal_state = ((9, 2))   
  
    # Encoding other variables given in the problem statement
    num_rows = 13
    num_cols = 13
    district1 = range(0, 4)
    district2 = range(4, 9)
    district3 = range(9, 13)
    visited_districts = set()
    visited_districts.add(1)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the swaps required to get to each state in a list; no swaps performed to reach the initial state
    queue = [(0, 0, [], initial_state, visited_districts)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited_districts = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state and len(visited_districts) == 3:
            return actions

        # Generate all valid actions from the current state, which includes moving in any of the 4 directions
        # Generate the coordinates of the tiles neighboring "_"
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the move is valid, ie if the coordinate of the tile to be moved is a valid coordinate within the bounds of the board
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                # The move is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the number of minutes taken, as our objective is to minimize the time required to reach the goal state 
                new_cost = g + city_map[new_row][new_col]
                new_visited_districts = visited_districts.copy()
                if new_row in district1:
                    new_visited_districts.add(1)
                elif new_row in district2:
                    new_visited_districts.add(2)
                elif new_row in district3:
                    new_visited_districts.add(3)
              
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, new_visited_districts))
                  
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current position from the goal position
    # The heuristic relaxes the constraint that a tile can only be moved to a neighboring coordinate and presumes we can move the tile to the goal position directly
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving a tile to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the tile is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each tile from its goal position would be 0 in the goal state.
    h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
    return h


city_map = [['x', 17, 14, 18, 'x', 'x', 8, 18, 10, 5, 5, 'x', 'x'],
            ['x', 'x', 'x', 'x', 17, 18, 17, 17, 6, 12, 'x', 7, 16],
            [17, 'x', 17, 6, 18, 'x', 10, 13, 10, 19, 15, 4, 13],
            [15, 5, 15, 3, 17, 3, 'x', 'x', 18, 15, 19, 3, 2],
            ['x', 'x', 'x', 'x', 2, 10, 'x', 'x', 'x', 18, 14, 5, 12],
            ['x', 16, 'x', 12, 4, 7, 'x', 'x', 9, 'x', 'x', 'x', 'x'],
            ['x', 7, 'x', 'x', 16, 2, 9, 1, 3, 'x', 'x', 4, 'x'],
            [15, 16, 'x', 10, 1, 16, 'x', 'x', 2, 18, 1, 'x', 'x'],
            ['x', 'x', 8, 3, 'x', 19, 'x', 'x', 'x', 5, 9, 'x', 'x'],
            ['x', 8, 12, 14, 'x', 'x', 'x', 16, 'x', 8, 'x', 3, 2],
            [8, 1, 'x', 'x', 'x', 'x', 13, 'x', 'x', 'x', 9, 'x', 12],
            ['x', 'x', 3, 3, 11, 'x', 'x', 16, 'x', 'x', 5, 'x', 'x'],
            ['x', 11, 17, 'x', 'x', 'x', 'x', 9, 'x', 'x', 2, 15, 'x']]

city_map = [[int(cell) if cell != 'x' else 'x' for cell in row] for row in city_map]

print(a_star())
