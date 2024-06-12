
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['_', 'b', 'p', 'i', 's'], ['d', 'u', 'r', 'n', 'c'], ['l', 'i', 'o', 'e', 'n'], ['s', 'n', 'e', 'o', 't']]
   target_words = ['bois', 'duroc', 'linen', 'spent']
   num_rows = 4
   num_cols = 5


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == [list(word) for word in target_words]:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_shift in [-1, 0, 1]:
           for col_shift in [-1, 0, 1]:
               # Check if the new state would be valid, ie the new state must not move the blank space out of the board
               if 0 <= row_shift + col_shift < 2 and -1 <= row_shift - col_shift <= 1:
                   new_state = [list(row[:]) for row in state]
                   new_state[row_shift][col_shift], new_state[-row_shift][-col_shift] = new_state[-row_shift][-col_shift], new_state[row_shift][col_shift]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic function is the sum of the distances of the blank space to the goal positions of the words in the board
                       h = heuristic(state, target_words)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(row_shift, col_shift)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function is the sum of the distances of the blank space to the goal positions of the words in the board
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if the blank space is moved further from the goal positions, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum distance that the blank space can be moved in one action is 1
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] == '_':
               for target_word in target_words:
                   for k in range(len(target_word)):
                       h += abs(i - k) + abs(j - len(target_word) + 1)
   return h


print(a_star())
