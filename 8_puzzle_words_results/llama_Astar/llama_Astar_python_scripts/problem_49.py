
import heapq


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (['a', 'l', 'o', 'a', 'm', 'h'],
                   ['f', 'e', 'n', 'n', 'a', 't'],
                   ['t', 'r', 'a', 'g', '_', 'c'],
                   ['c', 'i', 'r', 'a', 'n', 'e'])
   # Define the target words
   target_words = ['leath', 'fanman', 'tragic', 'carone']
   # Define the possible directions for the blank space to move
   directions = ['up-right', 'down-right', 'up-left', 'down-left']
   num_rows = 4
   num_cols = 6


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(word[::-1] for word in target_words):
           return actions


       # Generate all possible actions from the current state
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == '_':
                   for direction in directions:
                       new_row, new_col = row, col
                       # Update the new position of the blank space based on the direction
                       if direction == 'up-right':
                           new_row -= 1
                           new_col += 1
                       elif direction == 'down-right':
                           new_row += 1
                           new_col += 1
                       elif direction == 'up-left':
                           new_row -= 1
                           new_col -= 1
                       elif direction == 'down-left':
                           new_row += 1
                           new_col -= 1
                       # Check if the new position is valid
                       if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state, target_words), new_cost, actions + [(row, col, direction)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the target state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the characters that are currently in their correct positions, which is exactly the characters used to fill the board in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != target_words[i][j - (i > 0)]:
               h += 1
   return h


print(a_star())
