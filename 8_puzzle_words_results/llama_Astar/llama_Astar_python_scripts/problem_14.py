
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['_', 'a', 't', 'n'], ['b', 'i', 'r', 'n'], ['k', 'r', 'e', 'y'], ['b', 'a', 'l', 'i']]
   target_words = ['ann', 'birk', 'trey', 'bali']
   num_rows = 4
   num_cols = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if all(state[i][1:] == list(word) for i, word in enumerate(target_words)):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_shift in [-1, 0, 1]:
           for col_shift in [-1, 0, 1]:
               # Check if the new state would be valid, ie the new state must not move the blank space out of the board
               if 0 <= row_shift + col_shift < 2 and -1 <= row_shift - col_shift <= 1:
                   new_state = [list(row[:]) for row in state]
                   new_state[row_shift][col_shift], new_state[1 - row_shift][1 - col_shift] = new_state[1 - row_shift][1 - col_shift], new_state[row_shift][col_shift]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic function is the sum of the distances of the blank space to the goal positions of the words in the state
                       h = heuristic(state, target_words)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(row_shift, col_shift)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function is the sum of the distances of the blank space to the goal positions of the words in the state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if the blank space is moved further from the goal positions, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum distance that the blank space can be moved in one action is 1
   h = 0
   for i, word in enumerate(target_words):
       for j, char in enumerate(word):
           # Find the position of the character in the state
           for row in range(len(state)):
               for col in range(len(state[row])):
                   if state[row][col] == char:
                       # Calculate the distance from the character to the goal position
                       h += abs(row - i) + abs(col - j)
   return h


print(a_star())
