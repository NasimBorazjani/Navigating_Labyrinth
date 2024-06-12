
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[82, '_', 39, 54], [55, 62, 53, 35], [69, 16, 11, 71]]
    goal_state = [[82, 71, 62, 55], [54, 53, 39, 35], [16, 11, '_', 0]]
    
    # Define the goal state as a dictionary for easy lookup
    goal_dict = {82: (0, 0), 71: (0, 1), 62: (0, 2), 55: (0, 3), 54: (1, 0), 53: (1, 1), 39: (1, 2), 35: (1, 3), 16: (2, 0), 11: (2, 1), '_': (2, 2), 0: (2, 3)}
    
    visited_costs = {}
    visited_costs[str(initial_state)] = 0
    
    queue = [(0, 0, [], initial_state)]
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Check if the current state is the goal state
        if state == goal_state:
            return actions
        
        # Find the position of the empty spot in the current state
        empty_spot = np.argwhere(np.array(state) == '_')[0]
        
        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col
            
            # Check if the new position is valid
            if 0 <= new_row < 3 and 0 <= new_col < 4:
                # Generate the new state by swapping the empty spot with the neighboring tile
                new_state = [row[:] for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                
                # Calculate the cost of the new state
                new_cost = g + 1
                
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of unvisited states
                if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                    visited_costs[str(new_state)] = new_cost
                    # Calculate the heuristic cost based on the Manhattan distance of each tile to its goal position
                    h = heuristic(new_state, goal_dict)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state[empty_spot[0]][empty_spot[1]]], new_state))
    
    return None


def heuristic(state, goal_dict):
    # Calculate the heuristic cost based on the Manhattan distance of each tile to its goal position
    h = 0
    for i in range(3):
        for j in range(4):
            if state[i][j] != '_':
                goal_row, goal_col = goal_dict[state[i][j]]
                h += abs(i - goal_row) + abs(j - goal_col)
    return h


print(a_star())
