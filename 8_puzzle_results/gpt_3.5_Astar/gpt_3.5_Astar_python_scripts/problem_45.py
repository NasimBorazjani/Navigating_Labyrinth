
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[11, 55, 69, 67], [19, 31, '_', 35], [64, 65, 88, 96]]
    goal_state = [[96, 88, 69, 67], [65, 55, 35, 31], [64, 55, 19, 11]]
    
    # Define the goal state as a 1D list for easier comparison
    goal_state_flat = [96, 88, 69, 67, 65, 55, 35, 31, 64, 55, 19, 11]
    
    visited_costs = {}
    visited_costs[np.array(initial_state).tostring()] = 0
    
    queue = []
    # No actions taken in the initial state
    heapq.heappush(queue, (0, 0, [], initial_state))
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Flatten the state for comparison
        state_flat = [cell for row in state for cell in row]
        
        # If the current state matches the goal state, return the actions taken
        if state_flat == goal_state_flat:
            return actions
        
        # Find the position of the empty spot
        empty_spot = [(i, j) for i in range(3) for j in range(4) if state[i][j] == '_'][0]
        
        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col
            
            # Check if the new position is valid
            if 0 <= new_row < 3 and 0 <= new_col < 4:
                # Generate the new state by swapping the empty spot with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                
                # Calculate the cost of the new state
                new_cost = g + 1
                
                # Check if the new state has been visited before or has a lower cost
                if np.array(new_state).tostring() not in visited_costs or new_cost < visited_costs[np.array(new_state).tostring()]:
                    visited_costs[np.array(new_state).tostring()] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state[new_row][new_col]], new_state))
    
    return None


def heuristic(state, goal_state):
    # The heuristic function is the sum of the Manhattan distances of each tile from its goal position
    h = 0
    for i in range(3):
        for j in range(4):
            if state[i][j] != '_':
                value = state[i][j]
                goal_pos = [(k, l) for k in range(3) for l in range(4) if goal_state[k][l] == value][0]
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return h


print(a_star())
