
import heapq
import math


def a_star():
    # Define the initial state of the puzzle
    initial_state = [['_', 67, 21, 97, 69], [61, 68, 55, 16, 73], [42, 41, 31, 83, 53]]
    goal_state = [[97, 83, 73, 69, '_'], [68, 67, 61, 55, 53], [42, 41, 31, 21, 16]]
    
    # Define the possible movements of the empty spot
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    visited_costs = {}
    visited_costs[str(initial_state)] = 0
    
    queue = [(0, 0, [], initial_state)]
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Check if the current state is the goal state
        if state == goal_state:
            return actions
        
        # Find the position of the empty spot
        empty_spot = [(i, j) for i in range(3) for j in range(5) if state[i][j] == '_'][0]
        
        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for move in movements:
            new_row = empty_spot[0] + move[0]
            new_col = empty_spot[1] + move[1]
            
            # Check if the new position is valid
            if 0 <= new_row < 3 and 0 <= new_col < 5:
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]] = new_state[new_row][new_col]
                new_state[new_row][new_col] = '_'
                new_state_str = str(new_state)
                
                # Calculate the cost of the new state
                new_cost = g + 1
                
                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state[empty_spot[0]][empty_spot[1]]], new_state))
    
    return None


def heuristic(state, goal_state):
    # An admissible and consistent heuristic for this problem is the sum of Manhattan distances of each tile from its goal position
    # This heuristic relaxes the constraint that only the empty spot can be moved, as it considers the distance of each tile from its goal position
    # It is admissible because it never overestimates the cost to reach the goal state, as each tile must be moved at least the Manhattan distance to reach its goal position
    # It is consistent because moving a tile closer to its goal position reduces the heuristic cost of the successor node by at most 1 (equal to the cost of reaching the successor node), which is equal to the cost of moving the tile
    h = 0
    for i in range(3):
        for j in range(5):
            if state[i][j] != '_':
                tile = state[i][j]
                goal_pos = [(k, l) for k in range(3) for l in range(5) if goal_state[k][l] == tile][0]
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    
    return h


print(a_star())