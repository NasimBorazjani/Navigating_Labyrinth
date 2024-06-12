
import heapq


def initialize():
   # Define the initial state of the board, with '_' representing the blank space
   initial_state = [['o', 'a', 'u', 'o'], ['p', 'r', 'l', 'e'], ['f', 'a', '_', 'f'], ['m', 'k', 'd', 'd']]
   num_rows = 4
   num_cols = 4
   target_words = ['ako', 'pole', 'raff', 'mudd']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, target_words, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, target_words, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == [list(word) for word in target_words]:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_shift in [-1, 0, 1]:
           for col_shift in [-1, 1]:
               # Check if the new state would be valid, ie the new state must not have any blank spaces out of the board or in the first word
               if 0 <= state[0].index('_') + row_shift < num_rows and 0 <= state[0].index('_') + col_shift < num_cols:
                   new_state = [list(row[:]) for row in state]
                   new_state[state[0].index('_') + row_shift][state[0].index('_') + col_shift], new_state[state[0].index('_')][state[0].index('_')] = new_state[state[0].index('_')][state[0].index('_')], new_state[state[0].index('_') + row_shift][state[0].index('_') + col_shift]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic function can be a simple count of the number of characters in the current state that are not in their correct position in the goal state
                       h = heuristic(state, target_words)
                       # The actions are reported in python syntax, with the direction of the swap represented as a string
                       direction = ['up-right', 'down-right', 'up-left', 'down-left'][(row_shift, col_shift)]
                       heappush(queue, (new_cost + h, new_cost, actions + [direction], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a simple count of the number of characters in the current state that are not in their correct position in the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each misplaced character must be moved at least once
   # The heuristic is consistent because moving a character from one position to another results in a valid state, and the estimated cost of the next node is higher if a character is moved back to its original position, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum number of swaps that can be made is by swapping a character with its correct position, which is exactly the character used to fill the position in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != target_words[i][j - (i == 0)]:
               h += 1
   return h


print(a_star())
