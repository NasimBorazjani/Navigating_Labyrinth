
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[67, 86, 68, 29], [10, 95, '_', 44], [19, 80, 6, 50]]
    goal_state = [[67, 86, 68, 50], [29, 95, 44, 44], [19, 80, 29, 10]]
    
    # Define the goal state as a 1D list for easier comparison
    goal_state_flat = [67, 86, 68, 50, 29, 95, 44, 44, 19, 80, 29, 10]
    
    # Define the possible moves for the empty spot
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    visited_costs = {}
    visited_costs[str(initial_state)] = 0
    
    queue = []
    heapq.heappush(queue, (0, 0, [], initial_state))
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Flatten the current state for comparison
        state_flat = [cell for row in state for cell in row]
        
        if state_flat == goal_state_flat:
            return actions
        
        # Find the position of the empty spot
        empty_spot = [(i, j) for i in range(3) for j in range(4) if state[i][j] == '_'][0]
        
        for move in moves:
            new_row = empty_spot[0] + move[0]
            new_col = empty_spot[1] + move[1]
            
            if 0 <= new_row < 3 and 0 <= new_col < 4:
                new_state = [row.copy() for row in state]
                new_state[empty_spot[0]][empty_spot[1]] = new_state[new_row][new_col]
                new_state[new_row][new_col] = '_'
                
                new_state_str = str(new_state)
                new_cost = g + 1
                
                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state[empty_spot[0]][empty_spot[1]]], new_state))
    
    return None


def heuristic(state, goal_state):
    # The heuristic is the sum of Manhattan distances of each tile from its goal position
    h = 0
    for i in range(3):
        for j in range(4):
            if state[i][j] != '_':
                value = state[i][j]
                goal_pos = np.where(goal_state == value)
                h += abs(i - goal_pos[0][0]) + abs(j - goal_pos[1][0])
    
    return h


print(a_star())
