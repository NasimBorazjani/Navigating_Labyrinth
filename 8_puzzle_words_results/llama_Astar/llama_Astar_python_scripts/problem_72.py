
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['o', 'l', '_', 't'], ['p', 'r', 'o', 'a'], ['e', 'i', 'k', 'k'], ['c', 'i', 'k', 'a'], ['s', 'l', 'r', 'm']]
   target_words = ['lit', 'poor', 'kirk', 'cake', 'slam']
   num_rows = len(initial_state)
   num_cols = len(initial_state[0])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == [list(word) for word in target_words]:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_shift in [-1, 0, 1]:
           for col_shift in [-1, 0, 1]:
               # Check if the new state would be valid, ie the new state must not have the blank space out of the board
               if 0 <= row_shift + col_shift < 2 and -1 <= row_shift - col_shift < 2:
                   new_state = [list(row[:]) for row in state]
                   new_state[row_shift][col_shift], new_state[-row_shift][-col_shift] = new_state[-row_shift][-col_shift], new_state[row_shift][col_shift]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the board
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state, target_words)
                       # The direction of the swap is represented as a tuple ('up-right', 'down-right', 'up-left', or 'down-left')
                       swap_direction = ('up-right', 'down-right', 'up-left', 'down-left')[row_shift * 3 + col_shift]
                       heappush(queue, (new_cost + h, new_cost, actions + [swap_direction], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the target state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the characters that are not in their correct positions in the current state. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != target_words[i][j - (i > 0)]:
               h += 1
   return h


print(a_star())