
import heapq
from collections import Counter


def a_star():
   # Define the initial state of the board, as a 2d tuple of characters
   initial_state = (('d', 't', 's', 'l', 'a'), 
                    ('u', 'a', 'a', 'e', 'i'), 
                    ('_', 'l', 'g', 'i', 'a'), 
                    ('w', 'r', 'n', 'c', 'h'))
   # Define the goal state of the board
   goal_state = (('t', 'a', 'l', 'a', '_'), 
                 ('u', 'd', 'a', 's', 'i'), 
                 ('g', 'l', 'a', 'i', 'r'), 
                 ('w', 'e', 'n', 'c', 'h'))
   num_rows = 4
   num_cols = 5
   # Define the directions of the possible moves
   directions = {'up-right': (-1, 1), 'down-right': (1, 1), 'up-left': (-1, -1), 'down-left': (1, -1)}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving the blank space to any of the 4 diagonal directions
       # First, find the position of the blank space in the current state
       blank_space_coord = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == '_'][0]
       for direction, (d_row, d_col) in directions.items():
           new_row, new_col = blank_space_coord[0] + d_row, blank_space_coord[1] + d_col
           # Check if the new position of the blank space would be valid, ie within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               # Swap the blank space with the tile in the new position
               new_state[blank_space_coord[0]][blank_space_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_space_coord[0]][blank_space_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), g + 1, actions + [(direction)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the count of tiles that are not in their goal position
   # This heuristic relaxes the constraint that only the blank space can be moved, and only to a diagonal position
   # It is admissible because it never overestimates the cost to reach the goal, as each misplaced tile must be moved at least once
   # It's consistent because moving a tile reduces the heuristic cost of the successor node by a max of 1 (if the moved tile is placed in its goal position), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles will be in their goal position
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != goal[i][j]:
               h += 1
   return h


print(a_star())
