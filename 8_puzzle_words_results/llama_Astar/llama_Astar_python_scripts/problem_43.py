
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['a', 'd', 'a', 'o', 'n', 'e'],
                   ['p', 'm', 'l', 'n', 'a', 'i'],
                   ['_', 'n', 'c', 'o', 'd', 'a'],
                   ['s', 'a', 'l', 't', 'l', 'y'])
   target_words = ['dione', 'palmad', 'ancona', 'saltly']
   num_rows = 4
   num_cols = 6


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == tuple(word[::-1] for word in target_words):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_shift, col_shift in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
           new_row, new_col = state[0].index('_') + row_shift, state[0].index('_') + col_shift
           # Check if the new state would be valid, ie the new position of the blank space must be within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[new_row][new_col], new_state[state[0].index('_')][state[0].index('_')] = new_state[state[0].index('_')][state[0].index('_')], new_state[new_row][new_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic function can be a simple count of the number of characters in the wrong position in the current state
                   h = heuristic(state, target_words)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [(row_shift, col_shift)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a simple count of the number of characters in the wrong position in the current state
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != target_words[i][j - (i > 0)]:
               h += 1
   return h


print(a_star())
