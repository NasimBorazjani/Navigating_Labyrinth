
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[88, 71, 83, 72, 37], [98, 43, 53, '_', 82], [24, 20, 54, 14, 21]]
    goal_state = [[98, 88, 83, 72, 71], [54, 43, 37, 24, 21], [20, 14, '_', 82, 53]]
    
    # Define the goal state as a dictionary for easy lookup
    goal_dict = {98: (0, 0), 88: (0, 1), 83: (0, 2), 72: (0, 3), 71: (0, 4),
                 54: (1, 0), 43: (1, 1), 37: (1, 2), 24: (1, 3), 21: (1, 4),
                 20: (2, 0), 14: (2, 1), '_': (2, 2), 82: (2, 3), 53: (2, 4)}
    
    visited_costs = {}
    visited_costs[str(initial_state)] = 0
    
    queue = []
    heapq.heappush(queue, (0, 0, [], initial_state))
    
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
            
            # Check if the new position is within the bounds of the puzzle
            if 0 <= new_row < 3 and 0 <= new_col < 5:
                # Create a new state by swapping the empty spot with the neighboring tile
                new_state = [row[:] for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                
                # Calculate the cost of the new state
                new_cost = g + 1
                
                # Check if the new state has been visited before or has a lower cost
                if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                    visited_costs[str(new_state)] = new_cost
                    # Calculate the heuristic cost based on the Manhattan distance of each tile from its goal position
                    h = heuristic(new_state, goal_dict)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state[empty_spot[0]][empty_spot[1]]], new_state))
    
    return None


def heuristic(state, goal_dict):
    # Calculate the heuristic cost based on the Manhattan distance of each tile from its goal position
    h = 0
    for i in range(3):
        for j in range(5):
            if state[i][j] != '_':
                goal_row, goal_col = goal_dict[state[i][j]]
                h += abs(i - goal_row) + abs(j - goal_col)
    return h


print(a_star())
