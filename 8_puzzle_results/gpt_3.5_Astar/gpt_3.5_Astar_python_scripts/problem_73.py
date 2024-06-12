
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[96, 93, '_', 26, 66], [46, 59, 38, 92, 50], [27, 7, 39, 77, 18]]
    goal_state = [[96, 93, 92, 77, 66], [59, 50, 39, 26, 18], [46, 38, 27, 7, '_']]
    
    # Define the goal state as a dictionary for easy lookup
    goal_dict = {96: (0, 0), 93: (0, 1), 92: (0, 2), 77: (0, 3), 66: (0, 4),
                 59: (1, 0), 50: (1, 1), 39: (1, 2), 26: (1, 3), 18: (1, 4),
                 46: (2, 0), 38: (2, 1), 27: (2, 2), 7: (2, 3), '_': (2, 4)}
    
    visited_costs = {}
    visited_costs[str(initial_state)] = 0
    
    queue = [(0, 0, [], initial_state)]
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Check if the current state is the goal state
        if state == goal_state:
            return actions
        
        # Find the position of the empty spot
        empty_spot = np.where(np.array(state) == '_')
        empty_spot = (empty_spot[0][0], empty_spot[1][0])
        
        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col
            
            # Check if the new position is within the bounds of the puzzle
            if 0 <= new_row < 3 and 0 <= new_col < 5:
                # Create a new state by swapping the empty spot with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                
                # Calculate the cost of the new state
                new_cost = g + 1
                
                # Check if the new state has been visited before or has a lower cost
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
        for j in range(5):
            if state[i][j] != '_':
                goal_pos = goal_dict[state[i][j]]
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return h


print(a_star())
