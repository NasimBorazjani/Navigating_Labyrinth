
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[97, 78, '_', 9, 67], [18, 65, 52, 27, 66], [38, 92, 50, 14, 6]]
    goal_state = [[97, 78, 67, 66, 65], [52, 50, 38, 27, 18], [14, 9, 6, '_', '']]
    
    # Define the goal state as a dictionary for easy lookup
    goal_dict = {97: (0, 0), 78: (0, 1), 67: (0, 2), 66: (0, 3), 65: (0, 4), 52: (1, 0), 50: (1, 1), 38: (1, 2), 27: (1, 3), 18: (1, 4), 14: (2, 0), 9: (2, 1), 6: (2, 2), '_': (2, 3), '': (2, 4)}
    
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
                    # Calculate the heuristic cost based on the Manhattan distance of each tile to its goal position
                    h = sum(abs(i - goal_dict[new_state[i][j]][0]) + abs(j - goal_dict[new_state[i][j]][1]) for i in range(3) for j in range(5) if new_state[i][j] != '_')
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state[new_row][new_col]], new_state))
    
    return None


print(a_star())
