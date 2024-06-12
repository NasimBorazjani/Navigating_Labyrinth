
import heapq


def initialize():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('h', 'k', 't', 'n'),
                   ('k', 'e', 'a', 'k'),
                   ('e', 'i', '_', 'l'),
                   ('w', 'l', 'n', 't'))
   num_rows = 4
   num_cols = 4
   target_words = ['ken', 'khat', 'kill', 'went']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, target_words, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, target_words, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(word.replace('_', '') for word in target_words):
           return actions


       # Generate all possible actions from the current state
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == '_':
                   for d_row, d_col in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                       new_row, new_col = row_ind + d_row, col_ind + d_col
                       # Check if the new state is valid
                       if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row_ind][col_ind], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row_ind][col_ind]
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of actions taken
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # Relaxing the constraints on the goal words to calculate the heuristic
                               h = heuristic(new_state, target_words)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(row_ind, col_ind, new_row, new_col)], new_state))
   return None


def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the character that is farthest from its correct position, which is exactly the character used to fill the position in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for target_word, state_row in zip(target_words, state):
       for state_char, target_char in zip(state_row, target_word):
           if state_char != target_char and state_char != '_':
               h += 1
   return h


print(a_star())
