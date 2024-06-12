
import heapq


def initialize():
   # Define the initial state of the board and the target words
   initial_state = [['l', 'a', 'e', 'o', 'n'], ['p', 'z', 'i', 'n', 'r'], ['l', 'a', 'g', 'o', '_'], ['i', 'e', 'e', 'u', 'm']]
   target_words = ['aeon', 'plier', 'gazon', 'ileum']
   num_rows = 4
   num_cols = 5


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, target_words, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, target_words, num_rows, num_cols, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == [list(word) for word in target_words]:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_diff in [-1, 0, 1]:
           for col_diff in [-1, 1]:
               # Check if the new state would be valid, ie the swap does not result in the blank space being out of the bounds of the board
               if 0 <= row_diff + state.index('_') < num_rows and 0 <= col_diff + state[0].index('_') < num_cols:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[row_diff + state.index('_')][col_diff + state[0].index('_')], new_state[state.index('_')][state[0].index('_')] = new_state[state.index('_')][state[0].index('_')], new_state[row_diff + state.index('_')][col_diff + state[0].index('_')]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required to sort the board
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, target_words)
                       # In the problem statement the directions are indexed starting from 1, thus must add 1 to the direction
                       heappush(queue, (new_cost + h, new_cost, actions + [(row_diff, col_diff)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a simulation of sorting the board greedily, using the next closest word as long as the word can be formed from the current state
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the board the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a word that is closer to the goal is not formed, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of swaps that can be made to form a word is by using the closest word that can be formed from the current state. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       # Find the closest word that can be formed from the current state
       word_diff = float('inf')
       for word in target_words:
           temp_diff = sum(state[i][j] != word[j] for j in range(len(word)))
           word_diff = min(word_diff, temp_diff)
       # Increment the estimated cost to the goal by the number of swaps required to form the closest word
       h += word_diff
   return h


print(a_star())
