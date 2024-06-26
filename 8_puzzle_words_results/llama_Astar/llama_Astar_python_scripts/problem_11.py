
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['o', 'b', 'e', 'd'], ['c', 'o', 'd', 'u'], ['w', 'a', '_', 'p'], ['y', 'u', 'l', 'p'])
   num_rows = 4
   num_cols = 4
   target_words = ['bud', 'codo', 'waup', 'yelp']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if all(state[i][j] == target_words[i][j] for i in range(num_rows) for j in range(num_cols) if state[i][j] != '_'):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_shift in [-1, 0, 1]:
           for col_shift in [-1, 0, 1]:
               # Check if the new state would be valid, ie the new state must not have the blank space out of the board
               if 0 <= state[0].index('_') + row_shift < num_rows and 0 <= state[0].index('_') + col_shift < num_cols:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[state[0].index('_') + row_shift][state[0].index('_') + col_shift], new_state[state[0].index('_')][state[0].index('_')] = new_state[state[0].index('_')][state[0].index('_')], new_state[state[0].index('_') + row_shift][state[0].index('_') + col_shift]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The direction of the swap is the direction in which the blank space was swapped in
                       direction = (row_shift, col_shift)
                       heapq.heappush(queue, (new_cost + heuristic(state, target_words), new_cost, actions + [direction], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of swaps that can be made is by moving a character from its correct position to its current position in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != '_' and state[i][j] != target_words[i][j]:
               h += 1
   return h


print(a_star())
