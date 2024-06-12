
import heapq
from collections import Counter


def a_star():
   # Define the initial state of the board, as a 2d tuple of characters
   initial_state = (('e', 'h', 'r', 'y'), ('w', 'f', 'r', 'r'), ('_', 'u', 'd', 'd'), ('f', 'a', 'i', 'b'))
   # Define the goal state of the board
   goal_state = (('h', 'a', 'y', '_'), ('w', 'e', 'r', 'f'), ('r', 'u', 'd', 'd'), ('f', 'r', 'i', 'b'))
   num_rows = 4
   num_cols = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       blank_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
       for d_row, d_col in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
           new_row, new_col = blank_coord[0] + d_row, blank_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the new tile is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_coord[0]][blank_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_coord[0]][blank_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The direction of the swap is the direction the blank space moved in
                   if d_row == -1 and d_col == 1:
                       direction = 'up-right'
                   elif d_row == 1 and d_col == 1:
                       direction = 'down-right'
                   elif d_row == -1 and d_col == -1:
                       direction = 'up-left'
                   elif d_row == 1 and d_col == -1:
                       direction = 'down-left'
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), g + 1, actions + [direction], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the count of tiles that are not in their goal position
   # This heuristic relaxes the constraint that only the blank space can be moved, and only to a diagonal position
   # It is admissible because it never overestimates the cost to reach the goal, as each misplaced tile must be moved at least once
   # It's consistent because moving a tile reduces the heuristic cost of the successor node by a max of 1 (if the moved tile is in its goal position in the successor state but not in the current state), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles will be in their goal position
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != goal[i][j]:
               h += 1
   return h


print(a_star())
