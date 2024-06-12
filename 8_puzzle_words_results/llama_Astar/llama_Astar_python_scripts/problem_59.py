
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['r', 'f', '_', 'e'], ['t', 'a', 'a', 'f'], ['a', 'e', 'f', 't'], ['f', 'i', 'n', 'h'], ['d', 'a', 'e', 'f']]
   target_words = ['fae', 'trah', 'feat', 'fine', 'daff']
   num_rows = 5
   num_cols = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == target_words:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_shift in [-1, 0, 1]:
           for col_shift in [-1, 1]:
               # Check if the new state would be valid, ie the new state must not have the blank space out of the grid or in the first row and first column
               if 0 <= row_shift + col_shift < num_rows and 0 <= row_shift - col_shift < num_cols:
                   new_state = [list(row[:]) for row in state]
                   new_state[row_shift][col_shift], new_state[row_shift + col_shift][col_shift + row_shift] = new_state[row_shift + col_shift][col_shift + row_shift], new_state[row_shift][col_shift]
                   new_state = [''.join(row) for row in new_state]
                   # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the board
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, target_words)
                       # The direction of the swap is up-right, down-right, up-left, or down-left, depending on the shift in rows and columns
                       direction = 'up-right' if row_shift == -1 and col_shift == 1 else 'down-right' if row_shift == 1 and col_shift == 1 else 'up-left' if row_shift == -1 and col_shift == -1 else 'down-left'
                       heappush(queue, (new_cost + h, new_cost, actions + [(direction)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the target state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the characters that are not in their correct positions in the current state. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != target_words[i][j]:
               h += 1
   return h


print(a_star())
