
import heapq


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('u', 't', '_', 'e'),
                   ('k', 'a', 'b', 'm'),
                   ('n', 'e', 'o', 'g'),
                   ('p', 'u', 's', 'o'),
                   ('y', 'o', 'e', 'p'))
   num_rows = 5
   num_cols = 4
   target_words = ['toe', 'kuba', 'meng', 'peso', 'youp']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if all(state[i][1:] == list(word) for i, word in enumerate(target_words)):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_diff in [-1, 0, 1]:
           for col_diff in [-1, 1]:
               new_row, new_col = state.index('_') + row_diff, state[0].index('_') + col_diff
               # Check if the new state would be valid, ie the new position of the blank space must be within the bounds of the board
               if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[state.index('_')][1], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[state.index('_')][1]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The direction of the swap is the direction in which the blank space was swapped in
                       direction = (row_diff, col_diff)
                       heapq.heappush(queue, (new_cost + heuristic(state, target_words), new_cost, actions + [direction], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the characters that are currently in their correct positions, which is exactly the characters used to fill the board in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i, word in enumerate(target_words):
       for j, char in enumerate(word):
           if state[i][j + 1] != char:
               h += 1
   return h


print(a_star())
