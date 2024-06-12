
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[74, 37, 2, 22], [4, 21, '_', 54], [33, 70, 9, 11]]
    goal_state = [[74, 37, 33, 22], [70, 54, 21, 11], [9, 4, 2, '_']]
    
    # Define the goal state as a dictionary for easy lookup of the coordinates of each number
    goal_dict = {}
    for i in range(len(goal_state)):
        for j in range(len(goal_state[0])):
            goal_dict[goal_state[i][j]] = (i, j)
    
    # Define the initial state as a tuple for hashing
    initial_state_tuple = tuple(tuple(row) for row in initial_state)
    
    visited_costs = {}
    visited_costs[initial_state_tuple] = 0
    
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
            
            # Check if the new coordinates are valid
            if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                new_state_tuple = tuple(tuple(row) for row in new_state)
                new_cost = g + 1
                
                if new_state_tuple not in visited_costs or new_cost < visited_costs[new_state_tuple]:
                    visited_costs[new_state_tuple] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_dict), new_cost, actions + [new_state[new_row][new_col]], new_state))
    
    return None


def heuristic(state, goal_dict):
    # The heuristic is the sum of Manhattan distances of each number from its goal position
    h = 0
    for i in range(len(state)):
        for j in range(len(state[0]):
            if state[i][j] != '_':
                goal_pos = goal_dict[state[i][j]]
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return h


print(a_star())
