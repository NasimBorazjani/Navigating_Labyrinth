
import heapq


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('a', 'm', '_', 'p'),
                   ('p', 'e', 'h', 'a'),
                   ('l', 'e', 'y', 'l'),
                   ('v', 'i', 'a', 'i'),
                   ('w', 'u', 's', 'p'))
   target_words = ['map', 'pahi', 'yeel', 'vial', 'wusp']
   num_rows = 5
   num_cols = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(word[::-1] for word in target_words):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_shift in [-1, 0, 1]:
           for col_shift in [-1, 0, 1]:
               # Check if the new state would be valid, ie the new state must not have the blank space out of the board
               if 0 <= row_shift + col_shift < 2 and -1 <= row_shift - col_shift <= 1:
                   new_state = [list(row[:]) for row in state]
                   new_state[row_shift][col_shift], new_state[1 - row_shift][1 - col_shift] = new_state[1 - row_shift][1 - col_shift], new_state[row_shift][col_shift]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic function can be a simple count of the number of characters in the wrong position
                       h = heuristic(state, target_words)
                       # The direction of the swap is up-right, down-right, up-left, or down-left, depending on the row_shift and col_shift
                       direction = 'up-right' if row_shift == -1 and col_shift == 1 else 'down-right' if row_shift == 1 and col_shift == 1 else 'up-left' if row_shift == 1 and col_shift == -1 else 'down-left'
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(direction)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a simple count of the number of characters in the wrong position
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != target_words[i][j - (i > 0)]:
               h += 1
   return h


print(a_star())
