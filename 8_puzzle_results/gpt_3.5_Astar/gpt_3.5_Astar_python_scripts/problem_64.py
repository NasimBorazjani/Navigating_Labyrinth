
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[54, 100, 91, 80, 56], [19, '_', 38, 74, 29], [14, 36, 44, 13, 10]]
    goal_state = [[100, 91, 80, 74, 56], [54, 44, 38, 36, 29], [19, 14, 13, 10, '_']]
    
    # Define the goal state as a dictionary for easy lookup of the coordinates of each number
    goal_dict = {}
    for i in range(len(goal_state)):
        for j in range(len(goal_state[0])):
            goal_dict[goal_state[i][j]] = (i, j)
    
    visited_costs = {}
    visited_costs[str(initial_state)] = 0
    
    queue = [(0, 0, [], initial_state)]
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Check if the current state is the goal state
        if state == goal_state:
            return actions
        
        # Find the coordinates of the empty spot
        empty_spot = np.argwhere(np.array(state) == '_')[0]
        
        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col
            
            # Check if the new coordinates are within the bounds of the puzzle
            if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
                # Create a new state by swapping the empty spot with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                
                # Calculate the cost of the new state
                new_cost = g + 1
                
                # Check if the new state has been visited before or has a lower cost
                if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                    visited_costs[str(new_state)] = new_cost
                    # Calculate the heuristic cost based on the Manhattan distance of each number from its goal position
                    h = heuristic(new_state, goal_dict)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state[empty_spot[0]][empty_spot[1]]], new_state))
    
    return None


def heuristic(state, goal_dict):
    # Calculate the Manhattan distance heuristic based on the distance of each number from its goal position
    h = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != '_':
                goal_row, goal_col = goal_dict[state[i][j]]
                h += abs(i - goal_row) + abs(j - goal_col)
    return h


print(a_star())
