
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['a', 's', '_', 'p', 'e'],
                   ['c', 'u', 'd', 'o', 's'],
                   ['l', 'u', 'u', 'a', 's'],
                   ['r', 'c', 'u', 'n', 'e'])
   # Define the target words
   target_words = ['supe', 'cadus', 'nucal', 'rouse']
   # Define the possible directions for swapping
   directions = ['ur', 'dr', 'ul', 'dl']
   num_rows = 4
   num_cols = 5


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(list(word) for word in target_words):
           return actions


       # Generate all possible actions from the current state
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == '_':
                   for direction in directions:
                       new_row, new_col = row + {'ur': -1, 'dr': 1, 'ul': -1, 'dl': 1}[direction], col + {'ur': 1, 'dr': 1, 'ul': -1, 'dl': -1}[direction]
                       # Check if the new position is valid
                       if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of actions taken
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The heuristic is the number of misplaced characters in the new state
                               h = heuristic(new_state, target_words)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(row, col, direction)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function counts the number of misplaced characters in the state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent because moving a character from one position to another results in a decrease in the heuristic cost of the successor node by a max of 1 (if the moved character is in the correct position in the new state), which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != '_' and state[i][j] != target_words[i][j - (i > 0)]:
               h += 1
   return h


print(a_star())
