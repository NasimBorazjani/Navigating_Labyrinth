
import heapq
from collections import Counter


def a_star():
   # Define the initial state of the board, as a 2d tuple of characters
   initial_state = (('a', 's', '_', 'p', 'e'),
                   ('c', 'u', 'd', 'o', 's'),
                   ('l', 'u', 'u', 'a', 's'),
                   ('r', 'c', 'u', 'n', 'e'))
   # Define the goal state of the board
   goal_state = (('s', 'u', 'p', 'e', '_'),
                ('c', 'a', 'd', 'u', 's'),
                ('n', 'u', 'c', 'a', 'l'),
                ('r', 'o', 'u', 's', 'e'))
   num_rows = 4
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
                   # The heuristic is the sum of the Manhattan distances from each tile to its goal position
                   h = heuristic(new_state, goal_state)
                   # The action is represented as the direction in which the blank space was moved
                   if d_row == -1 and d_col == 1:
                       action = 'up-right'
                   elif d_row == 1 and d_col == 1:
                       action = 'down-right'
                   elif d_row == -1 and d_col == -1:
                       action = 'up-left'
                   elif d_row == 1 and d_col == -1:
                       action = 'down-left'
                   heapq.heappush(queue, (g + h, g + 1, actions + [action], new_state))
   return None


def heuristic(state, goal):
   # The heuristic function can be the sum of the Manhattan distances from each tile to its goal position
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each tile must be moved at least once
   # It's consistent because moving a tile from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved tile's goal position is in the direction of the move), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles are in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           goal_coord = [(k, l) for k, row in enumerate(goal) for l, element in enumerate(row) if element == state[i][j]][0]
           h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


print(a_star())
