
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['y', 'h', 'r', 'm', '_', 's'],
                   ['b', 'o', 'w', 'k', 'r', 'u'],
                   ['r', 'e', 'l', 'e', 'u', 's'],
                   ['c', 'c', 'a', 'u', 't', 'y'])
   target_words = ['humus', 'bywork', 'cereus', 'clarty']
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
       for row_shift in [-1, 0, 1]:
           for col_shift in [-1, 1]:
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
   # The heuristic function can be a simulation of swapping the blank space greedily, using the next closest word as the goal word
   # This heuristic is admissible because it is greedy, always opting for the action that brings the board closer to the goal, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if the blank space is swapped to a farther word, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum distance that can be swapped to another word is by using the closest word that won't cause the board to be sorted
   # Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       # Calculate the Levenshtein distance between the current row and the target word
       distance = sum(state[i][j] != target_words[i][j] for j in range(len(target_words[i])))
       # Increment the estimated cost to the goal by the distance
       h += distance
   return h


print(a_star())
