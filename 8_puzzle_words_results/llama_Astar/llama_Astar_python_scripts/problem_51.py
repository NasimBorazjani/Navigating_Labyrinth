
import heapq


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (['l', 'b', 'l', 'u', 'i', 'e'],
                   ['a', 't', 'g', 'n', 's', 'c'],
                   ['l', 'a', 'o', 'u', '_', 'e'],
                   ['n', 'i', 'n', 'p', 'o', 'n'])
   target_words = ['biune', 'algist', 'palule', 'noncon']
   num_rows = 4
   num_cols = 6


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(list(word) for word in target_words):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == '_':
                   for d_row, d_col in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                       new_row, new_col = row_ind + d_row, col_ind + d_col
                       # Check if the new position is valid, ie if the new position is within the bounds of the board
                       if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row_ind][col_ind], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row_ind][col_ind]
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The direction of the swap is the direction in which the blank space was swapped in
                               heapq.heappush(queue, (new_cost + heuristic(state, target_words), new_cost, actions + [(row_ind, col_ind, new_row, new_col)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the characters that are currently in their correct positions, which is exactly the characters used to fill the board in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != target_words[i][j - (i > 0)]:
               h += 1
   return h


print(a_star())
