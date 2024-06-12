
import heapq
import math


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[92, 79, 74, 46, 64, 44], [39, 59, 75, 26, 47, 73], [29, 53, 56, '_', 16, 17]]
    
    # Define the goal state of the puzzle
    goal_state = [[92, 79, 75, 56, 47, 44], [64, 59, 53, 46, 26, 17], [39, 29, 16, '_', 74, 73]]
    
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
        empty_spot = None
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] == '_':
                    empty_spot = (i, j)
                    break
        
        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for move in movements:
            new_row = empty_spot[0] + move[0]
            new_col = empty_spot[1] + move[1]
            
            # Check if the new position is within the bounds of the puzzle
            if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
                new_state = [row[:] for row in state]
                new_state[empty_spot[0]][empty_spot[1]] = new_state[new_row][new_col]
                new_state[new_row][new_col] = '_'
                
                # Calculate the cost of the new state
                new_cost = g + 1
                
                if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                    visited_costs[str(new_state)] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state[empty_spot[0]][empty_spot[1]]], new_state))
    
    return None


def heuristic(state, goal_state):
    # An admissible and consistent heuristic for this problem is the sum of Manhattan distances of each tile from its goal position
    # This heuristic relaxes the constraint that only the empty spot can be moved, as it considers the distance of each tile from its goal position
    # It is admissible because the sum of Manhattan distances is always less than or equal to the actual number of moves required to reach the goal state
    # It is consistent because moving a tile closer to its goal position reduces the heuristic cost of the successor node by at most 1 (equal to the cost of reaching the successor node), which is equal to the cost of moving the tile
    h = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != '_':
                tile = state[i][j]
                goal_pos = [(k, l) for k in range(len(goal_state)) for l in range(len(goal_state[0]) if goal_state[k][l] == tile)][0]
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return h


print(a_star())
