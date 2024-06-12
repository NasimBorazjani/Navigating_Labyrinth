
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[95, '_', 80, 18], [67, 66, 35, 94], [27, 26, 69, 53]]
    goal_state = [[95, 94, 80, 69], [67, 66, 53, 35], [27, 26, 18, '_']]
    
    # Define the goal state as a dictionary for easier lookup
    goal_dict = {95: (0, 0), 94: (0, 1), 80: (0, 2), 69: (0, 3), 67: (1, 0), 66: (1, 1), 53: (1, 2), 35: (1, 3), 27: (2, 0), 26: (2, 1), 18: (2, 2), '_': (2, 3)}
    
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
            
            # Check if the new position is within the bounds of the puzzle
            if 0 <= new_row < 3 and 0 <= new_col < 4:
                # Create a new state by swapping the empty spot with the neighboring tile
                new_state = [row[:] for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                
                # Calculate the cost of the new state
                new_cost = g + 1
                
                # Check if the new state has not been visited or the new cost is lower than the previously recorded cost
                if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                    visited_costs[str(new_state)] = new_cost
                    # Calculate the heuristic cost based on the Manhattan distance of each tile to its goal position
                    h = heuristic(new_state, goal_dict)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state[empty_spot[0]][empty_spot[1]]], new_state))
    
    return None


def heuristic(state, goal_dict):
    # Calculate the Manhattan distance heuristic by summing the distances of each tile to its goal position
    h = 0
    for i in range(3):
        for j in range(4):
            if state[i][j] != '_':
                goal_pos = goal_dict[state[i][j]]
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    
    return h


print(a_star())
