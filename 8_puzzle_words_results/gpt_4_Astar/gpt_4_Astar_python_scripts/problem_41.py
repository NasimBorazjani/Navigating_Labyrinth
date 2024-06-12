
import heapq
import numpy as np


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('o', 'a', '_', 'i', 't', 's'),
                   ('d', 'r', 'o', 'o', 'o', 'a'),
                   ('c', 'e', 'm', 'i', 'l', 'e'),
                   ('c', 'c', 'm', 't', 'i', 'e'))
   num_rows = 4
   num_cols = 6
   target_words = ['alias', 'doocot', 'cerite', 'commie']
   # Define the 4 diagonal directions
   directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
   direction_names = ['down-right', 'down-left', 'up-right', 'up-left']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any unknown numbers, thus we need to get (the coordinates of) the unknown numbers to check whether the current state is the goal state
       blank_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
       if all(state[i][j] == target_words[i][j] for i in range(num_rows) for j in range(num_cols) if state[i][j] != '_'):
           return actions


       # If the state has at least 1 remaining unknown number, generate all possible actions from the current state, which includes replacing the next x in the grid with any of unique integers in the range
       else:
           for direction, direction_name in zip(directions, direction_names):
               new_row, new_col = blank_coord[0] + direction[0], blank_coord[1] + direction[1]
               # Check if the new coordinate is valid, ie if the new workshop is within the bounds of the city and it is not closed
               if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[blank_coord[0]][blank_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_coord[0]][blank_coord[1]]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The additional cost of this state is 1 as we are trying to minimize the number of swaps
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # Relaxing the constraints on the columns sums and the diagonal sum to calculate the heuristic
                       h = heuristic(new_state, target_words)
                       heapq.heappush(queue, (g + h, new_cost, actions + [direction_name], new_state))
   return None


def heuristic(state, target_words):
   # The heuristic function can be the sum of the Manhattan distances from each tile to its target position
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each tile must be moved at least once
   # It's consistent because moving a tile from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved tile's target position is in the direction of the move), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles are in their target positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_':
               target_i, target_j = target_words.index(state[i][j]), target_words[target_words.index(state[i][j])].index(state[i][j])
               h += abs(i - target_i) + abs(j - target_j)
   return h


print(a_star())
