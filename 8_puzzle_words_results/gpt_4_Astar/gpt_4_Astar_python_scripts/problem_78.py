
import heapq
from collections import Counter


def a_star():
   # Define the initial state of the board, as a 2d tuple of characters in the board
   initial_state = (('a', 'j', '_', 'k', 'e'),
                    ('t', 's', 'w', 'y', 'e'),
                    ('t', 'r', 'a', 'p', 'a'),
                    ('s', 'e', 'a', 'm', 'h'),
                    ('c', 'r', 's', 'e', 'p'))
   # Define the goal state of the board
   goal_state = (('j', 'a', 'k', 'e', '_'),
                 ('t', 'a', 'w', 's', 'e'),
                 ('t', 'r', 'y', 'p', 'a'),
                 ('s', 'm', 'a', 's', 'h'),
                 ('c', 'r', 'e', 'e', 'p'))
   num_rows = 5
   num_cols = 5


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving the blank space to any of its 4 diagonal neighboring tiles
       # First, find the coordinates of the blank space
       blank_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
       for d_row, d_col in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
           new_row, new_col = blank_coord[0] + d_row, blank_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the new tile is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               # Swap the blank space with the tile at the new coordinate
               new_state[blank_coord[0]][blank_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_coord[0]][blank_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The direction of the move is determined by the change in the row and column indices of the blank space
                   if d_row == -1 and d_col == 1:
                       move_direction = 'up-right'
                   elif d_row == 1 and d_col == 1:
                       move_direction = 'down-right'
                   elif d_row == -1 and d_col == -1:
                       move_direction = 'up-left'
                   elif d_row == 1 and d_col == -1:
                       move_direction = 'down-left'
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), g + 1, actions + [move_direction], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the count of tiles that are not in their goal position
   # This heuristic relaxes the constraint that only the blank space can be moved, and only to a diagonal neighboring tile
   # It is admissible because it never overestimates the cost to reach the goal, as each tile not in its goal position must be moved at least once
   # It's consistent because moving the blank space reduces the heuristic cost of the successor node by a max of 1 (if the moved tile is moved to its goal position), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles will be in their goal position
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != goal[i][j]:
               h += 1
   return h


print(a_star())
