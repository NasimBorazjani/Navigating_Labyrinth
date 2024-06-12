
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[87, 49, 79, 68, '_'], [56, 19, 64, 37, 7], [27, 15, 41, 35, 78]]
    goal_state = [[87, 79, 78, 68, 64], [56, 49, 41, 37, 35], [27, 19, 15, 7, '_']]
    
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
        empty_row, empty_col = empty_spot[0], empty_spot[1]
        
        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_row + d_row, empty_col + d_col
            
            # Check if the new position is within the bounds of the puzzle
            if 0 <= new_row < 3 and 0 <= new_col < 5:
                # Create a new state by swapping the empty spot with the neighboring tile
                new_state = [row[:] for row in state]
                new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
                
                # Calculate the cost of the new state
                new_cost = g + 1
                
                # If the new state has not been visited or the new cost is lower than the previous cost, add it to the queue
                if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                    visited_costs[str(new_state)] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state[new_row][new_col]], new_state))
    
    return None


def heuristic(state, goal_state):
    # The heuristic is the sum of the Manhattan distances of each tile from its goal position
    h = 0
    for i in range(3):
        for j in range(5):
            if state[i][j] != '_':
                value = state[i][j]
                goal_pos = np.argwhere(np.array(goal_state) == value)[0]
                goal_row, goal_col = goal_pos[0], goal_pos[1]
                h += abs(i - goal_row) + abs(j - goal_col)
    
    return h


print(a_star())
