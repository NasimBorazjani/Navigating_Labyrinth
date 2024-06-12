
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[25, 94, 12, '_'], [70, 43, 47, 85], [86, 64, 52, 92]]
    goal_state = [[25, 94, 12, 92], [70, 64, 47, 85], [86, 43, 52, '_']]
    
    # Define the goal state as a dictionary for easy lookup of the position of each number
    goal_dict = {25: (0, 0), 94: (0, 1), 12: (0, 2), 92: (0, 3), 70: (1, 0), 64: (1, 1), 47: (1, 2), 85: (1, 3), 86: (2, 0), 43: (2, 1), 52: (2, 2), '_': (2, 3)}
    
    visited_costs = {}
    visited_costs[str(initial_state)] = 0
    
    queue = [(0, 0, [], initial_state)]
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Check if the current state is the goal state
        if state == goal_state:
            return actions
        
        # Find the position of the empty spot
        empty_spot = np.argwhere(np.array(state) == '_')[0]
        
        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col
            
            # Check if the new position is valid
            if 0 <= new_row < 3 and 0 <= new_col < 4:
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                new_state_str = str(new_state)
                new_cost = g + 1
                
                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    # Calculate the heuristic cost as the Manhattan distance of each tile from its goal position
                    h = sum(abs(i - goal_dict[new_state[j][k]][0]) + abs(k - goal_dict[new_state[j][k]][1]) for j in range(3) for k in range(4) if new_state[j][k] != '_')
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state[new_row][new_col]], new_state))
    
    return None


print(a_star())
