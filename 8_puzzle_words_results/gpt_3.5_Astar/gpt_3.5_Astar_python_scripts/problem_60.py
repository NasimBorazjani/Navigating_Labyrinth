
import heapq
import math


def a_star():
   # Define the target words and the initial state of the board
   target_words = ['ball', 'oared', 'amnia', 'fuggy', 'marie']
   initial_state = [['a', 'b', 'n', 'l', 'l'],
                    ['o', 'r', 'r', 'u', 'd'],
                    ['g', 'm', 'e', 'i', '_'],
                    ['f', 'a', 'g', 'a', 'y'],
                    ['m', 'a', 'a', 'i', 'e']]
   num_rows = 5
   num_cols = 5


   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, where each row spells the corresponding word in the target words list
       if all(''.join(row) == target_words[i] for i, row in enumerate(state)):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
           new_row, new_col = None, None
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == '_':
                       new_row, new_col = i + d_row, j + d_col
           # Check if the new position is valid, ie within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state by swapping the blank space with the neighboring tile
               new_state = [list(row[:]) for row in state]
               new_state[new_row][new_col], new_state[new_row - d_row][new_col - d_col] = new_state[new_row - d_row][new_col - d_col], new_state[new_row][new_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost of the new state is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1

               if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                   visited_costs[str(new_state)] = new_cost
                   # Calculate the heuristic cost to reach the goal state from the current state
                   h = heuristic(new_state, target_words)
                   heapq.heappush(queue, (g + h, new_cost, actions + [(new_row, new_col, new_row - d_row, new_col - d_col)], new_state))
   return None


def heuristic(state, target_words):
   # An admissible and consistent heuristic for this problem is the sum of the number of characters that are not in the correct position in each row
   # This heuristic relaxes the constraint that only the blank space can be moved, as it considers the number of characters that need to be swapped to reach the goal state
   # It is admissible because it never overestimates the cost to reach the goal, as each character that is not in the correct position must be swapped at least once
   # It's consistent because moving a character from one position to another reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i, row in enumerate(state):
       for j, char in enumerate(row):
           if char != target_words[i][j]:
               h += 1
   return h


print(a_star())
